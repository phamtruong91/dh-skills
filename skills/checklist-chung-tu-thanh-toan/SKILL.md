---
name: "checklist-chung-tu-thanh-toan"
description: "Lập checklist chứng từ thanh toán cho từng loại chi của trường đại học (lương, học bổng, đề tài NCKH, mua sắm, công tác phí, tiếp khách – hội nghị). Dùng khi Phòng Tài chính – Kế toán kiểm soát tính đầy đủ, hợp lệ của bộ chứng từ trước khi chi tiền."
---

# Lập checklist chứng từ thanh toán

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .xlsx, .csv, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.xlsx**. Nếu yêu cầu gồm cả báo cáo thuyết minh, tạo thêm file Word cho báo cáo; không ghép báo cáo dài vào bảng tính. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu

Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm văn bản hoặc sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hoặc dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Các trường “bắt buộc” là điều kiện hoàn thiện hồ sơ, không ngăn việc soạn bản có chỗ chừa để điền. Mọi chỉ dẫn “để trống” trong skill được hiểu là không điền dữ liệu và giữ cách chừa chỗ của mẫu gốc, không phải xóa dấu chấm của mẫu.


## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu nội bộ hồ sơ có yếu tố pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp; không tự đính kèm bảng kiểm tra vào file giao.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Văn bản soạn chưa được coi là đã ban hành; không tự chèn nhãn trạng thái kiểm duyệt vào file giao; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.

## Khi nào dùng
Khi kiểm tra, đối chiếu bộ chứng từ của một khoản chi trước khi trình ký thanh toán:
xác định chứng từ bắt buộc theo từng loại chi, đơn vị lập, và các điểm kiểm soát trọng yếu.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `loai_chi` | Một trong 6 loại: (a) lương–phụ cấp, (b) học bổng–hỗ trợ SV, (c) đề tài NCKH, (d) mua sắm tài sản–thiết bị, (e) công tác phí, (f) tiếp khách–hội nghị | Có |
| `noi_dung_chi` | Nội dung cụ thể của khoản chi (vd: thanh toán đợt 2 hợp đồng mua máy chiếu) | Có |
| `so_tien` | Số tiền đề nghị thanh toán | Có |
| `chung_tu_hien_co` | Danh sách chứng từ đơn vị đã nộp (để đánh dấu đủ/thiếu) | Không |
| `don_vi_de_nghi` | Đơn vị đề nghị thanh toán | Có |

## Quy trình

**Bước 1. Xác định đúng loại chi**
- Làm gì: căn cứ `loai_chi` đã khai báo và đối chiếu với `noi_dung_chi`, `so_tien` thực tế;
  nếu nội dung chi không thuộc nhóm đã chọn (ví dụ khai (d) mua sắm nhưng thực chất là
  thuê dịch vụ tổ chức hội nghị), phân loại lại cho đúng trước khi lập checklist.
- Dùng input: `loai_chi`, `noi_dung_chi`, `so_tien`.
- Vai trò: Chuyên viên Phòng TCKT · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: phân loại sai loại chi dẫn đến áp sai danh mục chứng từ — kiểm tra bản
  chất khoản chi (mua tài sản, thuê dịch vụ, chi cho con người), không chỉ dựa vào tên gọi
  của đơn vị đề nghị.
- → Kết quả bước: phiếu phân loại chi (loại chi đã xác định trong 6 nhóm + nội dung chi).

**Bước 2. Liệt kê chứng từ bắt buộc, đơn vị lập và lưu ý kiểm soát theo loại chi**
- Làm gì: lấy danh mục chứng từ chuẩn của loại chi đã xác định ở Bước 1 (xem chi tiết
  (a)–(f) bên dưới); với mỗi chứng từ ghi rõ đơn vị lập và các điểm kiểm soát trọng yếu.
- Dùng input: kết quả Bước 1 (loại chi).
- Vai trò: Chuyên viên Phòng TCKT · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: danh mục chứng từ của từng loại chi là cố định theo quy định — không
  được tự ý bớt chứng từ bắt buộc; chứng từ do đơn vị nào lập thì đơn vị đó chịu trách
  nhiệm về tính đúng đắn.
- → Kết quả bước: danh mục chứng từ bắt buộc của loại chi (kèm đơn vị lập và lưu ý kiểm
  soát từng chứng từ).

Danh mục chi tiết theo từng loại chi:

**(a) Chi lương – phụ cấp**
- Chứng từ: Quyết định nâng lương/chuyển ngạch/bổ nhiệm (nếu có thay đổi); bảng chấm công
  (đơn vị lập: các đơn vị, Phòng Tổ chức cán bộ tổng hợp); bảng thanh toán tiền lương,
  phụ cấp (Phòng TCKT lập theo mẫu); danh sách ký nhận/ủy nhiệm chi chuyển khoản;
  quyết định phê duyệt quỹ lương tháng/quý của Hiệu trưởng.
- Đơn vị lập: Phòng Tổ chức cán bộ (chấm công, biến động nhân sự); Phòng TCKT (bảng lương).
- Lưu ý kiểm soát: đối chiếu họ tên, hệ số lương, phụ cấp với quyết định nhân sự còn hiệu lực;
  kiểm tra người nghỉ không lương, nghỉ thai sản đã trừ đúng; chữ ký phê duyệt của Hiệu trưởng.

**(b) Chi học bổng – hỗ trợ sinh viên**
- Chứng từ: Quyết định phê duyệt danh sách học bổng/hỗ trợ của Hiệu trưởng (kèm danh sách
  chi tiết: họ tên, mã SV, lớp, mức, số tiền); biên bản họp Hội đồng xét học bổng;
  bảng điểm/result xét duyệt (Phòng Đào tạo/Phòng CTSV cung cấp); danh sách ký nhận
  hoặc ủy nhiệm chi chuyển khoản vào tài khoản sinh viên.
- Đơn vị lập: Phòng Công tác sinh viên (đề xuất, danh sách); Phòng Đào tạo (kết quả học tập);
  Phòng TCKT (chi trả).
- Lưu ý kiểm soát: sinh viên trong danh sách còn đang theo học (không bảo lưu/bị đình chỉ);
  mức học bổng đúng quy định, không trùng lặp hai nguồn học bổng cùng kỳ; số tài khoản
  nhận đúng tên sinh viên.

**(c) Thanh toán đề tài NCKH**
- Chứng từ: Quyết định phê duyệt đề tài và dự toán kinh phí; hợp đồng thực hiện đề tài
  (giữa Trường và chủ nhiệm đề tài); thuyết minh đề tài đã duyệt; biên bản nghiệm thu
  đề tài (cấp trường/cấp bộ); báo cáo quyết toán kinh phí đề tài; hóa đơn, chứng từ gốc
  của các khoản chi (mua vật tư, thuê chuyên gia, công tác phí...); thanh lý hợp đồng.
- Đơn vị lập: Phòng KHCN (quyết định, hợp đồng, nghiệm thu); chủ nhiệm đề tài (chứng từ chi);
  Phòng TCKT (kiểm tra, thanh toán).
- Lưu ý kiểm soát: nội dung chi đúng dự toán đã duyệt theo thuyết minh; hóa đơn hợp lệ,
  đúng thời gian thực hiện đề tài; nghiệm thu đạt mới thanh toán đợt cuối (thường giữ lại
  10–20% đến khi nghiệm thu).

**(d) Mua sắm tài sản – thiết bị**
- Chứng từ: Tờ trình/đề nghị mua sắm của đơn vị sử dụng; quyết định phê duyệt kế hoạch
  mua sắm; quyết định phê duyệt kết quả lựa chọn nhà thầu (hoặc phê duyệt chỉ định thầu/
  chào hàng cạnh tranh theo hạn mức); hợp đồng mua bán; hóa đơn GTGT; biên bản giao nhận;
  biên bản nghiệm thu, bàn giao đưa vào sử dụng; phiếu nhập kho (nếu qua kho); biên bản
  thanh lý hợp đồng; chứng từ bảo hành (nếu có).
- Đơn vị lập: Đơn vị sử dụng (tờ trình); Phòng Quản trị – Thiết bị (kế hoạch, hợp đồng,
  nghiệm thu); nhà cung cấp (hóa đơn); Phòng TCKT (thanh toán).
- Lưu ý kiểm soát: giá trị mua sắm đúng hạn mức được duyệt theo Luật Đấu thầu; tài sản
  có giá trị từ mức quy định phải ghi tăng TSCĐ và dán mã tài sản; đối chiếu số lượng,
  chủng loại, model trên biên bản nghiệm thu với hợp đồng và hóa đơn.

**(e) Công tác phí**
- Chứng từ: Quyết định/giấy đi công tác (ghi rõ họ tên, chức vụ, nơi đi, thời gian, nhiệm vụ);
  giấy đi đường có xác nhận của nơi đến; vé tàu xe, vé máy bay (cuống vé/hóa đơn điện tử);
  hóa đơn lưu trú; bảng kê thanh toán công tác phí (theo mẫu, Phòng TCKT); báo cáo kết quả
  công tác (đối với đoàn công tác dài ngày/nhiệm vụ quan trọng).
- Đơn vị lập: Đơn vị cử đi (đề xuất); Phòng HCTH/Văn phòng (quyết định); cá nhân đi công tác
  (chứng từ chi); Phòng TCKT (bảng kê, thanh toán).
- Lưu ý kiểm soát: thời gian, địa điểm trên giấy đi đường khớp với quyết định và vé;
  định mức khoán (phụ cấp lưu trú, tiền thuê phòng) đúng Quy chế chi tiêu nội bộ;
  không thanh toán trùng các khoản đã khoán; vé máy bay hạng thương gia chỉ khi được
  phê duyệt riêng theo quy định.

**(f) Tiếp khách – hội nghị**
- Chứng từ: Kế hoạch/tờ trình tổ chức (nêu rõ mục đích, thành phần, thời gian, địa điểm,
  dự toán kinh phí) đã được phê duyệt; quyết định phê duyệt của Hiệu trưởng (đối với
  hội nghị lớn/vượt định mức); hóa đơn dịch vụ (ăn uống, thuê hội trường, in ấn...);
  danh sách đại biểu/khách mời tham dự (ký xác nhận); bảng kê chi tiết các khoản chi;
  biên bản nghiệm thu dịch vụ (nếu thuê đơn vị tổ chức sự kiện).
- Đơn vị lập: Đơn vị tổ chức (kế hoạch, danh sách); Phòng HCTH (phối hợp); nhà cung cấp
  dịch vụ (hóa đơn); Phòng TCKT (kiểm tra, thanh toán).
- Lưu ý kiểm soát: định mức chi tiếp khách đúng Quy chế chi tiêu nội bộ (mức chi/người/
  buổi); không dùng ngân sách cho chi tiếp khách không phục vụ nhiệm vụ; hóa đơn ăn uống
  phải ghi rõ số lượng khách, khớp danh sách đại biểu; chi hội nghị có tài trợ phải tách
  bạch nguồn kinh phí.

**Bước 3. Đối chiếu chứng từ hiện có, đánh dấu Đủ/Thiếu**
- Làm gì: đối chiếu từng chứng từ trong `chung_tu_hien_co` với danh mục bắt buộc ở Bước 2;
  đánh dấu từng dòng "Đủ" hoặc "Thiếu"; chứng từ chưa đến hạn theo tiến độ hợp đồng
  (ví dụ biên bản thanh lý khi chưa thanh toán đợt cuối) ghi rõ "chưa đến hạn", không tính
  là thiếu.
- Dùng input: `chung_tu_hien_co`, kết quả Bước 2.
- Vai trò: Chuyên viên Phòng TCKT · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch, tính toán, phân tích số liệu · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chứng từ thiếu → trả lại đơn vị bổ sung, tuyệt đối không trình ký thanh
  toán khi thiếu chứng từ bắt buộc.
- → Kết quả bước: bảng đối chiếu chứng từ (từng chứng từ bắt buộc + trạng thái Đủ/Thiếu).

**Bước 4. Kiểm tra tính hợp lệ của nội dung chứng từ**
- Làm gì: với các chứng từ đã "Đủ", kiểm tra: số tiền khớp `so_tien`/hợp đồng; chữ ký người
  lập, người duyệt và con dấu đầy đủ; hóa đơn hợp lệ (MST, nội dung, số tiền khớp hợp đồng);
  thời hiệu chứng từ đúng niên độ ngân sách; áp dụng các lưu ý kiểm soát đặc thù của loại
  chi tại Bước 2.
- Dùng input: `so_tien`, kết quả Bước 2 – 3.
- Vai trò: Chuyên viên Phòng TCKT · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch, tính toán, phân tích số liệu · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: chứng từ đủ nhưng sai nội dung (số tiền, chữ ký, con dấu) → yêu cầu đơn
  vị điều chỉnh, không tự sửa thay; nguyên tắc kiểm soát: người lập, người kiểm tra và người
  phê duyệt thanh toán phải độc lập nhau.
- → Kết quả bước: danh sách lỗi chứng từ đã phân loại (thiếu chứng từ / sai nội dung).

**Bước 5. Kết luận kiểm soát và trả kết quả cho đơn vị**
- Làm gì: tổng hợp kết quả Bước 3 – 4 thành kết luận: đủ điều kiện trình ký thanh toán, hoặc
  chưa đủ điều kiện kèm danh mục cụ thể cần bổ sung/điều chỉnh; gửi trả `don_vi_de_nghi`
  để thực hiện; sau khi đơn vị bổ sung đầy đủ thì trình ký thanh toán.
- Dùng input: `don_vi_de_nghi`, kết quả Bước 3 – 4.
- Vai trò: Chuyên viên Phòng TCKT · AI hỗ trợ: tổng hợp, chuẩn hóa dữ liệu, chuẩn bị hồ sơ trình đầy đủ · ⏱ ~1–3 giờ (ước tính)
- Lưu ý nghiệp vụ: kết luận phải nêu đích danh từng chứng từ cần bổ sung, không ghi chung
  chung "bổ sung hồ sơ"; lưu vết các lần trả lại để theo dõi.
- → Kết quả bước: kết luận kiểm soát (đủ điều kiện trình ký / yêu cầu bổ sung chi tiết).

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Loại chi và bộ chứng từ hiện có"/] --> B["Xác định đúng loại chi trong 6 nhóm"]
    B --> C["Liệt kê chứng từ bắt buộc, đơn vị lập, lưu ý kiểm soát"]
    C --> D["Đánh dấu từng chứng từ: Đủ hoặc Thiếu"]
    D --> E{"Đủ chứng từ bắt buộc?"}
    E -->|Thiếu| F["Trả lại đơn vị bổ sung"]
    F --> D
    E -->|Đủ| G["Kiểm tra tính hợp lệ nội dung chứng từ"]
    G --> H{"Nội dung hợp lệ?"}
    H -->|Sai| I["Yêu cầu điều chỉnh"]
    I --> G
    H -->|Đúng| HG["👤 Kế toán trưởng kiểm soát"]
    HG --> J[["Kết luận đủ điều kiện trình ký thanh toán"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Có đầy đủ sản phẩm: Bảng checklist chứng từ đầy đủ cho loại chi được yêu cầu, gồm các cột: TT, Chứng từ bắt
- [ ] Có đầy đủ sản phẩm: Kết luận kiểm soát: đủ điều kiện trình ký thanh toán hay phải bổ sung
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Phân loại sai loại chi dẫn đến áp sai danh mục chứng từ — kiểm tra bản
- [ ] Danh mục chứng từ của từng loại chi là cố định theo quy định — không

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Căn cứ & lưu ý
- Luật Kế toán 2015: mọi nghiệp vụ kinh tế, tài chính phát sinh đều phải lập chứng từ
  kế toán; chứng từ phải đầy đủ, hợp lệ, hợp pháp trước khi ghi sổ và chi tiền.
- Luật Đấu thầu 2023 (sửa đổi): tuân thủ hạn mức, hình thức lựa chọn nhà thầu đối với
  chi mua sắm tài sản, thiết bị.
- Quy chế chi tiêu nội bộ của trường là căn cứ định mức trực tiếp cho công tác phí,
  tiếp khách – hội nghị, khoán chi.
- Nguyên tắc kiểm soát: người lập chứng từ, người kiểm tra và người phê duyệt thanh toán
  phải độc lập nhau; không chi tiền khi thiếu chứng từ bắt buộc.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.3.1`; ngày cập nhật: `2026-10-10`.
- Kho nguồn: https://github.com/phamtruong91/university-skills-framework
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `346719e6b0318ed034b4b016703f79733aa575e7`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/checklist-chung-tu-thanh-toan`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
