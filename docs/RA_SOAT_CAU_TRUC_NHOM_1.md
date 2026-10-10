# Rà soát cấu trúc và nhất quán: nhóm 1 (20 skill dùng nhiều nhất)

Phạm vi: cấu trúc, nhất quán nội bộ (đầu vào – bước – đầu ra – sơ đồ – mô tả). **Không** rà soát nội dung pháp lý từng điều khoản; căn cứ pháp lý chỉ được thêm yêu cầu "đối chiếu hiệu lực".
Công cụ: `scripts/audit_structure.py` (quét), `scripts/maintenance/restandardize_group1.py` (áp dụng thay đổi, có nhật ký), `scripts/validate_skills.py` (khóa lỗi mẫu).

Kết quả quét cấu trúc nhóm 1: trước khi sửa, một số skill lệch sơ đồ/bước hoặc mô tả thiếu câu "khi nào dùng"; sau khi sửa: 0/20 skill còn vấn đề, validator 171/171 đạt.

## Thay đổi theo từng skill

### soan-cong-van
- Vai trò duyệt/ký: không mặc định Hiệu trưởng

### soan-bien-ban-hop
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Kết quả bước kiểm tra ghi là nội bộ, không xuất kèm file
- Biên bản do chủ trì và thư ký ký, không phải Hiệu trưởng
- Bỏ ngày giờ ví dụ cụ thể, dùng chỗ điền

### soan-thong-bao
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Kết quả bước kiểm tra ghi là nội bộ, không xuất kèm file
- Vai trò ký theo đơn vị ban hành
- Bỏ ngày ví dụ cụ thể
- Bổ sung câu 'Dùng khi' và ranh giới sang skill lân cận

### soan-to-trinh
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Kết quả bước kiểm tra ghi là nội bộ, không xuất kèm file
- Tờ trình do thủ trưởng đơn vị trình ký (khớp Lưu ý của Bước 5)
- Sơ đồ thiếu Bước 7
- Không tự cấp số văn bản (khớp quy tắc chừa chỗ điền)

### soan-quyet-dinh-hc
- Vai trò duyệt/ký theo nguoi_ky
- Không tự cấp số văn bản (khớp quy tắc chừa chỗ điền)
- Bỏ tên trường giả định
- Khớp ranh giới với quyet-dinh-khen-thuong-kl trong mô tả
- Khớp ranh giới với quyet-dinh-khen-thuong-kl trong bảng đầu vào

### soan-giay-moi
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Giấy mời do thủ trưởng đơn vị tổ chức ký (khớp sơ đồ)
- Sơ đồ thêm nhãn Bước (x6)

### soan-ke-hoach-ct
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Vai trò ký theo thủ trưởng đơn vị (khớp Lưu ý)
- Đảo Bước 6/7: kiểm tra khả thi trước khi dựng thể thức và trình ký; sửa sơ đồ

### soan-mou-moa
- Sơ đồ thêm nhãn Bước (x6)
- Bỏ tên trường giả định (x2)
- Thêm yêu cầu đối chiếu hiệu lực căn cứ
- Thêm quy tắc căn cứ ký kết chỉ lấy từ input
- Thêm câu dẫn chuẩn cho mục kiểm tra nội bộ

### phieu-trinh-ky
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Bước chuẩn bị do đơn vị trình thực hiện; lãnh đạo chỉ ghi ý kiến ở Bước 6
- Sơ đồ thêm nhãn Bước (x6)

### so-van-ban-di-den
- Sơ đồ thêm nhãn Bước (x9)

### tham-dinh-phap-ly-van-ban
- Kết quả bước không khẳng định 'đã ký'
- Không tự giả định nội dung văn bản nội bộ
- Mô tả nêu rõ khi nào dùng, rút gọn dưới 400 ký tự

### quan-ly-phien-ban-tai-lieu
- Sơ đồ thêm nhãn Bước (x6)
- Mô tả nêu rõ khi nào dùng

### chuan-bi-hop-va-action-tracker
- Khớp quy tắc chừa chỗ điền, bỏ nhãn 'cần xác minh' trong file
- Mô tả nêu rõ khi nào dùng

### lap-lich-cong-tac-tuan
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Thống nhất người duyệt giữa Bước 6 và sơ đồ (x2)
- Mô tả nêu rõ khi nào dùng

### executive-brief-trinh-lanh-dao
- Mô tả nêu rõ khi nào dùng

### hop-nhat-bao-cao-don-vi
- Khớp quy tắc chừa chỗ điền
- Mô tả nêu rõ khi nào dùng

### bao-cao-tong-ket-vp
- Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- Sơ đồ thêm nhãn Bước (x6)

### bao-cao-tong-ket-nam-truong
- Khớp quy tắc chừa chỗ điền
- Kết quả bước không khẳng định 'đã duyệt'

### bao-cao-du-an-dinh-ky
- Phân biệt người soạn và người duyệt

### kiem-tra-day-du-ho-so
- Mô tả nêu rõ khi nào dùng

## Sửa ngoài nhóm 1 (cùng lỗi mẫu)

- kich-ban-khanh-tiet: Sửa mục kiểm tra thể thức bị ghép sai/cắt cụt
- quy-che-to-chuc-hoat-dong: Sửa mục kiểm tra thể thức bị cắt cụt
- checklist-ho-so-gs-pgs: Sửa mục kiểm tra thể thức bị cắt cụt
- de-an-vi-tri-viec-lam: Sửa mục kiểm tra thể thức bị cắt cụt

## Chưa xử lý, cần người có chuyên môn quyết định

- **58 skill còn bản rút gọn** (4 bước "Quy trình hiện hành" chung chung, quy trình thật nằm ở `references/quy-trinh-lich-su.md`). Khôi phục cần rà pháp lý từng nghiệp vụ nên chưa làm trong đợt này.
- **Căn cứ có dấu hiệu lỗi thời, chưa xác minh**: `checklist-ho-so-gs-pgs` viện dẫn Quyết định 37/2018/QĐ-TTg; `de-an-vi-tri-viec-lam` và `quy-che-to-chuc-hoat-dong` viện dẫn Nghị định 62/2017/NĐ-CP về vị trí việc làm; `soan-mou-moa` viện dẫn Luật Giáo dục đại học 2012 (sửa đổi 2018). Đã thêm yêu cầu đối chiếu hiệu lực tại ngày nghiệp vụ vào `soan-mou-moa`, `checklist-ho-so-gs-pgs`, `de-an-vi-tri-viec-lam`; chưa tra Công báo nên không đổi nội dung viện dẫn.
- **151 skill còn lại chưa rà** theo cách này (chỉ chạy quét tự động bằng `audit_structure.py`).
- Các mốc thời gian ước tính (⏱) trong bước quy trình là ước tính chung của mẫu, chưa hiệu chỉnh theo thực tế đơn vị.
