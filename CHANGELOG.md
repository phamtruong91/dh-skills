# Nhật ký thay đổi

## 1.3.1 — 2026-10-10

- Phân biệt định dạng mặc định với định dạng được chọn theo sản phẩm/yêu cầu; thêm available_output_formats trong manifest và từng skill.
- Bổ sung PDF, CSV, TXT, MD, HTML, JSON, YAML, PPTX, PNG, SVG, TEX, BIB đúng nhóm nghiệp vụ; không coi skill viết kịch bản là công cụ tạo MP4.
- Giữ bắt buộc file thực tế, không đổi đuôi giả và không tự xuất mọi định dạng cùng lúc.

## 1.3.0 — 2026-10-10

- Bắt buộc tạo file thực tế và cung cấp liên kết tải khi tạo sản phẩm nghiệp vụ; bỏ cách hoàn thành bằng nội dung chat rồi chờ yêu cầu xuất file.
- Gán định dạng mặc định cho 171 skill: 150 Word, 20 Excel, 1 ZIP; ưu tiên định dạng người dùng yêu cầu.
- Đồng bộ chỉ dẫn, lời nhắc giao diện, manifest và phiên bản; giữ chỗ điền theo mẫu và không xuất checklist kiểm tra.

## 1.2.1 — 2026-10-10

- Sửa quy tắc dữ liệu thiếu của 171 skill: giữ dấu chấm, dấu gạch hoặc ô trống đúng mẫu gốc; bỏ lệnh cấm dấu chấm.
- Bổ sung dòng dấu chấm trong khung biên bản, giữ ô bảng trống theo mẫu và đồng bộ phiên bản/manifest.
- Giữ quy tắc không xuất checklist hay phụ lục kiểm tra đầu ra.

## 1.2.0 — 2026-10-10

- Rà soát đầu ra 171 skill; thêm quy cách tự chứa trong từng gói và cấu trúc sản phẩm theo nghiệp vụ.
- File giao chỉ chứa sản phẩm chính; bỏ yêu cầu xuất checklist, phụ lục kiểm tra, bảng truy nguyên và danh sách thiếu dữ liệu; giữ phụ lục nghiệp vụ khi mẫu yêu cầu.
- Thông tin thiếu để trống; bỏ nhãn CHỜ KÝ và nhãn kiểm duyệt tự chèn; không tự gán số, ngày, người ký hoặc kết luận.
- Đối chiếu Phụ lục I/III Nghị định 30; sửa mẫu công văn, thông báo, giấy mời, biên bản và phân biệt cơ quan ban hành/phòng soạn.
- Bổ sung lựa chọn mẫu chuyên ngành cho công khai, tài chính, quyết toán, nhân sự, kiểm kê, kiểm định, đào tạo và đấu thầu. Mẫu lịch sử vẫn chỉ dùng cho hồ sơ thuộc chuyển tiếp.
- Cập nhật manifest, phiên bản và công cụ kiểm tra gói. Đây là rà soát quy cách đầu ra, không chứng nhận toàn bộ mọi căn cứ chuyên ngành còn hiệu lực.

## 1.1.1 — 2026-10-09

- Sửa bao-cao-thi-dua để chỉ tổng hợp dữ liệu đã được xác nhận, bỏ ví dụ tự sinh số liệu/nhận xét, không đánh giá hoặc quyết định quyền lợi cá nhân. Các skill khác giữ bản 1.1.0.


## 1.1.0 — 2026-10-09

- Bổ sung `agents/openai.yaml` cho 171 skill: display_name, short_description, default_prompt có tên gọi `$skill`.
- Chuẩn hóa YAML frontmatter; giữ nguyên 171 tên thư mục/tên gọi skill.
- Bổ sung kiểm soát áp dụng, giới hạn, phê duyệt và hồ sơ `references/version.json` cho 171 skill.
- Cập nhật có phạm vi 58 skill theo văn bản đào tạo, kiểm định, công khai, học phí, tuyển sinh, nhân sự, ngân sách, kế toán, đấu thầu và tài sản. Tách chỉ dẫn cũ thành tư liệu lịch sử để tránh dùng nhầm.
- Sửa TUQ./TL. và trạng thái bản trình ký; thống nhất input `thanh_phan`; loại số liệu ví dụ không có nguồn; giới hạn quyết định tốt nghiệp ở bước dự thảo từ kết quả đã duyệt.
- Thêm bảng căn cứ, manifest và trình kiểm tra đóng gói.

Nguồn trước cập nhật: commit `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Đây là phiên bản nội dung, chưa tạo tag hoặc GitHub Release.
