---
name: "bao-cao-cong-tac-y-te"
description: "Soạn báo cáo công tác y tế định kỳ (học kỳ/năm học/đột xuất) của Trạm Y tế: khám sức khỏe, phòng chống dịch bệnh, vệ sinh môi trường, BHYT. Dùng khi tổng kết gửi Ban Giám hiệu và cơ quan y tế cấp trên."
---

# Soạn báo cáo công tác y tế

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Khi báo cáo có số liệu cần so sánh hoặc nêu xu hướng, đọc mục “Biểu đồ và hình trong báo cáo số liệu” trong quy cách đầu ra trước khi vẽ.

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Khi Trạm Y tế cần báo cáo định kỳ (học kỳ, năm học) hoặc đột xuất (có dịch bệnh, sự cố y tế)
gửi Ban Giám hiệu, Phòng CTSV và cơ quan y tế địa phương.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ky_bao_cao` | Học kỳ I / Học kỳ II / Năm học / Đột xuất + thời gian | Có |
| `so_lieu_kham` | Số lượt khám sức khỏe, khám bệnh ban đầu (tổng hợp, không nêu tên cá nhân) | Có |
| `so_lieu_dich` | Tình hình dịch bệnh: số ca theo loại (tổng hợp ẩn danh) | Có |
| `so_lieu_vsmt` | Kết quả kiểm tra vệ sinh: số đợt kiểm tra, số cơ sở đạt/không đạt | Có |
| `so_lieu_bhyt` | Tỷ lệ CBVC/SV tham gia BHYT | Có |
| `ton_tai_kien_nghi` | Tồn tại, khó khăn và kiến nghị | Có |

## Quy trình

**Bước 1. Xác định kỳ báo cáo và biểu mẫu yêu cầu**
- Làm gì: chốt kỳ báo cáo (`ky_bao_cao`: học kỳ I/II, năm học hay đột xuất kèm mốc thời gian);
  kiểm tra biểu mẫu báo cáo mà Ban Giám hiệu hoặc cơ quan y tế địa phương yêu cầu
  (nếu có) để dùng đúng khung, đúng chỉ tiêu.
- Dùng input: `ky_bao_cao`.
- Vai trò: Cán bộ Trạm Y tế · AI hỗ trợ: chốt kỳ báo cáo và đối chiếu biểu mẫu theo danh sách yêu cầu · ⏱ 15–30 phút (ước tính)
- Lưu ý nghiệp vụ: báo cáo đột xuất (dịch bệnh, sự cố) có thời hạn gửi riêng, ngắn hơn
  báo cáo định kỳ — ghi rõ mốc thời gian sự kiện trong trích yếu; không gộp số liệu
  của hai kỳ khác nhau vào một báo cáo.
- → Kết quả bước: khung kỳ báo cáo đã chốt + biểu mẫu áp dụng (nếu có).

**Bước 2. Tổng hợp số liệu theo 4 mảng**
- Làm gì: tổng hợp từ sổ khám bệnh, sổ theo dõi dịch, biên bản kiểm tra vệ sinh, danh sách
  BHYT thành 4 bảng: (1) khám sức khỏe, khám chữa bệnh ban đầu (tổng lượt, số chuyển tuyến);
  (2) phòng chống dịch (số ca theo loại bệnh, số ca khỏi, biện pháp đã xử lý);
  (3) vệ sinh môi trường (số đợt kiểm tra, số cơ sở đạt/không đạt); (4) BHYT
  (tỷ lệ tham gia của CBVC và SV). Đối chiếu chéo với sổ gốc để loại số liệu trùng/lệch.
- Dùng input: `so_lieu_kham`, `so_lieu_dich`, `so_lieu_vsmt`, `so_lieu_bhyt`, `ky_bao_cao`.
- Vai trò: Cán bộ Trạm Y tế · AI hỗ trợ: tổng hợp, đối chiếu bảng số liệu ẩn danh; cán bộ y tế cung cấp và xác nhận số liệu gốc từ sổ · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: **chỉ dùng số liệu tổng hợp, ẩn danh — tuyệt đối không nêu tên, mã SV,
  mã CBVC hay thông tin nhận dạng cá nhân**; số ca dịch ghi đúng phân loại của y tế
  địa phương, không tự chẩn đoán nguyên nhân.
- → Kết quả bước: 4 bảng số liệu tổng hợp đã đối chiếu với sổ gốc, không chứa
  thông tin cá nhân.

**Bước 3. Đánh giá kết quả và tồn tại**
- Làm gì: so sánh kết quả 4 mảng với kế hoạch y tế học đường của kỳ (tỷ lệ hoàn thành
  từng chỉ tiêu); nêu tồn tại cụ thể có số liệu và nguyên nhân (VD: thiếu 01 y sĩ
  so với định biên → ảnh hưởng tiến độ khám).
- Dùng input: `ton_tai_kien_nghi`, 4 bảng số liệu (Bước 2).
- Vai trò: Cán bộ Trạm Y tế · AI hỗ trợ: soạn dự thảo so sánh chỉ tiêu với kế hoạch · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: đánh giá bằng số liệu, không dùng ngôn từ định tính chung chung;
  tồn tại nào không có nguyên nhân rõ thì ghi "đang làm rõ", không suy đoán.
- → Kết quả bước: dự thảo phần đánh giá — kết quả đạt được so với kế hoạch,
  tồn tại và nguyên nhân.

**Bước 4. Xây dựng kiến nghị**
- Làm gì: cụ thể hóa `ton_tai_kien_nghi` thành danh mục kiến nghị gửi Ban Giám hiệu:
  mỗi kiến nghị nêu rõ nội dung (nhân sự, kinh phí, trang thiết bị), lý do, mức độ
  ưu tiên và thời hạn đề xuất.
- Dùng input: `ton_tai_kien_nghi`, phần tồn tại (Bước 3).
- Vai trò: Trưởng Trạm Y tế và Ban Giám hiệu · AI hỗ trợ: cụ thể hóa thành danh mục kiến nghị, Trưởng Trạm rà soát tính khả thi và mức ưu tiên · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: kiến nghị phải khả thi trong thẩm quyền của trường (việc vượt thẩm
  quyền thì đề xuất "kiến nghị cấp trên xem xét"); không đưa kiến nghị không gắn với
  tồn tại đã nêu.
- → Kết quả bước: danh mục kiến nghị có mức ưu tiên và thời hạn đề xuất.

**Bước 5. Kiểm tra và hoàn thiện văn bản**
- Làm gì: gộp các phần thành văn bản hành chính đúng thể thức (quốc hiệu, số văn bản,
  kính gửi, chữ ký, nơi nhận); kiểm tra: số liệu giữa các bảng và phần đánh giá không
  mâu thuẫn, tổng các thành phần khớp tổng đã nêu; ngôn ngữ khách quan, không kết luận
  y khoa.
- Dùng input: toàn bộ dự thảo các bước 1–4.
- Vai trò: Cán bộ Trạm Y tế · AI hỗ trợ: kiểm tra nhất quán số liệu và thể thức văn bản · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: **tuyệt đối không** đưa chẩn đoán, kết luận nguyên nhân bệnh hay
  khuyến nghị điều trị vào báo cáo hành chính; đọc soát lần cuối trước khi trình ký.
- → Kết quả bước: dự thảo báo cáo công tác y tế hoàn chỉnh, đúng thể thức.

**Bước 6. Trình ký và phát hành**
- Làm gì: trình Trưởng Trạm Y tế kiểm tra số liệu và ký báo cáo; gửi Ban Giám hiệu
  (báo cáo), Phòng CTSV (phối hợp), cơ quan y tế địa phương (bản sao khi có yêu cầu);
  lưu hồ sơ tại Trạm theo quy định lưu trữ.
- Dùng input: `ky_bao_cao` (để ghi sổ văn bản đi đúng kỳ).
- Vai trò: Trưởng Trạm Y tế và Ban Giám hiệu · AI hỗ trợ: soạn dự thảo văn bản trình ký, kiểm tra thể thức · ⏱ 0,5–1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: số văn bản lấy theo sổ văn bản đi của Trạm; bản gửi cơ quan y tế
  địa phương phải đúng biểu mẫu và thời hạn của ngành y tế.
- → Kết quả bước: báo cáo công tác y tế hoàn chỉnh, đã ký và phát hành đúng nơi nhận.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Báo cáo công tác y tế hoàn chỉnh"/] --> B1["Bước 1: Xác định kỳ báo cáo và biểu mẫu yêu cầu"]
    B1 --> B2["Bước 2: Tổng hợp số liệu theo 4 mảng"]
    B2 --> B3["Bước 3: Đánh giá kết quả và tồn tại"]
    B3 --> B4["Bước 4: Xây dựng kiến nghị"]
    B4 --> B5["Bước 5: Kiểm tra và hoàn thiện văn bản"]
    B5 --> B6["Bước 6: Trình ký và phát hành"]
    B6 --> HG["👤 Trưởng Trạm kiểm tra và ký báo cáo"]
    HG --> OUT[["Sản phẩm đầu ra"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Số liệu trong output khớp với Input đã cho (số lượt khám, số ca dịch, kết quả kiểm tra vệ sinh, tỷ lệ BHYT).
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn; không tự chẩn đoán nguyên nhân bệnh.
- [ ] Đúng thể thức văn bản hành chính: quốc hiệu, số văn bản, kính gửi, chữ ký, nơi nhận.
- [ ] Căn cứ pháp lý đầy đủ, còn hiệu lực (quy định y tế trường học, chế độ báo cáo của ngành y tế).
- [ ] Đã qua Human gate: Trưởng Trạm Y tế kiểm tra số liệu và ký báo cáo.
- [ ] Không nêu tên, mã SV/CBVC hay thông tin nhận dạng cá nhân — chỉ dùng số liệu tổng hợp, ẩn danh.
- [ ] Không đưa chẩn đoán, kết luận nguyên nhân bệnh hay khuyến nghị điều trị vào báo cáo.
- [ ] Số liệu giữa các bảng và phần đánh giá nhất quán, tổng các thành phần khớp tổng đã nêu.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Human gate (người kiểm duyệt)
- Trưởng Trạm Y tế kiểm tra số liệu và ký báo cáo.
- Ban Giám hiệu tiếp nhận; cơ quan y tế địa phương tiếp nhận bản sao khi có yêu cầu.

## Giới hạn (guardrails)
- **Tuyệt đối không** nêu tên, mã số sinh viên, mã CBVC hay bất kỳ thông tin nhận dạng
  cá nhân nào trong báo cáo; chỉ dùng số liệu tổng hợp, ẩn danh.
- **Tuyệt đối không** chẩn đoán, kết luận nguyên nhân bệnh hay đưa khuyến nghị điều trị
  trong báo cáo hành chính.
- Mọi số liệu trong ví dụ đều giả lập.

## Căn cứ & lưu ý
- Quy định về y tế trường học; chế độ báo cáo của ngành y tế địa phương.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
