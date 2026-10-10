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

`build_tai_lon.py` sinh dữ liệu giả lớn (cố định, lặp lại được) rồi dựng 3 file nhiều trang, tên có hậu tố `--tai-lon`; `check_outputs.py` kiểm tra thêm số trang, số trang từ trang 2, tiêu đề bảng lặp lại, dòng không bị cắt, mã sinh viên không mất/không trùng, khối ký không tách khỏi nội dung cuối (cần LibreOffice và `pdftotext`).

**Hạn chế cần biết:** các file mẫu do script này dựng theo SKILL.md, không phải do một mô hình AI độc lập làm theo skill rồi nộp bài; nên kết quả chứng minh chỉ rằng skill làm theo được và file đạt quy tắc, chưa phải bằng chứng một AI bất kỳ sẽ làm đúng. Muốn kiểm chứng thật, cho AI khác nhận cùng `.input.json`, tạo file vào `outputs/` và chạy `check_outputs.py`.

## Báo cáo có biểu đồ

`python -X utf8 tests/build_bao_cao_bieu_do.py` dựng 3 báo cáo (khảo sát, tiến độ đề tài, KHCN năm) và 1 file Excel có biểu đồ gốc; `scripts/check_outputs.py` kiểm biểu đồ. Giới hạn: bộ kiểm tra không "nhìn" được nội dung ảnh, chỉ đối chiếu văn bản thay thế (alt) với bảng; việc hình đúng số thật phải xem bằng mắt (đã xem bản render LibreOffice, chưa mở bằng Word). Số trong hình được sinh từ cùng dữ liệu với bảng nên khớp là điều dễ; bẫy thật nằm ở dữ liệu đầu vào (xem findings).

## Bộ slide PowerPoint

`node tests/build_pptx.js` dựng 4 bộ slide (cần pptxgenjs và kỹ năng pptx ở /mnt/skills/public/pptx); `scripts/check_outputs.py` kiểm cấu trúc, kèm công cụ `validate.py` của kỹ năng pptx. Giới hạn: kiểm "chữ tràn" chỉ là ước lượng theo số ký tự, việc chữ có vừa khung thật phải xem ảnh render (đã xem bằng LibreOffice, chưa mở bằng PowerPoint); phông Cambria/Calibri trên máy người dùng có thể khác bản thay thế khi render.
