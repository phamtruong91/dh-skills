---
name: "ho-so-du-an-dau-tu-ha-tang"
description: "Soạn hồ sơ đề xuất dự án đầu tư hạ tầng của trường: mục tiêu, quy mô, tổng mức đầu tư, nguồn vốn, hiệu quả, tiến độ. Dùng khi chuẩn bị trình phê duyệt chủ trương đầu tư."
---

# Hồ sơ dự án đầu tư hạ tầng

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




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

## Đầu ra (Output)
- Tờ trình + Thuyết minh đề xuất dự án đầu tư (đầy đủ 7 nội dung trên).

**Cấu trúc output chuẩn** (khung mẫu cố định của sản phẩm chính — Thuyết minh đề xuất dự án đầu tư):
1. Tiêu đề (tên đơn vị + tên thuyết minh + tên dự án).
2. Sự cần thiết đầu tư (hiện trạng, bất cập, nhu cầu — có số liệu).
3. Mục tiêu đầu tư.
4. Quy mô đầu tư (hạng mục, diện tích/công suất).
5. Tổng mức đầu tư (chi tiết các khoản + cơ sở tính).
6. Nguồn vốn (cơ cấu theo hình thức đầu tư, nghĩa vụ đối ứng của trường).
7. Hiệu quả dự kiến (ghi rõ "dự kiến" + giả định tính toán).
8. Tiến độ thực hiện (theo giai đoạn).
9. Kiến nghị phê duyệt chủ trương.
- Kèm theo: Tờ trình + phụ lục (bảng tổng mức, tiến độ, phương án vốn).

## Checklist nghiệm thu

- [ ] Đủ các phần theo "Cấu trúc output chuẩn": Tiêu đề (tên đơn vị + tên thuyết minh + tên…; Sự cần thiết đầu tư (hiện trạng, bất cập,…; Mục tiêu đầu tư.; Quy mô đầu tư (hạng mục, diện tích/công…; Tổng mức đầu tư (chi tiết các khoản + cơ sở…; Nguồn vốn (cơ cấu theo hình thức đầu tư,…; …
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

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `ten_du_an` | Ký túc xá sinh viên 2.000 chỗ – Trường Đại học A |
| `muc_tieu` | Đáp ứng chỗ ở cho 60% sinh viên ngoại tỉnh; giảm áp lực thuê trọ |
| `quy_mo` | 02 tòa nhà 9 tầng, 500 phòng (4 SV/phòng), nhà ăn, khu sinh hoạt chung |
| `tong_muc_dau_tu` | 180 tỷ đồng (xây dựng 140, thiết bị 25, tư vấn + dự phòng 15) |
| `hinh_thuc_dau_tu` | Đối tác công – tư (PPP): nhà đầu tư 70%, trường đối ứng đất + 30% |
| `tien_do` | 2027: phê duyệt, thiết kế. 2028–2029: thi công. Quý I/2030: nghiệm thu, đưa vào sử dụng. |
| `hieu_qua` | Phục vụ 2.000 SV/năm; giá thuê dự kiến 800.000đ/SV/tháng; hoàn vốn ~15 năm |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A
BAN XÚC TIẾN ĐẦU TƯ & PT HẠ TẦNG

              THUYẾT MINH ĐỀ XUẤT DỰ ÁN ĐẦU TƯ
           Ký túc xá sinh viên 2.000 chỗ

1. SỰ CẦN THIẾT ĐẦU TƯ
Trường hiện có 12.000 sinh viên, trong đó ~7.000 sinh viên ngoại tỉnh; ký túc xá
hiện hữu chỉ đáp ứng 1.500 chỗ. Nhu cầu chỗ ở còn thiếu khoảng 5.500 chỗ, sinh viên
phải thuê trọ với chi phí cao và điều kiện không đảm bảo.

2. MỤC TIÊU
Xây dựng ký túc xá 2.000 chỗ, đáp ứng 60% nhu cầu sinh viên ngoại tỉnh, đi vào
sử dụng từ quý I/2030.

3. QUY MÔ
- 02 tòa nhà 9 tầng, 500 phòng ở (4 SV/phòng).
- Nhà ăn 800 chỗ, khu sinh hoạt chung, sân thể thao.

4. TỔNG MỨC ĐẦU TƯ: 180 tỷ đồng
- Chi phí xây dựng: 140 tỷ; thiết bị: 25 tỷ; tư vấn, quản lý, dự phòng: 15 tỷ.

5. NGUỒN VỐN (hình thức PPP)
- Nhà đầu tư: 126 tỷ đồng (70%).
- Trường đối ứng: quỹ đất + 54 tỷ đồng (30%).

6. HIỆU QUẢ DỰ KIẾN
- Phục vụ 2.000 SV/năm; giá thuê dự kiến 800.000đ/SV/tháng.
- Thời gian hoàn vốn dự kiến ~15 năm.

7. TIẾN ĐỘ
- 2027: phê duyệt chủ trương, thiết kế.
- 2028–2029: thi công xây dựng.
- Quý I/2030: nghiệm thu, bàn giao đưa vào sử dụng.

Kính trình Hội đồng trường xem xét, phê duyệt chủ trương đầu tư./.
```

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

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/ho-so-du-an-dau-tu-ha-tang`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
