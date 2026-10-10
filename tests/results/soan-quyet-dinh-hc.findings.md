# Phát hiện khi chạy thử soan-quyet-dinh-hc (dữ liệu giả)

- **SO_QD_KHONG_TU_CAP**: đầu vào không có số quyết định; file giao để "Số: ....../QĐ-......", không lấy số tiếp theo hay số tự đặt. Việc cấp số do văn thư khi đăng ký.
- **DANH_SACH_KEM_THEO_THIEU**: Điều 1 nhắc "danh sách kèm theo" nhưng đầu vào không có danh sách thành viên; file giao để dòng dấu chấm và phản hồi nêu người dùng cần bổ sung.
- **NGAY_HIEU_LUC**: hiệu lực "kể từ ngày ký" khớp ý đồ ban hành; không tự đặt ngày cụ thể.
- Căn cứ viết theo đúng chuỗi người dùng cung cấp; bỏ phần chú thích trong ngoặc của đầu vào khỏi văn bản.
- Chưa xác minh được từ nguồn nào ngoài đầu vào rằng Hiệu trưởng có thẩm quyền thành lập Ban này; skill yêu cầu người dùng xác nhận thẩm quyền.
