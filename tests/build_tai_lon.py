"""Thử tải lớn: file nhiều dữ liệu, nhiều trang (danh sách 140+ sinh viên, biên bản 40 người dự, kế hoạch 45 nhiệm vụ).

Sinh dữ liệu giả (cố định, lặp lại được) vào tests/samples, dựng file Word theo SKILL.md và ghi kỳ vọng.
Kiểm tra bằng: python -X utf8 scripts/check_outputs.py  (có LibreOffice thì kiểm cả số trang và số trang ở đầu trang)
Dùng: python -X utf8 tests/build_tai_lon.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_reference_outputs import *  # noqa: F401,F403
from build_reference_outputs import DOT, FONT, O, S, borders, cell_text, header_block, new_doc, para

HERE = Path(__file__).resolve().parent
R = HERE / "results"
C, J, L = WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.JUSTIFY, WD_ALIGN_PARAGRAPH.LEFT
NOTE = "Dữ liệu GIẢ để thử tải lớn. Tên cơ quan, người, mã số đều là mẫu."
CQ, TR = "CƠ QUAN CHỦ QUẢN (MẪU)", "TRƯỜNG ĐẠI HỌC MẪU A"
HO = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", "Đỗ", "Ngô"]
DEM = ["Văn", "Thị", "Minh", "Thu", "Quốc", "Ngọc", "Hữu", "Thanh"]
TEN = ["An", "Bình", "Châu", "Dũng", "Giang", "Hà", "Hải", "Hiếu", "Hoa", "Hùng", "Huy", "Khánh", "Lan", "Linh", "Long",
       "Mai", "Nam", "Nga", "Ngọc", "Phong", "Phúc", "Quân", "Quỳnh", "Sơn", "Thảo", "Thắng", "Trang", "Tuấn", "Vân", "Việt", "Yến"]


def ten_nguoi(i):
    return f"{HO[i % 10]} {DEM[(i // 10) % 8]} {TEN[i % 31]}"


def money(v):
    return f"{v:,}".replace(",", ".")


def parse_money(s):
    return int(s.replace(".", ""))


# ---------- tiện ích Word cho file nhiều trang ----------
def page_number(d):
    sec = d.sections[0]
    sec.different_first_page_header_footer = True  # NĐ 30/2020: số trang từ trang 2
    sec.header_distance = Cm(1.25)
    p = sec.header.paragraphs[0]
    p.alignment = C
    r = p.add_run()
    r.font.name, r.font.size = FONT, Pt(13)
    for kind, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if kind:
            e = OxmlElement("w:fldChar")
            e.set(qn("w:fldCharType"), kind)
        else:
            e = OxmlElement("w:instrText")
            e.set(qn("xml:space"), "preserve")
            e.text = txt
        r._r.append(e)


def mark_row(row, header=False, keep=True):
    trPr = row._tr.get_or_add_trPr()
    if keep:
        trPr.append(OxmlElement("w:cantSplit"))
    if header:
        trPr.append(OxmlElement("w:tblHeader"))


def _shade(cell, fill="D9D9D9"):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:color"), "auto")
    sh.set(qn("w:fill"), fill)
    tcPr.append(sh)


def _valign(cell, val="center"):
    tcPr = cell._tc.get_or_add_tcPr()
    v = OxmlElement("w:vAlign")
    v.set(qn("w:val"), val)
    tcPr.append(v)


def grid(d, headers, rows, widths, total=None, aligns=None, size=12):
    """Bảng chuẩn: bố cục cố định theo tổng bề rộng vùng chữ, cột STT đủ rộng, tiêu đề đậm có nền xám và lặp mỗi trang,
    chữ cỡ 12, căn giữa theo chiều dọc, dòng không bị cắt giữa hai trang."""
    t = d.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.autofit = False
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = t._tbl.tblPr
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)
    for e in tblPr.findall(qn("w:tblW")):
        tblPr.remove(e)
    w = OxmlElement("w:tblW")
    w.set(qn("w:w"), str(round(sum(widths) * 567)))
    w.set(qn("w:type"), "dxa")
    tblPr.append(w)
    for k, h in enumerate(headers):
        cell_text(t.rows[0].cells[k], [h], size=size, bold=True, align=C)
        _shade(t.rows[0].cells[k])
    mark_row(t.rows[0], header=True)
    for r in rows:
        cells = t.add_row().cells
        for k, v in enumerate(r):
            cell_text(cells[k], [v], size=size, align=(aligns[k] if aligns else L))
        mark_row(t.rows[-1])
    if total:
        cells = t.add_row().cells
        for k, v in enumerate(total):
            cell_text(cells[k], [v], size=size, bold=True, align=L)
            _shade(cells[k], "F2F2F2")
        mark_row(t.rows[-1])
    for k, wd in enumerate(widths):
        t.columns[k].width = Cm(wd)  # cập nhật lưới cột để Word/LibreOffice đều theo đúng bề rộng
    for row in t.rows:
        for k, wd in enumerate(widths):
            row.cells[k].width = Cm(wd)
            _valign(row.cells[k])
            for p in row.cells[k].paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
    return t


def head(d, i, ky_hieu):
    left = ([i["co_quan_chu_quan"], i["co_quan_ban_hanh"], f"Số: {'.' * 6}/{ky_hieu}-{'.' * 6}"], [False, True, False])
    right = (["CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", "Độc lập – Tự do – Hạnh phúc", f"{i['dia_danh']}, ngày ..... tháng ..... năm ........"],
             [True, True, False])
    t = header_block(d, left, right)
    t.cell(0, 1).paragraphs[2].runs[0].italic = True
    para(d, "", after=4)


def sign(d, noi_nhan, chuc_danh, ho_ten):
    t = d.add_table(rows=1, cols=2)
    borders(t, False)
    t.autofit = False
    t.columns[0].width, t.columns[1].width = Cm(7.5), Cm(8.5)
    nn = ["Nơi nhận:"] + [f"- {x};" for x in noi_nhan[:-1]] + [f"- {noi_nhan[-1]}."]
    cell_text(t.cell(0, 0), nn, size=12)
    t.cell(0, 0).paragraphs[0].runs[0].bold = True
    t.cell(0, 0).paragraphs[0].runs[0].italic = True
    cell_text(t.cell(0, 1), [chuc_danh.upper(), "", "", "", ho_ten or DOT], size=13, bold=True, align=C)
    mark_row(t.rows[0])


def keep_together(d, n_last):
    """Giữ n_last đoạn cuối trước khối ký dính với khối ký để chữ ký không đứng một mình ở trang mới."""
    ps = d.paragraphs
    for p in ps[-n_last:]:
        p.paragraph_format.keep_with_next = True


def dump(name, inp, expect, findings):
    (S / f"{name}.input.json").write_text(json.dumps({"_ghi_chu": NOTE, **inp}, ensure_ascii=False, indent=1), encoding="utf-8")
    e = {"skill": name, "output": f"{name}.docx", "kind": "docx", "nd30_format": True, **expect}
    (S / f"{name}.expect.json").write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
    (R / f"{name}.findings.md").write_text(f"# Phát hiện khi chạy thử tải lớn: {name} (dữ liệu giả)\n\n" + findings, encoding="utf-8")


# =====================================================================
# 1. quyet-dinh-cap-hoc-bong: danh sách ~145 sinh viên, nhiều trang
# =====================================================================
KHOA = [("CT", "Công nghệ thông tin", ["CT1", "CT2"]), ("KT", "Kinh tế", ["KT1", "KT2"]), ("NN", "Ngoại ngữ", ["NN1", "NN2"]),
        ("LU", "Luật", ["LU1", "LU2"]), ("SP", "Sư phạm", ["SP1", "SP2"])]
MUC = ["2.500.000", "3.500.000", "5.000.000"]


def gen_hoc_bong():
    rows = []
    for i in range(145):
        code, khoa, lops = KHOA[i % 5]
        rows.append({"ho_ten": ten_nguoi(i), "ma_sv": f"26{code}{i + 1:04d}", "lop": lops[(i // 5) % 2] + "-K26", "khoa": khoa,
                     "muc": MUC[(i // 3) % 3], "ghi_chu": ""})
    rows[10]["ghi_chu"] = "Chuyển ngành"
    rows[77]["ghi_chu"] = "Đạt thủ khoa"
    # bẫy: thiếu lớp
    for k in (20, 55, 99):
        rows[k]["lop"] = ""
    raw = list(rows)
    raw.append(dict(rows[30]))                                  # trùng hệt: giữ một
    raw.append(dict(rows[120]))                                  # trùng hệt: giữ một
    conf = dict(rows[40]); conf["ho_ten"] = "Lê Văn Nhầm"       # cùng mã, khác tên: loại cả hai, xác minh
    raw.append(conf)
    duyet = [r["ma_sv"] for r in rows]
    for k in (60, 61):                                          # không có trong biên bản hội đồng
        duyet.remove(rows[k]["ma_sv"])
    tong_raw = sum(parse_money(r["muc"]) for r in raw)
    inp = {"co_quan_chu_quan": CQ, "co_quan_ban_hanh": TR, "dia_danh": "Hà Nội", "so_van_ban": None,
           "loai_quyet_dinh": "Cấp học bổng khuyến khích", "ten_dot": "học kỳ 1 năm học 2026–2027",
           "danh_sach": raw, "ma_sv_hoi_dong_duyet": duyet,
           "can_cu": ["Quy chế học bổng của Trường Đại học Mẫu A", "Biên bản họp Hội đồng xét học bổng ngày 02/10/2026",
                      "Tờ trình số 21/TTr-CTSV ngày 03/10/2026 của Phòng Công tác sinh viên"],
           "tong_kinh_phi": money(tong_raw) + " đồng", "nguon_kinh_phi": "Ngân sách của Trường",
           "thoi_gian_ap_dung": "học kỳ 1 năm học 2026–2027",
           "don_vi_thuc_hien": ["Phòng Công tác sinh viên", "Phòng Kế hoạch – Tài chính", "Các khoa có sinh viên được xét", "Các sinh viên có tên trong danh sách"],
           "noi_nhan": ["Như Điều 4", "Lưu: VT, CTSV"], "nguoi_ky": {"chuc_danh": "Hiệu trưởng", "ho_ten": "Trần Thị Bình"}}
    return inp, raw, rows, duyet, tong_raw


def build_hoc_bong():
    inp, raw, rows, duyet, tong_raw = gen_hoc_bong()
    # Bước 1: làm sạch
    seen, clean, dup_ids, conflict = {}, [], [], set()
    for r in raw:
        if r["ma_sv"] in seen:
            if seen[r["ma_sv"]]["ho_ten"] != r["ho_ten"]:
                conflict.add(r["ma_sv"])
            else:
                dup_ids.append(r["ma_sv"])
            continue
        seen[r["ma_sv"]] = r
    clean = [r for m, r in seen.items() if m not in conflict and m in duyet]
    clean.sort(key=lambda r: (r["khoa"], r["lop"], r["ma_sv"]))
    n = len(clean)
    tong = sum(parse_money(r["muc"]) for r in clean)
    d = new_doc()
    page_number(d)
    head(d, inp, "QĐ")
    para(d, "QUYẾT ĐỊNH", bold=True, size=14, align=C, after=0)
    para(d, f"Về việc cấp học bổng khuyến khích học tập {inp['ten_dot']}", bold=True, align=C, after=8)
    para(d, f"HIỆU TRƯỞNG {TR}", bold=True, align=C, after=8)
    cc = inp["can_cu"]
    para(d, f"Căn cứ {cc[0]};", first_indent=1.0, align=J)
    para(d, f"Căn cứ {cc[1]};", first_indent=1.0, align=J)
    para(d, f"Xét đề nghị của Phòng Công tác sinh viên tại Tờ trình số 21/TTr-CTSV ngày 03/10/2026,", first_indent=1.0, align=J)
    para(d, "QUYẾT ĐỊNH:", bold=True, align=C, after=8)
    para(d, f"Điều 1. Cấp học bổng khuyến khích học tập {inp['ten_dot']} cho {n} sinh viên có tên trong danh sách kèm theo Quyết định này.",
         first_indent=1.0, align=J)
    para(d, f"Điều 2. Mức học bổng của từng sinh viên được ghi trong danh sách kèm theo. Tổng kinh phí: {DOT} đồng (bằng chữ: {DOT}). "
            f"Nguồn kinh phí: {inp['nguon_kinh_phi']}. Thời gian áp dụng: {inp['thoi_gian_ap_dung']}.", first_indent=1.0, align=J)
    para(d, "Điều 3. Quyết định này có hiệu lực kể từ ngày ký.", first_indent=1.0, align=J)
    dv = inp["don_vi_thuc_hien"]
    para(d, f"Điều 4. {dv[0]}, {dv[1]}, {dv[2]} và {dv[3]} chịu trách nhiệm thi hành Quyết định này./.", first_indent=1.0, align=J, after=10)
    keep_together(d, 2)
    sign(d, inp["noi_nhan"], inp["nguoi_ky"]["chuc_danh"], inp["nguoi_ky"]["ho_ten"])
    d.add_page_break()
    para(d, "DANH SÁCH SINH VIÊN ĐƯỢC CẤP HỌC BỔNG KHUYẾN KHÍCH HỌC TẬP", bold=True, align=C, after=0)
    para(d, inp["ten_dot"].upper() if False else f"({inp['ten_dot']})", align=C, after=0)
    para(d, f"Kèm theo Quyết định số {'.' * 6}/QĐ-{'.' * 6} ngày ..... tháng ..... năm ........ của Hiệu trưởng", italic=True, align=C, after=8)
    body = [[str(k), r["ho_ten"], r["ma_sv"], r["lop"], r["khoa"], r["muc"], r["ghi_chu"]] for k, r in enumerate(clean, 1)]
    grid(d, ["STT", "Họ và tên", "Mã SV", "Lớp", "Khoa", "Mức học bổng (đồng)", "Ghi chú"], body,
         [1.4, 3.5, 2.4, 2.0, 2.7, 2.2, 1.8], total=["Tổng cộng", f"{n} sinh viên", "", "", "", money(tong), ""],
         aligns=[C, L, L, L, L, WD_ALIGN_PARAGRAPH.RIGHT, L], size=11)
    out = O / "quyet-dinh-cap-hoc-bong--tai-lon.docx"
    d.save(out)
    # kỳ vọng
    ids = [r["ma_sv"] for r in clean]
    conf_ids = sorted(conflict)
    lops_thieu = [r["ma_sv"] for r in clean if not r["lop"]]
    excluded_hd = [r["ma_sv"] for r in raw if r["ma_sv"] not in duyet and r["ma_sv"] not in conflict]
    exp = {"must_contain": ["QUYẾT ĐỊNH", f"cho {n} sinh viên", "Kèm theo Quyết định số", "Tổng cộng", "HIỆU TRƯỞNG", "Trần Thị Bình",
                            "Phòng Công tác sinh viên", "Phòng Kế hoạch – Tài chính"],
           "must_not_contain": [money(tong_raw), "Lê Văn Nhầm"], "blank_labels": ["Số:", "Hà Nội, ngày", "Điều 2."],
           "allowed_derived": [str(n), money(tong)],
           "layout": {"page_number": True, "min_pages": 5, "same_page": [["Điều 4.", "Trần Thị Bình"]],
                      "tables": [{"index": 2, "header_repeat": True, "cant_split": True, "data_rows": n, "stt_continuous": True, "total_row_prefix": "Tổng cộng"}],
                      "unique_tokens": ids, "absent_tokens": conf_ids + excluded_hd},
           "traps": [{"id": "MA_SV_TRUNG_HET", "mo_ta": "2 dòng trùng hệt: giữ một"}, {"id": "MA_SV_TRUNG_KHAC_TEN", "mo_ta": "Cùng mã, khác tên: loại cả hai, hỏi lại"},
                     {"id": "SV_NGOAI_BIEN_BAN", "mo_ta": "2 sinh viên không có trong biên bản hội đồng: loại"},
                     {"id": "THIEU_LOP", "mo_ta": "3 dòng thiếu lớp: để ô trống"}, {"id": "TONG_KINH_PHI_LECH", "mo_ta": "Tổng đầu vào tính cả dòng trùng: lệch với bảng"},
                     {"id": "NHIEU_TRANG", "mo_ta": "Bảng dài nhiều trang: lặp tiêu đề, không cắt dòng, đánh số trang từ trang 2"}]}
    fnd = (f"- **MA_SV_TRUNG_HET**: {len(dup_ids)} dòng trùng hệt ({', '.join(dup_ids)}) chỉ giữ một dòng.\n"
           f"- **MA_SV_TRUNG_KHAC_TEN**: mã {', '.join(conf_ids)} xuất hiện với hai họ tên khác nhau. Theo skill không tự chọn: loại cả hai khỏi bảng và phản hồi phải yêu cầu Phòng CTSV xác minh.\n"
           f"- **SV_NGOAI_BIEN_BAN**: {', '.join(excluded_hd)} có trong danh sách nhưng không có trong biên bản hội đồng; loại khỏi quyết định.\n"
           f"- **THIEU_LOP**: {', '.join(lops_thieu)} thiếu lớp; giữ dòng, để ô Lớp trống, phản hồi nêu cần bổ sung.\n"
           f"- **TONG_KINH_PHI_LECH**: tổng đầu vào {money(tong_raw)} đồng (cộng cả dòng trùng và dòng bị loại) lệch tổng các dòng trong bảng {money(tong)} đồng ({money(tong_raw - tong)} đồng). Skill cấm tự chỉnh cho khớp nên Điều 2 để trống dòng tổng kinh phí và bằng chữ; bảng chỉ ghi tổng các dòng đã giữ. Chưa ký được cho tới khi xác định con số đúng.\n"
           f"- **NHIEU_TRANG**: bảng {n} dòng; dòng tiêu đề lặp lại mỗi trang, mỗi dòng không bị cắt giữa hai trang, số trang chỉ hiện từ trang 2.\n")
    dump("quyet-dinh-cap-hoc-bong--tai-lon", inp, exp, fnd)
    return out


# =====================================================================
# 2. soan-bien-ban-hop: 40 người dự, 16 nội dung dài
# =====================================================================
def gen_bien_ban():
    tp = [f"{ten_nguoi(200 + k)} – {['Trưởng phòng', 'Phó trưởng phòng', 'Chuyên viên', 'Giảng viên', 'Trưởng khoa'][k % 5]} {['Phòng Đào tạo', 'Phòng Tài chính', 'Khoa Kinh tế', 'Khoa Luật', 'Phòng Hành chính'][k % 5]}"
          for k in range(40)]
    tp.append(tp[7])  # trùng một người
    vande = ["kế hoạch tuyển sinh", "chương trình đào tạo", "học bổng", "cơ sở vật chất", "nghiên cứu khoa học", "hợp tác doanh nghiệp",
             "đảm bảo chất lượng", "tài chính", "tuyển dụng giảng viên", "chuyển đổi số", "ký túc xá", "hoạt động sinh viên",
             "thư viện", "kiểm định", "truyền thông", "an toàn thông tin"]
    nd = [{"van_de": v, "y_kien": f"Phòng chuyên môn báo cáo tiến độ {v}; các đại biểu thảo luận về khó khăn, đề xuất phương án và thời gian thực hiện. "
                                  f"Ý kiến thống nhất: tiếp tục triển khai {v} theo kế hoạch đã duyệt và báo cáo lại tại cuộc họp sau."} for v in vande]
    nd[4]["y_kien"] += " Ông Hoàng Quang Khải (khách mời, không có tên trong danh sách triệu tập) góp ý về hồ sơ đề tài."
    kl = [f"Giao {['Phòng Đào tạo', 'Phòng Tài chính', 'Khoa Kinh tế', 'Phòng Hành chính'][k % 4]} chủ trì nội dung số {k + 1}." for k in range(8)]
    kl.append("Giao Phòng Đào tạo hoàn thành báo cáo trước ngày 05/10/2026.")  # trước ngày họp
    return {"co_quan_chu_quan": CQ, "co_quan_ban_hanh": TR, "dia_danh": "Hà Nội", "so_van_ban": None,
            "ten_cuoc_hop": "họp giao ban toàn trường tháng 10/2026", "thoi_gian_bat_dau": "14 giờ 00 phút, ngày 12/10/2026", "thoi_gian_ket_thuc": None,
            "dia_diem": "Hội trường A", "chu_tri": "Bà Trần Thị Bình – Hiệu trưởng", "thu_ky": "Ông Lê Văn Cường – Chánh Văn phòng",
            "thanh_phan": tp, "noi_dung": nd, "ket_luan": kl, "noi_nhan": ["Các đơn vị thuộc Trường", "Lưu: VT, HCTH"]}


def build_bien_ban():
    i = gen_bien_ban()
    tp, seen = [], set()
    for x in i["thanh_phan"]:
        if x not in seen:
            seen.add(x); tp.append(x)
    d = new_doc()
    page_number(d)
    head(d, i, "BB")
    para(d, "BIÊN BẢN", bold=True, size=14, align=C, after=0)
    para(d, f"Cuộc {i['ten_cuoc_hop']}", bold=True, align=C, after=8)
    para(d, f"Thời gian bắt đầu: {i['thoi_gian_bat_dau']}", first_indent=1.0)
    para(d, f"Địa điểm: {i['dia_diem']}", first_indent=1.0)
    para(d, f"Chủ trì: {i['chu_tri']}", first_indent=1.0, after=2)
    para(d, f"Thư ký: {i['thu_ky']}", first_indent=1.0)
    para(d, f"Thành phần tham dự ({len(tp)} người):", bold=True, first_indent=1.0, after=2)
    for k, n in enumerate(tp, 1):
        para(d, f"{k}. {n}", first_indent=1.5, after=1)
    para(d, "Nội dung cuộc họp:", bold=True, first_indent=1.0, after=2)
    for k, n in enumerate(i["noi_dung"], 1):
        para(d, f"{k}. Về {n['van_de']}: {n['y_kien']}", first_indent=1.0, align=J, after=4)
    para(d, "Kết luận của chủ trì:", bold=True, first_indent=1.0, after=2)
    for k, x in enumerate(i["ket_luan"], 1):
        para(d, f"{k}. {x}", first_indent=1.0, align=J, after=2)
    para(d, f"Cuộc họp kết thúc lúc {DOT} cùng ngày./.", first_indent=1.0, after=10)
    keep_together(d, 2)
    t = d.add_table(rows=1, cols=2)
    borders(t, False)
    cell_text(t.cell(0, 0), ["THƯ KÝ", "", "", "", DOT], size=13, bold=True, align=C)
    cell_text(t.cell(0, 1), ["CHỦ TRÌ", "", "", "", DOT], size=13, bold=True, align=C)
    mark_row(t.rows[0])
    out = O / "soan-bien-ban-hop--tai-lon.docx"
    d.save(out)
    kh = tp[7]
    exp = {"must_contain": ["BIÊN BẢN", "họp giao ban toàn trường tháng 10/2026", "14 giờ 00 phút, ngày 12/10/2026", "Hội trường A",
                            "THƯ KÝ", "CHỦ TRÌ", "Giao Phòng Đào tạo hoàn thành báo cáo trước ngày 05/10/2026", f"Thành phần tham dự ({len(tp)} người)"],
           "must_not_contain": ["đã thông qua", "Thành phần tham dự (41 người)"], "blank_labels": ["Số:", "Hà Nội, ngày", "Cuộc họp kết thúc lúc"],
           "allowed_derived": [str(len(tp))],
           "layout": {"page_number": True, "min_pages": 3, "same_page": [["Cuộc họp kết thúc lúc", "THƯ KÝ"]], "unique_tokens": [kh], "absent_tokens": []},
           "traps": [{"id": "NGUOI_DU_TRUNG", "mo_ta": "1 người liệt kê hai lần"}, {"id": "KHACH_NGOAI_DANH_SACH", "mo_ta": "Người phát biểu không có trong danh sách triệu tập"},
                     {"id": "THOI_HAN_TRUOC_NGAY_HOP", "mo_ta": "Kết luận có hạn 05/10/2026 trước ngày họp 12/10/2026"}, {"id": "THIEU_GIO_KET_THUC", "mo_ta": "Không có giờ kết thúc"},
                     {"id": "NHIEU_TRANG", "mo_ta": "Danh sách 40 người, 16 nội dung, 9 kết luận trải nhiều trang; khối ký không tách khỏi dòng kết thúc"}]}
    fnd = (f"- **NGUOI_DU_TRUNG**: \"{kh}\" xuất hiện hai lần trong đầu vào; file giao chỉ ghi một lần, số người dự ghi {len(tp)} (41 dòng đầu vào trừ 1 dòng trùng).\n"
           "- **KHACH_NGOAI_DANH_SACH**: ông Hoàng Quang Khải phát biểu ở nội dung số 5 nhưng không có trong danh sách. Giữ nguyên ý kiến ghi nhận, không thêm vào danh sách tham dự; phản hồi hỏi lại có phải khách mời không.\n"
           "- **THOI_HAN_TRUOC_NGAY_HOP**: kết luận số 9 có hạn 05/10/2026, trước ngày họp 12/10/2026. Giữ nguyên lời chủ trì, không tự sửa ngày; phản hồi nêu nghi vấn nhập sai.\n"
           "- **THIEU_GIO_KET_THUC**: dòng \"Cuộc họp kết thúc lúc ......\" để trống.\n"
           "- **NHIEU_TRANG**: số trang chỉ hiện từ trang 2; dòng kết thúc và khối ký THƯ KÝ/CHỦ TRÌ nằm cùng một trang.\n")
    dump("soan-bien-ban-hop--tai-lon", i, exp, fnd)
    return out


# =====================================================================
# 3. soan-ke-hoach-ct: 45 nhiệm vụ
# =====================================================================
def gen_ke_hoach():
    donvi = ["Phòng Đào tạo", "Phòng Công tác sinh viên", "Phòng Kế hoạch – Tài chính", "Phòng Hành chính – Tổng hợp", "Khoa Kinh tế", "Khoa Luật"]
    nv = []
    for k in range(45):
        m = 11 + (k // 23)
        nv.append({"noi_dung": f"Nhiệm vụ {k + 1}: triển khai hạng mục công việc số {k + 1} phục vụ năm học 2026–2027",
                   "don_vi": donvi[k % 6], "thoi_gian": f"Từ {1 + k % 10:02d}/{m}/2026 đến {15 + k % 10:02d}/{m}/2026", "ket_qua": f"Hoàn thành hạng mục {k + 1}"})
    nv[12]["don_vi"] = ""
    nv[31]["don_vi"] = ""
    nv[20]["thoi_gian"] = "Từ 20/11/2026 đến 10/11/2026"
    kp = ["Hội nghị: 120.000.000 đồng", "Truyền thông: 80.000.000 đồng", "Khen thưởng: 100.000.000 đồng"]
    return {"co_quan_chu_quan": CQ, "co_quan_ban_hanh": TR, "dia_danh": "Hà Nội", "so_van_ban": None, "don_vi": "Phòng Hành chính – Tổng hợp",
            "thoi_gian": "quý IV năm 2026", "muc_tieu": ["Hoàn thành các hạng mục công tác trọng tâm của quý IV", "Bảo đảm chất lượng, tiến độ và phối hợp giữa các đơn vị"],
            "nhiem_vu": nv, "kinh_phi": kp, "kinh_phi_tong_ghi": "350.000.000 đồng", "noi_nhan": ["Các đơn vị thuộc Trường", "Lưu: VT, HCTH"],
            "nguoi_ky": {"chuc_danh": "Trưởng phòng", "ho_ten": None}}


def build_ke_hoach():
    i = gen_ke_hoach()
    d = new_doc()
    page_number(d)
    head(d, i, "KH")
    para(d, f"KẾ HOẠCH CÔNG TÁC {i['thoi_gian'].upper()}", bold=True, size=14, align=C, after=8)
    para(d, "I. MỤC ĐÍCH, YÊU CẦU", bold=True, after=2)
    for k, m in enumerate(i["muc_tieu"], 1):
        para(d, f"{k}. {m}.", first_indent=1.0, align=J, after=2)
    para(d, "II. NHIỆM VỤ CỤ THỂ", bold=True, after=4)
    body = [[str(k), n["noi_dung"], n["don_vi"], n["thoi_gian"], n["ket_qua"]] for k, n in enumerate(i["nhiem_vu"], 1)]
    grid(d, ["STT", "Nội dung", "Đơn vị/cá nhân thực hiện", "Thời gian", "Kết quả mong đợi"], body, [1.5, 5.0, 3.0, 3.6, 2.9], aligns=[C, L, L, L, L])
    para(d, "", after=4)
    para(d, "III. KINH PHÍ", bold=True, after=2)
    for x in i["kinh_phi"]:
        para(d, f"- {x};", first_indent=1.0, after=2)
    para(d, f"- Tổng dự toán: {DOT}", first_indent=1.0, after=4)
    para(d, "IV. TỔ CHỨC THỰC HIỆN", bold=True, after=2)
    para(d, "Các đơn vị thực hiện nhiệm vụ được phân công tại Mục II và báo cáo kết quả theo yêu cầu của Phòng Hành chính – Tổng hợp./.", first_indent=1.0, align=J, after=10)
    keep_together(d, 2)
    sign(d, i["noi_nhan"], i["nguoi_ky"]["chuc_danh"], i["nguoi_ky"]["ho_ten"])
    out = O / "soan-ke-hoach-ct--tai-lon.docx"
    d.save(out)
    exp = {"must_contain": ["KẾ HOẠCH CÔNG TÁC QUÝ IV NĂM 2026", "I. MỤC ĐÍCH, YÊU CẦU", "II. NHIỆM VỤ CỤ THỂ", "III. KINH PHÍ", "IV. TỔ CHỨC THỰC HIỆN",
                            "Từ 20/11/2026 đến 10/11/2026", "Hội nghị: 120.000.000 đồng", "TRƯỞNG PHÒNG"],
           "must_not_contain": ["350.000.000", "300.000.000"], "blank_labels": ["Số:", "Hà Nội, ngày", "- Tổng dự toán"],
           "layout": {"page_number": True, "min_pages": 3, "same_page": [["IV. TỔ CHỨC THỰC HIỆN", "TRƯỞNG PHÒNG"]],
                      "tables": [{"index": 1, "header_repeat": True, "cant_split": True, "data_rows": 45, "stt_continuous": True}]},
           "traps": [{"id": "THIEU_DON_VI", "mo_ta": "2 nhiệm vụ không có đơn vị thực hiện: ô trống"}, {"id": "THOI_GIAN_NGUOC", "mo_ta": "Nhiệm vụ 21 có ngày kết thúc trước ngày bắt đầu"},
                     {"id": "KINH_PHI_LECH", "mo_ta": "Ba khoản cộng 300 triệu, đầu vào ghi tổng 350 triệu"}, {"id": "THIEU_NGUOI_KY", "mo_ta": "Không có họ tên người ký"},
                     {"id": "NHIEU_TRANG", "mo_ta": "Bảng 45 dòng trải nhiều trang"}]}
    fnd = ("- **THIEU_DON_VI**: nhiệm vụ 13 và 32 không có đơn vị thực hiện; ô để trống, không tự phân công. Phản hồi nêu cần bổ sung.\n"
           "- **THOI_GIAN_NGUOC**: nhiệm vụ 21 ghi \"Từ 20/11/2026 đến 10/11/2026\"; giữ nguyên như đầu vào và phản hồi hỏi lại, không tự đổi chỗ hai ngày.\n"
           "- **KINH_PHI_LECH**: ba khoản 120 + 80 + 100 = 300 triệu, đầu vào ghi tổng 350 triệu. Dòng \"Tổng dự toán\" để trống, không chọn con số nào.\n"
           "- **THIEU_NGUOI_KY**: không có họ tên Trưởng phòng; khối ký để trống họ tên.\n"
           "- **NHIEU_TRANG**: bảng 45 dòng, tiêu đề lặp lại, mỗi dòng không bị cắt; mục IV và khối ký cùng một trang.\n")
    dump("soan-ke-hoach-ct--tai-lon", i, exp, fnd)
    return out


if __name__ == "__main__":
    for f in (build_hoc_bong, build_bien_ban, build_ke_hoach):
        print("đã tạo", f())
