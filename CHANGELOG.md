# Nhật ký thay đổi

## 1.3.2 (bổ sung) — 2026-10-10

Rà soát toàn bộ 171 skill về quy trình, đầu vào, đầu ra và thể thức.

- **Khôi phục quy trình đầy đủ cho 58 skill** từng chỉ còn 4 bước chung chung sau đợt cập nhật pháp lý: giữ nghiệp vụ gốc (bước, vai trò, lưu ý, kết quả bước, sơ đồ), thay viện dẫn văn bản đã bị thay thế bằng con trỏ tới `phap-ly.md`, thêm khối "Ràng buộc pháp lý khi thực hiện". Các con số/thời hạn gốc chưa được xác minh, chỉ gắn cờ.
- **Đầu vào/đầu ra:** mọi đầu vào đều được một bước dùng; tách các trường gộp (`nam_hoc`/`nam_tai_chinh`, người lập/kế toán trưởng/người ký); thêm câu "Dùng khi" cho 39 mô tả; sơ đồ khớp số bước ở cả 171 skill.
- **Thể thức NĐ 30/2020:** `scripts/check_outputs.py` kiểm tra khổ A4, lề, phông Times New Roman, cỡ chữ cho file có `nd30_format`; thêm mẫu thử `soan-quyet-dinh-hc` (4/4 mẫu đạt).
- **Validator:** thêm kiểm tra không cắt cụt mục thể thức, sơ đồ khớp bước, kết quả bước không là báo cáo kiểm tra, ≥3 bước, có ràng buộc pháp lý. `audit_structure.py`: 0/171 vấn đề.
- **Sửa căn cứ cũ còn sót:** `de-an-mo-nganh`, `quyet-dinh-nang-luong`; viết lại bước của `bao-cao-3-cong-khai` theo hướng TT 09/2024 (không mặc định 3 biểu).
- **Tài liệu:** `docs/DIEM_CAN_DOI_CHIEU_PHAP_LY.md` (danh sách dòng cần chuyên gia pháp lý đối chiếu), cập nhật `legal-register.json`.
- **Chưa làm:** chưa đối chiếu toàn văn/Công báo; sơ đồ dựng lại của 44 skill mất nhánh quyết định; thời lượng ⏱ là ước tính; một số quy-cach-dau-ra.md vẫn mang cấu trúc cũ; chưa chạy thử thêm skill ngoài 4 mẫu.

## 1.3.2 — 2026-10-10

Rà soát chất lượng sau khi đọc repo và chạy thử 3 skill bằng dữ liệu giả.

- **Pháp lý thanh tra:** `ke-hoach-thanh-tra-nam` và `ket-luan-thanh-tra` đổi căn cứ từ Luật Thanh tra 2022 và NĐ 43/2023 sang Luật Thanh tra 84/2025/QH15 (hiệu lực 01/07/2025) và NĐ 216/2025/NĐ-CP. Dựa trên nguồn thứ cấp; còn phải đối chiếu Công báo (phạm vi thay thế, ngày hiệu lực, chuyển tiếp). Cập nhật `docs/legal-register.json` và `docs/CAP_NHAT_PHAP_LY.md`, sửa lỗi dính chữ và nhãn `nhan-su-0..4`.
- **Sửa mâu thuẫn trong 171 skill:** bỏ kết quả bước "checklist đã đánh dấu" ở 3 skill (`soan-cong-van`, `soan-quyet-dinh-hc`, `thong-bao-hoc-bong`); bỏ nhắc "markdown" ở 16 skill có định dạng mặc định là Word/Excel.
- **Gọn SKILL.md:** nén 3 mục lặp lại và mục "Quản trị phiên bản"; bản đầy đủ chuyển sang `references/quy-tac-chung.md` của từng skill (giữ phần đặc thù của `bao-cao-thi-dua`, `chuan-bi-hop-hoi-dong-truong`, `quyet-dinh-tot-nghiep`). Tổng dung lượng SKILL.md giảm khoảng 8%.
- **Chống chọn nhầm skill:** thêm câu "Không dùng cho… (dùng skill X)" vào mô tả của 7 cặp skill dễ nhầm.
- **Sửa spec từ kết quả chạy thử:** `ke-hoach-thanh-tra-nam` thêm ngoại lệ cho cuộc thanh tra thi/tuyển sinh và bỏ việc tự đổi thời gian; `pmo-quan-tri-du-an` thêm input `nguong_trang_thai` và bước đối chiếu tổng ngân sách.
- **Rà soát cấu trúc nhóm 1 (20 skill dùng nhiều nhất):** sửa mục kiểm tra thể thức bị ghép sai hoặc cắt cụt (12 skill), thêm nhãn Bước vào sơ đồ, đảo thứ tự kiểm tra khả thi trước trình ký ở `soan-ke-hoach-ct`, đúng người ký/duyệt, bỏ ngày giờ và tên trường giả định, không tự cấp số văn bản, bổ sung câu "Dùng khi" ở mô tả. Chi tiết từng skill: `docs/RA_SOAT_CAU_TRUC_NHOM_1.md`. Validator thêm 3 kiểm tra khóa lỗi mẫu; thêm `scripts/audit_structure.py`.
- **Validator viết lại:** báo rõ kiểm tra nào hỏng ở skill nào; cho phép gán `approval_owner` (trước đây bắt buộc `null`); bỏ số 171 cố định; thêm kiểm tra mâu thuẫn, dung lượng, tên skill dễ nhầm, căn cứ thanh tra, lỗi dính chữ trong tài liệu pháp lý.
- **Thử nghiệm:** thêm `tests/` (dữ liệu giả, file đầu ra, kết quả phát hiện) và `scripts/check_outputs.py` kiểm tra file Word/Excel thật. Đây là thử nghiệm 3 trên 171 skill.
- **Chưa làm:** chưa có người phê duyệt nghiệp vụ hay pháp chế duyệt; chưa đối chiếu Công báo; chưa chạy thử 168 skill còn lại.

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
