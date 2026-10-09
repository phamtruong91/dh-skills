---
name: bao-cao-tong-ket-nam-truong
description: Tổng hợp báo cáo tổng kết năm học toàn trường đại học từ báo cáo của các phòng ban, khoa (đào tạo, NCKH, CTSV, TCCB, tài chính, CSVC, HTQT). Dùng khi Văn phòng / Phòng HCTH tổng hợp báo cáo tổng kết năm học.
---

# Skill: Soạn báo cáo tổng kết năm học toàn trường

## Khi nào dùng
Khi tổng hợp báo cáo tổng kết năm học để trình Hội nghị cán bộ viên chức, báo cáo
cơ quan chủ quản, Bộ GD&ĐT.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `nam_hoc` | Năm học (VD: 2025–2026) | Có |
| `bao_cao_don_vi` | Báo cáo / số liệu của các phòng, khoa, trung tâm theo từng mảng | Có |
| `dinh_huong_chung` | Định hướng, chỉ đạo của Ban Giám hiệu cho năm học | Không |

## Quy trình

**Bước 1. Xây dựng đề cương báo cáo**
- Làm gì: Dựng đề cương chi tiết với 6 mảng cố định: (1) Công tác đào tạo (tuyển sinh,
  CTĐT, học vụ, tốt nghiệp); (2) KHCN & hợp tác quốc tế; (3) Công tác sinh viên;
  (4) Tổ chức cán bộ, thi đua khen thưởng; (5) Tài chính, cơ sở vật chất; (6) Đảm bảo
  chất lượng, kiểm định. Với mỗi mảng, liệt kê các chỉ số bắt buộc phải có và biểu
  mẫu số liệu đính kèm; lấy ý kiến Ban Giám hiệu về định hướng, điểm nhấn của năm học.
- Dùng input: `nam_hoc`, `dinh_huong_chung`
- Vai trò: Ban Giám hiệu · AI hỗ trợ: dựng đề cương 6 mảng và biểu mẫu số liệu, Văn phòng trình Ban Giám hiệu chốt định hướng · ⏱ 3–5 giờ (ước tính)
- Lưu ý nghiệp vụ: Đề cương là "hợp đồng" với các đơn vị — càng chi tiết, số liệu thu
  về càng đồng đều, tránh mỗi đơn vị báo cáo một kiểu; chốt đề cương sớm (trước ít
  nhất 1 tháng so với hạn báo cáo) để đơn vị có thời gian chuẩn bị.
- → Kết quả bước: Đề cương báo cáo chi tiết 6 mảng (kèm biểu mẫu số liệu từng mảng).

**Bước 2. Gửi đề cương và thu thập báo cáo đơn vị**
- Làm gì: Gửi đề cương + biểu mẫu + thời hạn nộp đến tất cả phòng, khoa, trung tâm;
  đôn đốc các đơn vị nộp đúng hạn; tiếp nhận báo cáo/số liệu từng đơn vị; lập bảng
  theo dõi tiến độ nộp.
- Dùng input: `bao_cao_don_vi`
- Vai trò: Chuyên viên Văn phòng · AI hỗ trợ: hỗ trợ soạn văn bản, lập bảng theo dõi tiến độ nộp, Văn phòng đôn đốc và tiếp nhận báo cáo đơn vị · ⏱ 1–2 tuần (chờ đơn vị nộp) (ước tính)
- Lưu ý nghiệp vụ: Đơn vị nộp muộn là chuyện thường — gửi nhắc trước hạn 7 ngày và
  3 ngày; khi nhận báo cáo, kiểm tra ngay tính đầy đủ (có đủ các chỉ số trong đề cương
  không), thiếu thì yêu cầu bổ sung ngay, không để dồn đến lúc tổng hợp.
- → Kết quả bước: Tập hợp báo cáo/số liệu các đơn vị + bảng theo dõi tiến độ nộp.

**Bước 3. Tổng hợp theo mảng, chuẩn hóa số liệu**
- Làm gì: Gom số liệu các đơn vị theo 6 mảng; loại bỏ trùng lặp (nhiều đơn vị cùng
  báo một hoạt động); chuẩn hóa đơn vị tính và mốc thời gian; đối chiếu chéo số liệu
  liên quan giữa các đơn vị (VD: số SV tốt nghiệp của Đào tạo với số liệu việc làm
  của CTSV); yêu cầu đơn vị xác nhận lại các chênh lệch.
- Dùng input: `bao_cao_don_vi`
- Vai trò: Chuyên viên Văn phòng · AI hỗ trợ: gom số liệu, loại trùng lặp, chuẩn hóa đơn vị tính và đối chiếu chéo · ⏱ 2–4 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Số liệu tổng hợp phải thống nhất một mốc thời gian (VD: tính đến
  31/7); chênh lệch chưa giải trình được thì không đưa vào báo cáo chính thức; ghi rõ
  nguồn số liệu từng dòng để truy xuất khi Ban Giám hiệu hỏi.
- → Kết quả bước: Bảng số liệu tổng hợp 6 mảng đã chuẩn hóa, đối chiếu nhất quán.

**Bước 4. Viết phần kết quả, nêu bật điểm nổi bật**
- Làm gì: Viết phần I (Kết quả thực hiện các mặt công tác) theo 6 mảng; rút gọn số
  liệu đơn vị thành các con số tổng hợp cấp trường; nêu bật kết quả nổi bật, điểm sáng
  (vượt chỉ tiêu, lần đầu đạt được, được cấp trên ghi nhận) bằng gạch đầu dòng có số
  liệu minh chứng; trình bày bảng biểu tổng hợp.
- Dùng input: (xử lý trên số liệu tổng hợp từ Bước 3)
- Vai trò: Chuyên viên Văn phòng · AI hỗ trợ: viết dự thảo Phần I theo 6 mảng kèm bảng biểu · ⏱ 1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Báo cáo cấp trường phải có "tầm" — tránh liệt kê vụn vặt kiểu cộng
  gộp báo cáo đơn vị; mỗi nhận định tích cực phải có số liệu đi kèm; số liệu so sánh
  với năm trước giúp Ban Giám hiệu thấy xu hướng.
- → Kết quả bước: Bản thảo Phần I (kết quả 6 mảng) với bảng biểu tổng hợp.

**Bước 5. Đánh giá tồn tại, hạn chế và nguyên nhân**
- Làm gì: Đối chiếu kết quả với kế hoạch/mục tiêu đầu năm học để xác định tồn tại,
  hạn chế; phân tích nguyên nhân khách quan và chủ quan cho từng tồn tại chính; viết
  Phần II (Tồn tại, hạn chế) ngắn gọn, thẳng thắn.
- Dùng input: `dinh_huong_chung`
- Vai trò: Ban Giám hiệu · AI hỗ trợ: đề xuất tồn tại từ đối chiếu kế hoạch đầu năm, Ban Giám hiệu quyết định nội dung Phần II · ⏱ 3–5 giờ (ước tính)
- Lưu ý nghiệp vụ: Tồn tại phải nói thẳng — báo cáo trình Hội nghị CBVC và cấp trên
  mà "toàn ưu điểm" sẽ mất uy tín; không đổ lỗi chung chung ("do khách quan"), mỗi
  tồn tại cần nguyên nhân cụ thể để phần phương hướng có cơ sở đề xuất giải pháp.
- → Kết quả bước: Bản thảo Phần II (tồn tại, hạn chế + nguyên nhân).

**Bước 6. Xây dựng phương hướng năm học tới**
- Làm gì: Căn cứ định hướng của Ban Giám hiệu và các tồn tại đã xác định, xây dựng
  Phần III: nhiệm vụ trọng tâm, chỉ tiêu cụ thể từng mảng, giải pháp thực hiện; mỗi
  nhiệm vụ gắn đơn vị chủ trì và thời gian hoàn thành.
- Dùng input: `dinh_huong_chung`
- Vai trò: Ban Giám hiệu · AI hỗ trợ: soạn dự thảo Phần III (nhiệm vụ, chỉ tiêu, giải pháp), Ban Giám hiệu chốt phương hướng · ⏱ 3–5 giờ (ước tính)
- Lưu ý nghiệp vụ: Phương hướng phải trả lời được các tồn tại ở Phần II — tồn tại nào
  không có giải pháp tương ứng sẽ bị chất vấn tại Hội nghị CBVC; chỉ tiêu phải đo lường
  được, tránh khẩu hiệu chung chung.
- → Kết quả bước: Bản thảo Phần III (nhiệm vụ trọng tâm, chỉ tiêu, giải pháp).

**Bước 7. Hoàn thiện, trình Ban Giám hiệu duyệt**
- Làm gì: Gộp 3 phần thành văn bản hoàn chỉnh; kiểm tra lần cuối: số liệu trong văn
  bản khớp bảng biểu và phụ lục, chính tả, thể thức; lập phụ lục số liệu tổng hợp theo
  mảng; trình Ban Giám hiệu duyệt; sau duyệt, trình Hội nghị CBVC và gửi cơ quan chủ
  quản/Bộ GD&ĐT; lưu hồ sơ.
- Dùng input: `nam_hoc`
- Vai trò: Ban Giám hiệu · AI hỗ trợ: tổng hợp, đối chiếu và trình bày số liệu · ⏱ 2–3 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Kiểm tra số ký hiệu văn bản, ngày tháng, nơi nhận trước khi trình
  ký — sai thể thức ở báo cáo cấp trường rất mất điểm; phụ lục số liệu phải khớp 100%
  với số liệu trong văn bản chính.
- → Kết quả bước: Báo cáo tổng kết năm học toàn trường đã duyệt + phụ lục số liệu
  tổng hợp theo mảng.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Báo cáo của phòng, khoa, trung tâm"/] --> B["Bước 1. Xây dựng đề cương báo cáo 6 mảng"]
    B --> C["Bước 2. Gửi đề cương, thu thập báo cáo đơn vị"]
    C --> D["Bước 3. Tổng hợp theo mảng, chuẩn hóa số liệu"]
    D --> E["Bước 4. Viết kết quả, nêu bật điểm nổi bật"]
    E --> F["Bước 5. Đánh giá tồn tại, hạn chế, nguyên nhân"]
    F --> G["Bước 6. Xây dựng phương hướng năm học tới"]
    G --> HG["👤 Bước 7. Ban Giám hiệu duyệt"]
    HG --> H["Trình Hội nghị CBVC, gửi cấp trên"]
    H --> I[/"Báo cáo tổng kết, phụ lục số liệu"/]
```

## Đầu ra (Output)
- Báo cáo tổng kết năm học toàn trường.
- Phụ lục số liệu tổng hợp theo mảng.

**Cấu trúc output chuẩn** (sản phẩm chính: Báo cáo tổng kết năm học toàn trường) —
các phần bắt buộc theo đúng thứ tự:
1. Quốc hiệu – Tiêu ngữ (CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM / Độc lập – Tự do –
   Hạnh phúc).
2. Tên trường (dòng trên), địa danh + ngày tháng năm (dòng dưới, căn phải).
3. Tiêu đề: BÁO CÁO TỔNG KẾT NĂM HỌC ...
4. Phần I. KẾT QUẢ THỰC HIỆN CÁC MẶT CÔNG TÁC (6 mảng: đào tạo; KHCN & HTQT; CTSV;
   tổ chức cán bộ; tài chính – CSVC; đảm bảo chất lượng).
5. Phần II. TỒN TẠI, HẠN CHẾ (kèm nguyên nhân).
6. Phần III. PHƯƠNG HƯỚNG NĂM HỌC TỚI (nhiệm vụ trọng tâm, chỉ tiêu, giải pháp).
7. Nơi nhận – Lưu.
8. Chữ ký Hiệu trưởng (họ tên, học hàm/học vị).
9. Phụ lục: bảng số liệu tổng hợp theo mảng (đính kèm).

## Checklist nghiệm thu

- [ ] Đủ các phần của "Cấu trúc output chuẩn": quốc hiệu, tên trường, tiêu đề, Phần I/II/III, nơi nhận, chữ ký Hiệu trưởng, phụ lục số liệu.
- [ ] Phần I có đủ 6 mảng công tác; số liệu trong văn bản khớp 100% với phụ lục số liệu theo mảng.
- [ ] Số liệu khớp với báo cáo các đơn vị đã nộp; chênh lệch chưa giải trình được đã loại khỏi báo cáo.
- [ ] Không bịa đặt số liệu, minh chứng; số liệu thiếu được ghi rõ "chưa có số liệu".
- [ ] Mỗi nhận định tích cực có số liệu minh chứng đi kèm; có so sánh với năm học trước.
- [ ] Phần II: tồn tại nêu thẳng với nguyên nhân cụ thể; Phần III: mỗi tồn tại có giải pháp tương ứng, chỉ tiêu đo lường được.
- [ ] Đúng thể thức: số ký hiệu văn bản, ngày tháng, nơi nhận, chữ ký Hiệu trưởng.
- [ ] Đã qua Human gate: Ban Giám hiệu đã duyệt; đã trình Hội nghị CBVC và gửi cơ quan chủ quản/Bộ GD&ĐT.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `nam_hoc` | 2025–2026 |
| `bao_cao_don_vi` | Đào tạo: tuyển sinh đạt 102% chỉ tiêu (2.550/2.500); tốt nghiệp 1.980 SV. KHCN: 45 đề tài (12 cấp Bộ), 120 bài báo. CTSV: 320 suất học bổng. TCCB: tuyển 28 VC, bổ nhiệm 6. TCKT: thu 210 tỷ. QTTB: hoàn thành 90% KH sửa chữa. ĐBCL: đạt kiểm định 4 CTĐT. |

### Output mẫu (trích)

```
TRƯỜNG ĐẠI HỌC A            CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
                                             Độc lập – Tự do – Hạnh phúc
                                                    Thành phố C, ngày 25 tháng 08 năm 2026

BÁO CÁO TỔNG KẾT NĂM HỌC 2025–2026
(Dữ liệu giả lập)

I. KẾT QUẢ THỰC HIỆN CÁC MẶT CÔNG TÁC
1. Công tác đào tạo
- Tuyển sinh đạt 102% chỉ tiêu (2.550/2.500 thí sinh nhập học).
- Công nhận tốt nghiệp 1.980 sinh viên; tỷ lệ tốt nghiệp đúng hạn 78%.
2. Khoa học công nghệ và hợp tác quốc tế
- Triển khai 45 đề tài NCKH (12 đề tài cấp Bộ), nghiệm thu 40 đề tài.
- Công bố 120 bài báo khoa học (35 bài quốc tế).
- Ký mới 06 thỏa thuận hợp tác quốc tế.
3. Công tác sinh viên
- Cấp 320 suất học bổng khuyến khích học tập; hỗ trợ 150 SV khó khăn.
4. Tổ chức cán bộ
- Tuyển dụng 28 viên chức; bổ nhiệm, bổ nhiệm lại 06 cán bộ quản lý.
5. Tài chính – cơ sở vật chất
- Tổng thu 210 tỷ đồng, đảm bảo chi thường xuyên và đầu tư phát triển.
- Hoàn thành 90% kế hoạch sửa chữa CSVC.
6. Đảm bảo chất lượng
- 04 chương trình đào tạo đạt kiểm định chất lượng.

II. TỒN TẠI, HẠN CHẾ
- Tiến độ một số đề tài NCKH còn chậm so với kế hoạch.
- 10% kế hoạch sửa chữa CSVC chưa hoàn thành do vướng thủ tục.

III. PHƯƠNG HƯỚNG NĂM HỌC 2026–2027
1. Tuyển sinh đạt tối thiểu 100% chỉ tiêu; mở 02 ngành đào tạo mới.
2. Đẩy mạnh công bố quốc tế, phấn đấu 45 bài.
3. Hoàn thành kiểm định 06 chương trình đào tạo.

Nơi nhận:                                      HIỆU TRƯỞNG
- Cơ quan chủ quản (b/c);                         (đã ký)
- Các đơn vị trong trường;
- Lưu: VT, HCTH.                         PGS.TS. Phạm Văn A
```

## Căn cứ & lưu ý
- Quy chế tổ chức và hoạt động của trường; yêu cầu báo cáo của cơ quan chủ quản.
- Số liệu các đơn vị phải được đối chiếu, thống nhất trước khi đưa vào báo cáo chung.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
