---
name: ke-hoach-nam-hoc-truong
description: Xây dựng kế hoạch năm học toàn trường đại học (nhiệm vụ trọng tâm, chỉ tiêu các mảng, phân công đơn vị, tiến độ). Dùng khi Văn phòng tổng hợp kế hoạch năm học mới từ kế hoạch của các đơn vị.
---

# Skill: Lập kế hoạch năm học toàn trường

## Khi nào dùng
Khi xây dựng kế hoạch năm học mới (trước khi năm học bắt đầu); khi điều chỉnh kế hoạch
giữa năm học.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `nam_hoc` | Năm học (VD: 2026–2027) | Có |
| `nhiem_vu_trong_tam` | Các nhiệm vụ trọng tâm do Ban Giám hiệu xác định | Có |
| `ke_hoach_don_vi` | Kế hoạch của các phòng, khoa, trung tâm | Có |
| `chi_tieu` | Chỉ tiêu cụ thể từng mảng (tuyển sinh, NCKH, kiểm định...) | Không |

## Quy trình

**Bước 1. Tổng hợp định hướng và chốt nhiệm vụ trọng tâm**
- Làm gì: Thu thập định hướng phát triển của trường, chỉ đạo của cơ quan chủ quản/Bộ
  GD&ĐT cho năm học mới; đề xuất danh sách nhiệm vụ trọng tâm (thường 3–5 nhiệm vụ);
  lấy ý kiến Ban Giám hiệu và chốt danh sách chính thức.
- Dùng input: `nam_hoc`, `nhiem_vu_trong_tam`
- Vai trò: Ban Giám hiệu · AI hỗ trợ: tổng hợp định hướng và đề xuất danh sách nhiệm vụ trọng tâm, Ban Giám hiệu chốt · ⏱ 2–3 ngày làm việc (lấy ý kiến) (ước tính)
- Lưu ý nghiệp vụ: Nhiệm vụ trọng tâm không nên quá 5 — càng nhiều "trọng tâm" thì
  càng không có trọng tâm; mỗi nhiệm vụ trọng tâm phải có sản phẩm/chỉ tiêu đo được,
  tránh nhiệm vụ dạng khẩu hiệu.
- → Kết quả bước: Danh sách nhiệm vụ trọng tâm năm học đã được Ban Giám hiệu chốt.

**Bước 2. Thu thập kế hoạch các đơn vị**
- Làm gì: Gửi văn bản yêu cầu các phòng, khoa, trung tâm gửi kế hoạch năm học của
  đơn vị (kèm biểu mẫu: nhiệm vụ, chỉ tiêu, thời gian); đôn đốc, tiếp nhận; lập bảng
  rà soát: phát hiện nhiệm vụ trùng lặp giữa các đơn vị, nhiệm vụ không gắn với nhiệm
  vụ trọng tâm.
- Dùng input: `ke_hoach_don_vi`
- Vai trò: Chuyên viên Văn phòng · AI hỗ trợ: hỗ trợ soạn văn bản và lập bảng rà soát trùng lặp, Văn phòng đôn đốc các đơn vị gửi kế hoạch · ⏱ 1–2 tuần (chờ đơn vị) (ước tính)
- Lưu ý nghiệp vụ: Trùng lặp nhiệm vụ giữa các đơn vị là chuyện thường (VD: cả Đào
  tạo và các khoa cùng đăng ký "xây dựng ngân hàng đề thi") — phải gộp và phân rõ
  chủ trì/phối hợp ngay ở bước này; đơn vị nào chưa gửi thì nhắc trước hạn 7 ngày.
- → Kết quả bước: Tập hợp kế hoạch các đơn vị + bảng rà soát trùng lặp.

**Bước 3. Sắp xếp nhiệm vụ theo 6 mảng công tác**
- Làm gì: Gom các nhiệm vụ đơn vị theo 6 mảng: (1) Đào tạo; (2) KHCN & HTQT;
  (3) Công tác sinh viên; (4) Tổ chức cán bộ; (5) Tài chính, CSVC; (6) Đảm bảo chất
  lượng; loại bỏ nhiệm vụ trùng lặp, gộp nhiệm vụ tương đồng; kiểm tra mỗi nhiệm vụ
  trọng tâm (Bước 1) đều có nhiệm vụ cụ thể đỡ đầu.
- Dùng input: `nhiem_vu_trong_tam`
- Vai trò: Chuyên viên Văn phòng · AI hỗ trợ: gom, loại trùng lặp và sắp xếp nhiệm vụ theo 6 mảng, Văn phòng kiểm tra kết quả · ⏱ 1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Nhiệm vụ trọng tâm nào không có nhiệm vụ cụ thể đi kèm thì phải
  bổ sung — nếu không kế hoạch sẽ "treo" nhiệm vụ trọng tâm trên giấy; giữ mỗi nhiệm
  vụ một dòng mô tả ngắn gọn, chi tiết để sang Bước 4.
- → Kết quả bước: Bảng nhiệm vụ phân theo 6 mảng (đã loại trùng lặp).

**Bước 4. Giao chỉ tiêu và phân công cụ thể**
- Làm gì: Với từng nhiệm vụ, ghi rõ 5 yếu tố: đơn vị chủ trì, đơn vị phối hợp, thời
  gian hoàn thành, sản phẩm đầu ra, chỉ tiêu đo lường (lấy từ `chi_tieu` nếu có);
  kiểm tra không có nhiệm vụ "vô chủ" (thiếu đơn vị chủ trì) và không có đơn vị bị
  quá tải (một đơn vị chủ trì quá nhiều nhiệm vụ lớn cùng kỳ).
- Dùng input: `chi_tieu`
- Vai trò: Ban Giám hiệu · AI hỗ trợ: lập bảng phân công dự thảo (chủ trì/phối hợp/thời gian/sản phẩm), Ban Giám hiệu quyết định phân công · ⏱ 3–5 giờ (ước tính)
- Lưu ý nghiệp vụ: Nguyên tắc "một nhiệm vụ — một chủ trì": nhiệm vụ có 2 đơn vị
  cùng chủ trì thì khi chậm tiến độ không ai chịu trách nhiệm; thời gian hoàn thành
  phải cụ thể đến tháng, tránh ghi "cả năm" cho nhiệm vụ có thể chia mốc.
- → Kết quả bước: Bảng nhiệm vụ chi tiết (STT, nhiệm vụ, chủ trì, phối hợp, thời gian,
  sản phẩm, chỉ tiêu).

**Bước 5. Hoàn thiện văn bản kế hoạch và tờ trình**
- Làm gì: Soạn thảo văn bản kế hoạch đầy đủ 3 phần: I. Nhiệm vụ trọng tâm; II. Nhiệm
  vụ cụ thể (bảng chi tiết từ Bước 4); III. Tổ chức thực hiện (trách nhiệm các đơn vị,
  chế độ báo cáo tiến độ hằng quý); soạn tờ trình ban hành kế hoạch; kiểm tra tính
  nhất quán giữa các phần.
- Dùng input: `nam_hoc`
- Vai trò: Chuyên viên Văn phòng · AI hỗ trợ: soạn dự thảo văn bản kế hoạch và tờ trình · ⏱ 3–5 giờ (ước tính)
- Lưu ý nghiệp vụ: Phần III không được viết cho có — phải quy định rõ đơn vị nào báo
  cáo tiến độ cho ai, định kỳ nào, theo mẫu nào; nếu không kế hoạch ban hành xong sẽ
  không ai theo dõi; kiểm tra tổng chỉ tiêu trong bảng khớp với chỉ tiêu đã chốt.
- → Kết quả bước: Bản thảo kế hoạch năm học + tờ trình ban hành.

**Bước 6. Trình phê duyệt và ban hành**
- Làm gì: Trình Ban Giám hiệu duyệt; trình Hội đồng trường thông qua (nếu quy định
  yêu cầu); ban hành kế hoạch kèm quyết định; gửi đến tất cả đơn vị; các đơn vị cụ
  thể hóa thành kế hoạch của đơn vị mình.
- Dùng input: (không dùng trường input mới)
- Vai trò: Hội đồng chuyên môn · AI hỗ trợ: chuẩn bị dự thảo, tài liệu và số liệu phục vụ bước này · ⏱ 1–2 tuần (ước tính)
- Lưu ý nghiệp vụ: Kế hoạch phải ban hành trước khi năm học bắt đầu đủ sớm (ít nhất
  2–4 tuần) để đơn vị kịp triển khai; lưu quyết định ban hành kèm kế hoạch thành một
  bộ hồ sơ để tra cứu, kiểm tra sau này.
- → Kết quả bước: Kế hoạch năm học toàn trường đã ban hành + quyết định ban hành.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Định hướng trường, kế hoạch các đơn vị"/] --> B["Bước 1. Tổng hợp định hướng, chốt nhiệm vụ trọng tâm"]
    B --> C["Bước 2. Thu thập kế hoạch các đơn vị, rà soát trùng lặp"]
    C --> D["Bước 3. Sắp xếp nhiệm vụ theo 6 mảng công tác"]
    D --> E["Bước 4. Giao chỉ tiêu: chủ trì, phối hợp, thời gian, sản phẩm"]
    E --> F["Bước 5. Hoàn thiện văn bản kế hoạch, tờ trình"]
    F --> HG["👤 Bước 6. Ban Giám hiệu duyệt, Hội đồng trường thông qua"]
    HG --> G["Ban hành kế hoạch kèm quyết định"]
    G --> H[/"Kế hoạch năm học, tờ trình, quyết định ban hành"/]
```

## Đầu ra (Output)
- Kế hoạch năm học toàn trường (bảng nhiệm vụ chi tiết).
- Tờ trình / quyết định ban hành kế hoạch.

**Cấu trúc output chuẩn** (sản phẩm chính: Kế hoạch năm học toàn trường) — các phần
bắt buộc theo đúng thứ tự:
1. Tên trường (tiêu đề).
2. Tiêu đề: KẾ HOẠCH NĂM HỌC ...
3. Phần I. NHIỆM VỤ TRỌNG TÂM (3–5 nhiệm vụ, có chỉ tiêu/sản phẩm đo được).
4. Phần II. NHIỆM VỤ CỤ THỂ — bảng chi tiết với đúng 6 cột theo thứ tự: STT |
   Nhiệm vụ | Đơn vị chủ trì | Đơn vị phối hợp | Thời gian hoàn thành | Sản phẩm
   (kèm chỉ tiêu đo lường).
5. Phần III. TỔ CHỨC THỰC HIỆN (trách nhiệm các đơn vị, chế độ báo cáo tiến độ
   hằng quý về đầu mối tổng hợp).
6. Chữ ký Hiệu trưởng (họ tên, học hàm/học vị).
7. Tờ trình / Quyết định ban hành kế hoạch (văn bản kèm theo).

## Checklist nghiệm thu

- [ ] Đủ các phần của "Cấu trúc output chuẩn": tiêu đề, Phần I/II/III, chữ ký Hiệu trưởng, tờ trình/quyết định ban hành.
- [ ] Bảng Phần II có đúng 6 cột theo đúng thứ tự: STT | Nhiệm vụ | Đơn vị chủ trì | Đơn vị phối hợp | Thời gian hoàn thành | Sản phẩm.
- [ ] Nội dung khớp với Input: 3–5 nhiệm vụ trọng tâm, chỉ tiêu, kế hoạch của các đơn vị.
- [ ] Mỗi nhiệm vụ có đúng một đơn vị chủ trì; không có nhiệm vụ "vô chủ"; không có đơn vị bị quá tải.
- [ ] Mọi nhiệm vụ trọng tâm đều có nhiệm vụ cụ thể đỡ đầu; nhiệm vụ trùng lặp đã gộp và phân rõ chủ trì/phối hợp.
- [ ] Thời gian hoàn thành cụ thể đến tháng; chỉ tiêu đo lường được.
- [ ] Đúng thể thức: số ký hiệu, ngày tháng, chữ ký Hiệu trưởng, quyết định ban hành kèm theo.
- [ ] Đã qua Human gate: Ban Giám hiệu duyệt (và Hội đồng trường thông qua nếu quy định yêu cầu); kế hoạch đã gửi đến tất cả đơn vị.
- [ ] Kế hoạch ban hành trước năm học ít nhất 2–4 tuần để đơn vị kịp triển khai.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `nam_hoc` | 2026–2027 |
| `nhiem_vu_trong_tam` | 1. Kiểm định 06 CTĐT. 2. Mở 02 ngành mới. 3. Chuyển đổi số quản trị. |
| `ke_hoach_don_vi` | Đào tạo: tuyển sinh 2.600; KHCN: 50 đề tài; CTSV: 350 suất HB; ĐBCL: kiểm định 6 CTĐT |
| `chi_tieu` | Tuyển sinh ≥100% chỉ tiêu; 45 bài báo quốc tế |

### Output mẫu (trích)

```
TRƯỜNG ĐẠI HỌC A
KẾ HOẠCH NĂM HỌC 2026–2027
(Dữ liệu giả lập)

I. NHIỆM VỤ TRỌNG TÂM
1. Hoàn thành kiểm định chất lượng 06 chương trình đào tạo.
2. Mở 02 ngành đào tạo mới đáp ứng nhu cầu xã hội.
3. Đẩy mạnh chuyển đổi số trong quản trị và đào tạo.

II. NHIỆM VỤ CỤ THỂ

| STT | Nhiệm vụ | Đơn vị chủ trì | Phối hợp | Thời gian | Sản phẩm |
|-----|----------|----------------|----------|-----------|----------|
| 1 | Tuyển sinh đạt ≥100% chỉ tiêu (2.600) | P. Đào tạo | Các khoa | T9/2026 | Báo cáo TS |
| 2 | Xây dựng đề án mở 02 ngành mới | P. Đào tạo | Khoa liên quan | T12/2026 | Đề án |
| 3 | Triển khai 50 đề tài NCKH | P. KHCN | Các khoa | Cả năm | QĐ giao ĐT |
| 4 | Công bố 45 bài báo quốc tế | P. KHCN | Các khoa | Cả năm | Danh mục |
| 5 | Kiểm định 06 CTĐT | P. KT&ĐBCL | Các khoa | T6/2027 | GCN kiểm định |
| 6 | Cấp 350 suất học bổng | P. CTSV | P. TCKT | Theo học kỳ | QĐ học bổng |
| 7 | Vận hành hệ thống quản trị số giai đoạn 2 | TT CNTT | Các đơn vị | T3/2027 | Hệ thống |

III. TỔ CHỨC THỰC HIỆN
Các đơn vị cụ thể hóa thành kế hoạch của đơn vị mình, báo cáo tiến độ hằng quý
về Phòng Hành chính – Tổng hợp để tổng hợp báo cáo Ban Giám hiệu.

HIỆU TRƯỞNG (đã ký)
PGS.TS. Phạm Văn A
```

## Căn cứ & lưu ý
- Chiến lược phát triển của trường; chỉ đạo của cơ quan chủ quản, Bộ GD&ĐT.
- Kế hoạch phải gắn chỉ tiêu đo lường được và đơn vị chịu trách nhiệm cụ thể.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
