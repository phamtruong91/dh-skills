"""Kiểm tra file đầu ra của skill theo các quy tắc trong quy cách đầu ra.

Không phụ thuộc cách file được tạo: dùng được cho file do AI nào tạo ra từ skill.
Chạy: python -X utf8 scripts/check_outputs.py [--samples tests/samples] [--outputs tests/outputs] [--results tests/results]

Với mỗi cặp <skill>.input.json / <skill>.expect.json kiểm tra:
  1. File tồn tại, mở được bằng thư viện thật (không đổi đuôi giả).
  2. Không có chuỗi bị cấm (nhãn chờ ký, checklist, "chưa cung cấp", số 0 thay dữ liệu...).
  3. Không bịa số liệu: mọi ngày và số từ 3 chữ số trong file phải có trong đầu vào.
  4. Có/không có các chuỗi bắt buộc; trường thiếu dữ liệu được chừa chỗ điền.
  5. Với Excel: tính lại công thức bằng LibreOffice rồi so các ô đã khai báo.
  6. Mỗi "bẫy" trong expect có ghi nhận trong tests/results/<skill>.findings.md.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

GLOBAL_FORBIDDEN = ["CHỜ KÝ", "CHƯA CUNG CẤP", "chưa cung cấp", "cần xác minh", "CẦN XÁC MINH", "(đã ký)",
                    "DỰ THẢO – CHỜ KIỂM DUYỆT", "checklist", "Checklist", "phụ lục kiểm tra", "Phụ lục kiểm tra",
                    "☐", "[ ]", "TODO", "Lorem", "nhật ký AI"]


def docx_text(path):
    from docx import Document
    d = Document(path)
    out = [p.text for p in d.paragraphs]

    def walk(tables):
        for t in tables:
            for row in t.rows:
                for c in row.cells:
                    out.extend(p.text for p in c.paragraphs)
                    walk(c.tables)
    walk(d.tables)
    return "\n".join(x for x in out if x.strip())


def _all_paragraphs(d):
    for p in d.paragraphs:
        yield p, False
    def walk(tables):
        for t in tables:
            for row in t.rows:
                for c in row.cells:
                    for p in c.paragraphs:
                        yield p, True
                    yield from walk(c.tables)
    yield from walk(d.tables)


def _para_size(p, d):
    sizes = {r.font.size.pt if r.font.size else (d.styles["Normal"].font.size.pt if d.styles["Normal"].font.size else None)
             for r in p.runs if r.text.strip()}
    return sizes


def _nd30_element_errors(d):
    """Cỡ chữ, kiểu chữ, thụt đầu dòng, cách đoạn của từng thành phần theo Phụ lục I NĐ 30/2020/NĐ-CP."""
    errs = []
    in_noi_nhan = False
    for p, in_table in _all_paragraphs(d):
        txt = p.text.strip()
        if not txt:
            continue
        sizes = _para_size(p, d)
        bold = all(r.bold for r in p.runs if r.text.strip())
        ital = all(r.italic for r in p.runs if r.text.strip())

        def need(label, lo, hi, want_bold=None, want_italic=None):
            if sizes and not all(lo <= s <= hi for s in sizes if s):
                errs.append(f"{label}: cỡ chữ {sorted(s for s in sizes if s)} ngoài {lo}–{hi} pt")
            if want_bold is True and not bold:
                errs.append(f"{label}: phải in đậm")
            if want_bold is False and bold:
                errs.append(f"{label}: không được in đậm")
            if want_italic is True and not ital:
                errs.append(f"{label}: phải in nghiêng")
        if txt == "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM":
            need("Quốc hiệu", 12, 13, True)
        elif txt.startswith("Độc lập"):
            if txt != "Độc lập - Tự do - Hạnh phúc":
                errs.append(f"Tiêu ngữ viết sai ({txt!r}); đúng: 'Độc lập - Tự do - Hạnh phúc'")
            need("Tiêu ngữ", 13, 14, True)
            if "w:pBdr" not in p._p.xml:
                errs.append("Tiêu ngữ thiếu đường kẻ dưới")
        elif re.match(r"^Số:", txt):
            need("Số, ký hiệu", 13, 13)
        elif re.search(r", ngày .* tháng .* năm", txt) and in_table:
            need("Địa danh, ngày tháng", 13, 14, None, True)
        elif txt == "Nơi nhận:":
            need("Nhãn 'Nơi nhận'", 12, 12, True, True)
            in_noi_nhan = True
            continue
        elif in_noi_nhan and txt.startswith("- "):
            need("Danh sách nơi nhận", 11, 11)
            continue
        if not in_table and p.paragraph_format.first_line_indent is not None:  # đoạn nội dung
            ind = p.paragraph_format.first_line_indent.cm
            if not (0.99 <= ind <= 1.28):
                errs.append(f"đoạn {txt[:30]!r}: thụt đầu dòng {ind:.2f} cm, phải 1–1,27 cm")
            aft = p.paragraph_format.space_after.pt if p.paragraph_format.space_after is not None else 0
            if aft < 6:
                errs.append(f"đoạn {txt[:30]!r}: cách đoạn {aft:.0f} pt, tối thiểu 6 pt")
            need("Nội dung", 13, 14, False if len(txt) > 80 else None)
    return sorted(set(errs))


def nd30_format_errors(path):
    """Kiểm tra thuộc tính trình bày thật của file Word theo Phụ lục I Nghị định 30/2020/NĐ-CP (văn bản hành chính)."""
    from docx import Document
    d = Document(path)
    errs = []
    s = d.sections[0]
    mm = lambda v: round(v / 36000, 1)  # EMU -> mm
    w, h = mm(s.page_width), mm(s.page_height)
    if not (abs(w - 210) <= 1 and abs(h - 297) <= 1):
        errs.append(f"khổ giấy không phải A4 ({w}x{h} mm)")
    for name, v, lo, hi in (("lề trên", mm(s.top_margin), 20, 25), ("lề dưới", mm(s.bottom_margin), 20, 25),
                            ("lề trái", mm(s.left_margin), 30, 35), ("lề phải", mm(s.right_margin), 15, 20)):
        if not (lo - 0.5 <= v <= hi + 0.5):
            errs.append(f"{name} {v} mm ngoài khoảng {lo}–{hi} mm")
    fonts, sizes = set(), set()

    def runs(doc_or_cell):
        for p in doc_or_cell.paragraphs:
            for r in p.runs:
                yield r
        for tb in getattr(doc_or_cell, "tables", []):
            for row in tb.rows:
                for c in row.cells:
                    yield from runs(c)
    normal = d.styles["Normal"].font
    for r in runs(d):
        if not r.text.strip():
            continue
        fonts.add(r.font.name or normal.name)
        sz = r.font.size or normal.size
        sizes.add(sz.pt if sz else None)
    errs.extend(_nd30_element_errors(d))
    if fonts - {"Times New Roman"}:
        errs.append(f"phông không phải Times New Roman: {sorted(f for f in fonts if f)}")
    bad = sorted(x for x in sizes if x is None or not (11 <= x <= 14))
    if bad:
        errs.append(f"cỡ chữ ngoài 11–14 pt: {bad}")
    return errs


def xlsx_load(path):
    from openpyxl import load_workbook
    return load_workbook(path)


def xlsx_text_and_numbers(wb):
    texts, nums = [], []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                v = c.value
                if v is None or (isinstance(v, str) and v.startswith("=")):
                    continue
                if isinstance(v, datetime):
                    texts.append(v.strftime("%d/%m/%Y"))
                elif isinstance(v, (int, float)):
                    nums.append(float(v))
                else:
                    texts.append(str(v))
    return "\n".join(texts), nums


def recalc(path):
    """Tính lại công thức bằng LibreOffice; trả về workbook data_only hoặc None."""
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return None
    from openpyxl import load_workbook
    tmp = Path(tempfile.mkdtemp())
    src = tmp / "in" / path.name
    src.parent.mkdir()
    shutil.copy(path, src)
    outdir = tmp / "out"
    subprocess.run([soffice, "--headless", "--convert-to", "xlsx", "--outdir", str(outdir), str(src)],
                   capture_output=True, timeout=180)
    res = outdir / path.name
    return load_workbook(res, data_only=True) if res.exists() else None


def allowed_tokens(input_text):
    dates = set(re.findall(r"\d{1,2}/\d{1,2}/\d{4}", input_text))
    nums = set(re.findall(r"\d{3,}", input_text))
    return dates, nums


_PDF_CACHE = {}


def to_pdf(path):
    """Word -> PDF bằng LibreOffice (có nhớ kết quả); trả về đường dẫn PDF hoặc None."""
    key = (str(path), Path(path).stat().st_mtime)
    if key in _PDF_CACHE:
        return _PDF_CACHE[key]
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice or not shutil.which("pdftotext"):
        return None
    tmp = Path(tempfile.mkdtemp())
    src = tmp / Path(path).name
    shutil.copy(path, src)
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(tmp), str(src)],
                   capture_output=True, timeout=240)
    pdf = tmp / (Path(path).stem + ".pdf")
    _PDF_CACHE[key] = pdf if pdf.exists() else None
    return _PDF_CACHE[key]


def pdf_pages(path):
    """Chuyển Word sang PDF bằng LibreOffice; trả về danh sách văn bản từng trang (hoặc None nếu không có công cụ)."""
    pdf = to_pdf(path)
    if not pdf:
        return None
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    return out.split("\f")[:-1] if out.endswith("\f") else out.split("\f")


def pdf_image_pages(path):
    """Số trang chứa từng hình trong PDF (theo thứ tự xuất hiện), cần pdfimages."""
    pdf = to_pdf(path)
    if not pdf or not shutil.which("pdfimages"):
        return None
    out = subprocess.run(["pdfimages", "-list", str(pdf)], capture_output=True, text=True).stdout.splitlines()[2:]
    return [int(ln.split()[0]) for ln in out if len(ln.split()) > 2 and ln.split()[2] == "image"]


def _norm_num(x):
    x = str(x).strip().replace("−", "-").replace("%", "")
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", x):
        x = x.replace(".", "")
    return x


def figure_errors(path, lay, pages, log):
    """Biểu đồ trong Word: hình thật, trong khổ chữ, đủ độ phân giải, có chú thích 'Hình n.' dưới hình và dòng 'Nguồn:',
    văn bản thay thế ghi số liệu khớp bảng, hình và chú thích cùng một trang."""
    from docx import Document
    from docx.shared import Emu
    d = Document(path)
    errs = []
    specs = lay.get("figures", [])
    body = d.element.body
    pics = []  # (đoạn chứa hình, thứ tự)
    for p in d.paragraphs:
        if p._p.xpath(".//pic:pic"):
            pics.append(p)
    if len(pics) != len(specs):
        errs.append(f"có {len(pics)} hình, kỳ vọng {len(specs)}")
    paras = d.paragraphs
    for k, (p, spec) in enumerate(zip(pics, specs), 1):
        no = spec.get("no", k)
        if no != k:
            errs.append(f"hình thứ {k} được kỳ vọng mang số {no}: số thứ tự hình phải liên tục từ 1")
        inl = p._p.xpath(".//wp:inline")
        w_cm = int(inl[0].xpath("./wp:extent/@cx")[0]) / 360000 if inl else 0
        if w_cm > 16.0 or w_cm < 8.0:
            errs.append(f"hình {no}: rộng {w_cm:.1f} cm, phải từ 8 đến 16 cm (vùng chữ 16 cm)")
        blip = p._p.xpath(".//a:blip/@r:embed")
        if blip:
            from io import BytesIO

            from PIL import Image
            img = Image.open(BytesIO(d.part.related_parts[blip[0]].blob))
            dpi = img.width / (w_cm / 2.54) if w_cm else 0
            if dpi < 150:
                errs.append(f"hình {no}: chỉ {dpi:.0f} dpi khi in, cần từ 150 dpi trở lên")
        alt = (p._p.xpath(".//wp:docPr/@descr") or [""])[0]
        if "Số liệu:" not in alt:
            errs.append(f"hình {no}: văn bản thay thế không ghi số liệu")
        pairs = [x.strip() for x in alt.split("Số liệu:", 1)[-1].split(". Đơn vị")[0].split(";") if "=" in x]
        if len(pairs) < spec.get("min_points", 1):
            errs.append(f"hình {no}: văn bản thay thế chỉ có {len(pairs)} điểm số liệu, kỳ vọng ít nhất {spec.get('min_points', 1)}")
        i = [q._p for q in paras].index(p._p)
        cap = paras[i + 1].text if i + 1 < len(paras) else ""
        src = paras[i + 2].text if i + 2 < len(paras) else ""
        if not cap.startswith(f"Hình {no}. "):
            errs.append(f"hình {no}: dưới hình phải là chú thích 'Hình {no}. ...' (thấy {cap[:30]!r})")
        if not src.startswith("Nguồn:"):
            errs.append(f"hình {no}: thiếu dòng 'Nguồn:' dưới chú thích")
        if not (p.paragraph_format.keep_with_next and paras[i + 1].paragraph_format.keep_with_next):
            errs.append(f"hình {no}: hình, chú thích và nguồn chưa dính nhau nên có thể tách trang")
        if p.alignment is None or int(p.alignment) != 1:
            errs.append(f"hình {no}: chưa căn giữa")
        if "table_index" in spec:
            tb = d.tables[spec["table_index"]]
            amap = {a.split("=", 1)[0].strip(): _norm_num(a.split("=", 1)[1]) for a in pairs}
            n = 0
            for r in tb.rows[1:]:
                cells = [c.text.strip() for c in r.cells]
                lab = cells[spec["label_col"]]
                if not lab or not lab[0].isalnum() or any(lab.startswith(x) for x in spec.get("skip_labels", ["Cộng"])):
                    continue
                if "label_fmt" in spec:
                    lab = spec["label_fmt"].format(lab)
                if cells[spec["value_col"]] == "":
                    continue
                n += 1
                if lab not in amap:
                    errs.append(f"hình {no}: không thấy {lab!r} trong số liệu của hình")
                elif amap[lab] != _norm_num(cells[spec["value_col"]]):
                    errs.append(f"hình {no}: {lab!r} trong hình là {amap[lab]}, trong bảng là {cells[spec['value_col']]}")
            if n == 0:
                errs.append(f"hình {no}: không đối chiếu được dòng nào với bảng")
    cap_nos = [int(m.group(1)) for q in paras for m in [re.match(r"Hình (\d+)\. ", q.text)] if m]
    if cap_nos != list(range(1, len(cap_nos) + 1)):
        errs.append(f"số thứ tự chú thích hình không liên tục: {cap_nos}")
    if pages is not None:
        ipg = pdf_image_pages(path)
        if ipg is None:
            log.append("  (bỏ qua kiểm hình cùng trang chú thích: thiếu pdfimages)")
        else:
            if len(ipg) < len(specs):
                errs.append(f"PDF chỉ có {len(ipg)} hình, kỳ vọng {len(specs)}")
            for k, pg in enumerate(ipg[:len(specs)], 1):
                cp = [n for n, t in enumerate(pages, 1) if re.search(rf"^\s*Hình {k}\. ", t, flags=re.M)]
                if cp and cp[0] != pg:
                    errs.append(f"hình {k} ở trang {pg} nhưng chú thích ở trang {cp[0]}")
            log.append(f"  hình ở các trang: {ipg}")
    return errs


def layout_errors(path, expect, text, log):
    """Kiểm tra file nhiều dữ liệu/nhiều trang: số trang, số trang ở đầu trang, bảng, token duy nhất, ràng buộc cùng trang."""
    from docx import Document
    from docx.oxml.ns import qn
    lay = expect.get("layout", {})
    errs = []
    d = Document(path)
    if lay.get("page_number"):  # NĐ 30/2020: đánh số trang từ trang 2, đặt giữa lề trên
        sect = d.sections[0]
        xml = sect._sectPr.xml
        hdr = "".join(p._p.xml for p in sect.header.paragraphs)
        if "w:titlePg" not in xml:
            errs.append("không bật 'trang đầu khác' nên số trang sẽ hiện cả ở trang 1")
        if "PAGE" not in hdr:
            errs.append("đầu trang không có trường số trang (PAGE)")
        elif 'w:jc w:val="center"' not in hdr:
            errs.append("số trang không căn giữa")
    for spec in lay.get("tables", []):
        if spec["index"] >= len(d.tables):
            errs.append(f"không có bảng thứ {spec['index']}")
            continue
        tb = d.tables[spec["index"]]
        rows = tb.rows
        if spec.get("header_repeat") and "w:tblHeader" not in rows[0]._tr.xml:
            errs.append(f"bảng {spec['index']}: dòng tiêu đề không lặp lại ở mỗi trang")
        if spec.get("cant_split") and not all("w:cantSplit" in r._tr.xml for r in rows[1:]):
            errs.append(f"bảng {spec['index']}: có dòng bị phép ngắt giữa hai trang")
        grid_w = [int(g.get(qn("w:w"))) / 567 for g in tb._tbl.tblGrid.findall(qn("w:gridCol"))]
        if "w:tblLayout" not in tb._tbl.tblPr.xml or 'w:type="fixed"' not in tb._tbl.tblPr.xml:
            errs.append(f"bảng {spec['index']}: chưa đặt bố cục cố định nên Word có thể co giãn cột")
        if sum(grid_w) > 16.1 or sum(grid_w) < 15.0:
            errs.append(f"bảng {spec['index']}: tổng bề rộng {sum(grid_w):.1f} cm, không khớp vùng chữ 16 cm")
        if grid_w and grid_w[0] < 1.4:
            errs.append(f"bảng {spec['index']}: cột STT chỉ {grid_w[0]:.1f} cm, chữ 'STT' sẽ bị tách dòng")
        if "w:shd" not in rows[0]._tr.xml:
            errs.append(f"bảng {spec['index']}: dòng tiêu đề chưa có nền phân biệt")
        body = [[c.text.strip() for c in r.cells] for r in rows[1:]]
        if not body:
            errs.append(f"bảng {spec['index']}: không có dòng dữ liệu")
            continue
        n_total = len(spec.get("total_row_prefix", "")) and 1 or 0
        data = body[:-1] if n_total else body
        if "data_rows" in spec and len(data) != spec["data_rows"]:
            errs.append(f"bảng {spec['index']}: có {len(data)} dòng dữ liệu, kỳ vọng {spec['data_rows']}")
        if spec.get("stt_continuous"):
            stt = [r[0] for r in data]
            if stt != [str(k) for k in range(1, len(data) + 1)]:
                errs.append(f"bảng {spec['index']}: cột STT không liên tục từ 1")
        if n_total and not body[-1][0].startswith(spec["total_row_prefix"]) and spec["total_row_prefix"] not in " ".join(body[-1]):
            errs.append(f"bảng {spec['index']}: thiếu dòng tổng cộng")
    for tok in lay.get("unique_tokens", []):
        c = text.count(tok)
        if c != 1:
            errs.append(f"{tok!r} xuất hiện {c} lần, kỳ vọng đúng 1 lần")
    for tok in lay.get("absent_tokens", []):
        if tok in text:
            errs.append(f"{tok!r} không được có trong file")
    need_pdf = lay.get("min_pages") or lay.get("same_page") or lay.get("figures")
    if need_pdf:
        pages = pdf_pages(path)
        if pages is None:
            log.append("  (bỏ qua kiểm số trang: không có LibreOffice/pdftotext)")
        else:
            if lay.get("min_pages") and len(pages) < lay["min_pages"]:
                errs.append(f"chỉ {len(pages)} trang, kỳ vọng ít nhất {lay['min_pages']}")
            log.append(f"  số trang thực tế: {len(pages)}")
            for k, p in enumerate(pages, 1):
                lines = [ln.strip() for ln in p.split("\n") if ln.strip()]
                for a_, b_ in zip(lines, lines[1:]):  # tiêu đề IN HOA có một chữ mồ côi ở dòng cuối
                    if len(a_) > 30 and a_ == a_.upper() and len(b_.split()) == 1 and b_ == b_.upper() and b_.isalpha() and len(b_) <= 6:
                        errs.append(f"trang {k}: tiêu đề có một chữ rơi xuống dòng riêng: {b_!r}")
                if re.search(r"^\s*STT?\s*$", p, flags=re.M) and re.search(r"^\s*T\s*$", p, flags=re.M):
                    errs.append(f"trang {k}: chữ STT bị tách thành hai dòng")
            for a, b in lay.get("same_page", []):
                if not any(a in p and b in p for p in pages):
                    errs.append(f"{a!r} và {b!r} không cùng một trang (khối ký bị tách khỏi nội dung)")
            if lay.get("page_number") and len(pages) > 1:
                app = lay.get("appendix_from_page")  # phụ lục đánh số trang riêng từ 1
                for k, p in enumerate(pages[1:], 2):
                    want = k if not app or k < app else k - app + 1
                    first = [ln.strip() for ln in p.split("\n") if ln.strip()][:1]
                    if not first or first[0] != str(want):
                        errs.append(f"trang {k} phải có số trang {want} ở đầu trang (thấy {first})")
                        break
                first1 = [ln.strip() for ln in pages[0].split("\n") if ln.strip()][:1]
                if first1 and first1[0] == "1":
                    errs.append("trang 1 không được hiện số trang")
    if lay.get("figures"):
        errs.extend(figure_errors(path, lay, pages if need_pdf else None, log))
    return errs


def pptx_text(path):
    """Văn bản trên slide (kể cả bảng) và ghi chú người trình bày."""
    from pptx import Presentation
    prs = Presentation(path)
    out = []
    for sl in prs.slides:
        for sh in sl.shapes:
            if sh.has_text_frame:
                out.extend(p.text for p in sh.text_frame.paragraphs)
            if getattr(sh, "has_table", False) and sh.has_table:
                for r in sh.table.rows:
                    for c in r.cells:
                        out.append(c.text)
        if sl.has_notes_slide:
            out.append(sl.notes_slide.notes_text_frame.text)
    return "\n".join(x for x in out if x.strip())


def _run_sizes(tf):
    for p in tf.paragraphs:
        for r in p.runs:
            yield p, r, (r.font.size.pt if r.font.size else None)


def _title_shape(sl):
    """Tiêu đề slide: placeholder kiểu title/ctrTitle (python-pptx .shapes.title chỉ nhận idx 0 nên không dùng)."""
    from pptx.enum.shapes import PP_PLACEHOLDER
    for sh in sl.shapes:
        if sh.is_placeholder and sh.placeholder_format.type in (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE):
            return sh
    return None


def deck_errors(path, expect, log):
    """Bộ slide: số slide, tiêu đề, cỡ chữ, số chữ mỗi slide, ghi chú người trình bày, trong khung và không đè nhau,
    chữ không tràn khung (ước lượng), bảng, biểu đồ gốc khớp số liệu."""
    import math

    from pptx import Presentation
    from pptx.util import Emu
    dk = expect.get("deck", {})
    prs = Presentation(path)
    W, H = prs.slide_width, prs.slide_height
    errs = []
    n = len(prs.slides)
    if not dk.get("min_slides", 1) <= n <= dk.get("max_slides", 999):
        errs.append(f"có {n} slide, kỳ vọng {dk.get('min_slides')}–{dk.get('max_slides')}")
    if dk.get("talk_minutes") and n * 1.0 > dk["talk_minutes"]:
        errs.append(f"{n} slide cho bài nói {dk['talk_minutes']} phút: chưa tới 1 phút mỗi slide")
    titles = []
    for i, sl in enumerate(prs.slides, 1):
        t = _title_shape(sl)
        ttxt = t.text_frame.text.strip() if t is not None and t.has_text_frame else ""
        if not ttxt:
            errs.append(f"slide {i}: không có tiêu đề (placeholder tiêu đề)")
        else:
            if ttxt.endswith("."):
                errs.append(f"slide {i}: tiêu đề kết thúc bằng dấu chấm")
            if len(ttxt.split()) > 16:
                errs.append(f"slide {i}: tiêu đề dài {len(ttxt.split())} chữ")
            titles.append(ttxt)
        notes = sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else ""
        if dk.get("notes_required") and len(notes.split()) < 15:
            errs.append(f"slide {i}: ghi chú người trình bày thiếu hoặc dưới 15 chữ")
        words, boxes = 0, []
        for sh in sl.shapes:
            if sh.left is None:
                continue
            if sh.left < Emu(int(0.45 * 914400)) - 1 or sh.top < 0 or sh.left + sh.width > W - Emu(int(0.45 * 914400)) + 1 or sh.top + sh.height > H - Emu(int(0.1 * 914400)):
                if sh.name not in ("Rectangle 1",) and not (t is not None and sh.shape_id == t.shape_id and False):
                    if sh.left + sh.width > W or sh.top + sh.height > H or sh.left < 0 or sh.top < 0:
                        errs.append(f"slide {i}: '{sh.name}' vượt ra ngoài khung slide")
                    elif sh.has_text_frame and sh.text_frame.text.strip() and i > 1 and sh.left < Emu(int(0.45 * 914400)):
                        errs.append(f"slide {i}: '{sh.name}' sát mép trái dưới 0,45 inch")
            is_title = t is not None and sh.shape_id == t.shape_id
            is_src = sh.name.startswith("nguon")
            if getattr(sh, "has_table", False) and sh.has_table:
                tb = sh.table
                spec = next((x for x in dk.get("tables", []) if x["slide"] == i), None)
                if spec:
                    if len(tb.rows) != spec["rows"] or len(tb.columns) != spec["cols"]:
                        errs.append(f"slide {i}: bảng {len(tb.rows)}×{len(tb.columns)}, kỳ vọng {spec['rows']}×{spec['cols']}")
                    blanks = sum(1 for r in tb.rows for c in r.cells if spec["blank_text"] in c.text)
                    if blanks != spec["blank_cells"]:
                        errs.append(f"slide {i}: có {blanks} ô '{spec['blank_text']}', kỳ vọng {spec['blank_cells']}")
                for r in tb.rows:
                    for c in r.cells:
                        words += len(c.text.split())
                        for _, run, sz in _run_sizes(c.text_frame):
                            if sz is None or sz < dk.get("min_body_pt", 14):
                                errs.append(f"slide {i}: chữ trong bảng cỡ {sz} pt, dưới {dk.get('min_body_pt', 14)} pt")
                                break
                if sh.top + sh.height > H - Emu(int(0.35 * 914400)):
                    errs.append(f"slide {i}: bảng chạm sát đáy slide")
                boxes.append((sh.name, sh.left, sh.top, sh.width, sh.height))
                continue
            if sh.has_text_frame and sh.text_frame.text.strip():
                if not is_title and not is_src:
                    words += len(sh.text_frame.text.split())
                mn = dk.get("min_title_pt", 28) if is_title else (dk.get("min_caption_pt", 11) if is_src else dk.get("min_body_pt", 14))
                est_h, bodypr = 0.0, sh.text_frame._txBody.find("{http://schemas.openxmlformats.org/drawingml/2006/main}bodyPr")
                lI = int(bodypr.get("lIns", 91440)) if bodypr is not None else 91440
                rI = int(bodypr.get("rIns", 91440)) if bodypr is not None else 91440
                tI = int(bodypr.get("tIns", 45720)) if bodypr is not None else 45720
                bI = int(bodypr.get("bIns", 45720)) if bodypr is not None else 45720
                inner_w = (sh.width - lI - rI) / 12700
                size_seen = None
                for p in sh.text_frame.paragraphs:
                    txt = "".join(r.text for r in p.runs)
                    if not txt:
                        continue
                    sz = next((r.font.size.pt for r in p.runs if r.font.size), None)
                    if sz is None and is_title:
                        sz = dk.get("min_title_pt", 28)  # cỡ lấy từ bố cục, không đọc được trực tiếp: dùng mốc tối thiểu
                    if sz is None:
                        errs.append(f"slide {i}: '{sh.name}' không đặt cỡ chữ")
                        continue
                    size_seen = sz
                    if sz < mn:
                        errs.append(f"slide {i}: '{sh.name}' chữ {sz:g} pt, dưới {mn} pt")
                    cw = 0.55 * sz * (1.08 if is_title else 1.0)
                    lines = max(1, math.ceil(len(txt) * cw / max(inner_w, 1)))
                    est_h += lines * sz * 1.2 + (8 if "bullet" in p._p.xml or "buChar" in p._p.xml else 0)
                if size_seen and est_h > ((sh.height - tI - bI) / 12700) * 1.08:
                    errs.append(f"slide {i}: '{sh.name}' có thể tràn khung (cần ~{est_h:.0f} pt, khung {(sh.height - tI - bI) / 12700:.0f} pt)")
                boxes.append((sh.name, sh.left, sh.top, sh.width, sh.height))
        if words > dk.get("max_words_per_slide", 999):
            errs.append(f"slide {i}: {words} chữ, quá dày (tối đa {dk['max_words_per_slide']})")
        for a in range(len(boxes)):
            for b in range(a + 1, len(boxes)):
                A, B = boxes[a], boxes[b]
                ox = min(A[1] + A[3], B[1] + B[3]) - max(A[1], B[1])
                oy = min(A[2] + A[4], B[2] + B[4]) - max(A[2], B[2])
                if ox > 0 and oy > 0 and ox * oy > 0.1 * min(A[3] * A[4], B[3] * B[4]):
                    errs.append(f"slide {i}: '{A[0]}' và '{B[0]}' chồng lên nhau")
    if len(set(titles)) != len(titles):
        errs.append("có hai slide trùng tiêu đề")
    for spec in dk.get("charts", []):
        sl = prs.slides[spec["slide"] - 1]
        ch = next((sh.chart for sh in sl.shapes if getattr(sh, "has_chart", False) and sh.has_chart), None)
        if ch is None:
            errs.append(f"slide {spec['slide']}: không có biểu đồ gốc (có thể là ảnh chụp)")
            continue
        got = {s.name: [float(v) for v in s.values] for s in ch.plots[0].series}
        for name, vals in spec["series"].items():
            if name not in got:
                errs.append(f"slide {spec['slide']}: biểu đồ thiếu chuỗi {name!r}")
            elif [round(x, 4) for x in got[name]] != [float(v) for v in vals]:
                errs.append(f"slide {spec['slide']}: chuỗi {name!r} trong biểu đồ là {got[name]}, kỳ vọng {vals}")
        if len(list(ch.plots[0].categories)) != len(next(iter(spec["series"].values()))):
            errs.append(f"slide {spec['slide']}: số nhãn trục khác số giá trị")
    log.append(f"  {n} slide")
    return errs


def check_one(expect, samples, outputs, results, log):
    errs = []
    name = expect["skill"]
    inp = (samples / f"{name}.input.json").read_text(encoding="utf-8")
    path = outputs / expect["output"]
    if not path.is_file():
        return [f"không thấy file {path.name}"]
    magic = path.read_bytes()[:4]
    if magic != b"PK\x03\x04":
        return ["không phải gói OOXML thật (đuôi file giả?)"]
    dates_ok, nums_ok = allowed_tokens(inp)
    for spec in expect.get("layout", {}).get("tables", []):  # số thứ tự dòng (STT) là số do bảng tự sinh
        nums_ok |= {str(k) for k in range(1, spec.get("data_rows", 0) + 1) if k >= 100}
    for s in expect.get("allowed_derived", []):  # số suy ra bằng phép tính từ đầu vào (tổng cộng...)
        nums_ok |= set(re.findall(r"\d{3,}", str(s)))
    wb_values = None
    try:
        if expect["kind"] == "docx":
            docx_text(path)
        elif expect["kind"] == "pptx":
            pptx_text(path)
        else:
            xlsx_load(path)
    except Exception as e:  # file hỏng: báo lỗi, không làm sập bộ kiểm tra
        return [f"không mở được bằng thư viện ({type(e).__name__})"]
    if expect["kind"] == "pptx":
        text = pptx_text(path)
        nums = []
        errs.extend(deck_errors(path, expect, log))
    elif expect["kind"] == "docx":
        text = docx_text(path)
        nums = []
        if expect.get("nd30_format"):
            errs.extend(nd30_format_errors(path))
        if expect.get("layout"):
            errs.extend(layout_errors(path, expect, text, log))
    else:
        wb = xlsx_load(path)
        text, nums = xlsx_text_and_numbers(wb)
        sheets = [ws.title for ws in wb.worksheets]
        for s in expect.get("sheets", []):
            if s not in sheets:
                errs.append(f"thiếu sheet {s}")
        for s in expect.get("must_not_have_sheets", []):
            if s in sheets:
                errs.append(f"không được có sheet {s}")
        if "charts" in expect:  # biểu đồ gốc trong Excel và thiết lập in
            ws0 = wb.worksheets[0]
            if len(ws0._charts) != expect["charts"]:
                errs.append(f"có {len(ws0._charts)} biểu đồ, kỳ vọng {expect['charts']}")
            if expect.get("fit_to_width") and not (ws0.sheet_properties.pageSetUpPr and ws0.sheet_properties.pageSetUpPr.fitToPage and ws0.page_setup.fitToWidth == 1):
                errs.append("chưa đặt vừa chiều rộng trang khi in: bảng và biểu đồ sẽ bị cắt giữa các trang")
            if not ws0.print_title_rows:
                errs.append("chưa đặt lặp dòng tiêu đề khi in")
        wb_values = recalc(path)
        if wb_values is not None:
            for sheet, cells in expect.get("computed_approx", {}).items():
                for ref, want in cells.items():
                    got = wb_values[sheet][ref].value
                    if not isinstance(got, (int, float)) or abs(got - want) > 0.006:
                        errs.append(f"{sheet}!{ref}: được {got!r}, kỳ vọng xấp xỉ {want!r}")
        if wb_values is None:
            log.append("  (bỏ qua kiểm công thức: không có LibreOffice)")
        else:
            for sheet, cells in expect.get("computed", {}).items():
                for ref, want in cells.items():
                    got = wb_values[sheet][ref].value
                    got = "" if got is None else got
                    if got != want:
                        errs.append(f"{sheet}!{ref}: được {got!r}, kỳ vọng {want!r}")
            for ws in wb_values.worksheets:  # không để lỗi công thức
                for row in ws.iter_rows():
                    for c in row:
                        if isinstance(c.value, str) and c.value.startswith("#"):
                            errs.append(f"lỗi công thức {ws.title}!{c.coordinate}: {c.value}")
    for bad in GLOBAL_FORBIDDEN + expect.get("must_not_contain", []):
        if bad in text:
            errs.append(f"có chuỗi bị cấm: {bad!r}")
    for need in expect.get("must_contain", []):
        if need not in text:
            errs.append(f"thiếu chuỗi bắt buộc: {need!r}")
    for d in set(re.findall(r"\d{1,2}/\d{1,2}/\d{4}", text)):
        if d not in dates_ok:
            errs.append(f"ngày không có trong đầu vào (nghi bịa): {d}")
    for n in set(re.findall(r"\d{3,}", text)):
        if n not in nums_ok:
            errs.append(f"số không có trong đầu vào (nghi bịa): {n}")
    for v in nums:
        val = v * 100 if 0 < v < 1 else v  # ô phần trăm lưu dạng 0–1
        if float(val).is_integer() and len(str(int(val))) >= 3:
            sv = str(int(val))
            if sv not in nums_ok and sv not in expect.get("allowed_derived", []):
                errs.append(f"số trong ô không có trong đầu vào: {sv}")
    for label in expect.get("blank_labels", []):
        lines = [ln for ln in text.split("\n") if ln.strip().startswith(label)]
        if not lines:
            errs.append(f"không thấy nhãn cần chừa chỗ: {label!r}")
        elif not any(re.search(r"\.{4,}|…", ln) or ln.strip() == label for ln in lines) and \
                not any(re.search(r"\.{4,}", t) for t in _following(text, label)):
            errs.append(f"nhãn {label!r} chưa chừa chỗ điền (dòng dấu chấm)")
    findings = results / f"{name}.findings.md"
    if expect.get("traps"):
        if not findings.is_file():
            errs.append("thiếu file ghi nhận phát hiện (findings.md)")
        else:
            ft = findings.read_text(encoding="utf-8")
            for t in expect["traps"]:
                if t["id"] not in ft:
                    errs.append(f"findings chưa ghi nhận: {t['id']}")
    return errs


def _following(text, label):
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip().startswith(label):
            return lines[i + 1:i + 2]
    return []


def main():
    ap = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    ap.add_argument("--samples", default=root / "tests/samples")
    ap.add_argument("--outputs", default=root / "tests/outputs")
    ap.add_argument("--results", default=root / "tests/results")
    a = ap.parse_args()
    samples, outputs, results = Path(a.samples), Path(a.outputs), Path(a.results)
    failed = 0
    summary = {}
    for ep in sorted(samples.glob("*.expect.json")):
        expect = json.loads(ep.read_text(encoding="utf-8"))
        log = []
        errs = check_one(expect, samples, outputs, results, log)
        summary[expect["skill"]] = {"dat": not errs, "loi": errs}
        if log:
            summary[expect["skill"]]["ghi_chu"] = [x.strip() for x in log]
        failed += bool(errs)
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
