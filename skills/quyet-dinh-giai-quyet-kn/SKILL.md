---
name: "quyet-dinh-giai-quyet-kn"
description: "Soạn quyết định giải quyết khiếu nại / tố cáo trong trường đại học: tóm tắt đơn, quá trình xác minh, căn cứ pháp lý (Luật Khiếu nại 2011, Luật Tố cáo 2018), nội dung quyết định (giữ nguyên / sửa đổi / hủy bỏ / công nhận / bác) và quyền khiếu nại tiếp, khởi kiện. Dùng khi Hiệu trưởng giải quyết khiếu nại lần đầu hoặc tố cáo thuộc thẩm quyền."
---

# Soạn quyết định giải quyết khiếu nại / tố cáo

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




## Khi nào dùng
Khi cần ban hành quyết định giải quyết khiếu nại lần đầu hoặc kết luận nội dung tố cáo
thuộc thẩm quyền của Hiệu trưởng: sau khi đã thụ lý, tổ chức xác minh và có báo cáo
xác minh đầy đủ.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `loai_don` | Khiếu nại / Tố cáo | Có |
| `nguoi_kn_tc` | Họ tên, chức vụ/đơn vị, địa chỉ người khiếu nại hoặc người tố cáo | Có |
| `tom_tat_don` | Tóm tắt nội dung đơn: khiếu nại/tố cáo về việc gì, yêu cầu gì | Có |
| `quyet_dinh_bi_kn` | Quyết định hành chính bị khiếu nại (số, ký hiệu, ngày, nội dung chính) | Không (bắt buộc nếu là khiếu nại) |
| `qua_trinh_xac_minh` | Các bước đã thực hiện: thụ lý, thành lập tổ xác minh, làm việc các bên, kết quả xác minh | Có |
| `can_cu_phap_ly` | Luật Khiếu nại 2011 / Luật Tố cáo 2018, văn bản hướng dẫn và quy định nội bộ liên quan | Có |
| `noi_dung_quyet_dinh` | Giữ nguyên / sửa đổi, hủy bỏ một phần hoặc toàn bộ quyết định bị khiếu nại; công nhận toàn bộ/một phần hoặc bác khiếu nại; kết luận tố cáo đúng/sai | Có |
| `quyen_kn_tiep` | Hướng dẫn quyền khiếu nại lần hai / khởi kiện vụ án hành chính | Có |

## Quy trình

**Bước 1. Kiểm tra điều kiện thụ lý**
- Làm gì: kiểm tra từng điều kiện: đơn có đủ họ tên, địa chỉ, nội dung rõ ràng; còn thời hiệu khiếu nại/tố cáo theo luật; vụ việc thuộc thẩm quyền giải quyết của Hiệu trưởng (không thuộc thẩm quyền cơ quan khác, không đang được tòa án thụ lý).
- Dùng input: `loai_don`, `nguoi_kn_tc`, `tom_tat_don`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: nếu không đủ điều kiện thì trả đơn kèm văn bản hướng dẫn, không im lặng; bảo mật thông tin người tố cáo ngay từ khâu tiếp nhận.
- → Kết quả bước: Phiếu kiểm tra điều kiện thụ lý (đủ / không đủ + lý do).

**Bước 2. Tóm tắt nội dung đơn**
- Làm gì: trích rõ 3 yếu tố: người khiếu nại/tố cáo là ai; khiếu nại/tố cáo về việc gì (quyết định hành chính nào / hành vi nào); yêu cầu cụ thể gì.
- Dùng input: `nguoi_kn_tc`, `tom_tat_don`, `quyet_dinh_bi_kn` (bắt buộc nếu là khiếu nại).
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: tóm tắt trung thực, không thêm bớt ý của người khiếu nại; nếu đơn chưa rõ thì yêu cầu bổ sung trước khi xác minh, không xác minh theo suy đoán.
- → Kết quả bước: Bản tóm tắt nội dung đơn.

**Bước 3. Tổ chức xác minh**
- Làm gì: thành lập tổ xác minh; làm việc với người khiếu nại/tố cáo, đơn vị, cá nhân liên quan; thu thập hồ sơ, chứng cứ; lập báo cáo kết quả xác minh nêu rõ sự việc đúng/sai ở mức nào.
- Dùng input: `qua_trinh_xac_minh`.
- Vai trò: Tổ xác minh · AI hỗ trợ: tổng hợp, chuẩn hóa dữ liệu, đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: bảo vệ bí mật người tố cáo trong suốt quá trình; mọi buổi làm việc phải có biên bản; chứng cứ phải được thu thập hợp pháp mới có giá trị.
- → Kết quả bước: Báo cáo kết quả xác minh.

**Bước 4. Đối chiếu căn cứ pháp lý**
- Làm gì: đối chiếu sự việc đã xác minh với căn cứ pháp lý tương ứng: Luật Khiếu nại 2011 + Nghị định 124/2020/NĐ-CP (đối với khiếu nại) hoặc Luật Tố cáo 2018 + Nghị định 31/2019/NĐ-CP (đối với tố cáo), cùng các quy định nội bộ liên quan.
- Dùng input: `can_cu_phap_ly`, `loai_don`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: kiểm tra văn bản viện dẫn còn hiệu lực; áp đúng luật theo loại đơn, không lẫn lộn khiếu nại với tố cáo.
- → Kết quả bước: Bảng đối chiếu sự việc – căn cứ pháp lý.

**Bước 5. Đánh giá và xác định nội dung quyết định**
- Làm gì: đánh giá mức độ: khiếu nại đúng toàn bộ / đúng một phần / sai; tố cáo đúng / sai / đúng một phần; xác định trách nhiệm tập thể, cá nhân và biện pháp khắc phục; chốt nội dung quyết định (giữ nguyên / sửa đổi / hủy bỏ / công nhận / bác).
- Dùng input: `noi_dung_quyet_dinh` (kết hợp kết quả Bước 3, 4).
- Vai trò: Trưởng phòng Thanh tra – Pháp chế (đánh giá, chốt nội dung quyết định) · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: nội dung quyết định phải tương ứng với mức độ đúng/sai đã đánh giá; biện pháp khắc phục phải khả thi, có thời hạn cụ thể.
- → Kết quả bước: Bản đánh giá + nội dung quyết định đã chốt.

**Bước 6. Soạn quyết định theo bố cục chuẩn**
- Làm gì: soạn văn bản theo bố cục: phần căn cứ → Điều 1. Tóm tắt nội dung khiếu nại/tố cáo → Điều 2. Quá trình xác minh → Điều 3. Căn cứ giải quyết → Điều 4. Nội dung quyết định → Điều 5. Quyền khiếu nại tiếp/khởi kiện → Điều 6. Hiệu lực thi hành → nơi nhận, chữ ký.
- Dùng input: `quyen_kn_tiep`, `nguoi_kn_tc`.
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế · AI hỗ trợ: soạn dự thảo, đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: quyết định giải quyết khiếu nại lần đầu BẮT BUỘC ghi rõ quyền khiếu nại lần hai và quyền khởi kiện; thời hạn, tên cơ quan cấp trên/tòa án ghi chính xác.
- → Kết quả bước: Dự thảo Quyết định giải quyết.

**Bước 7. Trình ký, ban hành và lưu hồ sơ**
- Làm gì: trình Hiệu trưởng ký; gửi quyết định đến người khiếu nại/tố cáo, đơn vị, cá nhân liên quan; lưu toàn bộ hồ sơ giải quyết theo quy định; theo dõi việc thực hiện biện pháp khắc phục.
- Dùng input: (kết quả Bước 6).
- Vai trò: Chuyên viên Phòng Thanh tra – Pháp chế (chuẩn bị hồ sơ trình); Hiệu trưởng (người ký) ban hành · AI hỗ trợ: chuẩn bị hồ sơ trình đầy đủ, lưu trữ hồ sơ · ⏱ ~1–3 giờ (ước tính)
- Lưu ý nghiệp vụ: bảo đảm thời hạn giải quyết theo luật định; hồ sơ phải đầy đủ để phục vụ giải quyết lần hai hoặc khởi kiện.
- → Kết quả bước: Quyết định đã ban hành + hồ sơ giải quyết hoàn chỉnh.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Đơn khiếu nại hoặc tố cáo"/] --> B["Bước 1: Kiểm tra điều kiện thụ lý"]
    B --> C{"Đủ điều kiện thụ lý?"}
    C -->|Không| Z["Không thụ lý: trả đơn và hướng dẫn"]
    C -->|Có| D["Bước 2: Tóm tắt nội dung đơn"]
    D --> E["Bước 3: Thành lập tổ xác minh, làm việc, lập báo cáo"]
    E --> F["Bước 4: Đối chiếu căn cứ pháp lý"]
    F --> G["Bước 5: Đánh giá và xác định nội dung quyết định"]
    G --> H["Bước 6: Soạn quyết định theo bố cục chuẩn"]
    H --> HG["👤 Hiệu trưởng ký ban hành"]
    HG --> I[["Quyết định giải quyết khiếu nại hoặc tố cáo"]]
```
```

## Đầu ra (Output)
- Quyết định giải quyết khiếu nại / kết luận nội dung tố cáo hoàn chỉnh (markdown).
- Tóm tắt kết quả: khiếu nại đúng/sai mức nào, biện pháp khắc phục, thời hạn thực hiện.

**Cấu trúc output chuẩn:** Quyết định giải quyết khiếu nại (lần đầu) gồm các phần bắt buộc theo đúng thứ tự sau:
1. Phần đầu: quốc hiệu – tiêu ngữ, số/ký hiệu, địa danh – ngày tháng, tên văn bản "QUYẾT ĐỊNH" + trích yếu (về việc giải quyết khiếu nại của ... (lần đầu)).
2. Phần căn cứ: luật, nghị định, quy chế nội bộ; "Xét đề nghị của ...".
3. Điều 1. Tóm tắt nội dung khiếu nại/tố cáo.
4. Điều 2. Quá trình xác minh.
5. Điều 3. Căn cứ giải quyết.
6. Điều 4. Nội dung quyết định (công nhận/bác; giữ nguyên/sửa đổi/hủy bỏ; biện pháp khắc phục; xử lý trách nhiệm nếu có).
7. Điều 5. Quyền khiếu nại tiếp / khởi kiện (thời hạn, cơ quan tiếp nhận).
8. Điều 6. Hiệu lực thi hành (ngày hiệu lực, trách nhiệm thi hành).
9. Phần cuối: nơi nhận, chữ ký Hiệu trưởng.

## Checklist nghiệm thu

- [ ] Đủ các phần theo "Cấu trúc output chuẩn": Phần đầu; Phần căn cứ; Điều 1. Tóm tắt nội dung khiếu nại/tố cáo.; Điều 2. Quá trình xác minh.; Điều 3. Căn cứ giải quyết.; Điều 4. Nội dung quyết định (công nhận/bác;…; …
- [ ] Có đầy đủ sản phẩm: Quyết định giải quyết khiếu nại / kết luận nội dung tố cáo hoàn chỉnh (markdown)
- [ ] Có đầy đủ sản phẩm: Tóm tắt kết quả: khiếu nại đúng/sai mức nào, biện pháp khắc phục, thời hạn thực hiện
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Nếu không đủ điều kiện thì trả đơn kèm văn bản hướng dẫn, không im lặng
- [ ] Tóm tắt trung thực, không thêm bớt ý của người khiếu nại

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `loai_don` | Khiếu nại |
| `nguoi_kn_tc` | ThS. Vũ Thị A, giảng viên Khoa Kinh tế, Trường Đại học A |
| `tom_tat_don` | Khiếu nại Quyết định số 118/QĐ-ĐHA-TCCB ngày 20/01/2026 xếp loại viên chức năm 2025 là "Hoàn thành nhiệm vụ"; đề nghị điều chỉnh thành "Hoàn thành xuất sắc nhiệm vụ" |
| `quyet_dinh_bi_kn` | Quyết định số 118/QĐ-ĐHA-TCCB ngày 20/01/2026 của Hiệu trưởng về xếp loại viên chức năm 2025 |
| `qua_trinh_xac_minh` | Thụ lý ngày 05/02/2026; tổ xác minh làm việc với bà Lan, Phòng TCCB, Khoa Kinh tế; đối chiếu hồ sơ NCKH; phát hiện thiếu 02 bài báo đã công bố khi tính điểm tiêu chí NCKH |
| `can_cu_phap_ly` | Luật Khiếu nại 2011; Nghị định 124/2020/NĐ-CP; Quy định đánh giá, xếp loại viên chức của Trường |
| `noi_dung_quyet_dinh` | Công nhận một phần khiếu nại; sửa đổi Quyết định 118/QĐ-ĐHA-TCCB, điều chỉnh xếp loại thành "Hoàn thành xuất sắc nhiệm vụ" |
| `quyen_kn_tiep` | Khiếu nại lần hai đến cơ quan cấp trên trực tiếp hoặc khởi kiện vụ án hành chính tại Tòa án |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A            CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
                                                   Độc lập – Tự do – Hạnh phúc
      Số: 24/QĐ-ĐHA
                                                 Thành phố C, ngày 10 tháng 3 năm 2026

QUYẾT ĐỊNH
Về việc giải quyết khiếu nại của bà Vũ Thị A
(lần đầu)

HIỆU TRƯỞNG TRƯỜNG ĐẠI HỌC A

Căn cứ Luật Khiếu nại năm 2011;
Căn cứ Nghị định số 124/2020/NĐ-CP ngày 19/10/2020 của Chính phủ quy định chi tiết
một số điều và biện pháp thi hành Luật Khiếu nại;
Căn cứ Quy chế tổ chức và hoạt động của Trường Đại học A;
Xét đề nghị của Trưởng phòng Thanh tra & Pháp chế,

QUYẾT ĐỊNH:

Điều 1. Tóm tắt nội dung khiếu nại
Bà Vũ Thị A, giảng viên Khoa Kinh tế, khiếu nại Quyết định số 118/QĐ-ĐHA-TCCB
ngày 20/01/2026 của Hiệu trưởng về việc xếp loại viên chức năm 2025 của bà là
"Hoàn thành nhiệm vụ"; đề nghị điều chỉnh xếp loại thành "Hoàn thành xuất sắc
nhiệm vụ".

Điều 2. Quá trình xác minh
Ngày 05/02/2026, Nhà trường thụ lý đơn khiếu nại của bà Vũ Thị A và thành
lập Tổ xác minh. Tổ xác minh đã làm việc với bà Lan, Phòng Tổ chức cán bộ, Ban
Chủ nhiệm Khoa Kinh tế; đối chiếu hồ sơ nghiên cứu khoa học của bà Lan với bảng
tổng hợp điểm đánh giá. Kết quả xác minh: khi tính điểm tiêu chí nghiên cứu khoa
học, Phòng Tổ chức cán bộ đã bỏ sót 02 bài báo khoa học của bà Lan đã được công
bố trên tạp chí trong năm 2025.

Điều 3. Căn cứ giải quyết
Luật Khiếu nại năm 2011; Nghị định số 124/2020/NĐ-CP; Quy định đánh giá, xếp loại
viên chức của Trường Đại học A và kết quả xác minh nêu tại Điều 2.

Điều 4. Nội dung quyết định
1. Công nhận một phần khiếu nại của bà Vũ Thị A.
2. Sửa đổi Quyết định số 118/QĐ-ĐHA-TCCB ngày 20/01/2026: điều chỉnh kết quả xếp
loại viên chức năm 2025 của bà Vũ Thị A từ "Hoàn thành nhiệm vụ" thành
"Hoàn thành xuất sắc nhiệm vụ".
3. Yêu cầu Phòng Tổ chức cán bộ rút kinh nghiệm, rà soát quy trình tổng hợp điểm
đánh giá viên chức, không để xảy ra sai sót tương tự.

Điều 5. Quyền khiếu nại tiếp
Trong thời hạn 30 ngày kể từ ngày nhận được Quyết định này, nếu không đồng ý,
bà Vũ Thị A có quyền khiếu nại lần hai đến cơ quan cấp trên trực tiếp của
Nhà trường hoặc khởi kiện vụ án hành chính tại Tòa án theo quy định của pháp luật.

Điều 6. Hiệu lực thi hành
Quyết định này có hiệu lực kể từ ngày ký. Trưởng phòng Thanh tra & Pháp chế,
Trưởng phòng Tổ chức cán bộ, Trưởng Khoa Kinh tế, bà Vũ Thị A và các đơn
vị, cá nhân liên quan chịu trách nhiệm thi hành Quyết định này./.

Nơi nhận:                                           HIỆU TRƯỞNG
- Như Điều 6;
- Lưu: VT, TTPC, TCCB.                                  [CHỜ KÝ]

                                                 PGS.TS. Trần Văn B
```

### Tóm tắt kết quả (output kèm theo)
- Khiếu nại: **đúng một phần** (có sai sót khi tính điểm tiêu chí NCKH).
- Biện pháp: sửa đổi quyết định, điều chỉnh xếp loại thành "Hoàn thành xuất sắc nhiệm vụ".
- Phòng TCCB rút kinh nghiệm, rà soát quy trình tổng hợp điểm.

## Căn cứ & lưu ý
- Luật Khiếu nại 2011 (Luật số 02/2011/QH13); Nghị định 124/2020/NĐ-CP.
- Luật Tố cáo 2018 (Luật số 25/2018/QH14); Nghị định 31/2019/NĐ-CP quy định chi tiết
thi hành Luật Tố cáo.
- Phải bảo đảm thời hạn giải quyết theo luật định; bảo vệ bí mật thông tin người tố cáo.
- Quyết định giải quyết khiếu nại lần đầu phải ghi rõ quyền khiếu nại lần hai và quyền
khởi kiện để người khiếu nại thực hiện.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/quyet-dinh-giai-quyet-kn`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
