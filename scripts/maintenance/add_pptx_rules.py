"""Đưa quy tắc xuất PowerPoint vào mọi skill (chạy lại an toàn).

Thêm mục "## Xuất PowerPoint (.pptx) khi được yêu cầu" vào references/quy-cach-dau-ra.md và một câu dẫn vào SKILL.md.
Dùng: python -X utf8 scripts/maintenance/add_pptx_rules.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MARK = "## Xuất PowerPoint (.pptx) khi được yêu cầu"
NOTE = "Khi người dùng yêu cầu bộ slide (.pptx), đọc mục “Xuất PowerPoint (.pptx) khi được yêu cầu” trong quy cách đầu ra."
SECTION = f"""
{MARK}

- **Bộ slide là tài liệu trình bày, không thay văn bản gốc.** Không dùng quốc hiệu, nơi nhận, khối chữ ký của văn bản hành chính trên slide. Công văn, quyết định, báo cáo chính thức vẫn giao bằng .docx; nói rõ điều này trong phản hồi.
- **Xác định cách dùng**: trình chiếu trực tiếp (ít chữ, mỗi slide một ý, khoảng 1,5–2 phút mỗi slide, số slide không vượt số phút của bài nói) hay đọc trước (được nhiều chữ hơn, nhưng vẫn một ý mỗi slide). Chưa biết thì ghi giả định đã dùng.
- **Cấu trúc**: slide mở đầu, kết luận hoặc tóm tắt đặt trước, các phần nội dung, tồn tại hoặc điểm cần quyết, bước tiếp theo. Tiêu đề mỗi slide nêu kết luận (không quá 16 chữ, không dấu chấm cuối) và là ô tiêu đề thật của slide để có dàn ý và đọc được bằng trình đọc màn hình.
- **Cỡ chữ**: tiêu đề từ 28 pt, nội dung và chữ trong bảng từ 14 pt, nguồn và chú thích từ 11 pt. Không thu nhỏ chữ để nhét thêm; quá dày thì tách slide. Khi trình chiếu trực tiếp, mỗi slide không quá khoảng 85 chữ.
- **Số liệu và biểu đồ**: dùng biểu đồ gốc của PowerPoint (sửa được), không dán ảnh; áp dụng quy tắc biểu đồ trong quy cách này nếu có. Mỗi biểu đồ và mỗi số nổi bật có dòng “Nguồn”. Thiếu số liệu thì ghi “Chưa có số liệu”, không vẽ cột 0.
- **Dữ liệu lệch hoặc thiếu**: số liệu lệch nhau, mục tiêu không đo được, đơn vị chưa nộp báo cáo, thiếu định hướng của lãnh đạo: nói thẳng trên slide (ô “Cần rà lại”, “Chưa có số liệu”) và trong ghi chú. Không điền cho đẹp, không bịa chỉ tiêu, nguồn, tên sách.
- **Ghi chú người trình bày** trên mọi slide (từ 15 chữ): lời nói chính, nguồn, điểm cần thận trọng. Không đặt ghi chú vào ô chữ trên slide.
- **Trình bày**: một bảng màu, bố cục và vị trí tiêu đề nhất quán, lề từ 0,5 inch, chữ không đè nhau, không có slide toàn chữ khi có thể dùng số liệu hoặc hình. Các nhãn trục, cột, ô trong sơ đồ phải đủ để đọc mà không cần lời nói.
- **Trước khi giao**: chạy công cụ kiểm tra cấu trúc của kỹ năng pptx, xuất ảnh từng slide và xem: chữ không tràn khung, không đè nhau, số khớp nguồn. Kiểm tra tự động không thay việc xem ảnh.
"""


def main():
    changed = 0
    for d in sorted((ROOT / "skills").iterdir()):
        q, s = d / "references" / "quy-cach-dau-ra.md", d / "SKILL.md"
        if not q.is_file() or not s.is_file():
            continue
        t = q.read_text(encoding="utf-8")
        if MARK not in t:
            q.write_text(t.rstrip("\n") + "\n" + SECTION, encoding="utf-8")
            changed += 1
        t = s.read_text(encoding="utf-8")
        if NOTE not in t:
            lines = t.split("\n")
            for i, ln in enumerate(lines):
                if ln.startswith("Khi dựng file Word/Excel, áp dụng mục"):
                    lines[i] = ln + "\n\n" + NOTE
                    s.write_text("\n".join(lines), encoding="utf-8")
                    break
            else:
                print("không thấy câu dẫn (skill không dựng Word/Excel):", d.name)
    print("đã cập nhật", changed, "skill")


if __name__ == "__main__":
    main()
