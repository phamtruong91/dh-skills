# Thể thức và trình bày file Word, Excel

Áp dụng cho mọi skill xuất file. Văn bản hành chính theo Phụ lục I Nghị định 30/2020/NĐ-CP; biểu chuyên ngành giữ nguyên mẫu của văn bản chuyên ngành. Quy tắc cũng được ghi trong `references/quy-cach-dau-ra.md` của từng skill để cài riêng vẫn dùng được.

**Trạng thái xác minh:** các trị số dưới đây đối chiếu với bản sao Phụ lục I Nghị định 30/2020/NĐ-CP trên trang vanban.vcci.com.vn ngày 10/10/2026 (trùng với phần "Trình bày văn bản hành chính" đã có sẵn trong quy cách của skill). Chưa đối chiếu bản Công báo và chưa kiểm tra văn bản sửa đổi nếu có. Quy tắc bảng và nhiều trang (mục 3) là quy ước trình bày của bộ skill, không phải điều khoản của nghị định.

## 1. Trang giấy, phông, đoạn văn (Phụ lục I NĐ 30/2020)

| Hạng mục | Quy định |
| --- | --- |
| Khổ giấy | A4 (210 × 297 mm), thường chiều dọc; văn bản có bảng không tách phụ lục có thể dùng chiều ngang |
| Lề | Trên và dưới 20–25 mm; trái 30–35 mm; phải 15–20 mm |
| Phông | Times New Roman, Unicode TCVN 6909:2001, màu đen |
| Nội dung | Cỡ 13–14, canh đều hai lề, thụt đầu dòng 1 cm hoặc 1,27 cm |
| Khoảng cách | Cách đoạn tối thiểu 6 pt; giãn dòng từ đơn đến 1,5 |
| Số trang | Chữ số Ả Rập, giữa lề trên, cỡ 13–14, không in đậm; không hiện số ở trang đầu; phụ lục đánh số trang riêng |

## 2. Cỡ chữ và kiểu chữ từng thành phần

| Thành phần | Cỡ (pt) | Kiểu |
| --- | --- | --- |
| Quốc hiệu | 12–13 | Hoa, đậm |
| Tiêu ngữ "Độc lập - Tự do - Hạnh phúc" (gạch ngang) | 13–14 | Đậm, có đường kẻ dưới |
| Tên cơ quan chủ quản | 12–13 | Hoa, không đậm |
| Tên cơ quan ban hành | 12–13 | Hoa, đậm, có đường kẻ dưới |
| Số, ký hiệu | 13 | Thường |
| Địa danh, ngày tháng năm | 13–14 | Nghiêng |
| Tên loại văn bản | 13–14 | Hoa, đậm |
| Trích yếu (văn bản có tên loại) | 13–14 | Đậm |
| Trích yếu của công văn | 12–13 | Thường |
| Chức vụ người ký | 13–14 | Hoa, đậm |
| Họ tên người ký | 13–14 | Đậm |
| Nhãn "Nơi nhận:" | 12 | Đậm, nghiêng |
| Danh sách nơi nhận | 11 | Thường |

## 3. Bảng, danh sách và văn bản nhiều trang (quy ước của bộ skill)

- Bố cục bảng cố định, tổng bề rộng không vượt vùng chữ; cột STT rộng tối thiểu 1,4 cm để chữ "STT" không bị tách dòng.
- Cột STT, mã, lớp, ngày, đơn vị căn giữa; cột họ tên và nội dung dài căn trái; cột số tiền căn thống nhất cả cột. Cột ngày đủ rộng để mỗi khoảng thời gian không quá hai dòng.
- Chữ trong bảng cỡ 11–13 (khuyến nghị 12; 11 khi từ 7 cột trở lên).
- Dòng tiêu đề đậm, nền xám nhạt, lặp lại ở đầu mỗi trang; mọi dòng cao tối thiểu như nhau, căn giữa theo chiều dọc, có khoảng đệm trên dưới 2 pt; dòng không bị cắt giữa hai trang.
- STT liên tục từ 1; dòng tổng cộng ở cuối bảng, nền nhạt hơn; ô thiếu dữ liệu để trống theo mẫu.
- Tiêu đề IN HOA ngắt dòng cân đối; không để một chữ rơi xuống dòng riêng. Tên cơ quan ở phần đầu không ngắt chữ giữa chừng.
- Danh sách kèm theo là phụ lục: bắt đầu ở trang mới, ghi "Kèm theo Quyết định số ... ngày ..." (để trống nếu chưa có số), đánh số trang riêng từ 1.
- Khối chữ ký cùng trang với ít nhất một đoạn nội dung cuối; không đứng một mình ở trang mới.

## 4. Excel

- Dòng tiêu đề đậm, nền nhạt, cố định (freeze) khi bảng dài; bề rộng cột vừa chữ; số tiền có dấu phân cách hàng nghìn; ngày theo dd/mm/yyyy; công thức giữ nguyên, không dán giá trị thay công thức.
- Đặt vùng in và lặp dòng tiêu đề khi in; một bảng một sheet khi dữ liệu khác bản chất; ô thiếu dữ liệu để trống, không ghi 0.

## 5. Kiểm tra

`scripts/check_outputs.py` kiểm tự động các điểm ở mục 1–3 trên file Word (khổ giấy, lề, phông, cỡ chữ từng thành phần, tiêu ngữ, thụt đầu dòng, cách đoạn, số trang từ trang 2, phụ lục đánh số riêng, tiêu đề bảng lặp, dòng không bị cắt, STT, chữ mồ côi ở tiêu đề). Cần LibreOffice và `pdftotext` để kiểm số trang và ngắt dòng. Bộ kiểm tra không thay việc mở file xem bố cục thực tế; đã có lỗi hiển thị mà kiểm tra tự động báo "đạt".
