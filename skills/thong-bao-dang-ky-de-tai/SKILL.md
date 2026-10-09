---
name: "thong-bao-dang-ky-de-tai"
description: "Soạn thông báo đăng ký đề tài NCKH các cấp (cấp trường, cấp bộ/tỉnh, cấp nhà nước) đúng thể thức hành chính. Dùng khi Phòng KHCN triển khai đợt đăng ký đề tài NCKH hằng năm hoặc đột xuất cho cán bộ, giảng viên trong trường."
---

# Thông báo đăng ký đề tài NCKH các cấp

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.



## Quy trình cập nhật pháp lý

1. Xác nhận thời điểm, loại hình trường, hồ sơ gốc và căn cứ áp dụng.
- Yêu cầu cấp nhiệm vụ, nguồn kinh phí, tài trợ/đặt hàng, ngày phê duyệt, quy chế cơ quan tài trợ, phương thức khoán và quyền sử dụng kết quả. Đối chiếu NĐ265 về tài chính và NĐ267 về nhiệm vụ; không cố định thang xếp loại hoặc thu hồi toàn bộ kinh phí cho mọi đề tài. Nghiệm thu dựa hợp đồng và tiêu chí được duyệt, hội đồng có thẩm quyền xác nhận.

2. Lập dự thảo trên dữ liệu đã xác nhận, kèm bảng đối chiếu căn cứ/điều khoản và nguồn dữ liệu. Thiếu văn bản gốc hoặc điều khoản ghi [CẦN XÁC MINH]. Không dùng mẫu/công thức lịch sử như hiện hành.
3. Cán bộ nghiệp vụ kiểm tra và trình người có thẩm quyền; không tự ký, phát hành hoặc thay quyết định.

Xem [căn cứ pháp lý](references/phap-ly.md). Tư liệu trước cập nhật ở `references/quy-trinh-lich-su.md` chỉ dùng đối chiếu hồ sơ lịch sử.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/thong-bao-dang-ky-de-tai`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
