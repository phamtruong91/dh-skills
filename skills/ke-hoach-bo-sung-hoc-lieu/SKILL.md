---
name: ke-hoach-bo-sung-hoc-lieu
description: Lập kế hoạch bổ sung và số hóa học liệu của thư viện trường đại học theo nhu cầu đào tạo của các khoa: sách, giáo trình, cơ sở dữ liệu điện tử, tài liệu số hóa. Dùng khi xây dựng kế hoạch phát triển vốn tài liệu hằng năm.
---

# Skill: Kế hoạch bổ sung, số hóa học liệu

## Khi nào dùng
Khi thư viện cần lập kế hoạch mua sắm, tiếp nhận và số hóa học liệu phục vụ
chương trình đào tạo, nghiên cứu khoa học trong năm.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `nam_ke_hoach` | Năm kế hoạch | Có |
| `nhu_cau_cac_khoa` | Bảng nhu cầu học liệu do các khoa đề xuất (tên tài liệu, số lượng, phục vụ học phần nào) | Có |
| `hinh_thuc_bo_sung` | Mua mới / Số hóa / Tiếp nhận tài trợ / Mua quyền truy cập CSDL | Có |
| `ngan_sach` | Ngân sách dự kiến | Không |
| `chi_tieu_so_hoa` | Số đầu tài liệu số hóa trong năm | Không |

## Quy trình

**Bước 1. Thu thập và tổng hợp nhu cầu từ các khoa**
- Làm gì: Thu phiếu đề xuất của các khoa: tên tài liệu, tác giả/NXB, số lượng, phục vụ
  học phần/CTĐT nào, lý do đề xuất; gộp các đề xuất trùng nhau giữa các khoa (cộng dồn
  số lượng); trả lại đề xuất thiếu thông tin để khoa bổ sung.
- Dùng input: `nam_ke_hoach`, `nhu_cau_cac_khoa`.
- Vai trò: Cán bộ Thư viện · AI hỗ trợ: soạn biểu mẫu và tổng hợp đề xuất, các khoa cung cấp nhu cầu và bổ sung thông tin thiếu · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: mỗi đề xuất phải gắn với học phần/CTĐT cụ thể — đề xuất chung chung
  kiểu "sách tham khảo ngành" thì yêu cầu khoa làm rõ; đặt hạn chót nhận đề xuất để kịp
  tiến độ lập kế hoạch năm.
- → Kết quả bước: Bảng tổng hợp nhu cầu (đã gộp trùng, phân theo khoa, gắn học phần).

**Bước 2. Đối chiếu với vốn tài liệu hiện có**
- Làm gì: Tra cứu từng đầu tài liệu trong hệ thống quản lý thư viện: đã có chưa, có bao
  nhiêu bản, tình trạng bản in (còn mới/cũ nát), đã có bản điện tử/quyền CSDL chưa; đánh
  dấu từng đầu: "đã có đủ" (loại), "có nhưng thiếu bản" (giữ lại với số lượng bổ sung),
  "chưa có" (giữ lại).
- Dùng input: `nhu_cau_cac_khoa` + bảng tổng hợp (kết quả bước 1).
- Vai trò: Cán bộ Thư viện · AI hỗ trợ: tra cứu hệ thống ILS và đánh dấu giữ/loại, thủ thư kiểm tra trường hợp tên khác cùng nội dung · ⏱ 2–4 giờ (ước tính)
- Lưu ý nghiệp vụ: kiểm tra cả trường hợp tên khác nhau nhưng cùng nội dung (tái bản,
  bản dịch khác); tài liệu đã có bản điện tử đầy đủ thì ưu tiên không mua bản in trùng;
  ghi rõ căn cứ loại trừ để giải trình với khoa.
- → Kết quả bước: Bảng đối chiếu (tài liệu × tình trạng hiện có × quyết định giữ/loại).

**Bước 3. Phân loại hình thức bổ sung**
- Làm gì: Với từng tài liệu còn lại sau bước 2, xếp vào một trong các hình thức
  (`hinh_thuc_bo_sung`): mua mới (sách/giáo trình in), số hóa (tài liệu nội sinh, luận
  văn, tài liệu quý hiếm), mua quyền truy cập CSDL điện tử, tiếp nhận tài trợ/tặng; ghi
  lý do chọn hình thức cho từng nhóm.
- Dùng input: `hinh_thuc_bo_sung`, `chi_tieu_so_hoa` (giới hạn số đầu số hóa trong năm).
- Vai trò: Cán bộ Thư viện · AI hỗ trợ: gợi ý phân loại hình thức bổ sung, thư viện quyết định hình thức cho từng nhóm · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chỉ số hóa tài liệu thuộc quyền của trường hoặc được phép (tuân thủ
  pháp luật SHTT); CSDL mua quyền phải kiểm tra trùng lặp với CSDL đã mua các năm trước;
  tài liệu nội sinh (giáo trình, luận văn của trường) ưu tiên số hóa thay vì mua.
- → Kết quả bước: Danh mục tài liệu đã phân loại theo hình thức bổ sung.

**Bước 4. Xếp thứ tự ưu tiên**
- Làm gì: Chấm ưu tiên từng nhóm tài liệu theo tiêu chí: phục vụ ngành đào tạo mới, học
  phần chưa có tài liệu chính, lượt mượn/truy cập cao, tài liệu quý có nguy cơ hư hỏng
  (đối với số hóa); sắp xếp danh mục theo thứ tự ưu tiên để có căn cứ cắt giảm khi ngân
  sách không đủ.
- Dùng input: `ngan_sach` (mức ngân sách → xác định ranh giới cắt), `nhu_cau_cac_khoa`.
- Vai trò: Giám đốc Thư viện · AI hỗ trợ: chấm điểm ưu tiên theo tiêu chí · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: ranh giới "ngân sách đáp ứng đến đâu" phải rõ ràng — khi bị cắt giảm
  thì cắt từ cuối danh sách; ưu tiên phải có căn cứ số liệu (lượt mượn, học phần thiếu
  tài liệu), không theo cảm tính.
- → Kết quả bước: Danh mục đã xếp hạng ưu tiên (có vạch cắt theo ngân sách).

**Bước 5. Lập danh mục chi tiết và dự toán kinh phí**
- Làm gì: Lập bảng danh mục cuối cùng: tên tài liệu, hình thức, số lượng, đơn giá dự kiến,
  thành tiền; tính tổng dự toán theo từng hình thức và tổng chung; đối chiếu với
  `ngan_sach` — nếu vượt thì cắt theo thứ tự ưu tiên bước 4 và ghi rõ phần chưa thực hiện
  được chuyển sang năm sau.
- Dùng input: `ngan_sach`.
- Vai trò: Cán bộ Thư viện · AI hỗ trợ: lập bảng danh mục và tính dự toán, thư viện đối chiếu ngân sách và chốt phần cắt · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: đơn giá dự kiến lấy từ báo giá nhà cung cấp hoặc giá mua năm trước +
  trượt giá; dự toán tách rõ từng hình thức để lãnh đạo dễ phê duyệt từng phần; phần bị
  cắt phải có danh sách dự phòng cho năm sau.
- → Kết quả bước: Bảng danh mục chi tiết + dự toán kinh phí (đã đối chiếu ngân sách).

**Bước 6. Soạn thảo văn bản kế hoạch và trình phê duyệt**
- Làm gì: Soạn văn bản kế hoạch theo cấu trúc chuẩn (mục tiêu, nội dung theo từng hình
  thức, tiến độ quý, tổ chức thực hiện); đính kèm danh mục + dự toán (kết quả bước 5);
  trình Giám đốc thư viện ký và Hiệu trưởng phê duyệt; sau phê duyệt, giao nhiệm vụ triển
  khai theo tiến độ quý.
- Dùng input: `nam_ke_hoach` (năm kế hoạch trong văn bản).
- Vai trò: Giám đốc Thư viện · AI hỗ trợ: soạn văn bản đúng thể thức · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: văn bản phải đủ thể thức (số hiệu, ngày ban hành, nơi nhận); kế hoạch
  năm phải ban hành trước quý 1 để kịp triển khai đợt mua sắm đầu năm.
- → Kết quả bước: Văn bản kế hoạch bổ sung, số hóa học liệu đã được phê duyệt.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/Đề xuất học liệu từ các khoa/] --> B["Bước 1. Thu thập và tổng hợp nhu cầu từ các khoa"]
    B --> C["Bước 2. Đối chiếu với vốn tài liệu hiện có"]
    C --> D{"Đã có đủ tài liệu này?"}
    D -->|Có đủ| E["Loại khỏi danh mục"]
    D -->|Chưa có hoặc thiếu| F["Bước 3. Phân loại hình thức bổ sung"]
    F --> G["Bước 4. Xếp thứ tự ưu tiên"]
    G --> H["Bước 5. Lập danh mục chi tiết và dự toán kinh phí"]
    H --> I["Bước 6. Soạn thảo văn bản kế hoạch và trình phê duyệt"]
    I --> J["👤 Giám đốc thư viện trình Hiệu trưởng phê duyệt"]
    J --> K[/Kế hoạch bổ sung học liệu ban hành/]
```

## Đầu ra (Output)
- Văn bản kế hoạch bổ sung, số hóa học liệu hoàn chỉnh.
- Bảng danh mục học liệu + dự toán kinh phí.

**Cấu trúc output chuẩn** (văn bản kế hoạch bổ sung, số hóa học liệu — các phần theo
đúng thứ tự):
1. Tiêu đề hành chính: tên trường, tên đơn vị, quốc hiệu, số hiệu văn bản, địa danh và
   ngày ban hành.
2. Tên kế hoạch + năm kế hoạch.
3. Mục tiêu: số lượng theo từng hình thức bổ sung, chuẩn đầu ra (VD: 100% học phần có
   ít nhất 01 tài liệu chính).
4. Nội dung: chi tiết theo từng hình thức (mua mới, mua quyền CSDL, số hóa, tiếp nhận
   tài trợ) — kèm bảng danh mục và dự toán từng hình thức.
5. Tiến độ thực hiện theo quý.
6. Tổ chức thực hiện: phân công trách nhiệm từng đơn vị.
7. Nơi nhận + chữ ký (giám đốc thư viện, ghi rõ họ tên).

## Checklist nghiệm thu

- [ ] Đủ 7 phần theo "Cấu trúc output chuẩn": tiêu đề hành chính, tên kế hoạch + năm, mục tiêu, nội dung theo hình thức, tiến độ theo quý, tổ chức thực hiện, nơi nhận + chữ ký.
- [ ] Danh mục và dự toán khớp với Input: nhu cầu các khoa, ngân sách, chỉ tiêu số hóa.
- [ ] Không bịa đặt đơn giá, báo giá nhà cung cấp hay nhu cầu không có trong đề xuất của khoa.
- [ ] Mỗi đề xuất gắn với học phần/CTĐT cụ thể; đã gộp các đề xuất trùng nhau giữa các khoa.
- [ ] Đã đối chiếu vốn tài liệu hiện có: đầu đã có đủ bị loại có ghi căn cứ; phát hiện trường hợp tên khác nhưng cùng nội dung.
- [ ] Danh mục xếp ưu tiên có vạch cắt rõ theo ngân sách; phần bị cắt có danh sách dự phòng cho năm sau.
- [ ] Số hóa chỉ với tài liệu thuộc quyền của trường hoặc được phép (tuân thủ pháp luật sở hữu trí tuệ).
- [ ] Đúng thể thức: số hiệu văn bản, ngày ban hành, nơi nhận đầy đủ.
- [ ] Đã qua Human gate: giám đốc thư viện ký, hiệu trưởng phê duyệt kế hoạch.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `nam_ke_hoach` | 2027 |
| `nhu_cau_cac_khoa` | 04 khoa đề xuất 320 đầu sách, 15 CSDL, 500 luận văn cần số hóa |
| `hinh_thuc_bo_sung` | Mua mới + số hóa + mua quyền CSDL |
| `ngan_sach` | 2,2 tỷ đồng |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A            CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
THƯ VIỆN                                        Độc lập – Tự do – Hạnh phúc
      Số: 08/KH-ĐHA-TV
                                                 Thành phố C, ngày 09 tháng 10 năm 2026

KẾ HOẠCH
Bổ sung và số hóa học liệu năm 2027

I. MỤC TIÊU
Bổ sung 320 đầu sách, 15 cơ sở dữ liệu điện tử; số hóa 500 luận văn, luận án;
đáp ứng 100% học phần có ít nhất 01 giáo trình/tài liệu tham khảo chính.

II. NỘI DUNG

1. Mua mới tài liệu in (dự kiến 1,2 tỷ đồng):

| Khoa | Số đầu sách | Phục vụ | Kinh phí (tr.đ) |
|---|---|---|---|
| Công nghệ thông tin | 95 | Ngành CNTT, AI (mở mới 2026) | 380 |
| Kinh tế | 80 | Kế toán, QTKD | 320 |
| Ngoại ngữ | 70 | Ngôn ngữ Anh | 280 |
| Khoa học cơ bản | 75 | Toán, Lý đại cương | 220 |

2. Mua quyền truy cập CSDL điện tử (dự kiến 700 triệu đồng):
   - 10 CSDL tạp chí khoa học quốc tế; 05 CSDL sách điện tử tiếng Việt.

3. Số hóa tài liệu (dự kiến 300 triệu đồng):
   - Số hóa 500 luận văn thạc sĩ, luận án tiến sĩ bảo vệ năm 2024–2026;
   - Số hóa 50 giáo trình nội bộ của trường.

III. TIẾN ĐỘ
- Quý 1: hoàn thành mua sắm đợt 1 (50% danh mục).
- Quý 2–3: số hóa tài liệu; mua sắm đợt 2.
- Quý 4: nghiệm thu, tổng kết, báo cáo.

IV. TỔ CHỨC THỰC HIỆN
- Thư viện: đầu mối, chịu trách nhiệm toàn bộ kế hoạch.
- Các khoa: phối hợp lựa chọn danh mục, nghiệm thu nội dung chuyên môn.
- Phòng Tài chính – Kế toán: bố trí kinh phí theo tiến độ.

Nơi nhận:                                         GIÁM ĐỐC THƯ VIỆN
- Ban Giám hiệu (phê duyệt);                           (đã ký)
- Các khoa; P. TCKT;
- Lưu: VT, TV.

                                                  ThS. Hoàng Thị D
```

## Căn cứ & lưu ý
- Chiến lược phát triển Trường Đại học A (giả lập); quy định về công tác
  thư viện trường đại học.
- Ưu tiên học liệu phục vụ ngành mở mới và học phần chưa có tài liệu chính.
- Tuân thủ pháp luật sở hữu trí tuệ khi số hóa tài liệu (chỉ số hóa tài liệu thuộc
  quyền của trường hoặc được phép).
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
