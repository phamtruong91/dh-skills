---
name: "soan-to-trinh"
description: "Soạn tờ trình xin chủ trương, phê duyệt của Ban Giám hiệu / Hội đồng trường / cấp trên. Dùng cho mọi đề xuất cần được phê duyệt trước khi triển khai trong trường đại học."
---

# Soạn tờ trình

## Quy cách đầu ra và thông tin thiếu

Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm văn bản hoặc sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hoặc dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Các trường “bắt buộc” là điều kiện hoàn thiện hồ sơ, không ngăn việc soạn bản có chỗ chừa để điền. Mọi chỉ dẫn “để trống” trong skill được hiểu là không điền dữ liệu và giữ cách chừa chỗ của mẫu gốc, không phải xóa dấu chấm của mẫu.


## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu nội bộ hồ sơ có yếu tố pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp; không tự đính kèm bảng kiểm tra vào file giao.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Văn bản soạn chưa được coi là đã ban hành; không tự chèn nhãn trạng thái kiểm duyệt vào file giao; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.

## Khi nào dùng
Khi một đơn vị/cá nhân cần trình lãnh đạo xem xét, quyết định một chủ trương, kế hoạch, dự án,
kinh phí...: mở ngành, tổ chức sự kiện, mua sắm, cử đi công tác, ban hành văn bản...

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_to_trinh` | Tên tờ trình (ngắn gọn, nêu việc đề xuất) | Có |
| `kinh_gui` | Ban Giám hiệu / Hội đồng trường / Hiệu trưởng... | Có |
| `don_vi_trinh` | Đơn vị trình tờ trình | Có |
| `can_cu` | Các căn cứ pháp lý, thực tiễn (quy định, công văn, tình hình) | Có |
| `noi_dung_de_xuat` | Nội dung đề xuất chi tiết, dạng gạch đầu dòng | Có |
| `kien_nghi` | Kiến nghị cụ thể mong lãnh đạo quyết định | Có |
| `tai_lieu_kem_theo` | Danh mục tài liệu đính kèm (dự thảo, dự toán...) | Không |

## Quy trình

**Bước 1. Xác định việc đề xuất và thẩm quyền phê duyệt**
- Làm gì: Đọc `ten_to_trinh` và `noi_dung_de_xuat`, tóm tắt việc đề xuất trong một câu (làm gì – cho ai – để đạt gì); đọc `kinh_gui` để xác định cấp phê duyệt (Ban Giám hiệu / Hiệu trưởng / Hội đồng trường / cấp trên) vì cấp phê duyệt quyết định độ chi tiết số liệu và căn cứ cần viện dẫn; kiểm tra `don_vi_trinh` có đúng là đơn vị được giao nhiệm vụ liên quan không.
- Dùng input: `ten_to_trinh`, `kinh_gui`, `don_vi_trinh`, `noi_dung_de_xuat`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: phân tích input, xác định yêu cầu · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Việc vượt thẩm quyền của Ban Giám hiệu (vd: mở ngành mới, chiến lược dài hạn) phải trình Hội đồng trường — xác định sai cấp phê duyệt là lỗi nghiêm trọng khiến tờ trình bị trả lại.
- → Kết quả bước: Xác nhận việc đề xuất + cấp phê duyệt phù hợp.

**Bước 2. Thu thập và sắp xếp căn cứ**
- Làm gì: Từ `can_cu`, liệt kê từng văn bản pháp lý/quy định/công văn liên quan, kiểm tra hiệu lực (văn bản còn hiệu lực, không bị thay thế), sắp xếp từ văn bản có hiệu lực cao xuống thấp (luật → nghị định/thông tư → quy chế trường → nghị quyết hội đồng trường → công văn), bổ sung căn cứ thực tiễn (số liệu năm trước, tình hình thực tế) nếu `can_cu` còn thiếu.
- Dùng input: `can_cu`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: xử lý sơ bộ theo quy trình · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Bẫy thường gặp — viện dẫn văn bản đã hết hiệu lực hoặc bị thay thế; căn cứ thực tiễn thiếu số liệu khiến lý do đề xuất yếu. Mỗi căn cứ phải ghi đủ tên văn bản, số/ký hiệu, ngày ban hành.
- → Kết quả bước: Danh sách căn cứ đã kiểm chuẩn, sắp xếp đúng thứ tự hiệu lực.

**Bước 3. Xây dựng nội dung đề xuất chi tiết**
- Làm gì: Chuyển từng gạch đầu dòng trong `noi_dung_de_xuat` thành các mục đánh số 1., 2., 3..., mỗi mục một nội dung trọn vẹn; với nội dung liên quan kinh phí/nhân sự/thời gian, bổ sung số liệu cụ thể (tổng số, mức tăng/giảm so với năm trước, mốc thời gian); kiểm tra số liệu giữa các mục có nhất quán không; đối chiếu `tai_lieu_kem_theo` để đảm bảo tài liệu đính kèm khớp với nội dung đề xuất.
- Dùng input: `noi_dung_de_xuat`, `tai_lieu_kem_theo`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Đề xuất xin kinh phí phải có dự toán chi tiết ở tài liệu kèm theo, không dồn hết số liệu vào thân tờ trình; tránh đề xuất chung chung kiểu "tổ chức hiệu quả" mà thiếu chỉ tiêu đo được.
- → Kết quả bước: Dự thảo nội dung đề xuất có số liệu nhất quán + danh mục tài liệu kèm theo đã đối chiếu.

**Bước 4. Viết mở đầu và kiến nghị**
- Làm gì: Viết đoạn mở đầu sau dòng "Kính gửi": nêu lý do, sự cần thiết của việc đề xuất (gắn với nhiệm vụ của đơn vị và tình hình thực tế); sau phần nội dung đề xuất, viết kiến nghị: nêu dứt khoát trong 1–2 câu điều mong lãnh đạo xem xét, quyết định (phê duyệt cái gì, giao cho ai triển khai), lấy nguyên văn ý từ `kien_nghi`.
- Dùng input: `ten_to_trinh`, `don_vi_trinh`, `kien_nghi`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Kiến nghị phải là câu cầu khiến rõ ràng ("Kính đề nghị ... phê duyệt ..."), không viết lưng chừng kiểu "mong lãnh đạo cho ý kiến"; kiến nghị phải khớp đúng phạm vi nội dung đã đề xuất ở Bước 3.
- → Kết quả bước: Đoạn mở đầu + đoạn kiến nghị hoàn chỉnh.

**Bước 5. Dựng thể thức và phần kết thúc**
- Làm gì: Lắp ráp phần đầu: tên trường + quốc hiệu – tiêu ngữ, tên `don_vi_trinh`, số/ký hiệu tờ trình (ký hiệu TTr), địa danh ngày tháng, dòng chữ "TỜ TRÌNH" + tên tờ trình (in hoa, căn giữa), dòng "Kính gửi" + `kinh_gui`; phần kết thúc: câu kết "./.", nơi nhận ("- [cấp phê duyệt];", "- Lưu: VT, [mã đơn vị]."), danh mục tài liệu kèm theo, khối chữ ký người đứng đầu đơn vị trình (chức danh + họ tên).
- Dùng input: `don_vi_trinh`, `ten_to_trinh`, `kinh_gui`, `tai_lieu_kem_theo`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Người ký tờ trình là thủ trưởng đơn vị trình (Trưởng phòng/Trưởng khoa), không phải Hiệu trưởng; số tờ trình lấy tiếp theo sổ văn bản đi của đơn vị với ký hiệu "TTr".
- → Kết quả bước: Khung tờ trình hoàn chỉnh về thể thức, đã lắp đủ mở đầu – căn cứ – đề xuất – kiến nghị – kết thúc.

**Bước 6. Kiểm tra logic và số liệu**
- Làm gì: Đọc liền mạch từ lý do → căn cứ → đề xuất → kiến nghị, kiểm tra: lý do có dẫn tới đúng nội dung đề xuất không; căn cứ có đủ cơ sở pháp lý cho nội dung đề xuất không; kiến nghị có bao quát hết nội dung đề xuất không; số liệu trong thân tờ trình có khớp với tài liệu kèm theo không; chính tả, tên văn bản viện dẫn chính xác.
- Dùng input: toàn bộ input (đối chiếu chéo).
- Vai trò: Chuyên viên Phòng HCTH (Trưởng phòng kiểm tra lại) · AI hỗ trợ: quét lỗi theo checklist · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: Lỗi phổ biến — kiến nghị xin phê duyệt nội dung không có trong phần đề xuất, hoặc đề xuất có nội dung nhưng kiến nghị không nhắc tới; số liệu tổng trong thân không khớp bảng chi tiết đính kèm.
- → Kết quả bước: Báo cáo kiểm tra logic + danh sách lỗi cần sửa (nếu có), trả về bước tương ứng để chỉnh.

**Bước 7. Xuất bản tờ trình trình ký**
- Làm gì: Ghép toàn bộ thành tờ trình hoàn chỉnh ở định dạng markdown; đính kèm ghi chú các tài liệu cần đính kèm theo tờ trình; chuyển cho thủ trưởng đơn vị trình duyệt (human gate) trước khi trình lên cấp phê duyệt.
- Dùng input: toàn bộ.
- Vai trò: Chuyên viên Phòng HCTH chuẩn bị, Hiệu trưởng phê duyệt · AI hỗ trợ: tổng hợp hồ sơ, soạn phiếu trình/tờ trình đầy đủ · ⏱ ~15–30 phút chuẩn bị + chờ duyệt (ước tính)
- Lưu ý nghiệp vụ: Không sửa nội dung đề xuất sau khi thủ trưởng đơn vị đã ký nháy/duyệt mà không xin ý kiến lại.
- → Kết quả bước: Tờ trình hoàn chỉnh + ghi chú tài liệu đính kèm, sẵn sàng trình ký.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Đề xuất cần trình lãnh đạo"/] --> B1["Bước 1: Xác định việc đề xuất và thẩm quyền phê duyệt"]
    B1 --> B2["Bước 2: Thu thập và sắp xếp căn cứ"]
    B2 --> B3["Bước 3: Xây dựng nội dung đề xuất chi tiết"]
    B3 --> B4["Bước 4: Viết mở đầu và kiến nghị"]
    B4 --> B5["Bước 5: Dựng thể thức và phần kết thúc"]
    B5 --> B6["Bước 6: Kiểm tra logic và số liệu"]
    B6 --> HG["👤 Thủ trưởng đơn vị duyệt tờ trình"]
    HG --> OUT[["Tờ trình trình ký"]]
```

## Đầu ra

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Nội dung và số liệu trong output khớp đúng với Input đã cho (không thêm, bớt hay suy diễn)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức và định dạng theo Tờ trình là văn bản nội bộ xin ý kiến quyết định — ngôn ngữ trang t…
- [ ] Căn cứ pháp lý được trích dẫn đầy đủ và còn hiệu lực
- [ ] Không coi bản soạn là đã ký/đã duyệt; việc phê duyệt thuộc người có thẩm quyền trước phát hành
- [ ] Mỗi căn cứ phải ghi đủ tên văn bản, số/ký hiệu, ngày ban hành
- [ ] Đề xuất xin kinh phí phải có dự toán chi tiết ở tài liệu kèm theo, không dồn hết số liệu vào thân tờ trình
- [ ] Tránh đề xuất chung chung kiểu "tổ chức hiệu quả" mà thiếu chỉ tiêu đo được

## Căn cứ & lưu ý
- Tờ trình là văn bản nội bộ xin ý kiến quyết định — ngôn ngữ trang trọng, kiến nghị dứt khoát.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.2.1`; ngày cập nhật: `2026-10-10`.
- Kho nguồn: https://github.com/phamtruong91/university-skills-framework
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `346719e6b0318ed034b4b016703f79733aa575e7`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/soan-to-trinh`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
