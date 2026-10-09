---
name: "chuan-bi-hop-hoi-dong-truong"
description: "Chuẩn bị họp Hội đồng trường: tổng hợp tài liệu, soạn chương trình và thư mời, dự thảo nghị quyết, ghi biên bản và theo dõi thực hiện nghị quyết. Dùng cho Văn phòng Hội đồng trường trước mỗi kỳ họp định kỳ/đột xuất."
---

# Chuẩn bị họp Hội đồng trường

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

Nếu có cập nhật pháp lý dưới đây, đọc [căn cứ và điều kiện áp dụng](references/phap-ly.md) trước khi làm. Phần quy trình lịch sử ở cuối chỉ để đối chiếu, không dùng làm chỉ dẫn hiện hành.

## Quy trình cập nhật 1.1.0

1. Xác nhận yêu cầu “Chuẩn bị họp Hội đồng trường”, dữ liệu gốc và thời điểm nghiệp vụ.
2. Chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi [CẦN XÁC MINH], chưa kết luận tuân thủ.
- 99/2019 không bị thay thế toàn bộ. NQ10 loại trừ quy định về hội đồng trường/đại học công lập: điểm b khoản4Điều2, điểm e khoản1Điều3, điểm a khoản2Điều4, điểm c khoản4Điều4, điểm b khoản2Điều5, Điều7, khoản1Điều9, điểm c khoản2Điều16. Không tổ chức hoạt động mới của hội đồng trường công lập theo quy trình cũ. Yêu cầu loại hình trường, thời điểm xử lý, quy chế hiện hành, quyết định phân quyền; tư thục phải đối chiếu Luật125.

3. Thực hiện nghiệp vụ trên dữ liệu đã xác nhận; lập dự thảo và bảng đối chiếu. Các công thức, tiêu chí, mẫu biểu và thẩm quyền phải lấy từ căn cứ đã chọn, không từ ví dụ lịch sử.
4. Xuất dự thảo, phụ lục, danh sách thiếu dữ liệu và checklist pháp lý; chuyển cán bộ phụ trách xác nhận trước khi trình người có thẩm quyền. Không tự phát hành, công bố hoặc xác nhận đã ký.

## Đầu ra bổ sung

Kèm bảng căn cứ áp dụng, bảng dữ liệu truy nguyên đến nguồn, danh sách điểm chưa xác minh và phiếu trình kiểm duyệt. Số liệu chưa có ghi [CHƯA CUNG CẤP]; không suy diễn từ ví dụ.

**Giới hạn phạm vi:** Không dùng để tổ chức hoạt động mới của hội đồng trường công lập theo mô hình cũ từ 2026. Chỉ xử lý hồ sơ lịch sử hoặc trường tư thục sau khi xác nhận mô hình quản trị và thẩm quyền theo pháp luật hiện hành.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.


## Tư liệu đối chiếu

Quy trình trước cập nhật được lưu tại `references/quy-trinh-lich-su.md`. Chỉ đọc khi cần đối chiếu hồ sơ lịch sử; phải chọn căn cứ theo ngày nghiệp vụ trước khi sử dụng.


## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/chuan-bi-hop-hoi-dong-truong`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản, cập nhật căn cứ pháp lý và tách quy trình lịch sử.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
