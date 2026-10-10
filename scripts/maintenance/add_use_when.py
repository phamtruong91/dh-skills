"""Bổ sung câu "Dùng khi ..." vào mô tả skill còn thiếu (nội dung rút từ mục "Khi nào dùng" của chính skill)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
USE = {
 "audit-tien-do-tot-nghiep": "cuối học kỳ hoặc trước đợt xét tốt nghiệp, cần rà nhanh sinh viên đã đủ điều kiện tốt nghiệp chưa",
 "bao-cao-chuyen-doi-so": "cần báo cáo Ban Giám hiệu hoặc cơ quan quản lý về tiến độ chuyển đổi số của trường",
 "bao-cao-cong-tac-thu-vien": "kết thúc năm học và thư viện cần tổng kết hoạt động phục vụ bạn đọc, phát triển vốn tài liệu",
 "bao-cao-dbcl-nam": "kết thúc năm học và Phòng Khảo thí & ĐBCL cần tổng hợp hoạt động đảm bảo chất lượng",
 "bao-cao-giam-sat-du-an-dau-tu": "dự án đầu tư hạ tầng đang triển khai và cần báo cáo định kỳ lãnh đạo/Hội đồng trường",
 "bao-cao-ket-qua-doan": "một đoàn công tác đã hoàn thành và cần báo cáo Ban Giám hiệu",
 "bao-cao-ket-qua-tuyen-sinh": "kết thúc đợt tuyển sinh và Phòng Đào tạo cần báo cáo kết quả gửi cơ quan quản lý",
 "bao-cao-kiem-toan-noi-bo": "kết thúc một cuộc kiểm toán nội bộ và đoàn cần lập báo cáo kết quả",
 "bao-cao-tien-do-de-tai": "đề tài đang thực hiện và đến kỳ báo cáo tiến độ định kỳ",
 "bao-cao-tong-ket-khoa": "kết thúc năm học và khoa cần tổng hợp hoạt động gửi Ban Giám hiệu",
 "bien-ban-bao-ve-luan-van": "ngay sau buổi bảo vệ luận văn thạc sĩ hoặc luận án tiến sĩ",
 "bien-ban-hop-hoi-dong-khdt": "sau mỗi phiên họp Hội đồng Khoa học và Đào tạo cần lập biên bản",
 "campaign-brief-tuyen-sinh": "trước mỗi đợt chiến dịch tuyển sinh cần một bản brief thống nhất để triển khai và trình duyệt",
 "cap-chung-chi-dao-tao-lien-tuc": "khóa bồi dưỡng ngắn hạn kết thúc và cần cấp chứng chỉ",
 "dich-thuat-song-ngu-va-thuat-ngu": "cần bản tiếng Anh (hoặc tiếng Việt) của văn bản trường học",
 "dong-goi-skill-tu-quy-trinh": "đơn vị muốn biến một quy trình công việc thành skill AI dùng lại được",
 "faq-chinh-sach-co-trich-nguon": "cần xây dựng hoặc vận hành kênh hỏi đáp về chính sách, quy định của trường",
 "funnel-theo-doi-thi-sinh": "trong chiến dịch tuyển sinh cần quản lý thí sinh tiềm năng theo từng giai đoạn phễu",
 "helpdesk-cntt-triage": "tiếp nhận yêu cầu hỗ trợ CNTT cần phân loại nhanh và ưu tiên đúng SLA",
 "hop-dong-thuc-hien-de-tai": "đề tài NCKH đã có quyết định phê duyệt và cần lập hợp đồng thực hiện",
 "ke-hoach-cai-tien-chat-luong": "đã có kết quả tự đánh giá hoặc kết luận đánh giá ngoài và cần chuyển khuyến nghị thành kế hoạch hành động",
 "ke-hoach-hoat-dong-trung-tam-thuc-hanh": "đầu năm học trung tâm thực hành cần lập kế hoạch hoạt động",
 "ke-hoach-nckh-khoa": "đầu năm học khoa cần xây dựng kế hoạch nghiên cứu khoa học",
 "ke-hoach-tiep-nhan-quan-ly-noi-tru": "đầu năm học hoặc đầu học kỳ cần lập kế hoạch tiếp nhận và quản lý sinh viên nội trú",
 "ke-hoach-to-chuc-su-kien": "tổ chức hội nghị, hội thảo, lễ khai giảng/bế giảng, ngày hội việc làm, lễ kỷ niệm",
 "nghi-quyet-hoi-dong-khdt": "Hội đồng Khoa học và Đào tạo đã biểu quyết và cần ban hành nghị quyết",
 "phan-cong-giang-day": "bắt đầu học kỳ và khoa/bộ môn cần phân công giảng viên theo học phần, lớp học phần",
 "phan-tich-chenh-lech-ngan-sach": "cuối quý/năm hoặc cần giải trình chênh lệch giữa dự toán và thực hiện",
 "phan-tich-ket-qua-khao-sat": "đã có dữ liệu khảo sát thô và cần báo cáo phân tích có kết luận, đề xuất",
 "phan-tich-ket-qua-thi": "kỳ thi kết thúc và đã có bảng điểm",
 "press-kit-su-kien": "tổ chức sự kiện cần mời báo chí đưa tin",
 "quyet-dinh-phan-cong-thi": "cần ban hành quyết định phân công coi thi, chấm thi, thanh tra thi cho một kỳ thi cụ thể",
 "quyet-dinh-phuc-khao": "đã chấm phúc khảo xong và cần ban hành quyết định công nhận kết quả",
 "ra-soat-du-thao-van-ban": "trước khi trình lãnh đạo ký bất kỳ văn bản nào",
 "theo-doi-grant-nghien-cuu": "chuẩn bị hồ sơ xin tài trợ nghiên cứu hoặc đang thực hiện grant cần theo dõi milestone, kinh phí",
 "theo-doi-thay-doi-van-ban-phap-quy": "có văn bản pháp quy mới thay thế hoặc sửa đổi văn bản đang áp dụng và cần đánh giá tác động",
 "tong-quan-tai-lieu-khoa-hoc": "viết phần tổng quan nghiên cứu cho đề tài, luận văn/luận án, bài báo",
 "triage-case-sinh-vien": "tiếp nhận phản ánh, khiếu nại, đề nghị của sinh viên và cần phân loại ưu tiên",
 "tro-ly-giang-day": "chuẩn bị bài giảng, xây dựng rubric hoặc soạn nhận xét phản hồi cho sinh viên",
}


def main():
    n = 0
    for name, use in USE.items():
        p = ROOT / "skills" / name / "SKILL.md"
        t = p.read_text(encoding="utf-8")
        m = re.search(r'^description: "(.*)"$', t, flags=re.M)
        d = m.group(1)
        if any(k in d for k in ("Dùng khi", "Dùng để", "Dùng cho")):
            continue
        d2 = d.rstrip() 
        d2 = d2 if d2.endswith(".") else d2 + "."
        d2 += f" Dùng khi {use}."
        if len(d2) > 400:
            print("quá dài", name, len(d2))
        t = t.replace(m.group(0), f'description: "{d2}"', 1)
        p.write_text(t, encoding="utf-8")
        n += 1
    print(n, "mô tả đã bổ sung")


if __name__ == "__main__":
    main()
