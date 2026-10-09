---
name: "ke-hoach-giao-duc-chinh-tri-tu-tuong"
description: "Soạn kế hoạch giáo dục chính trị, tư tưởng cho CBVC và sinh viên trong trường đại học: học tập nghị quyết, sinh hoạt chuyên đề, tuyên truyền. Dùng khi lập kế hoạch năm học hoặc đợt sinh hoạt chính trị."
---

# Soạn kế hoạch giáo dục chính trị, tư tưởng

## Quy cách đầu ra và thông tin thiếu

Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm văn bản hoặc sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hoặc dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Các trường “bắt buộc” là điều kiện hoàn thiện hồ sơ, không ngăn việc soạn bản có chỗ chừa để điền. Mọi chỉ dẫn “để trống” trong skill được hiểu là không điền dữ liệu và giữ cách chừa chỗ của mẫu gốc, không phải xóa dấu chấm của mẫu.


## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu nội bộ hồ sơ có yếu tố pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp; không tự đính kèm bảng kiểm tra vào file giao.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Văn bản soạn chưa được coi là đã ban hành; không tự chèn nhãn trạng thái kiểm duyệt vào file giao; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.

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
    IN[/"Năm học hoặc đợt, đối tượng, nội dung trọng tâm, hình thức"/]
    IN --> A["Bước 1. Xác định yêu cầu theo chỉ đạo"]
    A --> B["Bước 2. Xây dựng nội dung theo 3 nhóm"]
    B --> C["Bước 3. Phân đối tượng CBVC và sinh viên"]
    C --> D["Bước 4. Lập tiến độ chi tiết"]
    D --> E{"Nội dung bám sát chỉ đạo, hình thức đa dạng?"}
    E -->|Không| B
    E -->|Có| HG["👤 Đảng ủy duyệt nội dung chính trị"]
    HG --> F{"Đảng ủy phê duyệt?"}
    F -->|Không| B
    F -->|Có| G["Bước 6. Trình Đảng ủy phê duyệt và ban hành"]
    G --> OUT[["Kế hoạch giáo dục chính trị, tư tưởng"]]
```

## Đầu ra

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

- Phiên bản gói: `1.2.1`; ngày cập nhật: `2026-10-10`.
- Kho nguồn: https://github.com/phamtruong91/university-skills-framework
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `346719e6b0318ed034b4b016703f79733aa575e7`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/ke-hoach-giao-duc-chinh-tri-tu-tuong`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
