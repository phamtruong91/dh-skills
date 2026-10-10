# Kết quả chạy thử: pmo-quan-tri-du-an

Ngày chạy: 10/10/2026. Người chạy: Claude (đóng vai AI làm theo SKILL.md). Dữ liệu: `tests/samples/pmo-quan-tri-du-an.input.json` (dữ liệu giả, đơn vị triệu đồng).
File giao: `tests/outputs/pmo-quan-tri-du-an.xlsx` (Excel thật, 4 sheet: Dashboard, Tracker, Issue log, Risk log; công thức đã tính lại bằng LibreOffice; Dashboard vừa 1 trang). Không có sheet Lessons learned vì chưa đến mốc lớn.

Phát hiện khi chạy, thuộc phần trao đổi với người dùng, không đưa vào file:

- **TONG_NGAN_SACH_LECH**: ngân sách được duyệt 600, nhưng tổng phân bổ theo gói việc là 640. Số liệu giữ nguyên, cả hai con số hiện trên Dashboard. Đã thêm bước đối chiếu này vào skill (Bước 1) vì trước đó không có.
- **THIEU_MINH_CHUNG_WP4**: WP4 có 65% nhưng không có minh chứng, nên ô % thực tế, chênh lệch, trạng thái để trống và % thực tế tổng thể cũng để trống (công thức chỉ tính khi mọi gói việc đã có minh chứng).
- **DELIVERABLE_MO_HO_WP5**: sản phẩm bàn giao "Hoàn thành giai đoạn chạy thử" không đo đếm được, trái lưu ý của Bước 1. File giữ nguyên, đề nghị chủ nhiệm viết lại.
- **ISSUE_QUA_HAN**: IS-02 hạn 30/09/2026, còn mở, bị đánh dấu "Quá hạn" so với ngày đối chiếu 10/10/2026 (ô ngày đối chiếu nhìn thấy và sửa được).
- **ISSUE_THIEU_NGUOI_XU_LY**: IS-03 chưa có người xử lý và hạn; ô để trống.
- **RISK_THIEU_GIAM_THIEU**: RK-02 chưa có biện pháp giảm thiểu; ô để trống.
- **QUYET_DINH_LANH_DAO_RONG**: đầu vào không có quyết định cần lãnh đạo nên bảng để trống. Đề nghị chủ nhiệm cân nhắc hai ứng viên: ưu tiên cấp quyền kết nối (IS-01, RK-01) và lệch ngân sách 40 triệu.

Phát hiện thêm: skill không định nghĩa ngưỡng phân loại 4 trạng thái. Đã thêm input `nguong_trang_thai` (thiếu thì để trống trạng thái, không tự đặt ngưỡng). Lần chạy dùng ngưỡng trong dữ liệu mẫu: WP2 chênh -10 điểm nên xếp "Chậm".
