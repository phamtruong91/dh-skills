---
name: ke-hoach-nckh-khoa
description: Lập kế hoạch nghiên cứu khoa học cấp khoa của trường đại học trong năm học: đề tài các cấp, bài báo khoa học, hội thảo, giáo trình, hoạt động NCKH sinh viên. Dùng đầu mỗi năm học.
---

# Skill: Kế hoạch NCKH cấp khoa

## Khi nào dùng
Khi đầu năm học, khoa cần xây dựng kế hoạch nghiên cứu khoa học cho giảng viên
và sinh viên, làm căn cứ giao nhiệm vụ và đánh giá cuối năm.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `khoa` | Tên khoa | Có |
| `nam_hoc` | Năm học kế hoạch | Có |
| `dinh_huong` | Định hướng nghiên cứu của khoa (gắn với chiến lược trường) | Có |
| `chi_tieu` | Chỉ tiêu: số đề tài (cấp bộ/trường), bài báo (quốc tế/trong nước), hội thảo, giáo trình | Có |
| `luc_luong` | Số GV tham gia, nhóm nghiên cứu mạnh | Không |

## Quy trình

**Bước 1. Rà soát chiến lược và kết quả năm trước**
- Làm gì: Thu thập chiến lược KHCN của trường (giai đoạn hiện hành), kế hoạch NCKH
  khoa năm trước và kết quả thực hiện (tỷ lệ hoàn thành chỉ tiêu từng mảng); xác định
  thế mạnh, nhóm nghiên cứu mạnh của khoa; ghi nhận các vướng mắc năm trước (kinh phí,
  nhân lực, thủ tục) để tránh lặp lại.
- Dùng input: `khoa`, `nam_hoc`, `dinh_huong`
- Vai trò: Giảng viên · AI hỗ trợ: tổng hợp kết quả năm trước, thế mạnh và vướng mắc thành báo cáo rà soát · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: Kế hoạch mới phải kế thừa, không "làm lại từ số 0" — chỉ tiêu năm
  trước không đạt thì năm nay phải có giải pháp cụ thể đi kèm, không chỉ nâng số;
  định hướng nghiên cứu phải gắn với chiến lược của trường, tránh đặt hướng "trên trời"
  không có lực lượng thực hiện.
- → Kết quả bước: Báo cáo rà soát (định hướng chiến lược, kết quả năm trước, thế
  mạnh/vướng mắc của khoa).

**Bước 2. Xác định hướng nghiên cứu trọng tâm**
- Làm gì: Căn cứ chiến lược trường và thế mạnh khoa, đề xuất 02–03 hướng nghiên cứu
  trọng tâm của năm học; lấy ý kiến các bộ môn/nhóm nghiên cứu; chốt danh sách hướng
  trọng tâm được tập thể khoa thống nhất.
- Dùng input: `dinh_huong`, `luc_luong`
- Vai trò: Giảng viên · AI hỗ trợ: đề xuất các hướng nghiên cứu trọng tâm, tập thể khoa thảo luận và thống nhất · ⏱ 1–2 ngày làm việc (lấy ý kiến bộ môn) (ước tính)
- Lưu ý nghiệp vụ: Mỗi hướng trọng tâm phải có ít nhất một nhóm nghiên cứu "đỡ đầu" —
  hướng không có lực lượng là hướng chết; số hướng không nên quá 3 để tránh dàn trải
  nguồn lực.
- → Kết quả bước: Danh sách 02–03 hướng nghiên cứu trọng tâm đã thống nhất.

**Bước 3. Đặt chỉ tiêu cụ thể từng mảng**
- Làm gì: Đặt chỉ tiêu định lượng cho 5 mảng: (1) Đề tài — số lượng theo cấp
  (bộ/trường), tiến độ đăng ký – nghiệm thu; (2) Bài báo — số bài quốc tế/trong nước,
  gắn với từng nhóm nghiên cứu; (3) Hội thảo — số hội thảo tổ chức/tham gia;
  (4) Giáo trình, bài giảng — số biên soạn mới/tái bản; (5) NCKH sinh viên — số đề tài
  SV, giải thưởng mục tiêu. Đối chiếu chỉ tiêu với năng lực thực tế của đội ngũ.
- Dùng input: `chi_tieu`, `luc_luong`
- Vai trò: Giảng viên · AI hỗ trợ: lập bảng chỉ tiêu dự thảo 5 mảng theo năng lực đội ngũ, lãnh đạo khoa quyết định chỉ tiêu · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: Chỉ tiêu phải vừa sức nhưng có tính phấn đấu — chỉ tiêu "an toàn"
  quá thấp sẽ bị đánh giá thiếu tham vọng khi tổng hợp toàn trường; bài báo quốc tế
  nên gắn tên nhóm/cá nhân cụ thể, tránh chỉ tiêu chung chung không ai chịu trách nhiệm.
- → Kết quả bước: Bảng chỉ tiêu chi tiết 5 mảng (đề tài, bài báo, hội thảo, giáo
  trình, NCKH sinh viên).

**Bước 4. Giao chỉ tiêu đến bộ môn, nhóm, cá nhân**
- Làm gì: Phân bổ chỉ tiêu từ Bước 3 xuống từng bộ môn/nhóm nghiên cứu/cá nhân theo
  năng lực và hướng trọng tâm; lập bảng phân công chi tiết; gửi dự thảo cho các bộ môn
  góp ý, điều chỉnh trước khi chốt.
- Dùng input: `chi_tieu`, `luc_luong`
- Vai trò: Giảng viên · AI hỗ trợ: phân bổ chỉ tiêu dự thảo xuống bộ môn/nhóm, các bộ môn góp ý và điều chỉnh trước khi chốt · ⏱ 2–3 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Tổng chỉ tiêu các bộ môn cộng lại phải khớp với chỉ tiêu chung của
  khoa — lệch là lỗi hay gặp nhất; khi giao chỉ tiêu cho cá nhân phải gắn với đánh giá
  thi đua cuối năm thì mới có tính ràng buộc.
- → Kết quả bước: Bảng phân công chỉ tiêu theo bộ môn/nhóm nghiên cứu.

**Bước 5. Xây dựng tiến độ thực hiện theo quý**
- Làm gì: Lập lịch các mốc chính theo quý: đăng ký đề tài (thường Q4 năm trước/Q1),
  nộp bài báo (rải đều 4 quý), tổ chức/tham gia hội thảo, nghiệm thu giáo trình, tổng
  kết NCKH sinh viên; gắn mốc kiểm tra giữa kỳ (sơ kết 6 tháng) để điều chỉnh.
- Dùng input: `nam_hoc`
- Vai trò: Giảng viên · AI hỗ trợ: lập lịch tiến độ theo quý và mốc sơ kết giữa kỳ từ lịch chính thức của Phòng KHCN · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: Mốc đăng ký đề tài cấp bộ/cấp trường do cấp trên quy định — phải
  lấy lịch chính thức từ Phòng KHCN, không tự đặt; bài báo quốc tế cần thời gian phản
  biện dài, nên đặt mốc nộp sớm hơn mốc công bố ít nhất 2 quý.
- → Kết quả bước: Lịch tiến độ thực hiện theo quý (kèm mốc sơ kết giữa kỳ).

**Bước 6. Dự toán kinh phí**
- Làm gì: Dự toán chi tiết theo nguồn: nguồn của trường (đề tài cấp trường, hội thảo,
  hỗ trợ bài báo, NCKH sinh viên) và nguồn ngoài (đề tài cấp bộ, hợp tác doanh nghiệp,
  địa phương); đối chiếu với định mức chi của trường; tổng hợp thành bảng dự toán.
- Dùng input: `chi_tieu`
- Vai trò: Giảng viên · AI hỗ trợ: lập bảng dự toán theo định mức hiện hành, kế toán/khoa kiểm tra nguồn trường và nguồn ngoài · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: Nguồn ngoài chỉ ghi "dự kiến" kèm cơ sở (đề tài đã trúng tuyển,
  hợp đồng đã ký) — không ghi số "ảo" để làm đẹp kế hoạch; kinh phí hỗ trợ bài báo
  quốc tế phải theo đúng định mức hiện hành của trường.
- → Kết quả bước: Bảng dự toán kinh phí (nguồn trường + nguồn ngoài).

**Bước 7. Hoàn thiện văn bản, trình ký ban hành**
- Làm gì: Soạn thảo văn bản kế hoạch đầy đủ các phần (định hướng, chỉ tiêu, phân công,
  tiến độ, kinh phí, tổ chức thực hiện); kiểm tra tính nhất quán giữa các bảng;
  trình Trưởng khoa ký ban hành; gửi Phòng KHCN để tổng hợp kế hoạch toàn trường;
  phổ biến đến các bộ môn.
- Dùng input: `khoa`, `nam_hoc`
- Vai trò: Trưởng khoa · AI hỗ trợ: chuẩn bị dự thảo, tài liệu và số liệu phục vụ bước này · ⏱ 1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Kiểm tra lần cuối: tổng các bảng phân công khớp với bảng chỉ tiêu
  chung; số ký hiệu văn bản, ngày tháng đúng thể thức; kế hoạch phải ban hành trước
  khi năm học bắt đầu đủ sớm để các bộ môn kịp cụ thể hóa thành kế hoạch bộ môn.
- → Kết quả bước: Văn bản kế hoạch NCKH cấp khoa đã ký ban hành + bảng chỉ tiêu chi
  tiết theo bộ môn/nhóm nghiên cứu.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Chiến lược KHCN trường, thế mạnh khoa"/] --> B["Bước 1. Rà soát chiến lược, kết quả năm trước"]
    B --> C["Bước 2. Xác định 02-03 hướng nghiên cứu trọng tâm"]
    C --> D["Bước 3. Đặt chỉ tiêu: đề tài, bài báo, hội thảo, giáo trình, NCKH SV"]
    D --> E["Bước 4. Giao chỉ tiêu đến bộ môn, nhóm, cá nhân"]
    E --> F["Bước 5. Xây dựng tiến độ theo quý"]
    F --> G["Bước 6. Dự toán kinh phí: nguồn trường + nguồn ngoài"]
    G --> HG["👤 Bước 7. Trưởng khoa ký ban hành"]
    HG --> H["Gửi Phòng KHCN tổng hợp kế hoạch toàn trường"]
    H --> I[/"Kế hoạch NCKH, bảng chỉ tiêu chi tiết"/]
```

## Đầu ra (Output)
- Văn bản kế hoạch NCKH cấp khoa hoàn chỉnh.
- Bảng chỉ tiêu chi tiết theo bộ môn/nhóm nghiên cứu.

**Cấu trúc output chuẩn** (sản phẩm chính: Văn bản kế hoạch NCKH cấp khoa) — các phần
bắt buộc theo đúng thứ tự:
1. Tên trường (dòng trên), tên khoa (dòng dưới).
2. Số ký hiệu văn bản.
3. Địa danh, ngày tháng năm ban hành.
4. Tiêu đề: KẾ HOẠCH / Nghiên cứu khoa học năm học ...
5. Phần I. ĐỊNH HƯỚNG (02–03 hướng nghiên cứu trọng tâm, gắn chiến lược trường).
6. Phần II. CHỈ TIÊU CỤ THỂ (bảng: STT, nội dung, chỉ tiêu, đơn vị thực hiện, tiến độ).
7. Phần III. PHÂN CÔNG THEO BỘ MÔN (bảng giao chỉ tiêu từng bộ môn/nhóm).
8. Phần IV. TIẾN ĐỘ THỰC HIỆN (các mốc chính theo quý + mốc sơ kết giữa kỳ).
9. Phần V. KINH PHÍ (nguồn trường + nguồn ngoài dự kiến).
10. Phần VI. TỔ CHỨC THỰC HIỆN (trách nhiệm bộ môn, theo dõi tiến độ, gắn thi đua).
11. Nơi nhận – Lưu.
12. Chữ ký Trưởng khoa (họ tên, học hàm/học vị).

## Checklist nghiệm thu

- [ ] Đủ 12 phần của "Cấu trúc output chuẩn": từ tiêu đề hành chính đến chữ ký Trưởng khoa.
- [ ] Nội dung khớp với Input: 02–03 hướng trọng tâm, chỉ tiêu 5 mảng (đề tài, bài báo, hội thảo, giáo trình, NCKH SV).
- [ ] Tổng chỉ tiêu các bộ môn cộng lại khớp với chỉ tiêu chung của khoa.
- [ ] Nguồn ngoài chỉ ghi "dự kiến" kèm cơ sở; kinh phí theo đúng định mức hiện hành của trường.
- [ ] Mỗi hướng trọng tâm có ít nhất một nhóm nghiên cứu "đỡ đầu".
- [ ] Bài báo quốc tế gắn tên nhóm/cá nhân cụ thể; mốc nộp sớm hơn mốc công bố ít nhất 2 quý.
- [ ] Mốc đăng ký đề tài cấp bộ/cấp trường lấy đúng lịch chính thức của Phòng KHCN.
- [ ] Đúng thể thức: số ký hiệu, ngày tháng, nơi nhận, chữ ký Trưởng khoa.
- [ ] Đã qua Human gate: Trưởng khoa đã ký ban hành; kế hoạch đã gửi Phòng KHCN và phổ biến đến các bộ môn.
- [ ] Kế hoạch ban hành đủ sớm để các bộ môn kịp cụ thể hóa thành kế hoạch bộ môn.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `khoa` | Khoa Công nghệ thông tin |
| `nam_hoc` | 2027–2028 |
| `dinh_huong` | Trí tuệ nhân tạo ứng dụng, an toàn thông tin, chuyển đổi số giáo dục |
| `chi_tieu` | 07 đề tài (02 cấp bộ, 05 cấp trường); 20 bài báo (10 quốc tế); 01 hội thảo quốc tế; 02 giáo trình |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A
KHOA CÔNG NGHỆ THÔNG TIN
      Số: 10/KH-ĐHA-CNTT
                                                 Thành phố C, ngày 09 tháng 10 năm 2026

KẾ HOẠCH
Nghiên cứu khoa học năm học 2027–2028

I. ĐỊNH HƯỚNG
Tập trung 03 hướng nghiên cứu trọng tâm: (1) Trí tuệ nhân tạo ứng dụng;
(2) An toàn thông tin; (3) Chuyển đổi số trong giáo dục – gắn với chiến lược
KHCN của Trường giai đoạn 2026–2030.

II. CHỈ TIÊU CỤ THỂ

| STT | Nội dung | Chỉ tiêu | Đơn vị thực hiện | Tiến độ |
|---|---|---|---|---|
| 1 | Đề tài cấp bộ | 02 đề tài | Nhóm AI, Nhóm ATTT | Đăng ký Q4/2027 |
| 2 | Đề tài cấp trường | 05 đề tài | Các bộ môn | Đăng ký Q1/2028 |
| 3 | Bài báo quốc tế | 10 bài | Các nhóm nghiên cứu | Rải đều 4 quý |
| 4 | Bài báo trong nước | 10 bài | Các bộ môn | Rải đều 4 quý |
| 5 | Hội thảo quốc tế | 01 hội thảo | Khoa chủ trì | Q2/2028 |
| 6 | Giáo trình | 02 giáo trình | Bộ môn KHMT, HTTT | Nghiệm thu Q3/2028 |
| 7 | NCKH sinh viên | 15 đề tài SV; phấn đấu 02 giải cấp bộ | Đoàn – Hội + các bộ môn | Q2/2028 |

III. PHÂN CÔNG THEO BỘ MÔN

| Bộ môn | Đề tài | Bài báo QT | Bài báo TN | Ghi chú |
|---|---|---|---|---|
| Khoa học máy tính | 01 cấp bộ + 02 cấp trường | 05 | 04 | Chủ trì hội thảo |
| Hệ thống thông tin | 01 cấp bộ + 02 cấp trường | 03 | 04 | — |
| Mạng máy tính & ATTT | 01 cấp trường | 02 | 02 | Hướng ATTT |

IV. TIẾN ĐỘ THỰC HIỆN
- Q4/2027: đăng ký 02 đề tài cấp bộ; sơ kết NCKH sinh viên đợt 1.
- Q1/2028: đăng ký 05 đề tài cấp trường; các bộ môn gửi kế hoạch bộ môn về khoa.
- Q2/2028: tổ chức 01 hội thảo quốc tế; tổng kết NCKH sinh viên, xét giải cấp bộ.
- Q3/2028: nghiệm thu 02 giáo trình; sơ kết 6 tháng, điều chỉnh chỉ tiêu nếu cần.
- Rải đều 4 quý: công bố 10 bài báo quốc tế, 10 bài báo trong nước.

V. KINH PHÍ
- Nguồn trường: 600 triệu đồng (đề tài cấp trường, hội thảo, hỗ trợ bài báo).
- Nguồn ngoài: đề tài cấp bộ và hợp tác doanh nghiệp (dự kiến 1,2 tỷ đồng).

VI. TỔ CHỨC THỰC HIỆN
- Các bộ môn cụ thể hóa thành kế hoạch bộ môn, gửi về khoa trước 30/11/2027.
- Trợ lý NCKH khoa theo dõi tiến độ hằng quý, báo cáo trưởng khoa.
- Kết quả NCKH là tiêu chí đánh giá thi đua của bộ môn và cá nhân.

Nơi nhận:                                        TRƯỞNG KHOA
- Ban Giám hiệu (báo cáo);                            (đã ký)
- Phòng KHCN (tổng hợp);
- Các bộ môn (thực hiện);
- Lưu: VT khoa.

                                              TS. Phạm Văn B
```

## Căn cứ & lưu ý
- Chiến lược phát triển khoa học công nghệ của Trường Đại học A (giả lập).
- Chỉ tiêu NCKH gắn với đánh giá thi đua và là minh chứng cho tiêu chí về NCKH
  trong kiểm định chất lượng.
- Khuyến khích đề tài gắn với doanh nghiệp, địa phương để tăng tính ứng dụng
  và nguồn kinh phí ngoài ngân sách.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
