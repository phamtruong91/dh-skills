---
name: "ke-hoach-kiem-toan-noi-bo"
description: "Lập kế hoạch kiểm toán nội bộ năm của trường đại học (theo mô hình Ban Thanh tra, Pháp chế và Kiểm toán nội bộ): xác định đối tượng, phạm vi, phương pháp và lịch kiểm toán. Dùng khi xây dựng kế hoạch kiểm toán năm trình Hiệu trưởng/Hội đồng trường phê duyệt. Không dùng cho kế hoạch thanh tra (dùng ke-hoach-thanh-tra-nam)."
---

# Lập kế hoạch kiểm toán nội bộ

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Đầu mỗi năm (hoặc đầu nhiệm kỳ), khi Ban Thanh tra, Pháp chế và Kiểm toán nội bộ cần xây dựng
kế hoạch kiểm toán nội bộ năm để trình Hiệu trưởng (hoặc Hội đồng trường) phê duyệt và tổ chức thực hiện.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `nam_ke_hoach` | Năm thực hiện kiểm toán | Có |
| `doi_tuong_kiem_toan` | Danh sách đơn vị/hoạt động dự kiến kiểm toán (VD: thu học phí, mua sắm, đề tài NCKH) | Có |
| `tieu_chi_uu_tien` | Tiêu chí lựa chọn: rủi ro cao, kiến nghị tồn đọng, luân phiên bao phủ | Không |
| `nguon_luc` | Nhân sự kiểm toán, thời gian, kinh phí dự kiến | Có |
| `don_vi_chu_tri` | Ban Thanh tra, Pháp chế và Kiểm toán nội bộ | Có |

## Quy trình

**Bước 1. Rà soát rủi ro và kiến nghị tồn đọng**
- Làm gì: tổng hợp kiến nghị kiểm toán/kiểm tra các năm trước còn tồn đọng (chưa khắc phục); xác định các lĩnh vực rủi ro cao (tài chính, mua sắm, tuyển sinh, quản lý văn bằng, đề tài NCKH); lập bảng rủi ro sơ bộ theo lĩnh vực.
- Dùng input: `doi_tuong_kiem_toan` (danh mục sơ bộ để rà soát), `tieu_chi_uu_tien`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: tổng hợp, chuẩn hóa dữ liệu, đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: ưu tiên đối tượng có kiến nghị tồn đọng nhiều kỳ; lĩnh vực chưa được kiểm toán trong 3–5 năm phải được xem xét theo nguyên tắc luân phiên bao phủ.
- → Kết quả bước: Bảng rủi ro – kiến nghị tồn đọng theo lĩnh vực.

**Bước 2. Lựa chọn đối tượng kiểm toán**
- Làm gì: áp tiêu chí ưu tiên (mức độ rủi ro, tính trọng yếu, luân phiên bao phủ 3–5 năm) vào bảng rủi ro Bước 1 để chốt danh sách các cuộc kiểm toán trong năm; mỗi cuộc ghi rõ lý do lựa chọn.
- Dùng input: `tieu_chi_uu_tien`, `doi_tuong_kiem_toan`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: tính toán, phân tích số liệu · ⏱ ~30–90 phút (ước tính)
- Lưu ý nghiệp vụ: số cuộc phải phù hợp với nguồn lực; ghi rõ căn cứ lựa chọn để giải trình khi trình duyệt.
- → Kết quả bước: Danh mục cuộc kiểm toán đã chốt (đối tượng – lý do lựa chọn).

**Bước 3. Xác định phạm vi và phương pháp từng cuộc**
- Làm gì: với từng cuộc kiểm toán: xác định thời kỳ kiểm toán, nội dung kiểm tra trọng tâm; chọn phương pháp: kiểm tra chứng từ, đối chiếu sổ sách, phỏng vấn, kiểm tra thực tế chọn mẫu theo mức độ rủi ro.
- Dùng input: `doi_tuong_kiem_toan`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~0,5–1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: phạm vi phải đủ rộng để bao phủ rủi ro đã xác định nhưng vừa sức nguồn lực; chọn mẫu phải có cơ sở (rủi ro cao → cỡ mẫu lớn).
- → Kết quả bước: Bảng phạm vi – phương pháp của từng cuộc.

**Bước 4. Lập lịch và phân công đoàn kiểm toán**
- Làm gì: gán thời gian thực hiện (quý/tháng) cho từng cuộc; chỉ định trưởng đoàn và thành viên đoàn; xác định thời hạn hoàn thành báo cáo của từng cuộc.
- Dùng input: `nguon_luc`, `don_vi_chu_tri`.
- Vai trò: Trưởng phòng Thanh tra – Pháp chế (phân công đoàn kiểm toán) · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: không để kiểm toán viên kiểm toán đơn vị mình đang công tác; giãn lịch tránh dồn nhiều cuộc vào cùng thời điểm.
- → Kết quả bước: Lịch triển khai + phân công đoàn kiểm toán.

**Bước 5. Kiểm tra khả thi và đối chiếu kế hoạch thanh tra**
- Làm gì: kiểm tra 3 điểm: nguồn lực có đủ cho toàn bộ các cuộc không; có trùng lặp đối tượng/thời gian với kế hoạch thanh tra nội bộ năm không; độ bao phủ rủi ro đã đủ chưa; nếu chưa đạt thì quay lại điều chỉnh Bước 2–4.
- Dùng input: `nguon_luc`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: trùng lặp với thanh tra gây lãng phí nguồn lực và phiền hà cho đơn vị → phải loại trừ trước khi trình duyệt.
- → Kết quả bước: Phiếu kiểm tra khả thi (đạt / chưa đạt + nội dung điều chỉnh).

**Bước 6. Dự thảo kế hoạch theo cấu trúc chuẩn**
- Làm gì: soạn văn bản kế hoạch: I. Căn cứ; II. Mục tiêu; III. Đối tượng, phạm vi và thời gian (bảng); IV. Phương pháp; V. Tổ chức thực hiện; kèm phụ lục danh mục các cuộc kiểm toán.
- Dùng input: `nam_ke_hoach`, `don_vi_chu_tri`, `nguon_luc`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: soạn dự thảo · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: số liệu giữa văn bản và phụ lục phải khớp nhau; thẩm quyền phê duyệt: Hiệu trưởng hoặc Hội đồng trường.
- → Kết quả bước: Dự thảo Kế hoạch kiểm toán nội bộ năm.

**Bước 7. Trình phê duyệt và công bố**
- Làm gì: trình Hiệu trưởng (hoặc Hội đồng trường) phê duyệt; công bố kế hoạch cho các đơn vị được kiểm toán biết để phối hợp; lưu hồ sơ.
- Dùng input: (kết quả Bước 6).
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế (chuẩn bị hồ sơ trình); Hiệu trưởng (người ký) ban hành · AI hỗ trợ: chuẩn bị hồ sơ trình đầy đủ, lưu trữ hồ sơ · ⏱ ~1–3 giờ (ước tính)
- Lưu ý nghiệp vụ: Trưởng Ban soát xét toàn bộ kế hoạch trước khi trình; điều chỉnh giữa năm phải trình phê duyệt lại.
- → Kết quả bước: Kế hoạch kiểm toán nội bộ năm đã phê duyệt.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Kiến nghị tồn đọng + lĩnh vực rủi ro cao"/] --> B1["Bước 1: Rà soát rủi ro và kiến nghị tồn đọng"]
    B1 --> B2["Bước 2: Lựa chọn đối tượng kiểm toán"]
    B2 --> B3["Bước 3: Xác định phạm vi và phương pháp từng cuộc"]
    B3 --> B4["Bước 4: Lập lịch và phân công đoàn kiểm toán"]
    B4 --> B5["Bước 5: Kiểm tra khả thi và đối chiếu kế hoạch thanh tra"]
    B5 --> B6["Bước 6: Dự thảo kế hoạch theo cấu trúc chuẩn"]
    B6 --> B7["Bước 7: Trình phê duyệt và công bố"]
    B7 --> HG["👤 Hiệu trưởng hoặc HĐ trường phê duyệt"]
    HG --> OUT[["Kế hoạch kiểm toán nội bộ năm"]]
```
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Có đầy đủ sản phẩm: Kế hoạch kiểm toán nội bộ năm hoàn chỉnh, sẵn sàng trình ký
- [ ] Có đầy đủ sản phẩm: Phụ lục: danh mục các cuộc kiểm toán (đối tượng, thời kỳ, thời gian, trưởng đoàn)
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Ưu tiên đối tượng có kiến nghị tồn đọng nhiều kỳ
- [ ] Số cuộc phải phù hợp với nguồn lực

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Human gate (người kiểm duyệt)
- Trưởng Ban Thanh tra, Pháp chế và Kiểm toán nội bộ soát xét toàn bộ kế hoạch trước khi trình.
- Hiệu trưởng (hoặc Hội đồng trường) là người duy nhất phê duyệt kế hoạch.

## Giới hạn (guardrails)
- AI không tự quyết định đối tượng/phạm vi kiểm toán thay lãnh đạo.
- AI không đưa ra kết luận về sai phạm khi chưa có bằng chứng kiểm toán.
- AI không thay thế kiểm toán viên trong việc thu thập và đánh giá bằng chứng.

## Căn cứ & lưu ý
- Quy chế kiểm toán nội bộ của trường (văn bản nội bộ).
- Nghị định 05/2019/NĐ-CP về kiểm toán nội bộ (áp dụng tham khảo nguyên tắc cho đơn vị sự nghiệp).
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
