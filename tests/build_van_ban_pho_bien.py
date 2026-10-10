"""Dựng file đầu ra mẫu cho 4 skill văn bản phổ biến: thông báo, biên bản, tờ trình, giấy mời.

Đóng vai AI làm theo SKILL.md và quy cách đầu ra; dùng dữ liệu giả trong tests/samples.
Dùng: python -X utf8 tests/build_van_ban_pho_bien.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_reference_outputs import *  # noqa: F401,F403
from build_reference_outputs import DOT, O, borders, cell_text, header_block, load, new_doc, para

C = WD_ALIGN_PARAGRAPH.CENTER
J = WD_ALIGN_PARAGRAPH.JUSTIFY
DATE = "{}, ngày ..... tháng ..... năm ........"


def head(d, i, ky_hieu, so_dong=True):
    left = ([i["co_quan_chu_quan"], i["co_quan_ban_hanh"], f"Số: {'.' * 6}/{ky_hieu}-{'.' * 6}"], [False, True, False])
    right = (["CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", "Độc lập – Tự do – Hạnh phúc", DATE.format(i["dia_danh"])], [True, True, False])
    t = header_block(d, left, right)
    t.cell(0, 1).paragraphs[2].runs[0].italic = True
    para(d, "", after=4)


def sign(d, noi_nhan, chuc_danh, ho_ten, left_title="Nơi nhận:"):
    t = d.add_table(rows=1, cols=2)
    borders(t, False)
    t.autofit = False
    t.columns[0].width, t.columns[1].width = Cm(7.5), Cm(8.5)
    nn = [left_title] + [f"- {x};" for x in noi_nhan[:-1]] + [f"- {noi_nhan[-1]}."]
    cell_text(t.cell(0, 0), nn, size=12)
    t.cell(0, 0).paragraphs[0].runs[0].bold = True
    t.cell(0, 0).paragraphs[0].runs[0].italic = True
    cell_text(t.cell(0, 1), [chuc_danh.upper(), "", "", "", ho_ten or DOT], size=13, bold=True, align=C)


def build_thong_bao():
    i = load("soan-thong-bao.input.json")
    d = new_doc()
    head(d, i, "TB")
    para(d, "THÔNG BÁO", bold=True, size=14, align=C, after=0)
    para(d, f"Về việc {i['tieu_de']}", bold=True, align=C, after=8)
    para(d, f"Kính gửi: {i['doi_tuong']}", first_indent=1.0, align=J)
    para(d, f"{i['co_quan_ban_hanh'].title().replace('Đại Học','Đại học')} thông báo như sau:", first_indent=1.0, align=J)
    ev = i["noi_dung"][0].replace("thứ Sáu, ", "")  # bỏ thứ vì không khớp lịch; hỏi lại người dùng
    reg = i["noi_dung"][1]
    para(d, f"1. {ev}.", first_indent=1.0, align=J)
    para(d, f"2. {reg.replace('trước ngày 12/10/2026', 'trước ngày 12/10/2026')}.", first_indent=1.0, align=J, after=10)
    para(d, "Đề nghị các đơn vị và cá nhân có liên quan thực hiện./.", first_indent=1.0, align=J, after=10)
    sign(d, i["noi_nhan"], i["nguoi_ky"]["chuc_danh"], i["nguoi_ky"]["ho_ten"])
    out = O / "soan-thong-bao.docx"
    d.save(out)
    return out


def build_bien_ban():
    i = load("soan-bien-ban-hop.input.json")
    d = new_doc()
    head(d, i, "BB")
    para(d, "BIÊN BẢN", bold=True, size=14, align=C, after=0)
    para(d, f"Cuộc {i['ten_cuoc_hop']}", bold=True, align=C, after=8)
    para(d, f"Thời gian bắt đầu: {i['thoi_gian_bat_dau']}", first_indent=1.0)
    para(d, f"Địa điểm: {i['dia_diem']}", first_indent=1.0)
    para(d, "Thành phần tham dự:", first_indent=1.0, after=2)
    for n in i["thanh_phan"]:
        para(d, f"- {n}", first_indent=1.5, after=2)
    para(d, f"Chủ trì: {i['chu_tri']}", first_indent=1.0, after=2)
    para(d, f"Thư ký: {i['thu_ky']}", first_indent=1.0)
    para(d, "Nội dung cuộc họp:", bold=True, first_indent=1.0, after=2)
    for k, n in enumerate(i["noi_dung"], 1):
        para(d, f"{k}. {n}.", first_indent=1.0, align=J)
    para(d, f"Kết luận: {i['ket_luan']}", first_indent=1.0, align=J)
    para(d, f"Kết thúc lúc {DOT} cùng ngày.", first_indent=1.0, after=10)
    t = d.add_table(rows=1, cols=2)
    borders(t, False)
    cell_text(t.cell(0, 0), ["THƯ KÝ", "", "", "", DOT], size=13, bold=True, align=C)
    cell_text(t.cell(0, 1), ["CHỦ TRÌ", "", "", "", DOT], size=13, bold=True, align=C)
    out = O / "soan-bien-ban-hop.docx"
    d.save(out)
    return out


def build_to_trinh():
    i = load("soan-to-trinh.input.json")
    d = new_doc()
    head(d, i, "TTr")
    para(d, "TỜ TRÌNH", bold=True, size=14, align=C, after=0)
    para(d, f"Về việc {i['ten_to_trinh']}", bold=True, align=C, after=8)
    para(d, f"Kính gửi: {i['kinh_gui']}", first_indent=1.0, after=8)
    para(d, f"{i['don_vi_trinh']} kính trình {i['kinh_gui'].split(' Trường')[0]} nội dung như sau:", first_indent=1.0, align=J)
    para(d, f"Căn cứ {i['can_cu'][0]};", first_indent=1.0, align=J)
    para(d, "1. Nội dung đề xuất:", bold=True, first_indent=1.0, after=2)
    for n in i["noi_dung_de_xuat"][:3]:
        para(d, f"- {n};", first_indent=1.5, after=2, align=J)
    para(d, f"- Tổng kinh phí dự kiến: {DOT}", first_indent=1.5, after=6)
    para(d, "2. Kiến nghị:", bold=True, first_indent=1.0, after=2)
    para(d, f"{i['kien_nghi']}./.", first_indent=1.0, align=J, after=10)
    sign(d, i["noi_nhan"], i["nguoi_ky"]["chuc_danh"], i["nguoi_ky"]["ho_ten"])
    out = O / "soan-to-trinh.docx"
    d.save(out)
    return out


def build_giay_moi():
    i = load("soan-giay-moi.input.json")
    d = new_doc()
    head(d, i, "GM")
    para(d, "GIẤY MỜI", bold=True, size=14, align=C, after=0)
    para(d, f"Dự {i['su_kien']}", bold=True, align=C, after=8)
    para(d, f"Kính mời: {DOT}", first_indent=1.0, after=2)
    para(d, f"Thành phần mời: {i['thanh_phan']}", first_indent=1.0, align=J, after=2)
    para(d, f"Tới dự {i['su_kien']}.", first_indent=1.0, align=J, after=2)
    para(d, f"Thời gian: {i['thoi_gian']}", first_indent=1.0, after=2)
    para(d, f"Địa điểm: {DOT}", first_indent=1.0, after=2)
    para(d, f"{i['xac_nhan']}; hạn xác nhận {DOT}", first_indent=1.0, after=2)
    para(d, "Trân trọng kính mời./.", first_indent=1.0, after=10)
    sign(d, i["noi_nhan"], i["don_vi_moi"]["chuc_danh"], i["don_vi_moi"]["ho_ten"])
    out = O / "soan-giay-moi.docx"
    d.save(out)
    return out


if __name__ == "__main__":
    for f in (build_thong_bao, build_bien_ban, build_to_trinh, build_giay_moi):
        print("đã tạo", f())
