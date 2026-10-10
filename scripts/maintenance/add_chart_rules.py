"""Đưa quy tắc biểu đồ/hình vào các skill báo cáo số liệu (chạy lại an toàn).

Danh sách skill: scripts/chart_skills.txt. Thêm mục "## Biểu đồ và hình trong báo cáo số liệu" vào references/quy-cach-dau-ra.md
và một câu dẫn vào SKILL.md (ngay sau câu dẫn mục thể thức). Dùng: python -X utf8 scripts/maintenance/add_chart_rules.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MARK = "## Biểu đồ và hình trong báo cáo số liệu"
NOTE = "Khi báo cáo có số liệu cần so sánh hoặc nêu xu hướng, đọc mục “Biểu đồ và hình trong báo cáo số liệu” trong quy cách đầu ra trước khi vẽ."
SECTION = f"""
{MARK}

**Khi nào vẽ**
- Chỉ vẽ khi có từ 3 giá trị trở lên cần so sánh hoặc theo dõi xu hướng, và mọi số đều có trong đầu vào hoặc tính được từ đầu vào. Không vẽ cho 1–2 con số.
- Không vẽ nhóm có mẫu quá nhỏ (khảo sát dưới 30 phiếu), số liệu chưa có minh chứng, hoặc để gợi ra kết luận mà dữ liệu không nói.
- Mỗi hình đi kèm một bảng cùng số liệu trong báo cáo. Số trong hình phải trùng số trong bảng (cùng cách làm tròn). Khi hai nguồn lệch nhau, giữ nguyên, nêu độ lệch ở mục hạn chế, không tự chọn số cho đẹp.

**Chọn loại biểu đồ**
- So sánh giữa các nhóm: cột. So sánh hai kỳ hoặc dự toán với thực hiện: cột ghép. Thang đo nhiều mức (Likert): cột xếp chồng 100%. Xu hướng từ 4 mốc thời gian trở lên: đường.
- Không dùng biểu đồ 3D. Biểu đồ tròn chỉ khi có không quá 5 phần và tổng là 100%.

**Trục, nhãn, màu**
- Cột bắt đầu từ 0. Ghi tên trục và đơn vị (điểm, %, triệu đồng, số công trình). Ghi số trên cột nếu không quá dày; nếu dày thì ghi trong bảng.
- Đường ngưỡng đánh giá vẽ bằng nét đứt, chú giải đặt ngoài vùng vẽ để không đè lên nhãn số.
- Phải phân biệt được khi in đen trắng: dùng độ đậm nhạt khác nhau kèm hoa văn, không dựa riêng vào màu. Chữ trong hình dùng Times New Roman hoặc phông tương đương, từ 8 pt trở lên khi in.

**Dữ liệu thiếu, chưa đủ kỳ, câu đảo**
- Thiếu dữ liệu: ghi “n/a” hoặc “chưa có minh chứng” đúng vị trí, không vẽ cột 0 và không cộng thiếu vào tổng.
- Năm chưa đủ (ví dụ đến 30/9): ghi mốc ngay trong nhãn trục và dòng Nguồn; không nhận xét tăng giảm so với năm đủ 12 tháng.
- Câu hỏi đảo mã hóa ngược trước khi tính và vẽ, ghi chú trong dòng Nguồn. Hai kỳ chỉ so sánh khi câu hỏi và thang đo giữ nguyên.

**Dựng trong Word**
- Ảnh PNG từ 150 dpi khi in (khuyến nghị 200), rộng 8–16 cm, căn giữa, không vượt vùng chữ.
- Dưới hình: dòng “Hình n. Tên hình” (cỡ 13, đậm, căn giữa), rồi dòng “Nguồn: …” (cỡ 13, nghiêng, căn giữa; ghi kỳ, phạm vi, ghi chú). Hình, chú thích và nguồn dính nhau để không tách trang. Số hình liên tục từ 1. Tên bảng ghi “Bảng n. …” đặt phía trên bảng.
- Văn bản thay thế (alt) của hình ghi số liệu theo dạng “nhãn=giá trị; …” kèm đơn vị, để người dùng đọc màn hình và để đối chiếu với bảng.
- Hình PNG không sửa được số. Nếu người dùng cần sửa, giao kèm file Excel có biểu đồ gốc, và nói rõ khi số liệu đổi thì phải vẽ lại hình.
- Số thập phân dùng một kiểu thống nhất trong cả văn bản (khuyến nghị dấu phẩy: 4,12); ngưỡng và ví dụ trong báo cáo viết cùng kiểu.

**Dựng trong Excel**
- Dùng biểu đồ gốc tham chiếu ô dữ liệu (không dán ảnh). Đặt biểu đồ bên dưới bảng, không đè lên dữ liệu.
- Đặt hướng in ngang, vừa chiều rộng một trang, đặt vùng in và lặp dòng tiêu đề, để bảng và biểu đồ không bị cắt giữa các trang.

**Trước khi giao**: mở file xem từng hình: nhãn không đè nhau, chữ không bị cắt, hình nằm cùng trang với chú thích, số khớp bảng. Kiểm tra tự động chỉ bắt được lỗi cấu trúc, không thay việc nhìn hình.
"""


def main():
    names = [n.strip() for n in (ROOT / "scripts" / "chart_skills.txt").read_text(encoding="utf-8").splitlines() if n.strip()]
    changed = 0
    for n in names:
        d = ROOT / "skills" / n
        q, s = d / "references" / "quy-cach-dau-ra.md", d / "SKILL.md"
        if not q.exists() or not s.exists():
            print("thiếu", n)
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
                    break
            else:
                print("không thấy câu dẫn thể thức:", n)
                continue
            s.write_text("\n".join(lines), encoding="utf-8")
    print("đã cập nhật", changed, "skill")


if __name__ == "__main__":
    main()
