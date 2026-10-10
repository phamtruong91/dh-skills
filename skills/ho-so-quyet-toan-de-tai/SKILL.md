---
name: "ho-so-quyet-toan-de-tai"
description: "Kiểm tra và soạn hồ sơ thanh quyết toán kinh phí đề tài nghiên cứu khoa học: phân loại chứng từ theo nội dung chi (thuê khoán, vật tư, hội thảo, công tác phí...), đối chiếu với dự toán được duyệt, lập bảng quyết toán và checklist hồ sơ. Dùng khi đề tài kết thúc hoặc đến kỳ thanh toán kinh phí."
---

# Hồ sơ thanh quyết toán kinh phí đề tài

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
Khi đề tài/dự án nghiên cứu khoa học các cấp cần thanh quyết toán kinh phí: chuẩn bị hồ sơ
chứng từ thanh toán đợt, quyết toán khi đề tài kết thúc, đối chiếu chi thực tế với dự toán
được phê duyệt, kiểm tra trước khi nộp về Phòng KHCN / Phòng Tài chính.

## Đầu vào (Input)
| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_de_tai` | Tên đầy đủ của đề tài/dự án | Có |
| `ma_de_tai` | Mã số đề tài (nếu có) | Không |
| `chu_nhiem` | Họ tên, chức danh, đơn vị của chủ nhiệm đề tài | Có |
| `cap_de_tai` | Cấp Bộ / Tỉnh / Trường / cơ sở | Có |
| `tong_kinh_phi` | Tổng kinh phí được phê duyệt (VNĐ) | Có |
| `du_toan_chi_tiet` | Bảng dự toán theo từng nội dung chi: nội dung, số tiền, tỷ lệ | Có |
| `chung_tu` | Danh sách chứng từ phát sinh: ngày, nội dung chi, số tiền, loại chứng từ (hóa đơn/chứng từ thuê khoán/biên lai...) | Có |
| `dot_thanh_toan` | Đợt thanh toán (đợt 1/2/... hoặc quyết toán cuối kỳ) | Có |
| `thoi_gian_thuc_hien` | Thời gian thực hiện đề tài (từ–đến) | Không |

## Quy trình
**Ràng buộc pháp lý khi thực hiện** (trích references/phap-ly.md; đối chiếu toàn văn và hiệu lực tại ngày nghiệp vụ):
- Luật 93/2025/QH15; Nghị định 265/2025 và 267/2025, hiệu lực 14/10/2025: Yêu cầu cấp nhiệm vụ, nguồn kinh phí, tài trợ/đặt hàng, ngày phê duyệt, quy chế cơ quan tài trợ, phương thức khoán và quyền sử dụng kết quả. Đối chiếu NĐ 265 về tài chính và NĐ 267 về nhiệm vụ; không cố định thang xếp loại hoặc thu hồi toàn bộ kinh phí cho mọi đề tài. Nghiệm thu dựa hợp đồng và tiêu chí được duyệt, hội đồng có thẩm quyền xác nhận.
- Trước Bước 1: chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi nhận nội bộ [CẦN XÁC MINH] (không đưa vào file giao), để trống phần tương ứng, chưa kết luận tuân thủ.

**Bước 1. Phân loại chứng từ theo nhóm nội dung chi**
- Làm gì: từ `chung_tu` phân loại từng chứng từ vào 6 nhóm chuẩn: (1) thuê khoán chuyên môn; (2) vật tư, nguyên liệu, dụng cụ thí nghiệm; (3) hội thảo, hội nghị khoa học; (4) công tác phí; (5) in ấn, tài liệu, xuất bản; (6) quản lý chung, chi khác; mỗi chứng từ ghi rõ: ngày, nội dung chi, số tiền, loại chứng từ (hóa đơn/chứng từ thuê khoán/biên lai...).
- Dùng input: `chung_tu`, `ten_de_tai`, `ma_de_tai`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: phân loại chứng từ vào 6 nhóm · ⏱ ~30–45 phút (ước tính, tùy số lượng chứng từ)
- Lưu ý nghiệp vụ: một chứng từ chỉ thuộc một nhóm — chứng từ "lưỡng tính" (VD: in tài liệu hội thảo) thì xếp theo mục đích chính và ghi chú rõ; sắp xếp chứng từ theo thứ tự thời gian trong từng nhóm.
- → Kết quả bước: bảng phân loại chứng từ (chứng từ – nhóm nội dung chi – số tiền).

**Bước 2. Kiểm tra tính hợp lệ từng chứng từ**
- Làm gì: kiểm tra từng chứng từ theo 5 tiêu chí: đúng mẫu quy định; đủ chữ ký (người đề nghị chi, kế toán, thủ trưởng); phát sinh trong `thoi_gian_thuc_hien` của đề tài; nội dung chi phù hợp mục đích đề tài; số tiền không vượt định mức; lập danh sách chứng từ đạt/không đạt — chứng từ không đạt thì yêu cầu bổ sung, hoàn thiện rồi kiểm tra lại.
- Dùng input: kết quả bước 1, `thoi_gian_thuc_hien`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: lập bảng đạt/cần bổ sung · ⏱ ~45–60 phút (ước tính, tùy số lượng chứng từ)
- Lưu ý nghiệp vụ: 2 lỗi bị loại nhiều nhất — chứng từ phát sinh ngoài thời gian thực hiện đề tài và thiếu chữ ký/người duyệt; hóa đơn phải là hóa đơn hợp pháp (tra cứu được).
- → Kết quả bước: bảng kiểm tra hợp lệ từng chứng từ (đạt / cần bổ sung + lý do).

**Bước 3. Đối chiếu dự toán với thực chi**
- Làm gì: từ `du_toan_chi_tiet` và kết quả bước 2, lập bảng so sánh theo từng nội dung chi: Dự toán – Thực chi – Chênh lệch (số tiền và %); đánh dấu các khoản vượt dự toán hoặc chi sai nội dung; khoản vượt trong ngưỡng cho phép thì soạn thuyết minh điều chỉnh, vượt ngưỡng thì báo cáo xin điều chỉnh dự toán chính thức.
- Dùng input: `du_toan_chi_tiet`, `tong_kinh_phi`, kết quả bước 2.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: lập bảng đối chiếu dự toán – thực chi · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: mức điều chỉnh giữa các nội dung chi tuân theo quy định của cơ quan quản lý (thường ≤10–20% cần thuyết minh, vượt ngưỡng phải xin điều chỉnh dự toán) — không tự ý "cấn trừ" giữa các khoản mục.
- → Kết quả bước: bảng đối chiếu dự toán – thực chi – chênh lệch + danh sách khoản cần thuyết minh/điều chỉnh.

**Bước 4. Lập bảng quyết toán tổng hợp**
- Làm gì: tổng hợp từ kết quả bước 3: tổng thực chi, số kinh phí đã tạm ứng, số còn phải thanh toán hoặc số phải nộp trả ngân sách (nếu chi không hết); viết kết luận quyết toán (tiết kiệm/vượt chi bao nhiêu, tỷ lệ %).
- Dùng input: kết quả bước 3, `dot_thanh_toan`, `tong_kinh_phi`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: tổng hợp số liệu và viết kết luận quyết toán · ⏱ ~15–20 phút (ước tính)
- Lưu ý nghiệp vụ: tổng thực chi không được vượt `tong_kinh_phi` đã phê duyệt; nếu là quyết toán cuối kỳ thì số liệu phải khớp với bảng quyết toán trong báo cáo tổng kết nghiệm thu.
- → Kết quả bước: bảng quyết toán tổng hợp + kết luận quyết toán.

**Bước 5. Lập checklist hồ sơ thanh quyết toán**
- Làm gì: lập checklist các thành phần: tờ trình đề nghị thanh toán/quyết toán; bảng quyết toán tổng hợp (có xác nhận chủ nhiệm); bảng đối chiếu dự toán – thực chi; bộ chứng từ gốc sắp xếp theo nhóm nội dung chi; thuyết minh điều chỉnh (nếu có ở bước 3); biên bản nghiệm thu (nếu quyết toán cuối kỳ); xác nhận của đơn vị chủ trì; đánh dấu đủ/thiếu từng thành phần.
- Dùng input: kết quả bước 1–4, `dot_thanh_toan`, `chu_nhiem`, `cap_de_tai`.
- Vai trò: Chủ nhiệm đề tài · AI hỗ trợ: lập checklist các thành phần hồ sơ theo đợt thanh toán · ⏱ ~15–20 phút (ước tính)
- Lưu ý nghiệp vụ: quyết toán cuối kỳ bắt buộc có biên bản nghiệm thu; thanh toán đợt giữa kỳ thì thay bằng báo cáo tiến độ đã được đánh giá đạt yêu cầu.
- → Kết quả bước: checklist hồ sơ (đánh dấu đủ/thiếu từng thành phần).

**Bước 6. Hoàn thiện và trình duyệt**
- Làm gì: trình chủ nhiệm ký xác nhận, đơn vị chủ trì xác nhận; nộp Phòng KHCN / Phòng Tài chính kiểm tra và duyệt; xuất bộ hồ sơ hoàn chỉnh ở theo định dạng đầu ra của skill, sẵn sàng in/ký và nộp.
- Dùng input: kết quả bước 4–5.
- Vai trò: Phòng KHCN, Phòng Tài chính · AI hỗ trợ: chuẩn bị hồ sơ trình ký, nhắc lịch và theo dõi tiến độ · ⏱ ~1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: giữ lại 01 bộ chứng từ sao có đóng dấu của đơn vị; nộp bản gốc duy nhất mà không giữ bản lưu là rủi ro khi hồ sơ bị thất lạc.
- → Kết quả bước: bộ hồ sơ quyết toán hoàn chỉnh đã duyệt.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/Danh sách chứng từ và dự toán được duyệt/] --> A["Bước 1: Phân loại chứng từ theo nhóm nội dung chi"]
    A --> B{"Bước 2: Chứng từ hợp lệ?"}
    B -->|Không| C["Yêu cầu bổ sung, hoàn thiện"]
    C --> A
    B -->|Có| D["Bước 3: Đối chiếu dự toán với thực chi"]
    D --> E["Bước 4: Lập bảng quyết toán tổng hợp"]
    E --> F["Bước 5: Lập checklist hồ sơ"]
    F --> HG["👤 Bước 6: Phòng Tài chính kiểm tra và duyệt"]
    HG --> OUT[["Bộ hồ sơ quyết toán hoàn chỉnh"]]
```

## Đầu ra
- Bảng quyết toán kinh phí đề tài (dự toán – thực chi – chênh lệch theo nội dung).
- Bảng phân loại chứng từ kèm trạng thái hợp lệ/thiếu sót của từng chứng từ.
- Checklist hồ sơ thanh quyết toán (đánh dấu đủ/thiếu từng thành phần).
- Danh sách các khoản cần điều chỉnh/thuyết minh bổ sung (nếu có).

**Cấu trúc output chuẩn:** khung cố định của bộ hồ sơ quyết toán, các phần bắt buộc theo đúng thứ tự xuất hiện:
1. Tiêu đề "BẢNG QUYẾT TOÁN KINH PHÍ ĐỀ TÀI" + đợt thanh toán
2. Khối thông tin: tên đề tài, mã số, chủ nhiệm, cấp đề tài, thời gian thực hiện
3. Bảng quyết toán: TT – Nội dung chi – Dự toán – Thực chi – Chênh lệch (theo 6 nhóm nội dung chi) + dòng tổng cộng
4. Kết luận quyết toán (tổng thực chi, tiết kiệm/vượt chi, tỷ lệ %)
5. Bảng phân loại chứng từ (nhóm nội dung chi – chứng từ – trạng thái hợp lệ)
6. Danh sách khoản cần điều chỉnh/thuyết minh bổ sung (nếu có)
7. Checklist hồ sơ thanh quyết toán (đánh dấu đủ/thiếu từng thành phần)

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md); trường thiếu để trống, không kèm tài liệu kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao
Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Đủ 7 phần theo "Cấu trúc output chuẩn": tiêu đề + đợt thanh toán → khối thông tin → bảng quyết toán → kết luận quyết toán → bảng phân loại chứng từ → khoản cần điều chỉnh/thuyết minh → checklist hồ sơ
- [ ] Số liệu trong output khớp Input: tổng kinh phí = `tong_kinh_phi`; dự toán theo khoản mục = `du_toan_chi_tiet`; danh sách chứng từ = `chung_tu`
- [ ] Không bịa đặt số tiền, chứng từ, nội dung chi
- [ ] Bảng quyết toán đúng mẫu (TT – nội dung chi – dự toán – thực chi – chênh lệch); tổng thực chi không vượt kinh phí được phê duyệt
- [ ] Căn cứ pháp lý đầy đủ, còn hiệu lực (Thông tư 02/2023/TT-BKHCN, quy chế quản lý đề tài, quyết định phê duyệt kinh phí)
- [ ] Mọi chứng từ phát sinh trong thời gian thực hiện đề tài, đủ chữ ký theo quy định, hóa đơn hợp pháp; khoản vượt dự toán trong ngưỡng có thuyết minh, vượt ngưỡng có văn bản điều chỉnh chính thức
- [ ] Quyết toán cuối kỳ: số liệu khớp bảng quyết toán trong báo cáo tổng kết nghiệm thu; hồ sơ kèm biên bản nghiệm thu
- [ ] Đã qua Human gate: chủ nhiệm và đơn vị chủ trì ký xác nhận; Phòng KHCN / Phòng Tài chính kiểm tra và duyệt

## Căn cứ & lưu ý
- Thông tư 02/2023/TT-BKHCN về quản lý đề tài KHCN cấp Bộ và các văn bản quản lý
  đề tài cấp trường của Trường Đại học A.
- Chứng từ phải phát sinh trong thời gian thực hiện đề tài; chi ngoài thời gian
  không được quyết toán.
- Mức điều chỉnh giữa các nội dung chi tuân theo quy định của cơ quan quản lý
  đề tài (thường ≤ 10–20% cần thuyết minh, vượt ngưỡng phải xin điều chỉnh dự toán).
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Tư liệu đối chiếu
Bản gốc trước cập nhật pháp lý (kèm ví dụ giả lập) lưu tại `references/quy-trinh-lich-su.md`, chỉ để đối chiếu hồ sơ lịch sử; không dùng căn cứ, mẫu hay số liệu trong đó làm chỉ dẫn hiện hành.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
