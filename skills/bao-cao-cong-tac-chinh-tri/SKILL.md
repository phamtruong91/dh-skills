---
name: bao-cao-cong-tac-chinh-tri
description: Soạn báo cáo công tác chính trị, tư tưởng định kỳ (quý/năm học/đợt) trong trường đại học: tình hình tư tưởng CBVC/SV, kết quả tuyên truyền, giáo dục. Dùng khi báo cáo Đảng ủy và cấp trên.
---

# Skill: Soạn báo cáo công tác chính trị

## Khi nào dùng
Khi đơn vị phụ trách công tác chính trị cần báo cáo định kỳ (quý, năm học) hoặc sau đợt
sinh hoạt chính trị, gửi Đảng ủy trường và Đảng ủy cấp trên.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ky_bao_cao` | Quý / Năm học / Đợt + thời gian | Có |
| `tinh_hinh_tu_tuong` | Đánh giá chung tình hình tư tưởng CBVC, sinh viên (tổng hợp, không nêu tên cá nhân) | Có |
| `ket_qua_trien_khai` | Các hoạt động đã làm: số hội nghị, buổi sinh hoạt, lượt người tham gia | Có |
| `vu_viec_noi_bat` | Vụ việc tư tưởng phát sinh và cách xử lý (mô tả ẩn danh, khách quan) | Không |
| `ton_tai_kien_nghi` | Tồn tại và kiến nghị | Có |

## Quy trình

**Bước 1. Thu thập thông tin từ các nguồn**
- Làm gì: thu thập thông tin về tình hình tư tưởng và kết quả triển khai từ các chi bộ, Đoàn
  Thanh niên, Hội Sinh viên, các khoa; tổng hợp theo từng nguồn.
- Dùng input: `ky_bao_cao`.
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: tổng hợp và đối chiếu dữ liệu thu thập được · ⏱ ~2–3 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: thông tin về tư tưởng cá nhân chỉ thu thập ở mức tổng hợp, không ghi tên
  cá nhân vào tài liệu thu thập.
- → Kết quả bước: tập thông tin đầu vào phân theo nguồn (chi bộ, Đoàn, Hội, khoa).

**Bước 2. Tổng hợp tình hình tư tưởng**
- Làm gì: đánh giá chung tình hình tư tưởng theo nhóm đối tượng (CBVC, sinh viên); nêu mặt
  tích cực và biểu hiện cần lưu ý.
- Dùng input: `tinh_hinh_tu_tuong`, tập thông tin (kết quả bước 1).
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: tổng hợp dự thảo · ⏱ ~2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: tuyệt đối không nêu tên cá nhân cụ thể; không suy đoán, quy chụp động cơ
  tư tưởng của cá nhân.
- → Kết quả bước: dự thảo phần I. Tình hình tư tưởng (đánh giá tổng hợp theo nhóm đối tượng).

**Bước 3. Thống kê kết quả triển khai**
- Làm gì: thống kê số lượng hoạt động (hội nghị, buổi sinh hoạt), lượt người tham gia; so
  sánh với kế hoạch đề ra.
- Dùng input: `ket_qua_trien_khai`.
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: thống kê số liệu hoạt động, đối chiếu với kế hoạch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: số liệu phải có nguồn (biên bản, danh sách điểm danh); nêu rõ đạt/vượt/
  chưa đạt so với kế hoạch.
- → Kết quả bước: bảng thống kê kết quả triển khai so với kế hoạch.

**Bước 4. Nêu vụ việc và biện pháp xử lý**
- Làm gì: mô tả vụ việc tư tưởng phát sinh (nếu có) một cách khách quan, ẩn danh; nêu biện
  pháp đã xử lý và kết quả.
- Dùng input: `vu_viec_noi_bat`.
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: soạn khung · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: mô tả khách quan, ẩn danh tuyệt đối; không có vụ việc thì ghi rõ "không
  phát sinh vụ việc nghiêm trọng".
- → Kết quả bước: dự thảo phần vụ việc (mô tả ẩn danh + biện pháp xử lý).

**Bước 5. Đề xuất kiến nghị**
- Làm gì: tổng hợp tồn tại và đề xuất với Đảng ủy về nội dung, hình thức giáo dục chính trị,
  tư tưởng thời gian tới.
- Dùng input: `ton_tai_kien_nghi`, kết quả bước 2–4.
- Vai trò: Đảng ủy · AI hỗ trợ: soạn dự thảo · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: kiến nghị cụ thể, khả thi, gắn với đối tượng và hình thức triển khai.
- → Kết quả bước: dự thảo phần III. Tồn tại, kiến nghị.

**Bước 6. Kiểm tra ngôn từ và số liệu**
- Làm gì: kiểm tra ngôn từ chuẩn mực, thận trọng; đối chiếu số liệu có nguồn; rà soát không
  để lọt tên cá nhân, suy đoán chủ quan.
- Dùng input: dự thảo các phần (kết quả bước 2–5).
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: rà soát ngôn từ và số liệu · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chưa đạt thì quay lại chỉnh sửa phần tương ứng; đây là cửa kiểm soát chất
  lượng cuối trước khi trình Đảng ủy.
- → Kết quả bước: dự thảo báo cáo hoàn chỉnh, đạt yêu cầu ngôn từ và số liệu.

**Bước 7. Trình Đảng ủy thẩm định và ký duyệt**
- Làm gì: trình Đảng ủy thẩm định nội dung, số liệu; sau khi Bí thư ký duyệt mới gửi cấp trên
  (Human gate).
- Dùng input: dự thảo báo cáo (kết quả bước 6).
- Vai trò: Bí thư Đảng ủy · AI hỗ trợ: chuẩn bị hồ sơ trình ký, nhắc lịch và theo dõi tiến độ · ⏱ ~3–7 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: báo cáo gửi cấp trên bắt buộc qua Bí thư Đảng ủy ký duyệt; chưa đạt thì
  quay lại chỉnh sửa.
- → Kết quả bước: báo cáo công tác chính trị hoàn chỉnh, đã ký duyệt.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Kỳ báo cáo, tình hình tư tưởng, kết quả triển khai"/]
    IN --> A["Bước 1. Thu thập thông tin từ các nguồn"]
    A --> B["Bước 2. Tổng hợp tình hình tư tưởng"]
    B --> C["Bước 3. Thống kê kết quả triển khai"]
    C --> D["Bước 4. Nêu vụ việc và biện pháp xử lý"]
    D --> E["Bước 5. Đề xuất kiến nghị"]
    E --> F["Bước 6. Kiểm tra ngôn từ và số liệu"]
    F --> HG["👤 Đảng ủy thẩm định, Bí thư ký duyệt"]
    HG --> G{"Đạt yêu cầu?"}
    G -->|Không| E
    G -->|Có| H["Bước 7. Trình Đảng ủy thẩm định và ký duyệt"]
    H --> OUT[["Báo cáo công tác chính trị hoàn chỉnh"]]
```

## Đầu ra (Output)
- Báo cáo công tác chính trị, tư tưởng (markdown).

**Cấu trúc output chuẩn:** khung cố định của Báo cáo công tác chính trị, tư tưởng:
1. Tiêu đề: tên trường + "ĐẢNG ỦY" + tên báo cáo ("BÁO CÁO" + "Công tác chính trị, tư tưởng ..."
   + `ky_bao_cao`) + Kính gửi (Đảng ủy cấp trên).
2. I. Tình hình tư tưởng: đánh giá chung theo nhóm đối tượng (CBVC, sinh viên), mặt tích cực
   và biểu hiện cần lưu ý — không nêu tên cá nhân.
3. II. Kết quả triển khai: số hoạt động, lượt người tham gia so với kế hoạch; vụ việc phát
   sinh (mô tả ẩn danh, khách quan) và biện pháp xử lý.
4. III. Tồn tại, kiến nghị: tồn tại + đề xuất với Đảng ủy về nội dung, hình thức thời gian tới.
5. Đoạn kết (kính trình cấp trên xem xét) + Nơi nhận + chữ ký (T/M Đảng ủy, Bí thư).

## Checklist nghiệm thu

- [ ] Đủ 5 phần theo "Cấu trúc output chuẩn": tiêu đề (tên trường + ĐẢNG ỦY + tên báo cáo + Kính gửi cấp trên); I. Tình hình tư tưởng (theo nhóm đối tượng, không nêu tên cá nhân); II. Kết quả triển khai (số hoạt động, lượt người tham gia so với kế hoạch; vụ việc phát sinh mô tả ẩn danh + biện pháp xử lý); III. Tồn tại, kiến nghị; đoạn kết + Nơi nhận + chữ ký (T/M Đảng ủy, Bí thư).
- [ ] Kỳ báo cáo, tình hình tư tưởng, kết quả triển khai, tồn tại/kiến nghị trong output khớp với Input đã cho.
- [ ] Không bịa đặt số liệu; số liệu hoạt động có nguồn (biên bản, danh sách điểm danh); nêu rõ đạt/vượt/chưa đạt so với kế hoạch.
- [ ] Đúng thể thức văn bản báo cáo của Đảng ủy: ký tên theo thẩm quyền (T/M Đảng ủy, Bí thư).
- [ ] Căn cứ (văn kiện, nghị quyết của Đảng; hướng dẫn công tác tư tưởng của cấp trên) còn hiệu lực.
- [ ] Đã qua Human gate: Đảng ủy thẩm định nội dung, số liệu; Bí thư ký duyệt trước khi gửi cấp trên.
- [ ] Tuyệt đối không nêu tên cá nhân trong đánh giá tư tưởng; không suy đoán, quy chụp động cơ của cá nhân; vụ việc (nếu có) mô tả khách quan, ẩn danh; ngôn từ thận trọng, chuẩn mực; không dùng AI "sáng tác" trích dẫn văn kiện.
- [ ] Kiến nghị cụ thể, khả thi, gắn với đối tượng và hình thức triển khai thời gian tới.

Tiêu chí đạt = tất cả các ô được đánh dấu.


## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường (Trường Đại học A), cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `ky_bao_cao` | Quý I, năm học 2026–2027 |
| `tinh_hinh_tu_tuong` | Ổn định; CBVC yên tâm công tác; sinh viên tích cực học tập, không có biểu hiện lệch lạc nổi cộm |
| `ket_qua_trien_khai` | 4 hội nghị quán triệt (1.200 lượt CBVC); 60 buổi sinh hoạt chi đoàn chuyên đề (8.500 lượt SV) |
| `vu_viec_noi_bat` | Không có vụ việc nghiêm trọng |
| `ton_tai_kien_nghi` | Một bộ phận SV ít tham gia sinh hoạt chính trị; kiến nghị đa dạng hình thức trực tuyến |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A
ĐẢNG ỦY

                          BÁO CÁO
     Công tác chính trị, tư tưởng quý I, năm học 2026–2027

Kính gửi: Đảng ủy cấp trên

I. TÌNH HÌNH TƯ TƯỞNG
Tình hình tư tưởng của cán bộ, viên chức và sinh viên trong quý ổn định;
CBVC yên tâm công tác; sinh viên tích cực học tập, rèn luyện; không ghi nhận
biểu hiện lệch lạc nổi cộm về tư tưởng.

II. KẾT QUẢ TRIỂN KHAI
- Tổ chức 4 hội nghị học tập, quán triệt với 1.200 lượt CBVC tham dự;
- 60 buổi sinh hoạt chi đoàn theo chuyên đề với 8.500 lượt sinh viên tham gia;
- Không phát sinh vụ việc nghiêm trọng về tư tưởng.

III. TỒN TẠI, KIẾN NGHỊ
- Tồn tại: một bộ phận sinh viên chưa tích cực tham gia sinh hoạt chính trị.
- Kiến nghị: đa dạng hóa hình thức sinh hoạt, tăng cường sinh hoạt trực tuyến
phù hợp với sinh viên.

Trên đây là báo cáo của Đảng ủy Trường, kính trình cấp trên xem xét./.

Nơi nhận:                                      T/M ĐẢNG ỦY
- Đảng ủy cấp trên;                             BÍ THƯ
- Lưu: VPĐU.                                        (đã ký)

                                              Nguyễn Văn Đức
```

## Human gate (người kiểm duyệt)
- Đảng ủy trường thẩm định nội dung, số liệu trước khi ký ban hành.
- Báo cáo gửi cấp trên phải qua Bí thư Đảng ủy ký duyệt.

## Giới hạn (guardrails)
- **Tuyệt đối không** nêu tên cá nhân cụ thể trong đánh giá tư tưởng; chỉ đánh giá
  ở mức tổng hợp nhóm đối tượng.
- **Tuyệt đối không** suy đoán, quy chụp động cơ tư tưởng của cá nhân; mô tả vụ việc
  (nếu có) phải khách quan, ẩn danh.
- Ngôn từ thận trọng, chuẩn mực; không dùng AI để "sáng tác" trích dẫn văn kiện.
- Mọi dữ liệu trong ví dụ đều giả lập.

## Căn cứ & lưu ý
- Văn kiện, nghị quyết của Đảng; hướng dẫn công tác tư tưởng của cấp ủy cấp trên.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
