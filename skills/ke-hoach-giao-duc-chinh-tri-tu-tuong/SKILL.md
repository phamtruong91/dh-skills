---
name: "ke-hoach-giao-duc-chinh-tri-tu-tuong"
description: "Soạn kế hoạch giáo dục chính trị, tư tưởng cho CBVC và sinh viên trong trường đại học: học tập nghị quyết, sinh hoạt chuyên đề, tuyên truyền. Dùng khi lập kế hoạch năm học hoặc đợt sinh hoạt chính trị."
---

# Soạn kế hoạch giáo dục chính trị, tư tưởng

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
Khi đơn vị phụ trách công tác chính trị (Phòng Chính trị & CTSV hoặc Ban Tuyên giáo)
lập kế hoạch giáo dục chính trị, tư tưởng năm học hoặc kế hoạch đợt sinh hoạt chuyên đề
(học tập nghị quyết, kỷ niệm ngày lễ lớn, phòng chống "tự diễn biến", "tự chuyển hóa").

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `nam_hoc_dot` | Năm học hoặc đợt sinh hoạt | Có |
| `doi_tuong` | CBVC / Sinh viên / Cả hai (có thể chia nhóm) | Có |
| `noi_dung_trong_tam` | Các chuyên đề, nội dung giáo dục | Có |
| `hinh_thuc` | Hội nghị học tập, sinh hoạt chi bộ/chi đoàn, tọa đàm, trực tuyến... | Có |
| `don_vi_phoi_hop` | Đảng ủy, Đoàn Thanh niên, Hội Sinh viên, các khoa... | Không |

## Quy trình

**Bước 1. Xác định yêu cầu theo chỉ đạo**
- Làm gì: căn cứ chỉ đạo của Đảng ủy cấp trên và Đảng ủy trường về công tác tư tưởng trong
  năm học/đợt; xác định yêu cầu, trọng tâm, thời gian thực hiện.
- Dùng input: `nam_hoc_dot`.
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: rà soát kỹ thuật, tổng hợp và lưu trữ hồ sơ · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: mọi nội dung sau này phải bám sát chỉ đạo — không tự đặt chủ đề ngoài
  văn bản chỉ đạo.
- → Kết quả bước: khung yêu cầu công tác chính trị, tư tưởng của năm học/đợt.

**Bước 2. Xây dựng nội dung theo 3 nhóm**
- Làm gì: xây dựng nội dung theo 3 nhóm: (1) học tập, quán triệt nghị quyết, chỉ thị; (2)
  sinh hoạt chuyên đề tư tưởng, đạo đức, lối sống; (3) tuyên truyền kỷ niệm các ngày lễ lớn,
  đấu tranh phản bác quan điểm sai trái.
- Dùng input: `noi_dung_trong_tam`, khung yêu cầu (kết quả bước 1).
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: soạn dự thảo nội dung · ⏱ ~2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: nội dung bám sát văn kiện, nghị quyết, chỉ thị chính thức; tuyệt đối không
  tự diễn giải đường lối hoặc đưa quan điểm cá nhân.
- → Kết quả bước: dự thảo nội dung 3 nhóm.

**Bước 3. Phân đối tượng CBVC và sinh viên**
- Làm gì: phân nội dung, hình thức phù hợp riêng cho CBVC và sinh viên (có thể chia nhóm);
  xác định nội dung chung cho cả hai đối tượng.
- Dùng input: `doi_tuong`, dự thảo nội dung (kết quả bước 2).
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: phân loại, đề xuất nội dung theo đối tượng CBVC/sinh viên · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: với sinh viên ưu tiên hình thức sinh động (tọa đàm, thi trực tuyến, sinh
  hoạt chi đoàn); với CBVC ưu tiên hội nghị, sinh hoạt chi bộ.
- → Kết quả bước: bảng nội dung phân theo đối tượng (CBVC / sinh viên / chung).

**Bước 4. Lập tiến độ chi tiết**
- Làm gì: lập bảng tiến độ cho từng hoạt động: nội dung, đối tượng, hình thức, thời gian, địa
  điểm, đơn vị chủ trì, đơn vị phối hợp.
- Dùng input: `hinh_thuc`, `don_vi_phoi_hop`, bảng nội dung theo đối tượng (kết quả bước 3).
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: lập bảng tiến độ chi tiết dự thảo · ⏱ ~2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: thời gian không trùng các đợt cao điểm (thi cử, tuyển sinh); mỗi hoạt động
  có một đơn vị chủ trì chịu trách nhiệm duy nhất.
- → Kết quả bước: bảng tiến độ chi tiết từng hoạt động.

**Bước 5. Kiểm tra nội dung**
- Làm gì: kiểm tra nội dung bám sát chỉ đạo của Đảng ủy; hình thức đa dạng, tránh hình thức,
  phong trào; rà soát mọi trích dẫn văn kiện từ nguồn chính thức.
- Dùng input: dự thảo nội dung và tiến độ (kết quả bước 2–4).
- Vai trò: Văn phòng Đảng ủy · AI hỗ trợ: đối chiếu checklist · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chưa đạt thì quay lại điều chỉnh nội dung (bước 2); tuyệt đối không dùng
  AI "sáng tác" trích dẫn lãnh tụ, văn kiện.
- → Kết quả bước: dự thảo kế hoạch đã kiểm tra, đạt yêu cầu.

**Bước 6. Trình Đảng ủy phê duyệt và ban hành**
- Làm gì: trình Đảng ủy duyệt nội dung chính trị, tư tưởng (Human gate); sau khi phê duyệt,
  ban hành kế hoạch và triển khai trong toàn trường.
- Dùng input: dự thảo kế hoạch (kết quả bước 5).
- Vai trò: Đảng ủy · AI hỗ trợ: chuẩn bị hồ sơ trình ký, nhắc lịch và theo dõi tiến độ · ⏱ ~3–7 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: Đảng ủy chưa phê duyệt thì quay lại điều chỉnh; kế hoạch chỉ triển khai
  sau khi có phê duyệt.
- → Kết quả bước: kế hoạch giáo dục chính trị, tư tưởng hoàn chỉnh, đã phê duyệt.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Năm học hoặc đợt, đối tượng, nội dung trọng tâm, hình thức"/] --> B1["Bước 1: Xác định yêu cầu theo chỉ đạo"]
    B1 --> B2["Bước 2: Xây dựng nội dung theo 3 nhóm"]
    B2 --> B3["Bước 3: Phân đối tượng CBVC và sinh viên"]
    B3 --> B4["Bước 4: Lập tiến độ chi tiết"]
    B4 --> B5["Bước 5: Kiểm tra nội dung"]
    B5 --> B6["Bước 6: Trình Đảng ủy phê duyệt và ban hành"]
    B6 --> HG["👤 Đảng ủy duyệt nội dung chính trị"]
    HG --> OUT[["Kế hoạch giáo dục chính trị, tư tưởng"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Nội dung đủ 3 nhóm: (1) học tập, quán triệt nghị quyết, chỉ thị; (2) sinh hoạt chuyên đề tư tưởng, đạo đức, lối sống; (3) tuyên truyền kỷ niệm ngày lễ lớn, đấu tranh phản bác quan điểm sai trái.
- [ ] Năm học/đợt, đối tượng, hình thức trong output khớp với Input đã cho.
- [ ] Không bịa đặt trích dẫn lãnh tụ, văn kiện; mọi trích dẫn đều kiểm chứng từ nguồn chính thức; không diễn giải đường lối hay đưa quan điểm cá nhân.
- [ ] Đúng thể thức văn bản kế hoạch của đơn vị chủ trì (Đảng ủy – Phòng Chính trị và CTSV).
- [ ] Căn cứ (văn kiện, nghị quyết của Đảng; chỉ đạo của Đảng ủy cấp trên và Đảng ủy trường) còn hiệu lực; nội dung bám sát chỉ đạo, không tự đặt chủ đề ngoài văn bản chỉ đạo.
- [ ] Đã qua Human gate: Đảng ủy trường duyệt nội dung chính trị, tư tưởng trước khi ban hành; kế hoạch chỉ triển khai sau khi được phê duyệt.
- [ ] Nội dung, hình thức phân theo đối tượng phù hợp (hội nghị, sinh hoạt chi bộ cho CBVC; tọa đàm, thi trực tuyến, sinh hoạt chi đoàn cho sinh viên); tiến độ không trùng đợt cao điểm (thi cử, tuyển sinh); mỗi hoạt động có một đơn vị chủ trì duy nhất.

Tiêu chí đạt = tất cả các ô được đánh dấu.


## Human gate (người kiểm duyệt)
- Đảng ủy trường duyệt nội dung chính trị, tư tưởng trước khi ban hành.
- Ban Giám hiệu phối hợp chỉ đạo triển khai trong toàn trường.

## Giới hạn (guardrails)
- Nội dung phải bám sát văn kiện, nghị quyết, chỉ thị chính thức; **tuyệt đối không**
  tự diễn giải, suy đoán đường lối hoặc đưa quan điểm cá nhân vào tài liệu giáo dục.
- Không dùng AI để "sáng tác" trích dẫn lãnh tụ, văn kiện — mọi trích dẫn phải kiểm chứng
  từ nguồn chính thức.
- Mọi dữ liệu trong ví dụ đều giả lập.

## Căn cứ & lưu ý
- Văn kiện, nghị quyết của Đảng; chỉ đạo của Đảng ủy cấp trên và Đảng ủy trường.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
