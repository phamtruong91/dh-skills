---
name: "soan-bien-ban-hop"
description: "Soạn biên bản cuộc họp / hội nghị / hội đồng từ ghi chép, gồm thành phần, diễn biến và kết luận. Dùng cho giao ban, họp hội đồng, họp đơn vị."
---

# Soạn biên bản cuộc họp

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu

Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm văn bản hoặc sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hoặc dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Các trường “bắt buộc” là điều kiện hoàn thiện hồ sơ, không ngăn việc soạn bản có chỗ chừa để điền. Mọi chỉ dẫn “để trống” trong skill được hiểu là không điền dữ liệu và giữ cách chừa chỗ của mẫu gốc, không phải xóa dấu chấm của mẫu.


## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu nội bộ hồ sơ có yếu tố pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp; không tự đính kèm bảng kiểm tra vào file giao.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Văn bản soạn chưa được coi là đã ban hành; không tự chèn nhãn trạng thái kiểm duyệt vào file giao; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.

## Khi nào dùng
Sau mỗi cuộc họp, hội nghị, phiên họp hội đồng cần lập biên bản ghi nhận diễn biến và kết luận
làm căn cứ triển khai.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_cuoc_hop` | Tên cuộc họp | Có |
| `thoi_gian` | Ngày, giờ bắt đầu – kết thúc | Có |
| `dia_diem` | Địa điểm họp | Có |
| `chu_tri` | Người chủ trì | Có |
| `thu_ky` | Thư ký ghi biên bản | Có |
| `thanh_phan` | Thành phần tham dự (và vắng mặt có lý do) | Có |
| `noi_dung` | Nội dung họp: từng vấn đề, ý kiến phát biểu chính | Có |
| `ket_luan` | Kết luận / phân công nhiệm vụ của chủ trì | Có |

## Quy trình

**Bước 1. Thu thập và đối chiếu ghi chép cuộc họp**
- Làm gì: Thu thập ghi chép/bản ghi âm cuộc họp; đối chiếu thông tin hành chính: `ten_cuoc_hop`, `thoi_gian` (giờ bắt đầu – kết thúc), `dia_diem`, `chu_tri`, `thu_ky`, `thanh_phan` (người dự, người vắng mặt và lý do); kiểm tra tên, chức danh người dự có chính xác không (đối chiếu danh sách triệu tập).
- Dùng input: `ten_cuoc_hop`, `thoi_gian`, `dia_diem`, `chu_tri`, `thu_ky`, `thanh_phan`.
- Vai trò: Chuyên viên Phòng HCTH (Trưởng phòng kiểm tra lại) · AI hỗ trợ: đối chiếu chéo tự động · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: Tên người và chức danh sai là lỗi nghiêm trọng trong biên bản — kiểm tra kỹ từng tên; người vắng mặt phải ghi rõ lý do (vắng có phép/vắng không phép/đi công tác).
- → Kết quả bước: Khung thông tin hành chính cuộc họp đã kiểm chuẩn.

**Bước 2. Ghi phần mở đầu biên bản**
- Làm gì: Viết phần đầu theo Mẫu 1.9: cơ quan chủ quản nếu có, cơ quan ban hành, quốc hiệu – tiêu ngữ, số/ký hiệu BB và địa danh/ngày (chưa có để trống), dòng "BIÊN BẢN" + tên cuộc họp (in hoa, căn giữa), các dòng Thời gian / Địa điểm / Chủ trì / Thư ký / Thành phần (ghi số lượng người dự, liệt kê người vắng mặt kèm lý do).
- Dùng input: `ten_cuoc_hop`, `thoi_gian`, `dia_diem`, `chu_tri`, `thu_ky`, `thanh_phan`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: xử lý sơ bộ theo quy trình · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Giờ họp ghi đầy đủ "08h00 – 10h00, ngày 12 tháng 10 năm 2026"; chủ trì và thư ký ghi đủ học hàm/học vị + họ tên + chức danh.
- → Kết quả bước: Phần mở đầu biên bản hoàn chỉnh.

**Bước 3. Ghi diễn biến theo từng nội dung**
- Làm gì: Với từng vấn đề trong `noi_dung`, ghi thành mục đánh số 1., 2., 3...; mỗi mục ghi: nội dung vấn đề được trình bày + ý kiến phát biểu chính (ghi tên người phát biểu + ý chính, không ghi nguyên văn dài dòng trừ phát biểu cần lưu chính xác); giữ giọng văn khách quan, trung thực, không bình luận.
- Dùng input: `noi_dung`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: xử lý sơ bộ theo quy trình · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Chỉ ghi ý kiến có giá trị (đề xuất, phản biện, số liệu) — bỏ qua phát biểu mang tính xã giao; ý kiến trái chiều phải ghi đầy đủ cả hai phía, không thiên lệch; không tự ý "làm đẹp" lời phát biểu.
- → Kết quả bước: Dự thảo phần diễn biến theo từng nội dung.

**Bước 4. Tổng hợp kết luận thành nhiệm vụ cụ thể**
- Làm gì: Từ `ket_luan`, chuyển từng kết luận/phân công của chủ trì thành mục đánh số, mỗi mục giữ việc gì – đơn vị/cá nhân thực hiện (đầu mối) – thời hạn hoàn thành theo ghi chép đã cung cấp; kiểm tra mỗi nhiệm vụ có đầu mối rõ ràng và deadline cụ thể (ngày/tháng/năm), để trống đầu mối hoặc thời hạn chưa được xác nhận.
- Dùng input: `ket_luan`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: tổng hợp và chuẩn hóa dữ liệu · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Bẫy thường gặp — kết luận ghi "các đơn vị triển khai" mà không chỉ rõ đơn vị nào; deadline ghi "sớm" hoặc "trong thời gian tới". Ghi đầu mối và thời hạn đúng kết luận nguồn; chưa có để trống, không tự giao việc hoặc đặt hạn.
- → Kết quả bước: Dự thảo phần kết luận với nhiệm vụ đã gắn đầu mối và thời hạn.

**Bước 5. Hoàn thiện phần kết thúc và chữ ký**
- Làm gì: Ghi dòng thời gian kết thúc cuộc họp ("Cuộc họp kết thúc lúc ... cùng ngày./."); bố trí khối chữ ký: bên trái "THƯ KÝ", bên phải "CHỦ TRÌ", họ tên người ký bên dưới (chừa khoảng trống ký ở bản trình ký).
- Dùng input: `thoi_gian`, `chu_tri`, `thu_ky`.
- Vai trò: Chuyên viên Phòng HCTH (Trưởng phòng kiểm tra lại) · AI hỗ trợ: áp dụng góp ý, hoàn thiện bản thảo · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: Giờ kết thúc phải khớp thực tế (không sớm hơn giờ bắt đầu đã ghi); biên bản hợp lệ cần chữ ký của cả chủ trì và thư ký.
- → Kết quả bước: Phần kết thúc + khối chữ ký hoàn chỉnh.

**Bước 6. Kiểm tra tính khả thi và chính xác**
- Làm gì: Kiểm tra từng nhiệm vụ trong kết luận: có khả thi không (đầu mối có năng lực/thẩm quyền thực hiện, deadline có thực tế không); đối chiếu tên người, chức danh, số liệu với ghi chép gốc; đọc soát chính tả toàn văn.
- Dùng input: toàn bộ input (đối chiếu chéo).
- Vai trò: Chuyên viên Phòng HCTH (Trưởng phòng kiểm tra lại) · AI hỗ trợ: quét lỗi theo checklist · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: Nhiệm vụ giao cho đơn vị không dự họp phải được xác nhận lại với đơn vị đó trước khi ban hành biên bản; deadline đã qua so với ngày lập biên bản là lỗi phải sửa ngay.
- → Kết quả bước: Báo cáo kiểm tra + danh sách chỗ cần sửa (nếu có), trả về bước tương ứng để chỉnh.

**Bước 7. Trình ký xác nhận và ban hành**
- Làm gì: Ghép toàn bộ thành biên bản hoàn chỉnh theo quy cách đầu ra, bổ sung nơi nhận theo mẫu; chuyển cho thư ký và chủ trì ký xác nhận (human gate); sau khi ký, gửi biên bản cho các thành phần dự họp và đơn vị được phân công nhiệm vụ.
- Dùng input: toàn bộ.
- Vai trò: Chuyên viên Phòng HCTH chuẩn bị, Hiệu trưởng phê duyệt · AI hỗ trợ: tổng hợp hồ sơ, soạn phiếu trình/tờ trình đầy đủ · ⏱ ~15–30 phút chuẩn bị + chờ duyệt (ước tính)
- Lưu ý nghiệp vụ: Không sửa nội dung diễn biến/kết luận sau khi chủ trì đã ký mà không có ý kiến đồng ý bằng văn bản.
- → Kết quả bước: Biên bản cuộc họp đã ký xác nhận, gửi đến các bên liên quan.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Ghi chép cuộc họp"/] --> B1["Bước 1: Thu thập và đối chiếu ghi chép cuộc họp"]
    B1 --> B2["Bước 2: Ghi phần mở đầu biên bản"]
    B2 --> B3["Bước 3: Ghi diễn biến theo từng nội dung"]
    B3 --> B4["Bước 4: Tổng hợp kết luận thành nhiệm vụ cụ thể"]
    B4 --> B5["Bước 5: Hoàn thiện phần kết thúc và chữ ký"]
    B5 --> B6["Bước 6: Kiểm tra tính khả thi và chính xác"]
    B6 --> B7["Bước 7: Trình ký xác nhận và ban hành"]
    B7 --> HG["👤 Chủ trì và thư ký ký xác nhận"]
    HG --> OUT[["Biên bản cuộc họp"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Nội dung và số liệu trong output khớp đúng với Input đã cho (không thêm, bớt hay suy diễn)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức và định dạng theo Biên bản phải khách quan, trung thực
- [ ] Căn cứ pháp lý được trích dẫn đầy đủ và còn hiệu lực
- [ ] Không coi bản soạn là đã ký/đã duyệt; việc phê duyệt thuộc người có thẩm quyền trước phát hành
- [ ] Tên người và chức danh sai là lỗi nghiêm trọng trong biên bản — kiểm tra kỹ từng tên
- [ ] Người vắng mặt phải ghi rõ lý do (vắng có phép/vắng không phép/đi công tác)
- [ ] Giờ họp ghi đầy đủ "08h00 – 10h00, ngày 12 tháng 10 năm 2026"

## Căn cứ & lưu ý
- Biên bản phải khách quan, trung thực; kết luận ghi rõ đầu mối và thời hạn.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.3.1`; ngày cập nhật: `2026-10-10`.
- Kho nguồn: https://github.com/phamtruong91/university-skills-framework
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `346719e6b0318ed034b4b016703f79733aa575e7`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/soan-bien-ban-hop`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
