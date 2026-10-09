# Tư liệu lịch sử – không phải quy trình hiện hành

Nội dung từ phiên bản nguồn trước 1.1.0, giữ để đối chiếu dữ liệu đầu vào và thay đổi; căn cứ, điều kiện, mẫu và ví dụ có thể đã lỗi thời. Không dùng để thực hiện nghiệp vụ hiện tại.

## Khi nào dùng
Khi giảng viên được giao nhiệm vụ biên soạn giáo trình, bài giảng phục vụ giảng dạy
học phần (theo kế hoạch biên soạn của khoa/trường).

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_giao_trinh` | Tên giáo trình / bài giảng | Có |
| `hoc_phan` | Mã + tên học phần sử dụng | Có |
| `tac_gia` | Họ tên, học hàm/học vị, đơn vị của tác giả/nhóm tác giả | Có |
| `de_cuong_hoc_phan` | Đề cương chi tiết học phần (mục tiêu, nội dung, CLO) | Có |
| `doi_tuong_su_dung` | Sinh viên năm mấy, ngành nào | Không |

## Quy trình

**Bước 1. Xác định yêu cầu và phạm vi biên soạn**
- Làm gì: Tiếp nhận nhiệm vụ biên soạn từ khoa/trường; đọc kỹ đề cương chi tiết học
  phần để nắm mục tiêu, nội dung, chuẩn đầu ra (CLO); xác định đối tượng sử dụng
  (sinh viên năm mấy, ngành nào); xác minh học hàm/học vị, đơn vị của tác giả/nhóm
  tác giả; kiểm tra học phần có nằm trong kế hoạch biên soạn đã phê duyệt không;
  lập tiến độ biên soạn theo các mốc (đề cương → bản thảo → phản biện → nghiệm thu → xuất bản).
- Dùng input: `ten_giao_trinh`, `hoc_phan`, `tac_gia`, `de_cuong_hoc_phan`, `doi_tuong_su_dung`
- Vai trò: Giảng viên biên soạn · AI hỗ trợ: lập bảng yêu cầu và tiến độ dự thảo từ Input, chủ biên kiểm tra · ⏱ 3–5 giờ (ước tính)
- Lưu ý nghiệp vụ: Tên giáo trình nên trùng/khớp với tên học phần để tránh nhầm lẫn
  khi kiểm định học liệu; nếu là nhóm tác giả, phải phân công rõ chương/phần cho từng
  người ngay từ đầu và ghi vào biên bản; kiểm tra đề cương học phần là bản mới nhất
  đã phê duyệt, không dùng bản nháp cũ.
- → Kết quả bước: Bảng yêu cầu biên soạn (tên giáo trình, học phần, tác giả/phân công,
  đối tượng sử dụng, tiến độ các mốc).

**Bước 2. Xây dựng đề cương giáo trình**
- Làm gì: Từ đề cương chi tiết học phần, chia nội dung thành các chương; quyết định
  số chương và dung lượng mỗi chương (số trang dự kiến); đối chiếu từng chương với CLO
  để đảm bảo mọi chuẩn đầu ra đều được ít nhất một chương "phủ"; xác định thời lượng
  giảng dạy tương ứng từng chương (tiết lý thuyết/bài tập); trình tổ bộ môn/khoa góp
  ý và chốt đề cương.
- Dùng input: `de_cuong_hoc_phan`
- Vai trò: Giảng viên biên soạn · AI hỗ trợ: đề xuất chia chương và bảng đối chiếu chương–CLO, tổ bộ môn/khoa góp ý và chốt đề cương · ⏱ 1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Mỗi CLO phải được gắn với ít nhất một chương — đây là điểm kiểm
  định học liệu hay soi nhất; dung lượng các chương nên cân đối, tránh chương đầu quá
  dài, chương cuối sơ sài; số chương của giáo trình không nhất thiết bằng số chương
  trong đề cương học phần, có thể gộp/tách cho hợp lý về sư phạm.
- → Kết quả bước: Đề cương giáo trình (danh sách chương, dung lượng, thời lượng,
  bảng đối chiếu chương – CLO).

**Bước 3. Thiết kế cấu trúc chuẩn cho từng chương**
- Làm gì: Quy định khung mục bắt buộc áp dụng thống nhất cho mọi chương: (1) Mục tiêu
  chương (gắn CLO); (2) Nội dung lý thuyết có ví dụ minh họa; (3) Ví dụ/bài tập mẫu
  có lời giải; (4) Câu hỏi ôn tập; (5) Bài tập cuối chương (phân 3 mức độ: nhận biết –
  thông hiểu – vận dụng); (6) Tài liệu tham khảo của chương. Thống nhất quy tắc trình
  bày: cách đánh số mục/ví dụ/hình/bảng, kiểu trích dẫn, thuật ngữ chuyên môn dùng
  xuyên suốt giáo trình.
- Dùng input: `de_cuong_hoc_phan`
- Vai trò: Giảng viên biên soạn · AI hỗ trợ: soạn khung cấu trúc chuẩn và quy tắc trình bày, nhóm tác giả thống nhất áp dụng · ⏱ 3–5 giờ (ước tính)
- Lưu ý nghiệp vụ: Thuật ngữ phải thống nhất từ chương 1 đến chương cuối — bẫy thường
  gặp là mỗi tác giả trong nhóm dùng một cách dịch khác nhau; quy ước một chuẩn trích
  dẫn duy nhất (VD: [số thứ tự] hoặc APA) và áp dụng cho toàn giáo trình.
- → Kết quả bước: Khung giáo trình hoàn chỉnh (mục lục chi tiết + cấu trúc chuẩn
  từng chương) — sản phẩm chính thứ nhất.

**Bước 4. Biên soạn nội dung các chương**
- Làm gì: Viết đầy đủ từng chương theo cấu trúc chuẩn đã chốt: diễn đạt sư phạm,
  mạch lạc; mỗi khái niệm mới kèm ví dụ minh họa cụ thể; mỗi chương có ít nhất 2–3
  bài tập mẫu có lời giải chi tiết; cập nhật kiến thức, công nghệ mới của chuyên ngành;
  trích dẫn đầy đủ nguồn tài liệu tham khảo; viết Lời nói đầu và Phụ lục (nếu có).
- Dùng input: khung giáo trình từ Bước 3 (các trường input đã được cụ thể hóa ở
  các bước trước)
- Vai trò: Giảng viên · AI hỗ trợ: hỗ trợ soạn dự thảo nội dung từng chương · ⏱ 2–4 tuần (tùy dung lượng) (ước tính)
- Lưu ý nghiệp vụ: Tôn trọng bản quyền — trích dẫn đầy đủ, không sao chép nguyên văn
  tài liệu có bản quyền; tránh "viết cho xong": mỗi chương nên được đọc lại sau ít nhất
  1–2 ngày để phát hiện lỗi logic; nếu nhóm tác giả, chủ biên phải đọc soát toàn bộ
  để thống nhất giọng văn.
- → Kết quả bước: Bản thảo toàn văn giáo trình + 01 chương mẫu viết đầy đủ theo
  cấu trúc chuẩn.

**Bước 5. Tổ chức phản biện độc lập**
- Làm gì: Mời ít nhất 02 phản biện độc lập (01 trong trường, 01 ngoài trường — ưu tiên
  người có chuyên môn sâu về học phần); gửi bản thảo kèm phiếu nhận xét phản biện
  (đánh giá: tính khoa học, tính sư phạm, tính cập nhật, hình thức); thu phiếu nhận
  xét, phân loại ý kiến (bắt buộc sửa / nên sửa / góp ý tham khảo).
- Dùng input: (không dùng trường input mới; xử lý trên bản thảo từ Bước 4)
- Vai trò: Giảng viên biên soạn · AI hỗ trợ: chuẩn bị dự thảo, tài liệu và số liệu phục vụ bước này · ⏱ 2–3 tuần (ước tính)
- Lưu ý nghiệp vụ: Phản biện ngoài trường không được là đồng tác giả/cộng sự thân
  thiết của nhóm biên soạn để đảm bảo tính độc lập; yêu cầu phản biện trả lời đúng
  hạn và ghi rõ ý kiến nào "bắt buộc" để tác giả không bỏ sót.
- → Kết quả bước: Phiếu nhận xét phản biện + danh sách ý kiến phản biện đã phân loại.

**Bước 6. Hiệu đính theo ý kiến phản biện, lập bảng tiếp thu**
- Làm gì: Tác giả sửa bản thảo theo từng ý kiến phản biện; với ý kiến không tiếp thu
  phải ghi rõ lý do; lập bảng tiếp thu ý kiến (cột: STT, ý kiến phản biện, tiếp thu
  của tác giả); đối chiếu lần cuối thuật ngữ, đánh số mục/ví dụ/hình/bảng, trích dẫn
  sau hiệu đính.
- Dùng input: (không dùng trường input mới; xử lý trên ý kiến phản biện từ Bước 5)
- Vai trò: Giảng viên biên soạn · AI hỗ trợ: hỗ trợ đối chiếu và lập bảng tiếp thu, tác giả sửa bản thảo theo ý kiến phản biện · ⏱ 3–5 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Bảng tiếp thu là minh chứng bắt buộc trong hồ sơ nghiệm thu —
  không được bỏ trống cột "tiếp thu"; ý kiến "bắt buộc sửa" của phản biện mà không
  tiếp thu thì phải có lý do thuyết phục, nếu không hội đồng nghiệm thu sẽ trả hồ sơ về.
- → Kết quả bước: Bản thảo đã hiệu đính + Bảng tiếp thu ý kiến phản biện (mẫu) —
  sản phẩm chính thứ hai.

**Bước 7. Nghiệm thu tại hội đồng cấp trường**
- Làm gì: Nộp hồ sơ nghiệm thu (bản thảo, bảng tiếp thu, phiếu phản biện, đề cương
  học phần); hội đồng nghiệm thu cấp trường đánh giá theo tiêu chí (khoa học, sư phạm,
  cập nhật, hình thức); ghi biên bản nghiệm thu (đạt / đạt có sửa / không đạt); nếu
  "đạt có sửa", tác giả chỉnh sửa lần cuối theo kết luận hội đồng.
- Dùng input: (không dùng trường input mới; xử lý trên hồ sơ từ Bước 6)
- Vai trò: Hội đồng thẩm định · AI hỗ trợ: chuẩn bị dự thảo, tài liệu và số liệu phục vụ bước này · ⏱ 1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Kiểm tra đủ thành phần hồ sơ trước khi nộp — thiếu phiếu phản biện
  ngoài trường là lỗi hay gặp nhất khiến hồ sơ bị trả; giữ lại biên bản nghiệm thu vì
  đây là minh chứng tính giờ NCKH và kiểm định học liệu.
- → Kết quả bước: Biên bản nghiệm thu + bản thảo hoàn chỉnh sau chỉnh sửa lần cuối.

**Bước 8. Xuất bản, lưu hành và đưa vào thư viện**
- Làm gì: Đăng ký xuất bản (nhà xuất bản) hoặc lưu hành nội bộ theo quy định của
  trường; nộp bản lưu chiểu cho thư viện, đưa giáo trình vào danh mục học liệu của
  thư viện; thông báo cho bộ môn/khoa đưa vào danh mục học liệu của học phần; lập kế
  hoạch cập nhật, tái bản định kỳ (3–5 năm).
- Dùng input: `ten_giao_trinh`, `hoc_phan`
- Vai trò: Giảng viên biên soạn · AI hỗ trợ: chuẩn bị dự thảo, tài liệu và số liệu phục vụ bước này · ⏱ 2–4 tuần (ước tính)
- Lưu ý nghiệp vụ: Giáo trình chỉ được tính là "đã xuất bản" khi có giấy phép xuất
  bản hoặc quyết định lưu hành nội bộ — bản in thử không tính; cập nhật mã học liệu
  vào đề cương chi tiết học phần để phục vụ kiểm định.
- → Kết quả bước: Giáo trình đã xuất bản/lưu hành nội bộ + hồ sơ đưa vào danh mục
  học liệu thư viện.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Đề cương học phần, chuẩn đầu ra"/] --> B["Bước 1. Xác định yêu cầu, phạm vi biên soạn"]
    B --> C["Bước 2. Xây dựng đề cương giáo trình"]
    C --> D["Bước 3. Thiết kế cấu trúc chuẩn từng chương"]
    D --> E["Bước 4. Biên soạn nội dung các chương"]
    E --> HG1["👤 Bước 5. Phản biện độc lập: 01 trong, 01 ngoài trường"]
    HG1 --> F["Bước 6. Hiệu đính, lập bảng tiếp thu"]
    F --> G{"Bước 7. Hội đồng nghiệm thu đạt?"}
    G -->|Không| F
    G -->|Có| H["Bước 8. Xuất bản, đưa vào thư viện"]
    H --> I[/"Giáo trình, chương mẫu, bảng tiếp thu"/]
```

## Đầu ra (Output)
- Khung giáo trình hoàn chỉnh (mục lục chi tiết + cấu trúc từng chương).
- Chương mẫu (01 chương viết đầy đủ theo cấu trúc chuẩn).
- Bảng tiếp thu ý kiến phản biện (mẫu).

**Cấu trúc output chuẩn** (sản phẩm chính: Khung giáo trình hoàn chỉnh) — các phần
bắt buộc theo đúng thứ tự:
1. Trang bìa: tên giáo trình, tác giả (chủ biên), đơn vị, năm xuất bản.
2. Lời nói đầu: mục đích biên soạn, đối tượng sử dụng, cấu trúc cuốn sách.
3. Mục lục chi tiết: chương, mục, tiểu mục — mỗi chương ghi CLO tương ứng.
4. Nội dung các chương — mỗi chương gồm đúng 6 mục theo thứ tự:
   4.1. Mục tiêu chương (gắn CLO);
   4.2. Nội dung lý thuyết (có ví dụ minh họa);
   4.3. Ví dụ / bài tập mẫu có lời giải;
   4.4. Câu hỏi ôn tập;
   4.5. Bài tập cuối chương (phân 3 mức độ: nhận biết – thông hiểu – vận dụng);
   4.6. Tài liệu tham khảo của chương.
5. Phụ lục (nếu có).
6. Tài liệu tham khảo chung.

## Checklist nghiệm thu

- [ ] Đủ các phần của "Cấu trúc output chuẩn": bìa, Lời nói đầu, Mục lục chi tiết, nội dung các chương (đủ 6 mục/chương), Phụ lục, Tài liệu tham khảo.
- [ ] Mọi CLO của đề cương học phần đều được ít nhất một chương "phủ" (có bảng đối chiếu chương–CLO).
- [ ] Mỗi chương có đúng 6 mục theo đúng thứ tự; thuật ngữ và quy ước trích dẫn thống nhất toàn giáo trình.
- [ ] Nội dung output khớp với Input (`ten_giao_trinh`, `hoc_phan`, `tac_gia`, `de_cuong_hoc_phan`).
- [ ] Không sao chép nguyên văn tài liệu có bản quyền; trích dẫn đầy đủ nguồn tài liệu tham khảo.
- [ ] Đúng thể thức trình bày: đánh số mục/ví dụ/hình/bảng liên tục, chính tả chuẩn.
- [ ] Đã qua Human gate: đủ phiếu phản biện (01 trong trường, 01 ngoài trường) và biên bản nghiệm thu của hội đồng cấp trường.
- [ ] Bảng tiếp thu ý kiến phản biện đầy đủ cột "tiếp thu"; ý kiến "bắt buộc sửa" không tiếp thu đã có lý do thuyết phục.
- [ ] Hồ sơ nghiệm thu đầy đủ thành phần (bản thảo, bảng tiếp thu, phiếu phản biện, đề cương học phần).

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `ten_giao_trinh` | Giáo trình Nhập môn lập trình |
| `hoc_phan` | CNTT101 – Nhập môn lập trình (3 tín chỉ) |
| `tac_gia` | TS. Phạm Văn B (chủ biên), ThS. Bùi Thị B – Bộ môn Khoa học máy tính |
| `de_cuong_hoc_phan` | 7 chương, CLO1–CLO4 (kiến thức – kỹ năng lập trình cơ bản) |
| `doi_tuong_su_dung` | Sinh viên năm nhất ngành Công nghệ thông tin |

### Output mẫu

```
KHUNG GIÁO TRÌNH
Tên giáo trình: Nhập môn lập trình
Tác giả: TS. Phạm Văn B (chủ biên), ThS. Bùi Thị B
Đơn vị: Bộ môn Khoa học máy tính – Khoa CNTT, Trường Đại học A
Học phần sử dụng: CNTT101 (3 tín chỉ) – Sinh viên năm nhất ngành CNTT

LỜI NÓI ĐẦU
Giáo trình "Nhập môn lập trình" được biên soạn phục vụ giảng dạy học phần
CNTT101 cho sinh viên năm nhất ngành Công nghệ thông tin. Sách gồm 7 chương,
được thiết kế theo chuẩn đầu ra CLO1–CLO4 của học phần: mỗi chương có mục tiêu,
lý thuyết kèm ví dụ minh họa, bài tập mẫu có lời giải, câu hỏi ôn tập và bài tập
cuối chương phân theo 3 mức độ.

MỤC LỤC CHI TIẾT

Lời nói đầu
Chương 1. Tổng quan về máy tính và ngôn ngữ lập trình (CLO1)
  1.1. Khái niệm thuật toán và chương trình
  1.2. Các ngôn ngữ lập trình phổ biến
  1.3. Môi trường phát triển chương trình
  Câu hỏi ôn tập chương 1
Chương 2. Kiểu dữ liệu, biến và biểu thức (CLO1, CLO2)
  ...
Chương 3. Cấu trúc điều khiển: rẽ nhánh (CLO2, CLO3)
Chương 4. Cấu trúc điều khiển: vòng lặp (CLO2, CLO3)
Chương 5. Hàm và đệ quy (CLO3)
Chương 6. Mảng và chuỗi ký tự (CLO3)
Chương 7. Tệp tin và bài toán tổng hợp (CLO3, CLO4)
Phụ lục: Bảng mã ASCII, từ khóa ngôn ngữ
Tài liệu tham khảo

---
CHƯƠNG MẪU – Chương 4. Cấu trúc điều khiển: vòng lặp

Mục tiêu chương: Sau khi học xong chương này, sinh viên viết được chương trình
sử dụng vòng lặp for/while để giải các bài toán tính tổng, đếm, tìm kiếm cơ bản (CLO3).

4.1. Vòng lặp for
Khái niệm: vòng lặp for dùng khi biết trước số lần lặp...
Ví dụ 4.1 (giả lập): Tính tổng S = 1 + 2 + ... + n với n nhập từ bàn phím.
Lời giải và phân tích từng bước...
4.2. Vòng lặp while và do-while
4.3. Lệnh break, continue
4.4. Bài tập mẫu có lời giải (03 bài)
Câu hỏi ôn tập chương 4 (05 câu)
Bài tập chương 4 (10 bài, phân 3 mức độ)
Tài liệu tham khảo chương 4: [1], [2]

---
BẢNG TIẾP THU Ý KIẾN PHẢN BIỆN (mẫu)

| STT | Ý kiến phản biện (PGS.TS. Trần Văn D) | Tiếp thu của tác giả |
|---|---|---|
| 1 | Bổ sung ví dụ thực tế cho vòng lặp while ở mục 4.2 | Đã bổ sung Ví dụ 4.4 (bài toán kiểm tra số nguyên tố) |
| 2 | Bài tập chương 4 thiếu mức độ vận dụng cao | Đã bổ sung 02 bài tập mức vận dụng cao (bài 9, 10) |
```

## Căn cứ & lưu ý
- Quy định về biên soạn, lựa chọn, thẩm định giáo trình đại học của Trường
  Đại học A (giả lập).
- Tôn trọng quyền sở hữu trí tuệ: trích dẫn đầy đủ nguồn; không sao chép nội dung
  có bản quyền khi số hóa, xuất bản.
- Giáo trình nghiệm thu đạt được tính giờ NCKH và là minh chứng cho tiêu chí
  về học liệu trong kiểm định.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
