"""Chuẩn hóa lại cấu trúc 20 skill nhóm dùng nhiều nhất (đợt 1, phiên bản 1.3.2).

Chạy lại an toàn: mỗi thay đổi chỉ áp dụng khi tìm thấy đúng chuỗi cũ; in ra danh sách thay đổi theo skill.
Dùng: python -X utf8 scripts/maintenance/restandardize_group1.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = {}

FORMAL = ("Đúng thể thức văn bản theo Nghị định 30/2020/NĐ-CP (đối chiếu hiệu lực tại ngày nghiệp vụ) "
          "và cấu trúc tại references/quy-cach-dau-ra.md.")
STRUCT = "Đúng cấu trúc và thể thức theo references/quy-cach-dau-ra.md."
INTERNAL_RESULT = "Kết quả đối chiếu nội bộ (không xuất kèm file) + danh sách chỗ cần sửa (nếu có), trả về bước tương ứng để chỉnh."


def edit(skill, old, new, why, regex=False, count=1):
    p = ROOT / "skills" / skill / "SKILL.md"
    t = p.read_text(encoding="utf-8")
    if regex:
        t2, n = re.subn(old, new, t, count=count, flags=re.M)
    else:
        n = t.count(old)
        t2 = t.replace(old, new) if n else t
    if n and t2 != t:
        p.write_text(t2, encoding="utf-8")
        LOG.setdefault(skill, []).append(why)
    return n


def fix_checklist_line(skill, new_text, why="Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt"):
    edit(skill, r"^- \[ \] Đúng thể thức và định dạng theo .*$", "- [ ] " + new_text, why, regex=True)


def main():
    # (a) mục kiểm tra thể thức bị ghép sai hoặc cắt cụt
    for s in ("soan-bien-ban-hop", "soan-thong-bao", "soan-giay-moi", "soan-to-trinh"):
        fix_checklist_line(s, FORMAL)
    fix_checklist_line("phieu-trinh-ky",
                       "Đúng khung phiếu trình ký tại references/quy-cach-dau-ra.md; văn bản trình kèm đúng thể thức "
                       "Nghị định 30/2020/NĐ-CP (đối chiếu hiệu lực tại ngày nghiệp vụ).")
    for s in ("soan-ke-hoach-ct", "bao-cao-tong-ket-vp", "kich-ban-khanh-tiet", "lap-lich-cong-tac-tuan"):
        fix_checklist_line(s, STRUCT)
    # cắt cụt ngoài nhóm 1 (cùng lỗi mẫu, sửa luôn cho nhất quán)
    NA = "Nghị định 30/2020/NĐ-CP về công tác văn thư (thể thức văn bản)."
    fix_checklist_line("quy-che-to-chuc-hoat-dong", "Đúng thể thức và định dạng theo Nghị định 30/2020/NĐ-CP về công tác văn thư (thể thức quyết định và văn bản kèm theo).", "Sửa mục kiểm tra thể thức bị cắt cụt")
    fix_checklist_line("checklist-ho-so-gs-pgs",
                       "Đúng thể thức theo Quyết định số 37/2018/QĐ-TTg và Nghị định 30/2020/NĐ-CP; "
                       "đối chiếu hiệu lực của căn cứ tại ngày nghiệp vụ.", "Sửa mục kiểm tra thể thức bị cắt cụt")
    fix_checklist_line("de-an-vi-tri-viec-lam",
                       "Đúng thể thức theo Nghị định 62/2017/NĐ-CP và Nghị định 30/2020/NĐ-CP; "
                       "đối chiếu hiệu lực của căn cứ tại ngày nghiệp vụ.", "Sửa mục kiểm tra thể thức bị cắt cụt")

    # (b) kết quả bước "báo cáo kiểm tra" nghe như file xuất
    for s in ("soan-bien-ban-hop", "soan-thong-bao"):
        edit(s, "Báo cáo kiểm tra + danh sách chỗ cần sửa (nếu có), trả về bước tương ứng để chỉnh.", INTERNAL_RESULT,
             "Kết quả bước kiểm tra ghi là nội bộ, không xuất kèm file")
    edit("soan-to-trinh", "Báo cáo kiểm tra logic + danh sách lỗi cần sửa (nếu có), trả về bước tương ứng để chỉnh.",
         "Kết quả đối chiếu logic và số liệu (nội bộ, không xuất kèm file) + danh sách lỗi cần sửa (nếu có), trả về bước tương ứng để chỉnh.",
         "Kết quả bước kiểm tra ghi là nội bộ, không xuất kèm file")

    # (c) vai trò duyệt/ký đúng người
    OLD = "Chuyên viên Phòng HCTH chuẩn bị, Hiệu trưởng phê duyệt"
    edit("soan-cong-van", OLD, "Chuyên viên Phòng HCTH chuẩn bị, người có thẩm quyền ký", "Vai trò duyệt/ký: không mặc định Hiệu trưởng")
    edit("soan-quyet-dinh-hc", OLD, "Chuyên viên Phòng HCTH chuẩn bị, người ký theo `nguoi_ky`", "Vai trò duyệt/ký theo nguoi_ky")
    edit("soan-bien-ban-hop", OLD, "Thư ký chuẩn bị, chủ trì và thư ký cuộc họp ký", "Biên bản do chủ trì và thư ký ký, không phải Hiệu trưởng")
    edit("soan-thong-bao", OLD, "Chuyên viên Phòng HCTH chuẩn bị, thủ trưởng đơn vị ban hành ký", "Vai trò ký theo đơn vị ban hành")
    edit("soan-to-trinh", OLD, "Chuyên viên chuẩn bị, thủ trưởng đơn vị trình ký", "Tờ trình do thủ trưởng đơn vị trình ký (khớp Lưu ý của Bước 5)")
    edit("soan-giay-moi", OLD, "Chuyên viên chuẩn bị, thủ trưởng đơn vị tổ chức ký", "Giấy mời do thủ trưởng đơn vị tổ chức ký (khớp sơ đồ)")
    edit("soan-ke-hoach-ct", OLD, "Chuyên viên chuẩn bị, thủ trưởng đơn vị ký ban hành (hoặc cấp trên phê duyệt nếu vượt thẩm quyền)",
         "Vai trò ký theo thủ trưởng đơn vị (khớp Lưu ý)")
    edit("phieu-trinh-ky", OLD, "Chuyên viên đơn vị trình chuẩn bị", "Bước chuẩn bị do đơn vị trình thực hiện; lãnh đạo chỉ ghi ý kiến ở Bước 6")

    # (d) sơ đồ khớp số bước
    edit("soan-to-trinh", '    B6 --> HG["👤 Thủ trưởng đơn vị duyệt tờ trình"]',
         '    B6 --> B7["Bước 7: Xuất bản tờ trình trình ký"]\n    B7 --> HG["👤 Thủ trưởng đơn vị ký tờ trình"]',
         "Sơ đồ thiếu Bước 7")
    for old, new in [
        ('--> A["Rà soát thông tin', '--> A["Bước 1: Rà soát thông tin'),
        ('B["Soạn tiêu đề GIẤY MỜI và lời mời"]', 'B["Bước 2: Soạn tiêu đề GIẤY MỜI và lời mời"]'),
        ('C["Ghi thời gian, địa điểm, chương trình tóm tắt"]', 'C["Bước 3: Ghi thời gian, địa điểm, chương trình tóm tắt"]'),
        ('E["Ghi đầu mối và hạn xác nhận tham dự"]', 'E["Bước 4: Ghi đầu mối và hạn xác nhận tham dự"]'),
        ('F["Rà soát thể thức, chính tả"]', 'F["Bước 5: Rà soát thể thức, chính tả"]'),
        ('G["Phát hành giấy mời tới khách mời"]', 'G["Bước 6: Phát hành giấy mời tới khách mời"]')]:
        edit("soan-giay-moi", old, new, "Sơ đồ thêm nhãn Bước")
    for old, new in [
        ('A["Xác định loại văn bản MOU hay MOA"]', 'A["Bước 1: Xác định loại văn bản MOU hay MOA"]'),
        ('E["Soạn bản tiếng Việt đầy đủ điều khoản"]', 'E["Bước 2: Soạn bản tiếng Việt đầy đủ điều khoản"]'),
        ('F["Soạn bản tiếng Anh tương ứng"]', 'F["Bước 3: Soạn bản tiếng Anh tương ứng"]'),
        ('G{"Tương thích pháp lý?"}', 'G{"Bước 4: Tương thích pháp lý?"}'),
        ('HG["👤 Thẩm định nội bộ, Hiệu trưởng phê duyệt"]', 'HG["👤 Bước 5: Thẩm định nội bộ, Hiệu trưởng phê duyệt"]'),
        ('Z[["Xuất bản văn bản song ngữ, lưu hồ sơ"]]', 'Z[["Bước 6: Xuất bản văn bản song ngữ, lưu hồ sơ"]]')]:
        edit("soan-mou-moa", old, new, "Sơ đồ thêm nhãn Bước")
    for old, new in [
        ('A["Thu thập hồ sơ, kiểm tra đầy đủ tài liệu kèm"]', 'A["Bước 1: Thu thập hồ sơ, kiểm tra đầy đủ tài liệu kèm"]'),
        ('B["Viết tóm tắt nội dung 3-7 dòng"]', 'B["Bước 2: Viết tóm tắt nội dung 3-7 dòng"]'),
        ('C["Ghi ý kiến đề xuất của đơn vị soạn thảo"]', 'C["Bước 3: Ghi ý kiến đề xuất của đơn vị soạn thảo"]'),
        ('D["Hoàn thiện phiếu trình ký, chừa phần ý kiến lãnh đạo"]', 'D["Bước 4: Hoàn thiện phiếu trình ký, chừa phần ý kiến lãnh đạo"]'),
        ('E["Người trình ký xác nhận, kẹp phiếu lên trên cùng hồ sơ"]', 'E["Bước 5: Người trình ký xác nhận, kẹp phiếu lên trên cùng hồ sơ"]'),
        ('HG["👤 Lãnh đạo ghi ý kiến, ký duyệt"]', 'HG["👤 Bước 6: Lãnh đạo ghi ý kiến, ký duyệt"]')]:
        edit("phieu-trinh-ky", old, new, "Sơ đồ thêm nhãn Bước")
    for old, new in [
        ('--> A["Xác định loại sổ, chuẩn bị mẫu sổ năm mới"]', '--> A["Bước 1: Xác định loại sổ, chuẩn bị mẫu sổ năm mới"]'),
        ('B["Tiếp nhận, kiểm tra nguyên vẹn, niêm phong"]', 'B["Bước 2: Tiếp nhận, kiểm tra nguyên vẹn, niêm phong"]'),
        ('C["Đăng ký vào sổ văn bản đến trong ngày"]', 'C["Bước 3: Đăng ký vào sổ văn bản đến trong ngày"]'),
        ('D["Trình lãnh đạo cho ý kiến chỉ đạo"]', 'D["Bước 4: Trình lãnh đạo cho ý kiến chỉ đạo"]'),
        ('E["Chuyển đơn vị xử lý, đôn đốc tiến độ"]', 'E["Bước 5: Chuyển đơn vị xử lý, đôn đốc tiến độ"]'),
        ('F["Thu hồi, sắp xếp, lưu trữ hồ sơ"]', 'F["Bước 6: Thu hồi, sắp xếp, lưu trữ hồ sơ"]'),
        ('G["Đăng ký vào sổ văn bản đi"]', 'G["Bước 7: Đăng ký vào sổ văn bản đi"]'),
        ('H["Nhân bản, đóng dấu, gửi đi; lưu bản chính"]', 'H["Bước 7: Nhân bản, đóng dấu, gửi đi; lưu bản chính"]'),
        ('HG["👤 Văn thư kiểm tra sổ sách định kỳ"]', 'HG["👤 Bước 8: Văn thư kiểm tra sổ sách định kỳ"]')]:
        edit("so-van-ban-di-den", old, new, "Sơ đồ thêm nhãn Bước")
    for old, new in [
        ('B["Kiểm kê toàn bộ file (inventory)"]', 'B["Bước 1: Kiểm kê toàn bộ file (inventory)"]'),
        ('C["Nhóm file trùng, xác định quan hệ phiên bản"]', 'C["Bước 2: Nhóm file trùng, xác định quan hệ phiên bản"]'),
        ('D["Đề xuất taxonomy cấu trúc thư mục"]', 'D["Bước 3: Đề xuất taxonomy cấu trúc thư mục"]'),
        ('E["Đề xuất quy tắc đặt tên chuẩn"]', 'E["Bước 4: Đề xuất quy tắc đặt tên chuẩn"]'),
        ('F["Đối chiếu danh mục phải có, lập missing list"]', 'F["Bước 5: Đối chiếu danh mục phải có, lập missing list"]'),
        ('G["Xuất báo cáo + hướng dẫn thủ công"]', 'G["Bước 6: Xuất báo cáo + hướng dẫn thủ công"]')]:
        edit("quan-ly-phien-ban-tai-lieu", old, new, "Sơ đồ thêm nhãn Bước")
    for old, new in [
        ('IN[/"Số liệu hoạt động văn phòng"/] --> A["Thu thập', 'IN[/"Số liệu hoạt động văn phòng"/] --> A["Bước 1: Thu thập'),
        ('B["Tổng hợp kết quả 4 mảng công tác"]', 'B["Bước 2: Tổng hợp kết quả 4 mảng công tác"]'),
        ('C["Đánh giá ưu điểm, kết quả nổi bật"]', 'C["Bước 3: Đánh giá ưu điểm, kết quả nổi bật"]'),
        ('D["Chỉ ra tồn tại, hạn chế và nguyên nhân"]', 'D["Bước 4: Chỉ ra tồn tại, hạn chế và nguyên nhân"]'),
        ('E["Đề xuất phương hướng kỳ tới"]', 'E["Bước 5: Đề xuất phương hướng kỳ tới"]'),
        ('F["Soạn báo cáo theo thể thức, kèm phụ lục số liệu"]', 'F["Bước 6: Soạn báo cáo theo thể thức, kèm phụ lục số liệu"]')]:
        edit("bao-cao-tong-ket-vp", old, new, "Sơ đồ thêm nhãn Bước")

    # (e) ngày ví dụ cụ thể -> chỗ điền
    edit("soan-bien-ban-hop", 'Giờ họp ghi đầy đủ "08h00 – 10h00, ngày 12 tháng 10 năm 2026"',
         'Giờ họp ghi đầy đủ theo dạng "…h… – …h…, ngày … tháng … năm …" từ `thoi_gian` (chỗ nào input chưa có thì để dòng dấu chấm)',
         "Bỏ ngày giờ ví dụ cụ thể, dùng chỗ điền")
    edit("soan-thong-bao", 'vd ghi "thứ Sáu, 01/01/2027" nhưng tra lịch lại là thứ khác', 'vd ghi "thứ Sáu, ngày …" nhưng tra lịch lại là thứ khác',
         "Bỏ ngày ví dụ cụ thể")
    edit("soan-thong-bao", 'description: "Soạn thông báo nội bộ của trường đại học (lịch nghỉ lễ, cuộc họp, quy định mới, tuyển dụng, học bổng...). Ngắn gọn, rõ đối tượng, rõ thời hạn."',
         'description: "Soạn thông báo nội bộ của trường đại học (lịch nghỉ lễ, cuộc họp, quy định mới, tuyển dụng, học bổng...), ngắn gọn, rõ đối tượng, rõ thời hạn. Dùng khi cần thông tin chính thức tới toàn trường hoặc một nhóm đối tượng. Không dùng cho văn bản chỉ đạo/quy phạm (dùng soan-quyet-dinh-hc) hay thư mời (dùng soan-giay-moi)."',
         "Bổ sung câu 'Dùng khi' và ranh giới sang skill lân cận")

    # (f) số/ký hiệu văn bản: không tự cấp
    edit("soan-to-trinh", 'số tờ trình lấy tiếp theo sổ văn bản đi của đơn vị với ký hiệu "TTr".',
         'ký hiệu ghi "TTr"; số tờ trình chỉ ghi khi người dùng cung cấp, nếu chưa có thì để dòng dấu chấm (văn thư cấp số khi đăng ký sổ văn bản đi).',
         "Không tự cấp số văn bản (khớp quy tắc chừa chỗ điền)")
    edit("soan-quyet-dinh-hc", 'Số quyết định lấy tiếp theo từ sổ đăng ký văn bản đi, ký hiệu "QĐ" (+ mã đơn vị nếu có)',
         'Ký hiệu ghi "QĐ" (+ mã đơn vị nếu có); số quyết định chỉ ghi khi người dùng cung cấp, nếu chưa có thì để dòng dấu chấm (văn thư cấp số khi đăng ký sổ văn bản đi)',
         "Không tự cấp số văn bản (khớp quy tắc chừa chỗ điền)")
    edit("soan-quyet-dinh-hc", '"HIỆU TRƯỞNG TRƯỜNG ĐẠI HỌC A"', '"HIỆU TRƯỞNG TRƯỜNG …"', "Bỏ tên trường giả định")
    edit("soan-quyet-dinh-hc", "khen thưởng – kỷ luật, phê duyệt kế hoạch – đề án.",
         "khen thưởng – kỷ luật sinh viên (khen thưởng/kỷ luật viên chức, người lao động dùng quyet-dinh-khen-thuong-kl), phê duyệt kế hoạch – đề án.",
         "Khớp ranh giới với quyet-dinh-khen-thuong-kl trong mô tả")
    edit("soan-quyet-dinh-hc", "| `loai_quyet_dinh` | Thành lập / Ban hành văn bản / Nhân sự / Khen thưởng – kỷ luật / Phê duyệt |",
         "| `loai_quyet_dinh` | Thành lập / Ban hành văn bản / Nhân sự / Khen thưởng – kỷ luật sinh viên / Phê duyệt |",
         "Khớp ranh giới với quyet-dinh-khen-thuong-kl trong bảng đầu vào")

    # (g) soan-mou-moa
    edit("soan-mou-moa", "giữa Trường Đại học A với đối tác", "giữa trường với đối tác", "Bỏ tên trường giả định")
    edit("soan-mou-moa", "| Trách nhiệm của Trường Đại học A |", "| Trách nhiệm của Bên A (trường) |", "Bỏ tên trường giả định")
    edit("soan-mou-moa", "Luật Giáo dục đại học 2012 (sửa đổi 2018) và văn bản hướng dẫn hợp tác quốc tế.",
         "Luật Giáo dục đại học 2012 (sửa đổi 2018) và văn bản hướng dẫn hợp tác quốc tế; đối chiếu hiệu lực tại ngày nghiệp vụ (xem docs/CAP_NHAT_PHAP_LY.md).",
         "Thêm yêu cầu đối chiếu hiệu lực căn cứ")
    edit("soan-mou-moa", "- Luật Giáo dục đại học 2012 (sửa đổi, bổ sung 2018) và các văn bản hướng dẫn về hợp tác quốc tế trong giáo dục.",
         "- Luật Giáo dục đại học 2012 (sửa đổi, bổ sung 2018) và các văn bản hướng dẫn về hợp tác quốc tế trong giáo dục; đối chiếu hiệu lực tại ngày nghiệp vụ (xem docs/CAP_NHAT_PHAP_LY.md).\n- Phần \"căn cứ ký kết\" trong văn bản chỉ ghi các căn cứ do người dùng cung cấp; chưa có thì để dòng dấu chấm.",
         "Thêm quy tắc căn cứ ký kết chỉ lấy từ input")
    edit("soan-mou-moa", "## Kiểm tra nội bộ trước khi giao\n- [ ] Bố cục",
         "## Kiểm tra nội bộ trước khi giao\n\nCác tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.\n\n- [ ] Bố cục",
         "Thêm câu dẫn chuẩn cho mục kiểm tra nội bộ")

    # (h) soan-ke-hoach-ct: kiểm tra khả thi phải trước khi trình ký -> đảo thứ tự bước 6 và 7
    p = ROOT / "skills/soan-ke-hoach-ct/SKILL.md"
    t = p.read_text(encoding="utf-8")
    m6 = re.search(r"\*\*Bước 6\. Dựng thể thức và trình ký ban hành\*\*.*?(?=\n\*\*Bước 7\.)", t, re.S)
    m7 = re.search(r"\*\*Bước 7\. Kiểm tra tính khả thi trước khi ban hành\*\*.*?(?=\n## )", t, re.S)
    if m6 and m7:
        b6, b7 = m6.group(0), m7.group(0).rstrip("\n")
        n_check = b7.replace("**Bước 7. Kiểm tra tính khả thi trước khi ban hành**", "**Bước 6. Kiểm tra tính khả thi trước khi trình ký**")
        n_check = n_check.replace("Báo cáo kiểm tra + danh sách chỗ cần sửa (nếu có); sau khi sửa xong thì ban hành.",
                                  "Kết quả đối chiếu nội bộ (không xuất kèm file) + danh sách chỗ cần sửa (nếu có); sửa xong thì chuyển Bước 7.")
        n_fmt = b6.replace("**Bước 6. Dựng thể thức và trình ký ban hành**", "**Bước 7. Dựng thể thức và trình ký ban hành**")
        n_fmt = n_fmt.replace("Văn bản kế hoạch hoàn chỉnh về thể thức, đã trình ký.", "Văn bản kế hoạch hoàn chỉnh về thể thức, sẵn sàng trình ký.")
        t = t[:m6.start()] + n_check + "\n\n" + n_fmt + "\n" + t[m7.end():]
        t = t.replace('    B5 --> B6["Bước 6: Dựng thể thức và trình ký ban hành"]\n    B6 --> DP{"Vượt thẩm quyền đơn vị?"}\n    DP -->|Có| B6A["Trình cấp trên phê duyệt"]\n    DP -->|Không| B7["Bước 7: Kiểm tra tính khả thi trước khi ban hành"]\n    B6A --> B7\n    B7 --> HG',
                      '    B5 --> B6["Bước 6: Kiểm tra tính khả thi trước khi trình ký"]\n    B6 --> B7["Bước 7: Dựng thể thức và trình ký ban hành"]\n    B7 --> DP{"Vượt thẩm quyền đơn vị?"}\n    DP -->|Có| B7A["Trình cấp trên phê duyệt"]\n    DP -->|Không| HG\n    B7A --> HG')
        p.write_text(t, encoding="utf-8")
        LOG.setdefault("soan-ke-hoach-ct", []).append("Đảo Bước 6/7: kiểm tra khả thi trước khi dựng thể thức và trình ký; sửa sơ đồ")

    # (i) tham-dinh-phap-ly-van-ban
    edit("tham-dinh-phap-ly-van-ban", "Phiếu ý kiến pháp lý đã ký + bảng đối chiếu gửi đơn vị soạn thảo.",
         "Phiếu ý kiến pháp lý (trình Trưởng phòng ký) + bảng đối chiếu, gửi đơn vị soạn thảo sau khi ký.",
         "Kết quả bước không khẳng định 'đã ký'")
    edit("tham-dinh-phap-ly-van-ban", "nếu không có thì tự tra cứu văn bản nội bộ liên quan",
         "nếu không có thì chỉ đối chiếu với văn bản người dùng cung cấp và ghi rõ phần chưa đối chiếu được, không tự giả định nội dung văn bản nội bộ",
         "Không tự giả định nội dung văn bản nội bộ")

    # (j) chuan-bi-hop-va-action-tracker, hop-nhat-bao-cao-don-vi, bao-cao-tong-ket-nam-truong
    edit("chuan-bi-hop-va-action-tracker", 'chỗ chưa rõ đã đánh dấu "cần xác minh", không suy diễn.',
         "chỗ chưa rõ để trống (owner/deadline) và nêu trong phản hồi cho thư ký, không suy diễn.", "Khớp quy tắc chừa chỗ điền, bỏ nhãn 'cần xác minh' trong file")
    edit("hop-nhat-bao-cao-don-vi", 'chỉ tiêu thiếu ghi rõ "chưa có số liệu"', "chỉ tiêu thiếu để trống ô số liệu và ghi vào data gap log",
         "Khớp quy tắc chừa chỗ điền")
    edit("bao-cao-tong-ket-nam-truong", 'số liệu thiếu được ghi rõ "chưa có số liệu"', "số liệu thiếu để trống ô và ghi nhận trong bảng theo dõi nộp",
         "Khớp quy tắc chừa chỗ điền")
    edit("bao-cao-tong-ket-nam-truong", "Báo cáo tổng kết năm học toàn trường đã duyệt + phụ lục số liệu",
         "Báo cáo tổng kết năm học toàn trường trình Ban Giám hiệu duyệt + phụ lục số liệu", "Kết quả bước không khẳng định 'đã duyệt'")

    # (k) bao-cao-du-an-dinh-ky: người soạn/duyệt
    edit("bao-cao-du-an-dinh-ky", "- Vai trò: Viện trưởng · AI hỗ trợ: ghép khung", "- Vai trò: Chủ nhiệm dự án soạn, Viện trưởng duyệt ở bước cuối · AI hỗ trợ: ghép khung",
         "Phân biệt người soạn và người duyệt")

    # (l) lap-lich-cong-tac-tuan: người duyệt không nhất quán giữa Bước 6 và sơ đồ
    edit("lap-lich-cong-tac-tuan", "Chuyên viên Phòng HCTH chuẩn bị, Trưởng phòng HCTH phê duyệt", "Chuyên viên Phòng HCTH chuẩn bị, người có thẩm quyền duyệt lịch (theo quy chế làm việc của trường)",
         "Thống nhất người duyệt giữa Bước 6 và sơ đồ")
    edit("lap-lich-cong-tac-tuan", 'HG["👤 Chánh Văn phòng, Hiệu trưởng duyệt"]', 'HG["👤 Người có thẩm quyền duyệt lịch"]', "Thống nhất người duyệt giữa Bước 6 và sơ đồ")

    # (m) mô tả: thêm 'Dùng khi'
    edit("executive-brief-trinh-lanh-dao", "Dùng chung cho mọi cấp lãnh đạo, mọi lĩnh vực trong trường.",
         "Dùng khi lãnh đạo cần nắm nhanh một vấn đề từ nhiều nguồn để ra quyết định (mọi cấp, mọi lĩnh vực trong trường).", "Mô tả nêu rõ khi nào dùng")
    edit("quan-ly-phien-ban-tai-lieu", "Dùng chung cho mọi đơn vị.", "Dùng khi đơn vị cần sắp xếp lại thư mục tài liệu mà chưa muốn thay đổi file nào.", "Mô tả nêu rõ khi nào dùng")
    edit("chuan-bi-hop-va-action-tracker", "Dùng chung cho mọi cuộc họp trong trường: giao ban, hội đồng, họp đơn vị.",
         "Dùng khi chuẩn bị hoặc kết thúc một cuộc họp trong trường (giao ban, hội đồng, họp đơn vị).", "Mô tả nêu rõ khi nào dùng")
    edit("lap-lich-cong-tac-tuan", "chuẩn hóa và xuất bảng lịch tuần.\"", "chuẩn hóa và xuất bảng lịch tuần. Dùng khi Phòng HCTH lập lịch công tác tuần của Ban Giám hiệu.\"",
         "Mô tả nêu rõ khi nào dùng")
    edit("kiem-tra-day-du-ho-so", "Dùng chung cho mọi loại hồ sơ trong trường", "Dùng khi tiếp nhận hồ sơ cần kiểm tra đủ/thiếu, bất kỳ loại hồ sơ nào trong trường",
         "Mô tả nêu rõ khi nào dùng")
    edit("hop-nhat-bao-cao-don-vi", "Dùng cho báo cáo 3 công khai", "Dùng khi hợp nhất báo cáo nhiều đơn vị, như báo cáo 3 công khai", "Mô tả nêu rõ khi nào dùng")

    edit("tham-dinh-phap-ly-van-ban", "Output là phiếu ý kiến pháp lý với một trong ba mức: đồng ý / đồng ý với điều kiện chỉnh sửa / không đồng ý kèm lý do.",
         "Dùng khi đơn vị trình dự thảo văn bản nội bộ cần ý kiến pháp lý. Kết quả: phiếu ý kiến pháp lý một trong ba mức (đồng ý / đồng ý có điều kiện / không đồng ý kèm lý do).", "Mô tả nêu rõ khi nào dùng, rút gọn dưới 400 ký tự")

    out = ROOT / "docs" / "ra_soat_nhom_1.json"
    if LOG:  # chạy lại không ghi đè nhật ký của lần chạy đầu
        out.write_text(json.dumps(LOG, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in LOG.items():
        print(k, len(v))
    print("tổng thay đổi:", sum(len(v) for v in LOG.values()))


if __name__ == "__main__":
    main()
