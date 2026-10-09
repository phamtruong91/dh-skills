---
name: "bao-cao-tu-danh-gia"
description: "Soạn báo cáo tự đánh giá cơ sở giáo dục hoặc chương trình đào tạo của trường đại học theo bộ tiêu chuẩn kiểm định (Thông tư 20/2026/TT-BGDĐT cho CSGD, Thông tư 04/2025/TT-BGDĐT cho CTĐT). Dùng khi chuẩn bị kiểm định chất lượng giáo dục."
---

# Báo cáo tự đánh giá (kiểm định chất lượng)

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

Nếu có cập nhật pháp lý dưới đây, đọc [căn cứ và điều kiện áp dụng](references/phap-ly.md) trước khi làm. Phần quy trình lịch sử ở cuối chỉ để đối chiếu, không dùng làm chỉ dẫn hiện hành.

## Quy trình cập nhật 1.1.0

1. Xác nhận yêu cầu “Báo cáo tự đánh giá (kiểm định chất lượng)”, dữ liệu gốc và thời điểm nghiệp vụ.
2. Chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi [CẦN XÁC MINH], chưa kết luận tuân thủ.
- Yêu cầu ngày hoàn tất tự đánh giá, ngày đăng ký đánh giá ngoài, khung tiêu chuẩn và minh chứng. Điều 51: chỉ cơ sở đã tự đánh giá VÀ đăng ký đánh giá ngoài trước 15/05/2026 được tiếp tục khung 12/2017, hoàn tất chậm nhất 31/12/2026. Ngoài chuyển tiếp dùng 20/2026; không chuyển thang điểm cơ học.
- Tách kiểm định chương trình khỏi kiểm định cơ sở. Yêu cầu phiên bản tiêu chuẩn, ngày đăng ký và bộ minh chứng; trích tiêu chí từ phụ lục hiện hành. Không mặc định khung 11 tiêu chuẩn của 04/2016 là khung hiện hành; đối chiếu chuyển tiếp trước khi tiếp tục hồ sơ cũ.

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
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/bao-cao-tu-danh-gia`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản, cập nhật căn cứ pháp lý và tách quy trình lịch sử.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
