---
name: "theo-doi-grant-nghien-cuu"
description: "Hỗ trợ quản lý grant/tài trợ nghiên cứu: checklist điều kiện tham gia, đối chiếu hồ sơ với yêu cầu của call, outline đề xuất, tracker milestone và deliverable. Dùng chung cho PI, nhóm nghiên cứu, phòng KHCN."
---

# Theo dõi grant nghiên cứu

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




## Khi nào dùng
Khi chuẩn bị hồ sơ đề xuất xin tài trợ nghiên cứu, hoặc đang thực hiện grant cần theo dõi
milestone/deliverable/kinh phí. Dùng chung cho chủ nhiệm đề tài (PI), nhóm nghiên cứu,
phòng KHCN ở mọi trường.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `thong_bao_call` | Thông báo mời nộp: điều kiện tham gia, yêu cầu hồ sơ, deadline, mẫu biểu | Có (giai đoạn đề xuất) |
| `ho_so_du_thao` | Hồ sơ dự thảo hiện có | Không |
| `grant_dang_thuc_hien` | Thông tin grant đang chạy: milestone, deliverable, tiến độ, kinh phí đã dùng | Không (giai đoạn theo dõi) |

## Quy trình

**Bước 1. Lập checklist điều kiện tham gia (eligibility)**
- Làm gì: Đọc `thong_bao_call`, tách từng điều kiện (tư cách chủ nhiệm, lĩnh vực ưu tiên, kinh phí tối đa, thời gian thực hiện, yêu cầu đặc thù); đối chiếu với năng lực và đề xuất hiện có; đánh dấu từng điều kiện: đạt / chưa đạt / cần làm rõ.
- Dùng input: `thong_bao_call`.
- Vai trò: Chủ nhiệm đề tài (PI) · AI hỗ trợ: đọc call, tách và đánh dấu sơ bộ từng điều kiện để PI xác nhận · ⏱ ~30 phút–1 giờ (ước tính)
- Lưu ý nghiệp vụ: điều kiện "cần làm rõ" phải kèm câu hỏi cụ thể để hỏi đơn vị tài trợ, không đoán; kinh phí và thời gian kiểm tra cả số tuyệt đối lẫn cách tính.
- → Kết quả bước: Eligibility checklist (đạt/chưa đạt/cần làm rõ từng điều kiện).

**Bước 2. Đối chiếu hồ sơ dự thảo, liệt kê gap**
- Làm gì: So từng hạng mục trong `ho_so_du_thao` với danh mục yêu cầu của call (thuyết minh, dự toán, CV chủ nhiệm, cam kết đơn vị...); liệt kê gap: thiếu tài liệu gì, mục nào chưa đúng mẫu, mục nào còn sơ sài; gắn mức độ cho từng gap (thiếu bắt buộc / cần bổ sung).
- Dùng input: `thong_bao_call`, `ho_so_du_thao`.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: đối chiếu hồ sơ với yêu cầu call, liệt kê gap (thiếu/sai mẫu/sơ sài) theo mức độ · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: phân biệt "thiếu tài liệu" với "có nhưng sai mẫu" — cách khắc phục khác nhau; mục còn sơ sài phải chỉ rõ cần bổ sung nội dung gì.
- → Kết quả bước: Gap list hồ sơ (thiếu/sai mẫu/sơ sài + mức độ).

**Bước 3. Dự thảo outline đề xuất theo cấu trúc call**
- Làm gì: Dự thảo outline đề xuất bám đúng thứ tự các mục mà call yêu cầu (tính cấp thiết, mục tiêu, nội dung & phương pháp, sản phẩm, tiến độ, dự toán, năng lực nhóm); mỗi mục ghi gợi ý nội dung cần viết — không viết hộ nội dung khoa học, không bịa số liệu.
- Dùng input: `thong_bao_call` (gap list từ bước 2).
- Vai trò: Chủ nhiệm đề tài (PI) · AI hỗ trợ: dự thảo outline theo đúng thứ tự cấu trúc call · ⏱ ~15–20 phút (ước tính)
- Lưu ý nghiệp vụ: thứ tự các mục phải y hệt call yêu cầu — sai thứ tự có thể bị loại về hành chính; outline chỉ là khung gợi ý, nội dung khoa học do PI viết.
- → Kết quả bước: Outline đề xuất theo đúng cấu trúc call.

**Bước 4. Lập tracker milestone và cảnh báo deadline**
- Làm gì: Nếu có `grant_dang_thuc_hien`: dựng bảng milestone → deliverable → deadline → trạng thái → kinh phí đã dùng; đánh dấu các hạng mục trễ hạn/sắp đến hạn. Nếu đang ở giai đoạn đề xuất: ghi deadline nộp hồ sơ và các mốc chuẩn bị tính ngược từ deadline.
- Dùng input: `grant_dang_thuc_hien`, `thong_bao_call`.
- Vai trò: Chủ nhiệm đề tài (PI) · AI hỗ trợ: dựng bảng tracker milestone/deliverable và cảnh báo deadline từ số liệu đã cho · ⏱ ~10–15 phút (ước tính)
- Lưu ý nghiệp vụ: không tự ý điều chỉnh kinh phí/milestone đã được phê duyệt; cảnh báo trễ hạn phải nêu rõ số ngày và hạng mục bị ảnh hưởng.
- → Kết quả bước: Tracker milestone/deliverable + cảnh báo deadline.

**Bước 5. Tổng hợp nhắc việc**
- Làm gì: Gộp checklist, gap list và tracker thành danh sách việc cần làm: deadline sắp tới, hạng mục còn thiếu, người phụ trách đề xuất; sắp xếp theo độ khẩn cấp.
- Dùng input: (kết quả các bước 1–4).
- Vai trò: Chủ nhiệm đề tài (PI) · AI hỗ trợ: tổng hợp danh sách nhắc việc, sắp xếp theo độ khẩn cấp · ⏱ ~10 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi việc phải có deadline cụ thể và đầu mối rõ ràng; nhắc việc chỉ là hỗ trợ — không thay PI ra quyết định nộp hay điều chỉnh hồ sơ.
- → Kết quả bước: Danh sách nhắc việc theo độ khẩn cấp — sản phẩm cuối.
## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Thông tin call + hồ sơ dự thảo"/]
    B["Checklist điều kiện (eligibility)"]
    C{"Đạt đủ điều kiện?"}
    D["Đối chiếu hồ sơ, liệt kê gap"]
    E["Ghi rõ lý do chưa đủ điều kiện"]
    F["Dự thảo outline đề xuất theo cấu trúc call"]
    G["Lập tracker milestone + cảnh báo deadline"]
    N["Tổng hợp nhắc việc theo độ khẩn cấp"]
    HG["👤 PI duyệt; Phòng KHCN kiểm tra"]
    H[/"Gap list + outline + tracker grant"/]
    A --> B --> C
    C -->|Có| D --> F --> G --> N --> HG --> H
    C -->|Không| E --> H
```

## Đầu ra (Output)
- Eligibility checklist.
- Gap list hồ sơ so với yêu cầu call.
- Outline đề xuất theo cấu trúc call.
- Tracker milestone/deliverable (nếu theo dõi grant đang thực hiện).

**Cấu trúc output chuẩn:** khung mẫu CỐ ĐỊNH của sản phẩm chính (Bộ hồ sơ theo dõi grant):
1. Thông tin call: tên quỹ, hạn mức kinh phí, thời gian thực hiện, deadline nộp hồ sơ.
2. Eligibility checklist: từng điều kiện — đạt/chưa đạt/cần làm rõ.
3. Gap list hồ sơ: thiếu tài liệu gì / mục nào sai mẫu / mục nào còn sơ sài (+ mức độ).
4. Outline đề xuất theo đúng cấu trúc call yêu cầu.
5. Tracker milestone/deliverable + cảnh báo deadline (nếu theo dõi grant đang chạy).
6. Danh sách nhắc việc: deadline sắp tới + hạng mục còn thiếu, sắp xếp theo độ khẩn cấp.

## Checklist nghiệm thu

- [ ] Đủ 6 phần theo Cấu trúc output chuẩn: thông tin call, eligibility checklist, gap list, outline, tracker, nhắc việc.
- [ ] Thông tin call (hạn mức, thời gian, deadline) khớp đúng thông báo call trong Input.
- [ ] Eligibility checklist đánh dấu đầy đủ từng điều kiện: đạt / chưa đạt / cần làm rõ (điều kiện "cần làm rõ" kèm câu hỏi cụ thể để hỏi đơn vị tài trợ).
- [ ] Gap list phân biệt rõ thiếu tài liệu / sai mẫu / sơ sài, kèm mức độ bắt buộc.
- [ ] Outline đúng thứ tự các mục call yêu cầu; chỉ là khung gợi ý — không viết hộ nội dung khoa học, không bịa số liệu.
- [ ] Không tự ý điều chỉnh kinh phí/milestone đã phê duyệt trong tracker; cảnh báo trễ hạn nêu rõ số ngày và hạng mục bị ảnh hưởng.
- [ ] Mỗi việc trong danh sách nhắc việc có deadline cụ thể và đầu mối đề xuất, sắp xếp theo độ khẩn cấp.
- [ ] Đã qua Human gate: PI duyệt toàn bộ hồ sơ; Phòng KHCN kiểm tra tính đầy đủ, đúng mẫu.

> Tiêu chí đạt: tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên quỹ, đề tài, số liệu dưới đây đều là **giả lập**.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `thong_bao_call` | Quỹ Đổi mới sáng tạo A 2027: tối đa 500 triệu đồng/đề tài, 24 tháng; yêu cầu: thuyết minh, dự toán, CV chủ nhiệm, cam kết đơn vị |
| `ho_so_du_thao` | Thuyết minh "AI hỗ trợ đánh giá học tập" (bản nháp), CV chủ nhiệm |
| `grant_dang_thuc_hien` | Không |

### Output mẫu

```
BỘ HỒ SƠ THEO DÕI GRANT (giả lập)

1. THÔNG TIN CALL — Quỹ Đổi mới sáng tạo A 2027: tối đa 500 triệu đồng/đề tài,
   thời gian 24 tháng; hồ sơ yêu cầu: thuyết minh, dự toán, CV chủ nhiệm, cam kết đơn vị.
   Deadline nộp: 30/11/2026 — còn 52 ngày.

2. CHECKLIST ĐIỀU KIỆN
[x] Chủ nhiệm có học vị tiến sĩ
[x] Lĩnh vực thuộc danh mục ưu tiên (chuyển đổi số giáo dục)
[x] Kinh phí đề xuất 450/500 triệu — trong hạn mức
[x] Thời gian 24 tháng — đúng quy định

3. GAP HỒ SƠ so với yêu cầu call:
[ ] Thiếu bắt buộc: dự toán kinh phí chi tiết theo mẫu QĐ-07
[ ] Thiếu bắt buộc: văn bản cam kết của đơn vị chủ trì
[!] Cần bổ sung: thuyết minh — mục "Sản phẩm và khả năng ứng dụng" còn sơ sài

4. OUTLINE ĐỀ XUẤT (theo cấu trúc call):
1. Tính cấp thiết | 2. Mục tiêu (tổng thể + cụ thể) | 3. Nội dung & phương pháp
4. Sản phẩm & địa chỉ ứng dụng | 5. Tiến độ 24 tháng | 6. Dự toán kinh phí
7. Năng lực nhóm thực hiện

5. TRACKER: không áp dụng (chưa có grant đang thực hiện).

6. NHẮC VIỆC (theo độ khẩn cấp):
- Lập dự toán theo mẫu QĐ-07 — trước 15/11/2026
- Xin văn bản cam kết của đơn vị chủ trì — trước 20/11/2026
- Bổ sung mục "Sản phẩm và khả năng ứng dụng" trong thuyết minh — trước 25/11/2026
```

## Human gate (người kiểm duyệt)
- **Chủ nhiệm đề tài (PI)** duyệt toàn bộ hồ sơ trước khi nộp.
- **Phòng KHCN** kiểm tra tính đầy đủ, đúng mẫu của hồ sơ.
- Hội đồng (nếu có) quyết định việc nộp/điều chỉnh.

## Giới hạn (guardrails)
- Không viết hoặc sáng tạo dữ liệu nghiên cứu giả (số liệu, kết quả) để "làm đẹp" hồ sơ.
- Không nộp hồ sơ, không ký thay, không cam kết thay đơn vị/chủ nhiệm.
- Không tự ý điều chỉnh kinh phí/milestone đã được phê duyệt trong tracker.

## Căn cứ & lưu ý
- Theo quy định của từng quỹ/tổ chức tài trợ và quy chế quản lý đề tài của trường.
- Không dùng tên thật của trường/cá nhân/tổ chức khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/theo-doi-grant-nghien-cuu`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
