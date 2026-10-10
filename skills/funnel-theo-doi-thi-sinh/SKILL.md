---
name: "funnel-theo-doi-thi-sinh"
description: "Theo dõi thí sinh theo phễu tuyển sinh: nhóm lead theo giai đoạn (biết đến → quan tâm → nộp hồ sơ → trúng tuyển → nhập học), checklist hồ sơ, báo cáo tỉ lệ chuyển đổi. Dùng trong suốt chiến dịch tuyển sinh. Dùng khi trong chiến dịch tuyển sinh cần quản lý thí sinh tiềm năng theo từng giai đoạn phễu."
---

# Funnel theo dõi thí sinh

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .xlsx, .csv, .pdf, .json, .html. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.xlsx**. Nếu yêu cầu gồm cả báo cáo thuyết minh, tạo thêm file Word cho báo cáo; không ghép báo cáo dài vào bảng tính. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Trong chiến dịch tuyển sinh, khi cần quản lý danh sách thí sinh tiềm năng theo từng giai đoạn
phễu, đôn đốc hồ sơ và báo cáo tỉ lệ chuyển đổi cho lãnh đạo.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `chien_dich` | Tên chiến dịch/đợt tuyển sinh | Có |
| `du_lieu_lead` | Danh sách lead: họ tên, kênh tiếp cận, giai đoạn hiện tại, ghi chú (đã ẩn danh/bảo mật) | Có |
| `moc_thoi_gian` | Các mốc: mở đăng ký, hạn nộp hồ sơ, công bố kết quả, nhập học | Có |
| `chi_tieu` | Chỉ tiêu lead và tỉ lệ chuyển đổi mục tiêu theo giai đoạn | Không |

## Quy trình

**Bước 1. Chuẩn hóa dữ liệu lead và gán giai đoạn phễu**
- Làm gì: loại bỏ lead trùng (trùng SĐT/email); chuẩn hóa tên kênh tiếp cận về danh mục thống nhất; gán mỗi lead vào đúng 1 giai đoạn theo định nghĩa thống nhất: Biết đến → Quan tâm (đăng ký tư vấn) → Nộp hồ sơ → Đủ điều kiện → Trúng tuyển → Nhập học.
- Dùng input: `du_lieu_lead`, `chien_dich`.
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: định nghĩa "giai đoạn" phải viết thành văn bản trước khi gán (VD: "Quan tâm" = đã để lại SĐT đăng ký tư vấn); dữ liệu cá nhân thí sinh chỉ xử lý trên hệ thống được phân quyền, ẩn danh khi xuất báo cáo.
- → Kết quả bước: Bộ dữ liệu lead sạch đã gán giai đoạn (kèm log số lead trùng bị loại).

**Bước 2. Lập checklist hồ sơ theo phương thức**
- Làm gì: với từng phương thức xét tuyển, liệt kê thành phần hồ sơ bắt buộc; đối chiếu từng lead ở giai đoạn "Nộp hồ sơ" → đánh dấu đủ/thiếu từng thành phần; lập danh sách lead cần bổ sung kèm hạn bổ sung.
- Dùng input: `du_lieu_lead` đã chuẩn hóa (Bước 1) + `moc_thoi_gian`.
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch, lập bảng biểu, định dạng · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi phương thức có checklist riêng (xét học bạ khác xét điểm thi); hạn bổ sung phải trước hạn nộp hồ sơ ít nhất 5 ngày làm việc.
- → Kết quả bước: Checklist hồ sơ từng phương thức + danh sách lead thiếu giấy tờ cần đôn đốc.

**Bước 3. Tính tỉ lệ chuyển đổi giữa các giai đoạn**
- Làm gì: đếm số lead từng giai đoạn → tính tỉ lệ chuyển đổi giữa các giai đoạn kề nhau; so sánh với `chi_tieu` (nếu có) và với cùng kỳ năm trước; xác định giai đoạn rớt nhiều nhất.
- Dùng input: bộ dữ liệu lead đã chuẩn hóa (Bước 1) + `chi_tieu`.
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: tính toán, phân tích số liệu · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: tỉ lệ tính trên số liệu thực tế chốt tại một thời điểm, không ước lượng; ghi rõ thời điểm chốt số liệu trong báo cáo.
- → Kết quả bước: Bảng phễu kèm tỉ lệ chuyển đổi + so sánh với chỉ tiêu/cùng kỳ.

**Bước 4. Rà soát cảnh báo**
- Làm gì: quét danh sách đôn đốc (Bước 2) tìm lead sắp quá hạn bổ sung (còn ≤ 5 ngày); quét bảng phễu (Bước 3) tìm giai đoạn có tỉ lệ rớt bất thường (giảm > 10 điểm % so với cùng kỳ hoặc thấp hơn chỉ tiêu); ghi nhận từng cảnh báo kèm số lượng cụ thể.
- Dùng input: danh sách đôn đốc (Bước 2) + bảng phễu (Bước 3) + `moc_thoi_gian`.
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: cảnh báo phải cụ thể đến nhóm lead (VD: "180 hồ sơ thiếu học bạ, hạn 25/06"), không cảnh báo chung chung.
- → Kết quả bước: Danh sách cảnh báo (lead sắp quá hạn / giai đoạn rớt bất thường).

**Bước 5. Xuất báo cáo và đề xuất hành động**
- Làm gì: tổng hợp bảng phễu + checklist đôn đốc + cảnh báo thành báo cáo ngắn; viết nhận xét (kênh nào hiệu quả nhất, nút thắt ở đâu) và đề xuất hành động cụ thể (tăng cường kênh nào, đôn đốc nhóm nào, trước ngày nào, ai phụ trách).
- Dùng input: bảng phễu (Bước 3) + danh sách đôn đốc (Bước 2) + cảnh báo (Bước 4) + `chien_dich`.
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: soạn dự thảo, tổng hợp, chuẩn hóa dữ liệu · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi đề xuất phải gắn người phụ trách và thời hạn; báo cáo ẩn danh thông tin cá nhân thí sinh.
- → Kết quả bước: Báo cáo phễu theo dõi thí sinh kèm đề xuất hành động.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Danh sách lead + mốc thời gian"/] --> B["Bước 1. Chuẩn hóa dữ liệu lead và gán giai đoạn phễu"]
    B --> C["Bước 2. Lập checklist hồ sơ theo phương thức"]
    C --> D{"Hồ sơ thiếu giấy tờ?"}
    D -->|Có| E["Lập danh sách đôn đốc bổ sung"]
    E --> F["Bước 3. Tính tỉ lệ chuyển đổi giữa các giai đoạn"]
    D -->|Không| F
    F --> G["Bước 4. Rà soát cảnh báo"]
    G --> HG["👤 Trưởng bộ phận tuyển sinh duyệt"]
    HG --> H[["Bước 5: Báo cáo phễu + đề xuất hành động"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Có đầy đủ sản phẩm: Bảng phễu lead theo giai đoạn + tỉ lệ chuyển đổi
- [ ] Có đầy đủ sản phẩm: Checklist hồ sơ thiếu cần đôn đốc
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Định nghĩa "giai đoạn" phải viết thành văn bản trước khi gán (VD: "Quan tâm" = đã để lại SĐT đăng ký tư vấn)
- [ ] Mỗi phương thức có checklist riêng (xét học bạ khác xét điểm thi)

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Human gate (người kiểm duyệt)
- Trưởng bộ phận tuyển sinh duyệt phân loại giai đoạn và báo cáo trước khi trình lãnh đạo.
- Dữ liệu thí sinh (họ tên, liên hệ) chỉ người được phân quyền mới truy cập.

## Giới hạn (guardrails)
- Không tự gửi tin nhắn/email cho thí sinh khi chưa được duyệt nội dung và danh sách.
- Không tự nhận/trả hồ sơ thay cán bộ tuyển sinh.
- Không quyết định trúng tuyển thay hội đồng tuyển sinh.
- Không chia sẻ dữ liệu cá nhân thí sinh ra ngoài; tuân thủ quy định bảo vệ dữ liệu cá nhân.
- Không bịa số liệu chuyển đổi.

## Căn cứ & lưu ý
- Gắn với đề án tuyển sinh và lịch tuyển sinh của Bộ GD&ĐT từng năm.
- Không dùng tên thật của trường/cá nhân khi mô phỏng; dữ liệu lead ví dụ đã ẩn danh.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
