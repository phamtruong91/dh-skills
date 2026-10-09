---
name: "bao-cao-cong-khai-tai-chinh"
description: "Soạn báo cáo công khai tài chính của trường đại học để minh bạch ngân sách, gắn với 3 công khai theo Thông tư 09/2024/TT-BGDĐT. Dùng khi Phòng Tài chính – Kế toán cần công bố học phí, tổng thu – chi, chi cho người học và kết quả kiểm toán trên cổng thông tin điện tử."
---

# Soạn báo cáo công khai tài chính

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

Nếu có cập nhật pháp lý dưới đây, đọc [căn cứ và điều kiện áp dụng](references/phap-ly.md) trước khi làm. Phần quy trình lịch sử ở cuối chỉ để đối chiếu, không dùng làm chỉ dẫn hiện hành.

## Quy trình cập nhật 1.1.0

1. Xác nhận yêu cầu “Soạn báo cáo công khai tài chính”, dữ liệu gốc và thời điểm nghiệp vụ.
2. Chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi [CẦN XÁC MINH], chưa kết luận tuân thủ.
- Chuyển từ mẫu ba công khai cũ sang nội dung công khai và báo cáo thường niên theo 09/2024. Đối chiếu phần thông tin chung, phần giáo dục đại học và phụ lục báo cáo thường niên; lưu nội dung trên website tối thiểu 5 năm. Ghi thời điểm, đường dẫn công bố, người duyệt và bằng chứng cập nhật. Không tự thêm số liệu hoặc tự công bố; không coi báo cáo gửi cơ quan quản lý là nghĩa vụ định kỳ nếu không có căn cứ/yêu cầu bằng văn bản.
- Yêu cầu năm học, trình độ, ngành, loại hình trường, mức tự chủ, quyết định học phí được duyệt và đối tượng miễn/giảm/hỗ trợ. Đối chiếu 238/2025 và chuyển tiếp; không lấy mức trần, tỷ lệ tăng hoặc đối tượng từ 81/2021/97/2023 làm mặc định hiện hành. Chỉ tính khi đủ căn cứ và dữ liệu từng người học.

3. Thực hiện nghiệp vụ trên dữ liệu đã xác nhận; lập dự thảo và bảng đối chiếu. Các công thức, tiêu chí, mẫu biểu và thẩm quyền phải lấy từ căn cứ đã chọn, không từ ví dụ lịch sử.
4. Xuất dự thảo, phụ lục, danh sách thiếu dữ liệu và checklist pháp lý; chuyển cán bộ phụ trách xác nhận trước khi trình người có thẩm quyền. Không tự phát hành, công bố hoặc xác nhận đã ký.

## Đầu ra bổ sung

Kèm bảng căn cứ áp dụng, bảng dữ liệu truy nguyên đến nguồn, danh sách điểm chưa xác minh và phiếu trình kiểm duyệt. Số liệu chưa có ghi [CHƯA CUNG CẤP]; không suy diễn từ ví dụ.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.


## Tư liệu đối chiếu

Quy trình trước cập nhật được lưu tại `references/quy-trinh-lich-su.md`. Chỉ đọc khi cần đối chiếu hồ sơ lịch sử; phải chọn căn cứ theo ngày nghiệp vụ trước khi sử dụng.


## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/bao-cao-cong-khai-tai-chinh`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản, cập nhật căn cứ pháp lý và tách quy trình lịch sử.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
