---
name: "quyet-dinh-cap-hoc-bong"
description: "Soạn quyết định cấp học bổng hoặc miễn, giảm học phí cho sinh viên đúng thể thức quyết định hành chính. Dùng khi Phòng Công tác sinh viên đã có danh sách sinh viên đủ điều kiện và cần trình Hiệu trưởng ký quyết định cấp học bổng / miễn giảm học phí kèm danh sách."
---

# Soạn quyết định cấp học bổng / miễn giảm học phí

## Định dạng và file đầu ra
Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Nếu có cập nhật pháp lý dưới đây, đọc [căn cứ và điều kiện áp dụng](references/phap-ly.md) trước khi làm. Quy trình dưới đây giữ nghiệp vụ từ bản gốc; mọi viện dẫn văn bản, mẫu biểu, điều khoản phải theo căn cứ đã chọn trong phap-ly.md, không theo văn bản cũ.

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Khi hội đồng xét học bổng (hoặc hội đồng xét miễn, giảm học phí) đã họp, thống nhất danh sách
sinh viên đủ điều kiện, cần ban hành quyết định của Hiệu trưởng để cấp học bổng khuyến khích học
tập, học bổng tài trợ, học bổng chính sách, hoặc miễn/giảm học phí, kèm danh sách sinh viên được
hưởng.

## Đầu vào (Input)
| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `loai_quyet_dinh` | Cấp học bổng khuyến khích / Cấp học bổng tài trợ / Cấp học bổng chính sách / Miễn, giảm học phí | Có |
| `ten_dot` | Tên đợt xét (ví dụ: học kỳ 1, năm học 2026–2027) | Có |
| `danh_sach` | Danh sách sinh viên: họ tên, mã SV, lớp, khoa, mức học bổng hoặc mức miễn/giảm, ghi chú | Có |
| `can_cu` | Các văn bản căn cứ: quy chế học bổng, biên bản họp hội đồng, tờ trình của Phòng CTSV... | Có |
| `tong_kinh_phi` | Tổng kinh phí của đợt (số tiền bằng số và bằng chữ) | Có |
| `nguon_kinh_phi` | Nguồn kinh phí chi trả (ngân sách trường, quỹ tài trợ, ngân sách nhà nước...) | Có |
| `thoi_gian_ap_dung` | Học kỳ / năm học áp dụng quyết định | Có |
| `don_vi_thuc_hien` | Các đơn vị chịu trách nhiệm thi hành (Phòng CTSV, Phòng Tài chính, các khoa...) | Có |
| `nguoi_ky` | Hiệu trưởng | Có (mặc định: Hiệu trưởng) |

## Quy trình
**Ràng buộc pháp lý khi thực hiện** (trích references/phap-ly.md; đối chiếu toàn văn và hiệu lực tại ngày nghiệp vụ):
- Nghị định 238/2025/NĐ-CP, hiệu lực 03/09/2025: Yêu cầu năm học, trình độ, ngành, loại hình trường, mức tự chủ, quyết định học phí được duyệt và đối tượng miễn/giảm/hỗ trợ. Đối chiếu 238/2025 và chuyển tiếp; không lấy mức trần, tỷ lệ tăng hoặc đối tượng từ 81/2021/97/2023 làm mặc định hiện hành. Chỉ tính khi đủ căn cứ và dữ liệu từng người học.
- Trước Bước 1: chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi nhận nội bộ [CẦN XÁC MINH] (không đưa vào file giao), để trống phần tương ứng, chưa kết luận tuân thủ.

**Bước 1. Kiểm tra và làm sạch danh sách đầu vào**
- Làm gì: kiểm tra từng sinh viên trong `danh_sach` phải có đủ họ tên, mã SV, lớp, khoa, mức học bổng hoặc mức miễn/giảm; loại bỏ trùng lặp (trùng mã SV); đối chiếu điều kiện từng sinh viên với biên bản họp hội đồng xét trong `can_cu`.
- Dùng input: `danh_sach`, `can_cu`.
- Vai trò: Chuyên viên Phòng Công tác sinh viên · AI hỗ trợ: đối chiếu và phát hiện lỗi danh sách · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: trùng mã SV nhưng khác tên là dấu hiệu danh sách lỗi nguồn — phải xác minh lại với Phòng CTSV, không tự chọn một trong hai; sinh viên có trong danh sách nhưng không có trong biên bản hội đồng thì loại khỏi quyết định.
- → Kết quả bước: danh sách sinh viên đã làm sạch (đủ trường thông tin, không trùng lặp) + danh sách lỗi/loại kèm lý do.

**Bước 2. Tính tổng kinh phí và đối chiếu nguồn**
- Làm gì: cộng mức hưởng của từng sinh viên trong danh sách đã làm sạch; ghi tổng kinh phí bằng số và bằng chữ; đối chiếu với `tong_kinh_phi` đầu vào và `nguon_kinh_phi` đã được phê duyệt.
- Dùng input: `danh_sach`, `tong_kinh_phi`, `nguon_kinh_phi`.
- Vai trò: Chuyên viên Phòng Công tác sinh viên · AI hỗ trợ: tính tổng kinh phí, ghi bằng số và bằng chữ, đối chiếu nguồn · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: tổng cộng tay phải khớp `tong_kinh_phi` — nếu lệch dù 1 đồng cũng phải rà lại từng dòng, không tự điều chỉnh cho khớp; số tiền bằng chữ phải viết đúng chính tả tiếng Việt (ví dụ "Ba mươi sáu triệu đồng").
- → Kết quả bước: bảng tính tổng kinh phí (tổng số SV, tổng tiền bằng số, bằng chữ, nguồn kinh phí) đã đối chiếu khớp.

**Bước 3. Dựng khung thể thức quyết định**
- Làm gì: dựng khung theo Nghị định 30/2020/NĐ-CP: Quốc hiệu – Tiêu ngữ → tên cơ quan ban hành → số, ký hiệu → địa danh, ngày tháng năm → tiêu đề "QUYẾT ĐỊNH" → trích yếu → phần Căn cứ (liệt kê từ `can_cu`: quy chế học bổng, biên bản họp hội đồng, tờ trình của Phòng CTSV theo trình tự) → khung Nơi nhận → khối chữ ký Hiệu trưởng.
- Dùng input: `can_cu`, `nguoi_ky`.
- Vai trò: Chuyên viên Phòng Công tác sinh viên · AI hỗ trợ: dựng khung thể thức quyết định theo Nghị định 30/2020 · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: căn cứ phải viện dẫn theo trình tự từ văn bản quy phạm đến văn bản cụ thể của đợt xét; kiểm tra các văn bản căn cứ còn hiệu lực — căn cứ hết hiệu lực thì quyết định vô giá trị.
- → Kết quả bước: khung thể thức quyết định (đầy đủ yếu tố hình thức + phần căn cứ).

**Bước 4. Soạn nội dung 4 Điều**
- Làm gì: viết 4 Điều: Điều 1 quyết định nội dung chính — cấp học bổng / miễn, giảm học phí cho các sinh viên có tên trong danh sách kèm theo (ghi rõ tổng số sinh viên); Điều 2 mức hưởng, tổng kinh phí (số và chữ), nguồn kinh phí, thời gian áp dụng; Điều 3 hiệu lực thi hành (kể từ ngày ký); Điều 4 trách nhiệm thi hành của các đơn vị, cá nhân.
- Dùng input: `loai_quyet_dinh`, `ten_dot`, `tong_kinh_phi`, `nguon_kinh_phi`, `thoi_gian_ap_dung`, `don_vi_thuc_hien`, kết quả Bước 1–2.
- Vai trò: Chuyên viên Phòng Công tác sinh viên · AI hỗ trợ: soạn dự thảo nội dung 4 Điều · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: tổng số sinh viên ở Điều 1 phải bằng số dòng trong danh sách kèm theo; Điều 4 phải nêu tên đầy đủ các đơn vị trong `don_vi_thuc_hien` — thiếu đơn vị thì đơn vị đó không có trách nhiệm thi hành.
- → Kết quả bước: dự thảo nội dung 4 Điều của quyết định.

**Bước 5. Lập danh sách sinh viên kèm theo**
- Làm gì: lập bảng danh sách với các cột STT | Họ và tên | Mã SV | Lớp | Khoa | Mức học bổng (hoặc Mức miễn/giảm) | Ghi chú; đánh số thứ tự liên tục; sắp xếp theo khoa/lớp; thêm dòng tổng cộng cuối bảng (tổng số SV, tổng kinh phí).
- Dùng input: `danh_sach`.
- Vai trò: Chuyên viên Phòng Công tác sinh viên · AI hỗ trợ: lập bảng danh sách sinh viên, thêm dòng tổng cộng · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: tiêu đề danh sách phải ghi rõ "Kèm theo Quyết định số ... ngày ... của Hiệu trưởng" — danh sách không gắn với quyết định cụ thể thì không có giá trị pháp lý; mức hưởng từng sinh viên trong bảng phải khớp mức đã duyệt ở biên bản hội đồng.
- → Kết quả bước: bảng danh sách sinh viên kèm theo (có dòng tổng cộng).

**Bước 6. Kiểm tra chéo toàn văn**
- Làm gì: kiểm tra thể thức theo Nghị định 30/2020/NĐ-CP; số sinh viên ở Điều 1 khớp số dòng trong danh sách kèm theo; tổng kinh phí bằng số khớp bằng chữ và khớp tổng các mức trong bảng; thẩm quyền ký là Hiệu trưởng; nơi nhận đầy đủ.
- Dùng input: toàn bộ input + dự thảo (đối chiếu chéo).
- Vai trò: Chuyên viên Phòng Công tác sinh viên · AI hỗ trợ: kiểm tra chéo số liệu toàn văn · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: đây là điểm kiểm tra cuối trước khi trình ký — lỗi thường gặp nhất là tổng tiền bảng không khớp Điều 2 và số SV Điều 1 không khớp số dòng bảng; phát hiện lỗi thì quay lại bước tương ứng sửa, không sửa "cho qua".
- → Kết quả bước: kết quả đối chiếu nội bộ (không xuất kèm file) (thể thức, căn cứ, số liệu, thẩm quyền, nơi nhận).

**Bước 7. Xuất bản quyết định**
- Làm gì: hoàn thiện quyết định + danh sách kèm theo theo định dạng đầu ra của skill, sẵn sàng trình Hiệu trưởng ký và ban hành.
- Dùng input: kết quả các Bước 1–6.
- Vai trò: Hiệu trưởng · AI hỗ trợ: chuẩn bị hồ sơ trình ký, nhắc lịch và theo dõi tiến độ · ⏱ ~1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: sau khi ký, lưu hồ sơ quyết định và danh sách kèm theo tại Phòng CTSV; chuyển bản đến Phòng Tài chính – Kế toán để chi trả — quyết định ký mà không chuyển thì sinh viên không nhận được học bổng.
- → Kết quả bước: quyết định cấp học bổng / miễn giảm học phí hoàn chỉnh + danh sách kèm theo, sẵn sàng trình ký.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Danh sách SV và biên bản hội đồng"/] --> B1["Bước 1: Kiểm tra và làm sạch danh sách đầu vào"]
    B1 --> B2["Bước 2: Tính tổng kinh phí và đối chiếu nguồn"]
    B2 --> B3["Bước 3: Dựng khung thể thức quyết định"]
    B3 --> B4["Bước 4: Soạn nội dung 4 Điều"]
    B4 --> B5["Bước 5: Lập danh sách sinh viên kèm theo"]
    B5 --> B6["Bước 6: Kiểm tra chéo toàn văn"]
    B6 --> B7["Bước 7: Xuất bản quyết định"]
    B7 --> OUT[["Quyết định cấp học bổng hoàn chỉnh"]]
```

## Đầu ra
- Văn bản quyết định hoàn chỉnh (4 Điều).
- Danh sách sinh viên kèm theo dạng bảng (STT, họ tên, mã SV, lớp, khoa, mức hưởng).
- Checklist kiểm tra thể thức và số liệu.

**Cấu trúc output chuẩn:** khung mẫu cố định của sản phẩm chính — Quyết định cấp học bổng /
miễn giảm học phí, các phần bắt buộc theo đúng thứ tự:
1. Quốc hiệu – Tiêu ngữ; tên cơ quan ban hành; số, ký hiệu văn bản; địa danh, ngày tháng năm.
2. Tiêu đề "QUYẾT ĐỊNH" + trích yếu (V/v...).
3. Tên và chức danh người ký (HIỆU TRƯỞNG TRƯỜNG ĐẠI HỌC...).
4. Các căn cứ (quy chế học bổng, biên bản họp hội đồng, tờ trình — viện dẫn theo trình tự).
5. Điều 1: nội dung cấp học bổng / miễn, giảm học phí + tổng số sinh viên (danh sách kèm theo).
6. Điều 2: mức hưởng từng sinh viên (theo danh sách kèm theo), tổng kinh phí (bằng số và bằng chữ), nguồn kinh phí, thời gian áp dụng.
7. Điều 3: hiệu lực thi hành (kể từ ngày ký).
8. Điều 4: trách nhiệm thi hành của các đơn vị, cá nhân có tên.
9. Nơi nhận.
10. Chữ ký (Hiệu trưởng: chức danh, họ tên).
11. Danh sách kèm theo: tiêu đề danh sách + dòng "Kèm theo Quyết định số ... ngày ... của Hiệu trưởng" + bảng (STT | Họ và tên | Mã SV | Lớp | Khoa | Mức học bổng/Mức miễn giảm | Ghi chú) + dòng tổng cộng (tổng số SV – tổng kinh phí).

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao
Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Đủ các phần theo "Cấu trúc output chuẩn": quốc hiệu – tiêu ngữ; tiêu đề "QUYẾT ĐỊNH" + trích yếu; tên và chức danh người ký; các căn cứ; Điều 1–4; nơi nhận; chữ ký; danh sách kèm theo có dòng "Kèm theo Quyết định số ... ngày ..." + bảng + dòng tổng cộng.
- [ ] Danh sách sinh viên khớp Input: đủ họ tên, mã SV, lớp, khoa, mức hưởng; không trùng mã SV.
- [ ] Số sinh viên ở Điều 1 khớp số dòng trong danh sách kèm theo.
- [ ] Tổng kinh phí bằng số khớp bằng chữ và khớp tổng các mức trong bảng.
- [ ] Mỗi sinh viên trong quyết định đều có trong biên bản họp hội đồng xét.
- [ ] Không bịa đặt danh sách sinh viên, mức hưởng, số hiệu biên bản hội đồng, văn bản căn cứ.
- [ ] Thể thức đúng Nghị định 30/2020/NĐ-CP; căn cứ còn hiệu lực, viện dẫn đúng trình tự; thẩm quyền ký là Hiệu trưởng.
- [ ] Đã qua Human gate: Hội đồng xét họp và thống nhất danh sách; Hiệu trưởng ký.
- [ ] Sau ký: chuyển bản đến Phòng Tài chính – Kế toán để chi trả; lưu hồ sơ tại Phòng CTSV.

## Căn cứ & lưu ý
- Nghị định 30/2020/NĐ-CP về công tác văn thư (thể thức quyết định).
- Quyết định 44/2007/QĐ-BGDĐT về học bổng khuyến khích học tập.
- Đối với miễn, giảm học phí: căn cứ Nghị định 81/2021/NĐ-CP về cơ chế thu, quản lý
  học phí và chính sách miễn, giảm học phí, hỗ trợ chi phí học tập.
- Quyết định cấp học bổng tài trợ phải phù hợp với văn bản thỏa thuận tài trợ.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Tư liệu đối chiếu
Bản gốc trước cập nhật pháp lý (kèm ví dụ giả lập) lưu tại `references/quy-trinh-lich-su.md`, chỉ để đối chiếu hồ sơ lịch sử; không dùng căn cứ, mẫu hay số liệu trong đó làm chỉ dẫn hiện hành.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
