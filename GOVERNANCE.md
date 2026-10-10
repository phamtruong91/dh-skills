# Quản trị phiên bản và kiểm duyệt

Kho nguồn: https://github.com/phamtruong91/university-skills-framework. Người duy trì ghi theo GitHub: `phamtruong91`, Phạm Văn Trường. Giấy phép và bản quyền theo LICENSE (CES Global); tài khoản duy trì không đồng nghĩa chủ sở hữu toàn bộ nội dung.

Phiên bản gói hiện tại: **1.3.2**, ngày cập nhật **2026-10-10**. Baseline trước cập nhật: `d2a835f00b0dbbafa13a66d56551a4f3102311ac`. Xác định commit thực tế bằng `git log -1` và `git log -1 -- skills/<ten-skill>`; không dùng baseline như commit của bản mới. Chưa có người phê duyệt nghiệp vụ trong kho. Khi chỉ định, ghi tên vào `approval_owner` của `references/version.json` và manifest; validator chấp nhận giá trị này. Trường triển khai phải giao người chịu trách nhiệm.

## Quy tắc thay đổi

1. Bản sửa lỗi tăng PATCH; bổ sung nghiệp vụ tương thích tăng MINOR; đổi đầu vào bắt buộc hoặc phá tương thích tăng MAJOR. Ghi rõ tác động và chuyển tiếp trong CHANGELOG.
2. Cập nhật SKILL.md, metadata giao diện, hồ sơ phiên bản và manifest cùng một commit; không đổi tên gọi nếu chưa có kế hoạch chuyển đổi.
3. Thay đổi pháp lý phải lưu nguồn chính thức, ngày hiệu lực, đối tượng, điều kiện chuyển tiếp, phạm vi xác minh và người kiểm duyệt. Không lấy ngày tra cứu làm bằng chứng toàn bộ văn bản còn hiệu lực.
4. Chạy `python scripts/validate_skills.py` trước hợp nhất. Kiểm tra tình huống nghiệp vụ bằng dữ liệu giả; người phụ trách pháp chế/nghiệp vụ duyệt căn cứ và mẫu trước dùng thật.
5. GitHub commit/PR lưu lịch sử thay đổi. Chỉ tạo tag/Release khi người duy trì quyết định phát hành; phiên bản nội dung không tự chứng minh đã có Release.

## Hồ sơ mỗi skill

`agents/openai.yaml` chứa metadata giao diện. `references/version.json` chứa phiên bản, ngày, kho nguồn, baseline, người duy trì, trạng thái rà soát và người phê duyệt. `references/phap-ly.md` có ở skill thuộc đợt cập nhật pháp lý. `references/quy-trinh-lich-su.md` chỉ giữ nội dung cũ để đối chiếu; không dùng cho hồ sơ hiện hành khi thiếu kiểm tra chuyển tiếp.

## File đầu ra bắt buộc

Khi tạo sản phẩm nghiệp vụ, phải tạo file thực tế và cung cấp liên kết tải ngay; không chờ yêu cầu xuất file bổ sung. Văn bản mặc định Word, bảng theo dõi mặc định Excel, gói skill mặc định ZIP; định dạng người dùng chỉ định được ưu tiên. Mỗi skill ghi định dạng tại đầu SKILL.md và manifest. Nội dung chat chỉ hỗ trợ trao đổi, không thay file giao.

## Lựa chọn định dạng bổ sung

Không giới hạn đầu ra vào định dạng mặc định. Chọn định dạng theo sản phẩm người dùng yêu cầu và công cụ thực tế: DOCX để sửa văn bản; PDF để đọc/in/công bố; XLSX để giữ sheet/công thức; CSV để trao đổi dữ liệu bảng; TXT/MD để giao nội dung thuần; HTML để giao nội dung web; JSON/YAML để giao dữ liệu hoặc cấu hình; PPTX để giao bài trình chiếu; PNG/SVG để giao biểu đồ; TEX/BIB để giao nguồn bài viết khoa học/danh mục trích dẫn; ZIP để gom bộ hồ sơ hoặc gói skill. Chỉ tạo định dạng bổ sung khi sản phẩm cần hoặc người dùng yêu cầu; danh sách định dạng là cách lựa chọn đầu ra, không cam kết mọi công cụ chuyển đổi đều có sẵn.

Markdown phải là file .md thật khi được yêu cầu, không phải đoạn Markdown trong chat. CSV/JSON không thay XLSX khi cần công thức/định dạng. PPTX phải có slide thực; PNG/SVG phải là biểu đồ hoặc hình thật. HTML không đồng nghĩa website đã được đăng. Skill kịch bản video chỉ giao kịch bản; MP4/âm thanh chỉ có thể giao khi người dùng yêu cầu sản xuất và có công cụ thực sự tạo được. Không đổi đuôi file hoặc gọi file mô tả là media đã hoàn thành.

## Kiểm tra trước khi hợp nhất

Chạy `python -X utf8 scripts/validate_skills.py` (cấu trúc, mâu thuẫn nội bộ) và `python -X utf8 scripts/check_outputs.py` (file đầu ra mẫu). Thay đổi pháp lý ghi nguồn đã dùng; nguồn thứ cấp phải được đánh dấu là chưa đối chiếu Công báo.
