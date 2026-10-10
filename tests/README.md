# Thử nghiệm bằng dữ liệu giả

Toàn bộ dữ liệu trong thư mục này là **giả** (cơ quan, người, số hiệu đều là mẫu).

| Thư mục | Nội dung |
| --- | --- |
| `samples/<skill>.input.json` | Đầu vào giả, có cài sẵn các "bẫy" (thiếu dữ liệu, xung đột, số liệu lệch) |
| `samples/<skill>.expect.json` | Kỳ vọng: chuỗi bắt buộc/bị cấm, chỗ phải chừa trống, ô công thức, danh sách bẫy |
| `outputs/` | File Word/Excel do AI làm theo SKILL.md tạo ra |
| `results/<skill>.findings.md` | Những điều phát hiện khi chạy, ghi theo mã bẫy |

Chạy: `python -X utf8 scripts/check_outputs.py` (cần `python-docx`, `openpyxl`; có LibreOffice thì tính lại công thức Excel).

`build_reference_outputs.py` (công văn, thanh tra, PMO, quyết định) và `build_van_ban_pho_bien.py` (thông báo, biên bản, tờ trình, giấy mời) dựng 8 file mẫu để làm bằng chứng; để thử skill khác hoặc AI khác, tạo file của bạn vào `outputs/` với cùng tên rồi chạy bộ kiểm tra. Để thêm skill: tạo cặp `.input.json`/`.expect.json` và `.findings.md`.

Giới hạn: bộ kiểm tra chứng minh file mở được, đúng quy tắc đầu ra và không bịa số liệu; không chứng minh nội dung pháp lý đúng.

**Hạn chế cần biết:** các file mẫu do script này dựng theo SKILL.md, không phải do một mô hình AI độc lập làm theo skill rồi nộp bài; nên kết quả chứng minh chỉ rằng skill làm theo được và file đạt quy tắc, chưa phải bằng chứng một AI bất kỳ sẽ làm đúng. Muốn kiểm chứng thật, cho AI khác nhận cùng `.input.json`, tạo file vào `outputs/` và chạy `check_outputs.py`.
