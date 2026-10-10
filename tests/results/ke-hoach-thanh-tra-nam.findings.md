# Kết quả chạy thử: ke-hoach-thanh-tra-nam

Ngày chạy: 10/10/2026. Người chạy: Claude (đóng vai AI làm theo SKILL.md). Dữ liệu: `tests/samples/ke-hoach-thanh-tra-nam.input.json` (dữ liệu giả).
File giao: `tests/outputs/ke-hoach-thanh-tra-nam.docx` (Word thật, 2 trang, đã dựng trang và xem lại).

Phát hiện khi chạy, thuộc phần trao đổi với người dùng, không đưa vào file:

- **XUNG_DOT_LOI_ICH**: cuộc 1 thanh tra Phòng Đào tạo nhưng thành viên Phạm Văn Dũng công tác tại Phòng Đào tạo. File giữ theo đầu vào, cần thay người trước khi trình ký (quy tắc tại Bước 4).
- **TRUNG_DON_VI_CUNG_QUY**: cuộc 3 và cuộc 5 cùng Phòng Tài chính – Kế toán, cùng Quý III/2027. File giữ theo đầu vào; đề nghị người phụ trách xác nhận hoặc giãn thời gian (quy tắc tại Bước 3).
- **THIEU_DOAN_CUOC_4**: cuộc 4 chưa có đoàn nên chừa dòng dấu chấm cho trưởng đoàn và thành viên.
- **THIEU_MUC_DICH**: đầu vào không có mục đích, yêu cầu; hai mục này để dòng dấu chấm, không tự soạn.
- **NGOAI_LE_THANH_TRA_THI**: lần chạy đầu cho thấy Bước 3 yêu cầu "loại trừ trùng lịch thi, tuyển sinh", trong khi cuộc thanh tra thi hoặc tuyển sinh phải diễn ra đúng thời điểm đó. Đã sửa spec (thêm ngoại lệ, và không tự đổi thời gian đã nhập). Lần chạy này không coi cuộc 1, 2 là trùng lịch.
- **MAU_THUAN_CO_QUAN_BAN_HANH**: "Cấu trúc sản phẩm" nêu tên đơn vị lập (Phòng Thanh tra & Pháp chế) ở phần đầu, còn quy tắc chung nói cơ quan ban hành là trường. File ghi trường là cơ quan ban hành; Phòng Thanh tra & Pháp chế xuất hiện ở mục IV. Cần chủ skill thống nhất lại cách ghi ở `references/quy-cach-dau-ra.md`.

Phát hiện bổ sung: phương pháp thanh tra mặc định theo lĩnh vực chưa được skill định nghĩa; phần III dùng danh sách phương pháp nêu ở Bước 5 và hai quy tắc bắt buộc (đối chiếu độc lập với tài chính, văn bằng; phỏng vấn có biên bản). Căn cứ pháp lý của skill đã cập nhật sang Luật Thanh tra 84/2025/QH15 và NĐ 216/2025/NĐ-CP theo nguồn thứ cấp, chưa đối chiếu Công báo.
