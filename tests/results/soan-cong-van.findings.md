# Kết quả chạy thử: soan-cong-van

Ngày chạy: 10/10/2026. Người chạy: Claude (đóng vai AI làm theo SKILL.md). Dữ liệu: `tests/samples/soan-cong-van.input.json` (dữ liệu giả).
File giao: `tests/outputs/soan-cong-van.docx` (Word thật, 1 trang, đã dựng trang bằng LibreOffice và xem lại).

Các điểm phát hiện khi chạy, thuộc phần trao đổi với người dùng, không đưa vào file:

- **HAN_DA_QUA**: nội dung điểm 3 ghi "trước ngày 05/10/2026", đã qua so với ngày chạy 10/10/2026. File giữ nguyên theo đầu vào; cần người soạn xác nhận lại mốc.
- **TUQ_THIEU_UY_QUYEN**: người ký là Trưởng phòng ký TUQ. nhưng đầu vào không có văn bản ủy quyền. File ghi khối ký theo đầu vào; cần kiểm tra căn cứ ủy quyền trước khi trình ký.
- **TRICH_YEU_THUA**: trích yếu đầu vào có sẵn "về việc"; khi ghi sau "V/v" đã bỏ cụm này, còn câu mở đầu phúc đáp giữ "về việc".
- **SO_VAN_BAN_CHUA_CAP**: số văn bản, ngày ban hành chưa có nên chừa dấu chấm; phần mã cơ quan trong ký hiệu cũng chưa có nên chừa chỗ, chỉ giữ mã đơn vị soạn "ĐT".

Nhận xét về skill: chạy được theo đúng 7 bước; quy tắc "không điền ngày, số từ ngày chạy" kiểm tra được bằng máy.
