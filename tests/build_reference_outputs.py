"""Dựng file đầu ra mẫu từ dữ liệu giả, đóng vai AI làm theo SKILL.md của 3 skill.

Mục đích: tạo bằng chứng chạy thử có thể kiểm bằng scripts/check_outputs.py. Đây không phải
bộ sinh văn bản dùng thật: nó chỉ chứng minh các hướng dẫn trong skill làm theo được và kiểm tra được.
Dùng: python -X utf8 tests/build_reference_outputs.py
"""
import json
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = Path(__file__).resolve().parent
S, O = HERE / "samples", HERE / "outputs"
O.mkdir(exist_ok=True)
DOT = "." * 12
FONT = "Times New Roman"


def load(n):
    return json.loads((S / n).read_text(encoding="utf-8"))


# ---------- tiện ích Word ----------
def new_doc():
    d = Document()
    sec = d.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin = sec.bottom_margin = Cm(2.0)
    sec.left_margin, sec.right_margin = Cm(3.0), Cm(2.0)
    st = d.styles["Normal"]
    st.font.name, st.font.size = FONT, Pt(13)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    st.paragraph_format.space_after = Pt(0)
    return d


def para(d_or_cell, text="", bold=False, italic=False, size=None, align=None, first_indent=None, after=6, keep=False):
    p = d_or_cell.add_paragraph()
    r = p.add_run(text)
    r.bold, r.italic = bold, italic
    r.font.name = FONT
    r._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    if size:
        r.font.size = Pt(size)
    if align is not None:
        p.alignment = align
    pf = p.paragraph_format
    pf.space_after = Pt(after)
    if first_indent:
        pf.first_line_indent = Cm(first_indent)
    pf.keep_with_next = keep
    return p


def cell_text(cell, lines, size=12, bold=False, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    first = True
    for ln in lines:
        p = cell.paragraphs[0] if first else cell.add_paragraph()
        first = False
        r = p.add_run(ln)
        r.bold = bold
        r.font.size = Pt(size)
        r.font.name = FONT
        r._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
        p.alignment = align
        p.paragraph_format.space_after = Pt(0)


def borders(table, on=True):
    tbl = table._tbl
    pr = tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
        x = OxmlElement(f"w:{e}")
        x.set(qn("w:val"), "single" if on else "nil")
        x.set(qn("w:sz"), "4")
        x.set(qn("w:color"), "000000")
        b.append(x)
    pr.append(b)


def header_block(d, left_lines, right_lines):
    t = d.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    borders(t, False)
    t.autofit = False
    t.columns[0].width, t.columns[1].width = Cm(6.6), Cm(9.4)
    cell_text(t.cell(0, 0), left_lines[0], size=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    for i, p in enumerate(t.cell(0, 0).paragraphs):
        for r in p.runs:
            r.bold = left_lines[1][i] if i < len(left_lines[1]) else False
    cell_text(t.cell(0, 1), right_lines[0], size=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    for i, p in enumerate(t.cell(0, 1).paragraphs):
        for r in p.runs:
            r.bold = right_lines[1][i] if i < len(right_lines[1]) else False
    return t


def sign_block(d, lines, bold_flags):
    t = d.add_table(rows=1, cols=2)
    borders(t, False)
    t.autofit = False
    t.columns[0].width, t.columns[1].width = Cm(8.0), Cm(8.0)
    return t


# ---------- 1. Công văn (soan-cong-van) ----------
def build_cong_van():
    i = load("soan-cong-van.input.json")
    d = new_doc()
    cvd = i["cong_van_den"]
    vv = i["trich_yeu"]
    if vv.lower().startswith("về việc "):
        vv = vv[len("về việc "):]
    left = ([i["co_quan_chu_quan"], i["co_quan_ban_hanh"], f"Số: {DOT}/{'.' * 6}-{i['ky_hieu_don_vi_soan']}", f"V/v {vv}"],
            [False, True, False, False])
    right = (["CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", "Độc lập – Tự do – Hạnh phúc", f"{i['dia_danh']}, ngày ..... tháng ..... năm ........"],
             [True, True, False])
    t = header_block(d, left, right)
    t.cell(0, 1).paragraphs[2].runs[0].italic = True
    para(d, "", after=6)
    para(d, f"Kính gửi: {i['noi_nhan'][0]}", bold=False, align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
    para(d, (f"Phúc đáp Công văn số {cvd['so_ky_hieu']} ngày {cvd['ngay']} của {cvd['co_quan']} "
             f"về việc {cvd['ve_viec']}, {i['co_quan_ban_hanh'].title().replace('Đại Học', 'Đại học')} có ý kiến như sau:"),
         first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    for n, ln in enumerate(i["noi_dung"], 1):
        para(d, f"{n}. {ln}", first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    para(d, "Trân trọng cảm ơn sự phối hợp của Quý Cơ quan./.", first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=10)
    # nơi nhận + chữ ký
    sg = i["nguoi_ky"]
    t2 = d.add_table(rows=1, cols=2)
    borders(t2, False)
    t2.autofit = False
    t2.columns[0].width, t2.columns[1].width = Cm(7.5), Cm(8.5)
    cell_text(t2.cell(0, 0), ["Nơi nhận:", "- Như trên;", f"- {i['noi_nhan'][-1]}."], size=12)
    t2.cell(0, 0).paragraphs[0].runs[0].bold = True
    t2.cell(0, 0).paragraphs[0].runs[0].italic = True
    cell_text(t2.cell(0, 1), [sg["hinh_thuc"], sg["chuc_danh"].upper(), "", "", "", sg["ho_ten"]], size=13,
              bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    out = O / "soan-cong-van.docx"
    d.save(out)
    return out


# ---------- 2. Kế hoạch thanh tra (ke-hoach-thanh-tra-nam) ----------
def doan_text(c):
    dn = c["doan"]
    if not dn:
        return [f"Trưởng đoàn: {DOT}", f"Thành viên: {DOT}"]
    tv = "; ".join(f"{m['ten']} ({m['don_vi']})" for m in dn["thanh_vien"])
    return [f"Trưởng đoàn: {dn['truong_doan']['ten']} ({dn['truong_doan']['don_vi']})", f"Thành viên: {tv}"]


def build_thanh_tra():
    i = load("ke-hoach-thanh-tra-nam.input.json")
    d = new_doc()
    left = ([i["co_quan_ban_hanh"], f"Số: {DOT}/KH-{'.' * 6}"], [True, False])
    right = (["CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", "Độc lập – Tự do – Hạnh phúc", f"{i['dia_danh']}, ngày ..... tháng ..... năm ........"],
             [True, True, False])
    t = header_block(d, left, right)
    t.cell(0, 1).paragraphs[2].runs[0].italic = True
    para(d, "", after=4)
    para(d, "KẾ HOẠCH", bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
    para(d, f"Thanh tra nội bộ năm {i['nam_ke_hoach']}", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=10)
    para(d, "I. MỤC ĐÍCH, YÊU CẦU", bold=True, keep=True)
    para(d, "1. Mục đích", bold=True, italic=False, keep=True)
    para(d, DOT * 6, first_indent=1.0)
    para(d, "2. Yêu cầu", bold=True, keep=True)
    para(d, DOT * 6, first_indent=1.0)
    para(d, "II. NỘI DUNG THANH TRA", bold=True, keep=True)
    tb = d.add_table(rows=1, cols=5)
    borders(tb, True)
    tb.autofit = False
    widths = [Cm(1.2), Cm(4.2), Cm(2.8), Cm(2.0), Cm(5.8)]
    for c, h in enumerate(["STT", "Nội dung thanh tra", "Đối tượng", "Thời gian", "Đoàn thanh tra"]):
        cell_text(tb.rows[0].cells[c], [h], bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=11)
    for cu in i["cuoc_thanh_tra"]:
        r = tb.add_row().cells
        cell_text(r[0], [str(cu["stt"])], size=11, align=WD_ALIGN_PARAGRAPH.CENTER)
        cell_text(r[1], [cu["noi_dung"]], size=11)
        cell_text(r[2], [cu["doi_tuong"]], size=11)
        cell_text(r[3], [cu["thoi_gian"]], size=11)
        cell_text(r[4], doan_text(cu), size=11)
    for c, w in enumerate(widths):
        tb.columns[c].width = w
    for row in tb.rows:
        for c, w in enumerate(widths):
            row.cells[c].width = w
    para(d, "", after=4)
    para(d, "III. PHƯƠNG PHÁP THANH TRA", bold=True, keep=True)
    for ln in ["1. Kiểm tra hồ sơ, sổ sách; đối chiếu số liệu giữa các nguồn.",
               "2. Làm việc trực tiếp, phỏng vấn người liên quan; việc phỏng vấn phải lập biên bản.",
               "3. Khảo sát, lấy ý kiến các bên liên quan khi cần.",
               "4. Lĩnh vực tài chính, văn bằng, chứng chỉ phải có đối chiếu số liệu độc lập."]:
        para(d, ln, first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=3)
    para(d, "IV. TỔ CHỨC THỰC HIỆN", bold=True, keep=True)
    for ln in ["1. Phòng Thanh tra & Pháp chế chủ trì, tham mưu thành lập đoàn thanh tra cho từng cuộc và theo dõi việc thực hiện kế hoạch.",
               "2. Các đơn vị được thanh tra phối hợp, cung cấp hồ sơ, số liệu và bố trí người làm việc với đoàn thanh tra.",
               "3. Trong năm, khi có dấu hiệu vi phạm hoặc đơn thư phản ánh, Hiệu trưởng quyết định thanh tra đột xuất. Việc điều chỉnh, bổ sung kế hoạch phải trình Hiệu trưởng phê duyệt lại."]:
        para(d, ln, first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=3)
    para(d, "", after=6)
    t2 = d.add_table(rows=1, cols=2)
    borders(t2, False)
    t2.autofit = False
    t2.columns[0].width, t2.columns[1].width = Cm(7.5), Cm(8.5)
    cell_text(t2.cell(0, 0), ["Nơi nhận:", "- Các đơn vị được thanh tra và đơn vị liên quan (để thực hiện);", f"- Lưu: VT, {'.' * 6}."], size=12)
    t2.cell(0, 0).paragraphs[0].runs[0].bold = True
    t2.cell(0, 0).paragraphs[0].runs[0].italic = True
    sg = i["nguoi_ky"]
    cell_text(t2.cell(0, 1), [sg["chuc_danh"], "", "", "", sg["ho_ten"] or DOT], size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    out = O / "ke-hoach-thanh-tra-nam.docx"
    d.save(out)
    return out


# ---------- 3. PMO (pmo-quan-tri-du-an) ----------
HFILL = PatternFill("solid", fgColor="D9E2F3")
THIN = Side(style="thin", color="808080")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def d2(s):
    return datetime.strptime(s, "%d/%m/%Y") if s else None


def style_table(ws, header_row, last_row, ncols):
    for c in range(1, ncols + 1):
        h = ws.cell(row=header_row, column=c)
        h.font, h.fill = Font(bold=True, name="Arial", size=10), HFILL
        h.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
    for r in range(header_row, last_row + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.border = BORDER
            if r > header_row:
                cell.font = Font(name="Arial", size=10)
                cell.alignment = Alignment(wrap_text=True, vertical="top")


def build_pmo():
    i = load("pmo-quan-tri-du-an.input.json")
    wb = Workbook()
    # --- Tracker ---
    ws = wb.active
    ws.title = "Tracker"
    ws["A1"] = f"Tracker tiến độ – {i['ten_du_an']} – Kỳ báo cáo {i['ky_bao_cao']}"
    ws["A1"].font = Font(bold=True, size=12, name="Arial")
    heads = ["Mã", "Gói việc", "Mốc hoàn thành", "Người phụ trách", "Sản phẩm bàn giao", "Ngân sách phân bổ (triệu đồng)",
             "% kế hoạch", "% thực tế", "Chênh lệch (điểm %)", "Trạng thái", "Minh chứng"]
    HR = 3
    for c, h in enumerate(heads, 1):
        ws.cell(row=HR, column=c, value=h)
    r = HR
    for w in i["workplan"]:
        r += 1
        ws.cell(row=r, column=1, value=w["ma"])
        ws.cell(row=r, column=2, value=w["ten"])
        ws.cell(row=r, column=3, value=d2(w["moc"])).number_format = "dd/mm/yyyy"
        ws.cell(row=r, column=4, value=w["phu_trach"])
        ws.cell(row=r, column=5, value=w["deliverable"])
        ws.cell(row=r, column=6, value=w["ngan_sach"])
        ws.cell(row=r, column=7, value=w["pct_ke_hoach"] / 100).number_format = "0%"
        # % thực tế chỉ nhận khi có minh chứng
        if w["minh_chung"]:
            ws.cell(row=r, column=8, value=w["pct_thuc_te"] / 100).number_format = "0%"
        else:
            ws.cell(row=r, column=8).number_format = "0%"
        ws.cell(row=r, column=9, value=f'=IF(H{r}="","",(H{r}-G{r})*100)').number_format = "0"
        ws.cell(row=r, column=10, value=(f'=IF(H{r}="","",IF(H{r}=1,"Hoàn thành",IF(I{r}>=-5,"Đúng tiến độ",'
                                         f'IF(I{r}>-10,"Có nguy cơ chậm","Chậm"))))'))
        ws.cell(row=r, column=11, value=w["minh_chung"])
    first, last = HR + 1, r
    tot = last + 1
    ws.cell(row=tot, column=2, value="Tổng ngân sách phân bổ theo gói việc").font = Font(bold=True, name="Arial", size=10)
    ws.cell(row=tot, column=6, value=f"=SUM(F{first}:F{last})").font = Font(bold=True, name="Arial", size=10)
    style_table(ws, HR, tot, len(heads))
    for col, wd in zip("ABCDEFGHIJK", [7, 34, 13, 18, 34, 15, 10, 10, 12, 16, 34]):
        ws.column_dimensions[col].width = wd
    ws.freeze_panes = ws.cell(row=HR + 1, column=3)
    ws.page_setup.orientation, ws.page_setup.fitToWidth, ws.page_setup.fitToHeight = "landscape", 1, 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    # --- Issue log ---
    wi = wb.create_sheet("Issue log")
    wi["A1"], wi["A2"] = "Ngày đối chiếu hạn xử lý:", d2(i["ngay_chay_thu"])
    wi["B2"].number_format = "dd/mm/yyyy"
    wi["A2"] = "Ngày đối chiếu hạn xử lý:"
    wi["B2"] = d2(i["ngay_chay_thu"])
    wi["A1"] = f"Issue log – {i['ten_du_an']}"
    wi["A1"].font = Font(bold=True, size=12, name="Arial")
    ih = ["Mã", "Mô tả vấn đề", "Mức độ", "Người xử lý", "Hạn xử lý", "Trạng thái", "Ngày ghi nhận", "Quá hạn chưa đóng"]
    for c, h in enumerate(ih, 1):
        wi.cell(row=4, column=c, value=h)
    r = 4
    for it in i["issue_trong_ky"]:
        r += 1
        wi.cell(row=r, column=1, value=it["ma"])
        wi.cell(row=r, column=2, value=it["mo_ta"])
        wi.cell(row=r, column=3, value=it["muc_do"])
        wi.cell(row=r, column=4, value=it["nguoi_xu_ly"])
        wi.cell(row=r, column=5, value=d2(it["han_xu_ly"])).number_format = "dd/mm/yyyy"
        wi.cell(row=r, column=6, value=it["trang_thai"])
        wi.cell(row=r, column=7, value=d2(it["ngay_ghi_nhan"])).number_format = "dd/mm/yyyy"
        wi.cell(row=r, column=8, value=f'=IF(AND(E{r}<>"",F{r}<>"đóng",E{r}<$B$2),"Quá hạn","")')
    style_table(wi, 4, r, len(ih))
    wi["A2"].font = Font(bold=True, name="Arial", size=10)
    for col, wd in zip("ABCDEFGH", [8, 48, 12, 18, 13, 14, 14, 16]):
        wi.column_dimensions[col].width = wd
    # --- Risk log ---
    wr = wb.create_sheet("Risk log")
    wr["A1"] = f"Risk log – {i['ten_du_an']}"
    wr["A1"].font = Font(bold=True, size=12, name="Arial")
    rh = ["Mã", "Rủi ro", "Xác suất", "Mức tác động", "Biện pháp giảm thiểu", "Người theo dõi", "Hạn rà soát lại"]
    for c, h in enumerate(rh, 1):
        wr.cell(row=3, column=c, value=h)
    r = 3
    for it in i["risk_hien_co"]:
        r += 1
        wr.cell(row=r, column=1, value=it["ma"])
        wr.cell(row=r, column=2, value=it["mo_ta"])
        wr.cell(row=r, column=3, value=it["xac_suat"])
        wr.cell(row=r, column=4, value=it["tac_dong"])
        wr.cell(row=r, column=5, value=it["giam_thieu"])
        wr.cell(row=r, column=6, value=it["nguoi_theo_doi"])
        wr.cell(row=r, column=7, value=d2(it["han_ra_soat"])).number_format = "dd/mm/yyyy"
    style_table(wr, 3, r, len(rh))
    for col, wd in zip("ABCDEFG", [8, 46, 12, 14, 46, 18, 14]):
        wr.column_dimensions[col].width = wd
    # --- Dashboard ---
    wd_ = wb.create_sheet("Dashboard", 0)
    wd_["A1"] = "DASHBOARD DỰ ÁN"
    wd_["A1"].font = Font(bold=True, size=14, name="Arial")
    rows = [("Dự án", i["ten_du_an"]), ("Chủ nhiệm dự án", i["chu_du_an"]), ("Kỳ báo cáo", i["ky_bao_cao"])]
    r = 2
    for k, v in rows:
        r += 1
        wd_.cell(row=r, column=1, value=k).font = Font(bold=True, name="Arial", size=10)
        wd_.cell(row=r, column=2, value=v)
    r += 2
    wd_.cell(row=r, column=1, value="1. Tiến độ tổng thể").font = Font(bold=True, name="Arial", size=11)
    t = f"Tracker!"
    stats = [
        ("% kế hoạch (trung bình các gói việc)", f"=AVERAGE({t}G{first}:G{last})", "0%"),
        ("% thực tế (chỉ tính khi mọi gói việc đã có minh chứng)", f'=IF(COUNT({t}H{first}:H{last})=COUNTA({t}A{first}:A{last}),AVERAGE({t}H{first}:H{last}),"")', "0%"),
        ("Số gói việc: Hoàn thành", f'=COUNTIF({t}J{first}:J{last},"Hoàn thành")', "0"),
        ("Số gói việc: Đúng tiến độ", f'=COUNTIF({t}J{first}:J{last},"Đúng tiến độ")', "0"),
        ("Số gói việc: Có nguy cơ chậm", f'=COUNTIF({t}J{first}:J{last},"Có nguy cơ chậm")', "0"),
        ("Số gói việc: Chậm", f'=COUNTIF({t}J{first}:J{last},"Chậm")', "0"),
        ("Ngân sách được duyệt (triệu đồng)", i["ngan_sach"]["tong_duoc_duyet"], "0"),
        ("Tổng ngân sách phân bổ theo gói việc (triệu đồng)", f"={t}F{tot}", "0"),
    ]
    for k, v, fmt in stats:
        r += 1
        wd_.cell(row=r, column=1, value=k)
        c = wd_.cell(row=r, column=2, value=v)
        c.number_format = fmt
        c.alignment = Alignment(horizontal="left")
    r += 2
    wd_.cell(row=r, column=1, value="2. Vấn đề nghiêm trọng nhất (theo mức độ)").font = Font(bold=True, name="Arial", size=11)
    r += 1
    for c, h in enumerate(["Mã", "Mô tả", "Mức độ", "Người xử lý", "Hạn xử lý"], 1):
        wd_.cell(row=r, column=c, value=h)
    hdr = r
    order = {"nghiêm trọng": 0, "trung bình": 1, "nhẹ": 2}
    for it in sorted(i["issue_trong_ky"], key=lambda x: order[x["muc_do"]])[:3]:
        r += 1
        for c, v in enumerate([it["ma"], it["mo_ta"], it["muc_do"], it["nguoi_xu_ly"], d2(it["han_xu_ly"])], 1):
            cell = wd_.cell(row=r, column=c, value=v)
            if c == 5:
                cell.number_format = "dd/mm/yyyy"
    style_table(wd_, hdr, r, 5)
    r += 2
    wd_.cell(row=r, column=1, value="3. Rủi ro hàng đầu").font = Font(bold=True, name="Arial", size=11)
    r += 1
    for c, h in enumerate(["Mã", "Rủi ro", "Xác suất", "Mức tác động", "Biện pháp giảm thiểu"], 1):
        wd_.cell(row=r, column=c, value=h)
    hdr = r
    rk = i["risk_hien_co"][:3]
    for k in range(3):
        r += 1
        if k < len(rk):
            it = rk[k]
            for c, v in enumerate([it["ma"], it["mo_ta"], it["xac_suat"], it["tac_dong"], it["giam_thieu"]], 1):
                wd_.cell(row=r, column=c, value=v)
    style_table(wd_, hdr, r, 5)
    r += 2
    wd_.cell(row=r, column=1, value="4. Quyết định cần lãnh đạo viện").font = Font(bold=True, name="Arial", size=11)
    r += 1
    for c, h in enumerate(["STT", "Nội dung quyết định", "Phương án đề xuất", "Hạn quyết định", "Hậu quả nếu không quyết"], 1):
        wd_.cell(row=r, column=c, value=h)
    hdr = r
    for _ in range(max(len(i["quyet_dinh_can_lanh_dao"]), 2)):
        r += 1
    style_table(wd_, hdr, r, 5)
    for col, wd in zip("ABCDE", [50, 52, 22, 22, 40]):
        wd_.column_dimensions[col].width = wd
    wd_.page_setup.orientation, wd_.page_setup.fitToWidth, wd_.page_setup.fitToHeight = "landscape", 1, 1
    wd_.sheet_properties.pageSetUpPr.fitToPage = True
    out = O / "pmo-quan-tri-du-an.xlsx"
    wb.save(out)
    return out


# ---------- 4. Quyết định hành chính (soan-quyet-dinh-hc) ----------
def build_quyet_dinh():
    i = load("soan-quyet-dinh-hc.input.json")
    d = new_doc()
    left = ([i["co_quan_chu_quan"], i["co_quan_ban_hanh"], f"Số: {DOT}/QĐ-{'.' * 6}"], [False, True, False])
    right = (["CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", "Độc lập – Tự do – Hạnh phúc", f"{i['dia_danh']}, ngày ..... tháng ..... năm ........"],
             [True, True, False])
    t = header_block(d, left, right)
    t.cell(0, 1).paragraphs[2].runs[0].italic = True
    para(d, "", after=4)
    para(d, "QUYẾT ĐỊNH", bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER, after=0)
    para(d, f"Về việc {i['trich_yeu']}", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
    para(d, f"HIỆU TRƯỞNG {i['co_quan_ban_hanh']}", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
    for k, c in enumerate(i["can_cu"]):
        end = ";" if k < len(i["can_cu"]) - 1 else ";"
        c = c.split(" (")[0]
        para(d, f"Căn cứ {c}{end}" if not c.startswith(("Tờ trình",)) else f"Xét đề nghị của {c.split(' của ')[-1]} tại {c.split(' của ')[0]};",
             first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    para(d, "QUYẾT ĐỊNH:", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=8)
    nd = i["noi_dung"]
    for n, key in enumerate(("dieu_1", "dieu_2", "dieu_3"), 1):
        para(d, f"Điều {n}. {nd[key]}", first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    para(d, "Danh sách thành viên: " + DOT * 4, first_indent=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=10)
    sg = i["nguoi_ky"]
    t2 = d.add_table(rows=1, cols=2)
    borders(t2, False)
    t2.autofit = False
    t2.columns[0].width, t2.columns[1].width = Cm(7.5), Cm(8.5)
    nn = ["Nơi nhận:"] + [f"- {x};" for x in i["noi_nhan"][:-1]] + [f"- {i['noi_nhan'][-1]}."]
    cell_text(t2.cell(0, 0), nn, size=12)
    t2.cell(0, 0).paragraphs[0].runs[0].bold = True
    t2.cell(0, 0).paragraphs[0].runs[0].italic = True
    cell_text(t2.cell(0, 1), [sg["chuc_danh"].upper(), "", "", "", sg["ho_ten"]], size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    out = O / "soan-quyet-dinh-hc.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    for f in (build_cong_van, build_thanh_tra, build_pmo, build_quyet_dinh):
        print("đã tạo", f())
