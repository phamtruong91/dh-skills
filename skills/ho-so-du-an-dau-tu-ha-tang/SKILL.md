---
name: "ho-so-du-an-dau-tu-ha-tang"
description: "Soạn hồ sơ đề xuất dự án đầu tư hạ tầng của trường: mục tiêu, quy mô, tổng mức đầu tư, nguồn vốn, hiệu quả, tiến độ. Dùng khi chuẩn bị trình phê duyệt chủ trương đầu tư."
---

# Hồ sơ dự án đầu tư hạ tầng

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Khi trường chuẩn bị một dự án đầu tư xây dựng/mua sắm hạ tầng (giảng đường, ký túc xá,
phòng lab, hạ tầng số...): cần bộ hồ sơ đề xuất đầy đủ để trình phê duyệt chủ trương đầu tư.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_du_an` | Tên dự án | Có |
| `muc_tieu` | Mục tiêu đầu tư, sự cần thiết | Có |
| `quy_mo` | Quy mô: diện tích, công suất, hạng mục chính | Có |
| `tong_muc_dau_tu` | Tổng mức đầu tư dự kiến và cơ cấu nguồn vốn | Có |
| `hinh_thuc_dau_tu` | Ngân sách / PPP / tài trợ / vốn tự có / kết hợp | Có |
| `tien_do` | Các giai đoạn và mốc thời gian dự kiến | Có |
| `hieu_qua` | Hiệu quả kinh tế – xã hội dự kiến | Không |

## Quy trình

**Bước 1. Phân tích sự cần thiết đầu tư**
- Làm gì: thu thập số liệu hiện trạng liên quan (quy mô sinh viên, công suất hiện hữu, mức độ thiếu hụt); mô tả bất cập cụ thể bằng số liệu; đối chiếu với quy hoạch/chiến lược phát triển trường để chứng minh tính cấp thiết.
- Dùng input: `muc_tieu`, `quy_mo`.
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: tổng hợp, chuẩn hóa dữ liệu, đối chiếu tự động, cảnh báo sai lệch · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: "sự cần thiết" phải trả lời được câu hỏi "không đầu tư thì sao" bằng số liệu, không viết định tính chung chung.
- → Kết quả bước: Bản phân tích sự cần thiết (hiện trạng – bất cập – nhu cầu, có số liệu).

**Bước 2. Xác định mục tiêu và quy mô đầu tư**
- Làm gì: từ `muc_tieu` và `quy_mo`, viết mục tiêu cụ thể (đáp ứng bao nhiêu % nhu cầu, đưa vào sử dụng khi nào); chi tiết hóa quy mô: hạng mục chính, diện tích/công suất, tiêu chuẩn kỹ thuật cơ bản.
- Dùng input: `muc_tieu`, `quy_mo` + bản phân tích sự cần thiết (Bước 1).
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: soạn dự thảo · ⏱ ~30–90 phút (ước tính)
- Lưu ý nghiệp vụ: quy mô phải tương xứng với nhu cầu đã chứng minh ở Bước 1 — tránh "làm quá to" hoặc "làm thiếu".
- → Kết quả bước: Mục tiêu và quy mô đầu tư đã chốt.

**Bước 3. Lập tổng mức đầu tư**
- Làm gì: từ `tong_muc_dau_tu`, bóc tách chi phí: xây dựng, thiết bị, tư vấn, quản lý dự án, dự phòng (tối thiểu 5–10%); ghi rõ cơ sở tính từng khoản (suất đầu tư, báo giá tham khảo, định mức); đối chiếu tổng các khoản với tổng mức.
- Dùng input: `tong_muc_dau_tu` + quy mô đầu tư (Bước 2).
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch, tính toán, phân tích số liệu · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: khoản dự phòng thường bị "quên" — thiếu dự phòng là nguyên nhân phổ biến phải điều chỉnh tổng mức sau này.
- → Kết quả bước: Bảng tổng mức đầu tư chi tiết (kèm cơ sở tính từng khoản).

**Bước 4. Xây dựng phương án nguồn vốn**
- Làm gì: từ `hinh_thuc_dau_tu`, phân bổ nguồn vốn: nhà đầu tư/đối tác bao nhiêu %, trường đối ứng bao nhiêu (tiền + hiện vật như quỹ đất); nêu nghĩa vụ đối ứng cụ thể của trường và khả năng cân đối; đánh giá rủi ro nguồn vốn.
- Dùng input: `hinh_thuc_dau_tu` + bảng tổng mức (Bước 3).
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: lập bảng biểu, định dạng · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: phần đối ứng của trường phải có ý kiến của Phòng TCKT về khả năng cân đối; với PPP phải tuân thủ quy định về quản lý tài sản công.
- → Kết quả bước: Phương án nguồn vốn (cơ cấu – nghĩa vụ đối ứng – đánh giá rủi ro).

**Bước 5. Đánh giá hiệu quả đầu tư**
- Làm gì: từ `hieu_qua`, phân tích hiệu quả phục vụ đào tạo/NCKH (số người thụ hưởng/năm), hiệu quả kinh tế (doanh thu dự kiến, thời gian hoàn vốn với giả định rõ ràng), tác động xã hội; ghi rõ mọi con số là "dự kiến".
- Dùng input: `hieu_qua` + quy mô (Bước 2) + tổng mức (Bước 3).
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: tính toán, phân tích số liệu · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: giả định tính hoàn vốn (tỷ lệ lấp đầy, giá thuê, lạm phát) phải ghi minh bạch — người thẩm định sẽ kiểm tra đầu tiên.
- → Kết quả bước: Bản đánh giá hiệu quả (kèm giả định tính toán minh bạch).

**Bước 6. Lập tiến độ thực hiện**
- Làm gì: từ `tien_do`, chi tiết hóa các giai đoạn: chuẩn bị đầu tư (phê duyệt, thiết kế) → thi công → nghiệm thu → bàn giao đưa vào sử dụng; mỗi giai đoạn ghi mốc thời gian và sản phẩm hoàn thành.
- Dùng input: `tien_do`.
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: lập bảng biểu, định dạng · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: tiến độ phải tính cả thời gian thủ tục phê duyệt (thường 3–6 tháng); mốc đưa vào sử dụng nên khớp năm học.
- → Kết quả bước: Bảng tiến độ thực hiện theo giai đoạn.

**Bước 7. Viết kiến nghị phê duyệt chủ trương**
- Làm gì: tổng hợp 6 nội dung trên thành phần kiến nghị: trình bày tóm tắt dự án (tên, quy mô, tổng mức, hình thức, tiến độ) và đề nghị cấp có thẩm quyền (HĐ trường/BGH) xem xét phê duyệt chủ trương đầu tư.
- Dùng input: toàn bộ bán thành phẩm Bước 1–6 + `ten_du_an`.
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: soạn dự thảo, tổng hợp, chuẩn hóa dữ liệu · ⏱ ~1–3 giờ (ước tính)
- Lưu ý nghiệp vụ: kiến nghị nêu đúng cấp phê duyệt theo phân cấp đầu tư; không kiến nghị vượt thẩm quyền.
- → Kết quả bước: Dự thảo kiến nghị phê duyệt chủ trương.

**Bước 8. Hoàn thiện bộ hồ sơ**
- Làm gì: đóng gói: tờ trình + thuyết minh dự án (đủ 7 nội dung: sự cần thiết, mục tiêu, quy mô, tổng mức, nguồn vốn, hiệu quả, tiến độ) + phụ lục (bảng tổng mức, tiến độ, phương án vốn); rà soát nhất quán số liệu giữa các tài liệu; gửi Trưởng ban XTĐT và Phòng TCKT thẩm định trước khi trình.
- Dùng input: toàn bộ bán thành phẩm Bước 1–7.
- Vai trò: Chuyên viên Ban Xúc tiến đầu tư · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch, chuẩn bị hồ sơ trình đầy đủ · ⏱ ~1–3 giờ (ước tính)
- Lưu ý nghiệp vụ: số liệu trong tờ trình, thuyết minh và phụ lục phải khớp tuyệt đối — lệch 1 con số cũng bị trả hồ sơ.
- → Kết quả bước: Bộ hồ sơ dự án đầu tư hoàn chỉnh (sẵn sàng trình phê duyệt).

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Nhu cầu đầu tư + hiện trạng"/] --> B["Bước 1. Phân tích sự cần thiết đầu tư"]
    B --> C["Bước 2. Xác định mục tiêu và quy mô đầu tư"]
    C --> D["Bước 3. Lập tổng mức đầu tư"]
    D --> E["Bước 4. Xây dựng phương án nguồn vốn"]
    E --> F["Bước 5. Đánh giá hiệu quả đầu tư"]
    F --> G["Bước 6. Lập tiến độ thực hiện"]
    G --> H["Bước 7. Viết kiến nghị phê duyệt chủ trương"]
    H --> I["Bước 8. Hoàn thiện bộ hồ sơ"]
    I --> HG["👤 Trưởng ban XTĐT + P.TCKT thẩm định"]
    HG --> J["👤 HĐ trường / BGH phê duyệt chủ trương"]
    J --> K[["Tờ trình + Thuyết minh dự án đầu tư"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Có đầy đủ sản phẩm: Tờ trình + Thuyết minh đề xuất dự án đầu tư (đầy đủ 7 nội dung trên)
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] "sự cần thiết" phải trả lời được câu hỏi "không đầu tư thì sao" bằng số liệu, không viết định tính chung chung.
- [ ] Quy mô phải tương xứng với nhu cầu đã chứng minh ở Bước 1 — tránh "làm quá to" hoặc "làm thiếu".
- [ ] Khoản dự phòng thường bị "quên" — thiếu dự phòng là nguyên nhân phổ biến phải điều chỉnh tổng mức sau này.

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Human gate
- Trưởng Ban XTĐT thẩm định hồ sơ; Hội đồng trường/Ban Giám hiệu phê duyệt chủ trương đầu tư.
- Phòng TCKT thẩm định tổng mức đầu tư và phương án nguồn vốn.

## Giới hạn
- Không tự ý điều chỉnh tổng mức đầu tư, quy mô, hình thức đầu tư sau khi đã trình.
- Số liệu hiệu quả/hoàn vốn phải ghi rõ là "dự kiến", kèm giả định tính toán.
- Không cam kết với nhà đầu tư trước khi có phê duyệt chủ trương.

## Căn cứ & lưu ý
- Luật Đầu tư công, Luật PPP, Luật Xây dựng, quy định quản lý tài sản công và phân cấp đầu tư.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
