---
name: hop-dong-thuc-hien-de-tai
description: Soạn hợp đồng thực hiện đề tài/nhiệm vụ khoa học công nghệ giữa bên giao (trường hoặc cơ quan quản lý) và bên nhận (chủ nhiệm đề tài). Dùng sau khi đề tài được phê duyệt, trước khi triển khai và cấp kinh phí.
---

# Skill: Soạn hợp đồng thực hiện đề tài KHCN

## Khi nào dùng
Khi đề tài NCKH đã được hội đồng xét duyệt và có quyết định phê duyệt: Phòng KHCN
soạn hợp đồng để Hiệu trưởng (bên giao) ký với chủ nhiệm đề tài (bên nhận), làm căn cứ
pháp lý cho việc cấp kinh phí, kiểm tra tiến độ, nghiệm thu và thanh lý đề tài.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `so_hop_dong` | Số, ký hiệu hợp đồng | Có |
| `ben_giao` | Tên cơ quan, người đại diện, chức vụ (VD: Hiệu trưởng) | Có |
| `ben_nhan` | Họ tên, học hàm/học vị, đơn vị của chủ nhiệm đề tài | Có |
| `ten_de_tai` | Tên đầy đủ của đề tài | Có |
| `ma_so_de_tai` | Mã số đề tài theo quyết định phê duyệt | Có |
| `quyet_dinh_phe_duyet` | Số, ngày quyết định phê duyệt đề tài | Có |
| `thoi_gian_thuc_hien` | Từ ngày/tháng/năm đến ngày/tháng/năm | Có |
| `tong_kinh_phi` | Tổng kinh phí (ghi cả số và chữ) | Có |
| `tien_do_cap_kinh_phi` | Các đợt cấp kinh phí (tỷ lệ %, điều kiện từng đợt) | Có |
| `san_pham_nghiem_thu` | Sản phẩm phải đạt khi nghiệm thu (đối chiếu thuyết minh đã duyệt) | Có |
| `dieu_khoan_dac_biet` | Thỏa thuận riêng nếu có (sở hữu trí tuệ, bảo mật...) | Không |
| `ngay_ky` | Địa danh, ngày tháng năm ký hợp đồng | Có |

## Quy trình

**Bước 1. Thu thập và đối chiếu căn cứ**
- Làm gì: thu thập `quyet_dinh_phe_duyet`, thuyết minh và dự toán kinh phí đã duyệt; lập bảng đối chiếu các số liệu then chốt (tên đề tài, mã số, thời gian, tổng kinh phí, danh mục sản phẩm) — mọi số liệu đưa vào hợp đồng phải khớp 100% với các văn bản này; ghi lại số và ngày ban hành của quyết định phê duyệt để dùng ở phần căn cứ.
- Dùng input: `quyet_dinh_phe_duyet`, `ten_de_tai`, `ma_so_de_tai`, `thoi_gian_thuc_hien`, `tong_kinh_phi`, `san_pham_nghiem_thu`.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: lập bảng đối chiếu số liệu căn cứ · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: sai lệch số liệu giữa hợp đồng và quyết định phê duyệt là căn cứ để từ chối thanh toán sau này — bước này không được làm qua loa.
- → Kết quả bước: bảng đối chiếu số liệu căn cứ (đã xác nhận khớp).

**Bước 2. Soạn phần mở đầu hợp đồng**
- Làm gì: viết tiêu đề "HỢP ĐỒNG THỰC HIỆN ĐỀ TÀI KHOA HỌC CÔNG NGHỆ" + `so_hop_dong`; viết các dòng căn cứ (quy chế quản lý đề tài, `quyet_dinh_phe_duyet`, thuyết minh và dự toán kinh phí đã duyệt); điền đầy đủ thông tin `ben_giao` (tên cơ quan, người đại diện, chức vụ) và `ben_nhan` (họ tên, học hàm/học vị, đơn vị); ghi địa điểm và ngày ký trong câu mở đầu "Hôm nay, ngày...".
- Dùng input: `so_hop_dong`, `ben_giao`, `ben_nhan`, `quyet_dinh_phe_duyet`, `ngay_ky`.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: soạn dự thảo phần mở đầu (tiêu đề, căn cứ, thông tin hai bên) · ⏱ ~20–30 phút (ước tính)
- Lưu ý nghiệp vụ: người đại diện bên giao phải có thẩm quyền ký (Hiệu trưởng hoặc người được ủy quyền bằng văn bản); kiểm tra số hợp đồng không trùng với các hợp đồng đã ký.
- → Kết quả bước: dự thảo phần mở đầu (tiêu đề + căn cứ + thông tin hai bên).

**Bước 3. Soạn Điều 1 – Đối tượng của hợp đồng**
- Làm gì: ghi `ten_de_tai`, `ma_so_de_tai`, mục tiêu chính (trích nguyên văn từ thuyết minh đã duyệt), danh mục `san_pham_nghiem_thu` phải hoàn thành.
- Dùng input: `ten_de_tai`, `ma_so_de_tai`, `san_pham_nghiem_thu`, kết quả bước 1.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: chép nguyên văn từ thuyết minh đã duyệt · ⏱ ~20–30 phút (ước tính)
- Lưu ý nghiệp vụ: danh mục sản phẩm ở Điều 1 là căn cứ duy nhất để nghiệm thu — phải chép nguyên văn từ thuyết minh đã duyệt, không được viết lại theo cách hiểu khác.
- → Kết quả bước: dự thảo Điều 1.

**Bước 4. Soạn Điều 2 – Thời gian thực hiện**
- Làm gì: ghi ngày bắt đầu – ngày kết thúc từ `thoi_gian_thuc_hien`; quy định các mốc báo cáo tiến độ định kỳ (6 tháng/lần) mà bên nhận phải nộp về Phòng KHCN.
- Dùng input: `thoi_gian_thuc_hien`.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: soạn Điều 2 và quy định mốc báo cáo tiến độ định kỳ · ⏱ ~15–20 phút (ước tính)
- Lưu ý nghiệp vụ: thời gian trong hợp đồng phải khớp quyết định phê duyệt; nên ghi rõ báo cáo tiến độ là nghĩa vụ gắn với điều kiện cấp kinh phí đợt 2 (liên kết với Điều 3).
- → Kết quả bước: dự thảo Điều 2.

**Bước 5. Soạn Điều 3 – Kinh phí**
- Làm gì: ghi `tong_kinh_phi` cả số và chữ, nguồn kinh phí; chi tiết `tien_do_cap_kinh_phi` theo từng đợt (tỷ lệ % + điều kiện cụ thể từng đợt); ghi nguyên tắc sử dụng kinh phí đúng mục đích, đúng chế độ và quyết toán theo quy định.
- Dùng input: `tong_kinh_phi`, `tien_do_cap_kinh_phi`.
- Vai trò: Trưởng Phòng KHCN · AI hỗ trợ: soạn chi tiết từng đợt cấp · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: điều kiện mỗi đợt cấp phải đo lường được ("sau khi báo cáo giữa kỳ được đánh giá đạt yêu cầu" — cần rõ ai đánh giá, theo tiêu chí nào); tránh ghi chung chung "cấp theo tiến độ".
- → Kết quả bước: dự thảo Điều 3.

**Bước 6. Soạn Điều 4 và Điều 5 – Quyền và nghĩa vụ hai bên**
- Làm gì: Điều 4 (Bên giao): cấp kinh phí đúng tiến độ; kiểm tra, giám sát tiến độ và việc sử dụng kinh phí; hỗ trợ thủ tục hành chính; tổ chức nghiệm thu đúng hạn. Điều 5 (Bên nhận): triển khai đúng thuyết minh đã duyệt; nộp báo cáo tiến độ định kỳ và đột xuất khi được yêu cầu; sử dụng kinh phí đúng mục đích, đúng chế độ; chịu trách nhiệm khoa học về kết quả; không được chuyển giao toàn bộ hoặc một phần công việc khi chưa được đồng ý bằng văn bản.
- Dùng input: `ben_giao`, `ben_nhan`.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: soạn dự thảo Điều 4 và Điều 5 theo mẫu chuẩn · ⏱ ~20–30 phút (ước tính)
- Lưu ý nghiệp vụ: nghĩa vụ của Bên nhận phải tương ứng với quyền giám sát của Bên giao; điều khoản "không chuyển giao" cần ghi rõ hình thức đồng ý (bằng văn bản) để tránh tranh chấp.
- → Kết quả bước: dự thảo Điều 4 và Điều 5.

**Bước 7. Soạn Điều 6, Điều 7 và điều khoản chung**
- Làm gì: Điều 6 (Nghiệm thu): điều kiện nghiệm thu (hoàn thành sản phẩm, báo cáo tổng kết, quyết toán), thành lập hội đồng, các mức xếp loại (Xuất sắc/Đạt/Không đạt). Điều 7 (Thanh lý): điều kiện thanh lý; xử lý khi không hoàn thành hoặc vi phạm (tạm dừng cấp kinh phí, thu hồi kinh phí đã cấp, xem xét trách nhiệm). Điều khoản chung: hiệu lực hợp đồng, sửa đổi bổ sung phải lập thành văn bản, số bản có giá trị pháp lý như nhau, chữ ký hai bên. Bổ sung `dieu_khoan_dac_biet` (sở hữu trí tuệ, bảo mật...) nếu có.
- Dùng input: `san_pham_nghiem_thu`, `dieu_khoan_dac_biet`, `ngay_ky`.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: soạn dự thảo Điều 6, Điều 7 và điều khoản chung · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: mức "Không đạt" phải gắn hậu quả cụ thể (thu hồi kinh phí) thì điều khoản mới có sức ràng buộc; điều khoản SHTT nên ghi rõ quyền sở hữu kết quả thuộc về bên nào ngay từ đầu.
- → Kết quả bước: dự thảo Điều 6, Điều 7 và điều khoản chung.

**Bước 8. Kiểm tra và trình hai bên ký**
- Làm gì: chạy checklist kiểm tra: số liệu khớp quyết định phê duyệt và thuyết minh đã duyệt, đủ 7 điều khoản + điều khoản chung, chính tả, thẩm quyền ký của hai bên; trình hai bên ký hợp đồng.
- Dùng input: toàn bộ input + kết quả bước 2–7.
- Vai trò: Hai bên ký kết · AI hỗ trợ: chuẩn bị hồ sơ trình ký, nhắc lịch và theo dõi tiến độ · ⏱ ~1–2 giờ (ước tính, kể cả hẹn ký)
- Lưu ý nghiệp vụ: hợp đồng đề tài thường lập thành 04 bản (mỗi bên giữ 02 bản) — kiểm tra số bản ghi trong điều khoản chung khớp thực tế.
- → Kết quả bước: hợp đồng đã được hai bên ký + checklist kiểm tra điều khoản.

**Bước 9. Xuất bản và lưu hồ sơ**
- Làm gì: xuất hợp đồng hoàn chỉnh ở định dạng markdown, sẵn sàng in/ký; lưu 01 bản vào hồ sơ quản lý đề tài tại Phòng KHCN làm căn cứ cấp kinh phí, kiểm tra tiến độ và nghiệm thu sau này.
- Dùng input: kết quả bước 8.
- Vai trò: Chuyên viên Phòng KHCN · AI hỗ trợ: xuất hợp đồng markdown và lưu vào hồ sơ quản lý đề tài · ⏱ ~10–15 phút (ước tính)
- Lưu ý nghiệp vụ: hồ sơ quản lý đề tài phải có đủ: quyết định phê duyệt, thuyết minh đã duyệt, hợp đồng đã ký — thiếu 1 trong 3 thì không đủ căn cứ cấp kinh phí đợt 1.
- → Kết quả bước: hợp đồng hoàn chỉnh + checklist, đã lưu hồ sơ quản lý đề tài.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/Quyết định phê duyệt và thuyết minh đã duyệt/] --> A["Bước 1: Thu thập căn cứ, đối chiếu số liệu"]
    A --> B["Bước 2: Soạn phần mở đầu hợp đồng"]
    B --> C["Bước 3-5: Điều 1, Điều 2, Điều 3"]
    C --> D["Bước 6: Điều 4 và 5 quyền nghĩa vụ hai bên"]
    D --> E["Bước 7: Điều 6, 7 và điều khoản chung"]
    E --> F{"Đủ điều khoản, số liệu khớp?"}
    F -->|Không| B
    F -->|Có| HG["👤 Bước 8: Hai bên ký hợp đồng"]
    HG --> OUT[["Bước 9: Hợp đồng hoàn chỉnh và checklist"]]
```

## Đầu ra (Output)
- Văn bản hợp đồng hoàn chỉnh (mở đầu + 7 điều khoản + điều khoản chung + chữ ký).
- Checklist kiểm tra điều khoản.

**Cấu trúc output chuẩn:** khung cố định của văn bản Hợp đồng, các phần bắt buộc theo đúng thứ tự xuất hiện:
1. Quốc hiệu – Tiêu ngữ
2. Tiêu đề "HỢP ĐỒNG THỰC HIỆN ĐỀ TÀI KHOA HỌC CÔNG NGHỆ" + Số hợp đồng
3. Các căn cứ (quy chế quản lý đề tài; quyết định phê duyệt; thuyết minh và dự toán kinh phí đã duyệt)
4. Câu mở đầu: thời gian, địa điểm ký + thông tin Bên giao (A) / Bên nhận (B)
5. Điều 1. Đối tượng của hợp đồng (tên đề tài, mã số, mục tiêu, danh mục sản phẩm)
6. Điều 2. Thời gian thực hiện (ngày bắt đầu – ngày kết thúc, mốc báo cáo tiến độ định kỳ)
7. Điều 3. Kinh phí (tổng mức số + chữ, nguồn kinh phí, tiến độ cấp theo đợt, nguyên tắc sử dụng và quyết toán)
8. Điều 4. Quyền và nghĩa vụ của Bên A (bên giao)
9. Điều 5. Quyền và nghĩa vụ của Bên B (bên nhận)
10. Điều 6. Nghiệm thu (điều kiện, hội đồng, các mức xếp loại)
11. Điều 7. Thanh lý hợp đồng (điều kiện thanh lý, xử lý vi phạm)
12. Điều khoản chung (hiệu lực, sửa đổi bổ sung, số bản có giá trị như nhau)
13. Khối chữ ký hai bên (chức danh, ký/đóng dấu, ghi rõ họ tên)

## Checklist nghiệm thu

- [ ] Đủ 13 phần theo "Cấu trúc output chuẩn": Quốc hiệu – Tiêu ngữ → tiêu đề + số hợp đồng → căn cứ → câu mở đầu + thông tin hai bên → Điều 1–7 → điều khoản chung → chữ ký hai bên
- [ ] Số liệu trong hợp đồng (tên đề tài, mã số, thời gian, tổng kinh phí, danh mục sản phẩm) khớp 100% với quyết định phê duyệt, thuyết minh và dự toán đã duyệt
- [ ] Không bịa đặt số/ngày quyết định phê duyệt, số hợp đồng, thông tin đại diện hai bên
- [ ] Đúng mẫu hợp đồng thực hiện đề tài theo quy chế quản lý đề tài của trường/cơ quan quản lý
- [ ] Căn cứ pháp lý đầy đủ, còn hiệu lực (quy chế quản lý đề tài, quyết định phê duyệt, thuyết minh và dự toán kinh phí đã duyệt)
- [ ] Điều 1 chép nguyên văn từ thuyết minh đã duyệt; điều kiện cấp từng đợt kinh phí cụ thể, đo lường được; số bản hợp đồng trong điều khoản chung khớp thực tế
- [ ] Người đại diện bên giao có thẩm quyền ký (Hiệu trưởng hoặc được ủy quyền bằng văn bản); số hợp đồng không trùng với các hợp đồng đã ký
- [ ] Đã qua Human gate: hai bên đã ký hợp đồng; 01 bản đã lưu vào hồ sơ quản lý đề tài

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, đề tài, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `so_hop_dong` | 12/HĐ-ĐHA-KHCN |
| `ben_giao` | Trường Đại học A – Đại diện: GS.TS. Vũ Văn B – Chức vụ: Hiệu trưởng |
| `ben_nhan` | PGS.TS. Trần Văn B – Khoa Công nghệ thông tin |
| `ten_de_tai` | Nghiên cứu ứng dụng trí tuệ nhân tạo trong dự báo năng suất lúa tại Đồng bằng sông Hồng |
| `ma_so_de_tai` | ĐHA.KHCN.2027.04 (giả lập) |
| `quyet_dinh_phe_duyet` | Quyết định số 88/QĐ-ĐHA ngày 20/12/2026 của Hiệu trưởng |
| `thoi_gian_thuc_hien` | Từ 01/01/2027 đến 31/12/2028 |
| `tong_kinh_phi` | 280.000.000 đồng (Hai trăm tám mươi triệu đồng) |
| `tien_do_cap_kinh_phi` | Đợt 1: 40% sau khi ký; Đợt 2: 40% sau báo cáo giữa kỳ đạt yêu cầu; Đợt 3: 20% sau nghiệm thu |
| `san_pham_nghiem_thu` | 02 bài báo; 01 phần mềm dự báo; 01 báo cáo tổng kết; 02 thạc sĩ |
| `ngay_ky` | Thành phố C, ngày 09 tháng 01 năm 2027 |

### Output mẫu

```
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
Độc lập – Tự do – Hạnh phúc
---------------

HỢP ĐỒNG THỰC HIỆN ĐỀ TÀI KHOA HỌC CÔNG NGHỆ
Số: 12/HĐ-ĐHA-KHCN

Căn cứ Quy chế quản lý đề tài nghiên cứu khoa học cấp trường của Trường Đại học
A;
Căn cứ Quyết định số 88/QĐ-ĐHA ngày 20/12/2026 của Hiệu trưởng Trường Đại học Minh
Đức về việc phê duyệt đề tài NCKH cấp trường năm 2027;
Căn cứ Thuyết minh và dự toán kinh phí đề tài đã được phê duyệt,

Hôm nay, ngày 09 tháng 01 năm 2027, tại Trường Đại học A, chúng tôi gồm:

BÊN GIAO (Bên A): TRƯỜNG ĐẠI HỌC A
Đại diện: GS.TS. Vũ Văn B – Chức vụ: Hiệu trưởng

BÊN NHẬN (Bên B): PGS.TS. Trần Văn B – Khoa Công nghệ thông tin
Cùng thỏa thuận ký kết hợp đồng với các điều khoản sau:

Điều 1. Đối tượng của hợp đồng
Bên A giao cho Bên B thực hiện đề tài: "Nghiên cứu ứng dụng trí tuệ nhân tạo trong
dự báo năng suất lúa tại Đồng bằng sông Hồng", mã số ĐHA.KHCN.2027.04, với mục tiêu
xây dựng mô hình AI dự báo năng suất lúa đạt độ chính xác ≥ 85%. Sản phẩm phải hoàn
thành: 02 bài báo khoa học, 01 phần mềm dự báo (bản thử nghiệm), 01 báo cáo tổng kết,
đào tạo 02 thạc sĩ.

Điều 2. Thời gian thực hiện
Từ ngày 01/01/2027 đến ngày 31/12/2028. Bên B nộp báo cáo tiến độ 6 tháng/lần về
Phòng Khoa học công nghệ theo quy định.

Điều 3. Kinh phí
Tổng kinh phí: 280.000.000 đồng (Hai trăm tám mươi triệu đồng), từ nguồn kinh phí
sự nghiệp KHCN của Trường. Tiến độ cấp: đợt 1: 40% sau khi ký hợp đồng; đợt 2: 40%
sau khi báo cáo giữa kỳ được đánh giá đạt yêu cầu; đợt 3: 20% sau khi nghiệm thu.
Bên B sử dụng kinh phí đúng mục đích, đúng chế độ tài chính hiện hành và quyết toán
theo quy định.

Điều 4. Quyền và nghĩa vụ của Bên A
- Cấp kinh phí đúng tiến độ quy định tại Điều 3;
- Kiểm tra, giám sát tiến độ và việc sử dụng kinh phí của Bên B;
- Hỗ trợ Bên B các thủ tục hành chính liên quan trong quá trình thực hiện;
- Tổ chức nghiệm thu đề tài đúng thời hạn.

Điều 5. Quyền và nghĩa vụ của Bên B
- Triển khai đề tài đúng thuyết minh và dự toán đã được phê duyệt;
- Nộp báo cáo tiến độ định kỳ và báo cáo đột xuất khi Bên A yêu cầu;
- Chịu trách nhiệm khoa học về tính trung thực, chất lượng của kết quả nghiên cứu;
- Không được chuyển giao toàn bộ hoặc một phần công việc khi chưa được Bên A
đồng ý bằng văn bản.

Điều 6. Nghiệm thu
Đề tài được nghiệm thu khi hoàn thành đầy đủ sản phẩm quy định tại Điều 1, có báo
cáo tổng kết và báo cáo quyết toán kinh phí. Bên A thành lập Hội đồng nghiệm thu;
kết quả xếp loại: Xuất sắc / Đạt / Không đạt.

Điều 7. Thanh lý hợp đồng
Hợp đồng được thanh lý sau khi đề tài được nghiệm thu đạt yêu cầu và Bên B hoàn
thành quyết toán kinh phí. Trường hợp Bên B không hoàn thành hoặc vi phạm nghiêm
trọng, Bên A có quyền tạm dừng cấp kinh phí, thu hồi kinh phí đã cấp và xem xét
trách nhiệm theo quy định.

ĐIỀU KHOẢN CHUNG
Hợp đồng có hiệu lực kể từ ngày ký. Hai bên cam kết thực hiện đúng các điều khoản
đã thỏa thuận; mọi sửa đổi, bổ sung phải lập thành văn bản. Hợp đồng được lập thành
04 bản có giá trị pháp lý như nhau, mỗi bên giữ 02 bản.

ĐẠI DIỆN BÊN A                          ĐẠI DIỆN BÊN B
HIỆU TRƯỞNG                            CHỦ NHIỆM ĐỀ TÀI
(đã ký, đóng dấu)                      (đã ký, ghi rõ họ tên)

GS.TS. Vũ Văn B                   PGS.TS. Trần Văn B
```

### Checklist kiểm tra điều khoản (output kèm theo)
- [x] Căn cứ pháp lý (quy chế + quyết định phê duyệt)
- [x] Thông tin đầy đủ hai bên
- [x] Điều 1 – Đối tượng (tên, mã số, mục tiêu, sản phẩm)
- [x] Điều 2 – Thời gian (bắt đầu, kết thúc, mốc báo cáo)
- [x] Điều 3 – Kinh phí (tổng mức số + chữ, tiến độ cấp theo đợt, quyết toán)
- [x] Điều 4 – Quyền/nghĩa vụ Bên giao
- [x] Điều 5 – Quyền/nghĩa vụ Bên nhận
- [x] Điều 6 – Nghiệm thu (điều kiện, hội đồng, xếp loại)
- [x] Điều 7 – Thanh lý (điều kiện, xử lý vi phạm)
- [x] Số liệu khớp quyết định phê duyệt và thuyết minh đã duyệt

## Căn cứ & lưu ý
- Quy chế quản lý đề tài NCKH của Trường Đại học A (giả lập); Quyết định phê
  duyệt đề tài của Hiệu trưởng.
- Số liệu (kinh phí, thời gian, sản phẩm) trong hợp đồng phải khớp tuyệt đối với
  thuyết minh và dự toán đã duyệt — sai lệch là căn cứ để từ chối thanh toán.
- Nên quy định rõ điều kiện cấp từng đợt kinh phí để gắn trách nhiệm tiến độ của Bên B.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
