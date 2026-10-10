# Phát hiện khi chạy thử soan-thong-bao (dữ liệu giả)

- **NGAY_KHONG_KHOP_THU**: đầu vào ghi "thứ Sáu, ngày 17/10/2026" nhưng 17/10/2026 là thứ Bảy. File giao bỏ phần thứ, chỉ giữ ngày, không tự quyết định đúng/sai; phản hồi phải hỏi lại người dùng ngày hay thứ nào đúng.
- **HAN_DANG_KY_PHAI_TRUOC_SU_KIEN**: hạn đăng ký 12/10/2026 đứng trước ngày họp 17/10/2026, hợp lý; file giao giữ nguyên hạn này.
- **SO_VAN_BAN_KHONG_TU_CAP**: đầu vào không có số; file giao để "Số: ....../TB-......".
