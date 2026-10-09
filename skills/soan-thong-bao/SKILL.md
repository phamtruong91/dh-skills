---
name: "soan-thong-bao"
description: "Soạn thông báo nội bộ của trường đại học (lịch nghỉ lễ, cuộc họp, quy định mới, tuyển dụng, học bổng...). Ngắn gọn, rõ đối tượng, rõ thời hạn."
---

# Soạn thông báo

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




## Khi nào dùng
Khi cần thông tin chính thức đến toàn thể hoặc một nhóm đối tượng trong trường: lịch nghỉ,
triệu tập họp, quy định mới, kế hoạch, kết quả...

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `tieu_de` | Tiêu đề thông báo (ngắn, nêu việc) | Có |
| `doi_tuong` | Toàn thể CBVC / sinh viên / các đơn vị... | Có |
| `noi_dung` | Các điểm cần thông báo, dạng gạch đầu dòng | Có |
| `thoi_han` | Thời gian hiệu lực / hạn thực hiện (nếu có) | Không |
| `don_vi_ban_hanh` | Phòng/ban ban hành | Có |
| `nguoi_ky` | Chức danh người ký | Có |

## Quy trình

**Bước 1. Xác định mục đích, đối tượng và thời hạn**
- Làm gì: Đọc `tieu_de` để xác định mục đích thông báo (thông tin / yêu cầu thực hiện / triệu tập); đọc `doi_tuong` để xác định phạm vi người nhận (toàn trường / nhóm đơn vị / sinh viên...); đọc `thoi_han` để xác định thời gian hiệu lực hoặc hạn thực hiện; kiểm tra `don_vi_ban_hanh` và `nguoi_ky` có thẩm quyền ban hành thông báo về nội dung này không.
- Dùng input: `tieu_de`, `doi_tuong`, `thoi_han`, `don_vi_ban_hanh`, `nguoi_ky`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: phân tích input, xác định yêu cầu · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Thông báo yêu cầu thực hiện bắt buộc phải có thời hạn rõ ràng; thông báo gửi "toàn thể" mà nội dung chỉ liên quan một nhóm sẽ gây nhiễu — thu hẹp đối tượng cho đúng.
- → Kết quả bước: Xác nhận mục đích + đối tượng nhận + thời hạn của thông báo.

**Bước 2. Thu thập và kiểm chứng nội dung cần thông báo**
- Làm gì: Từ `noi_dung`, kiểm chứng từng điểm: sự kiện có thật không (đối chiếu quyết định/kế hoạch liên quan), ngày giờ có chính xác và rơi đúng thứ trong tuần không, địa điểm có tồn tại và đủ sức chứa đối tượng không; loại bỏ điểm trùng lặp, gộp các điểm cùng chủ đề.
- Dùng input: `noi_dung`, `thoi_han`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: xử lý sơ bộ theo quy trình · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Bẫy thường gặp — ngày tháng trong nội dung không khớp thứ (vd ghi "thứ Sáu, 01/01/2027" nhưng tra lịch lại là thứ khác); hạn đăng ký đặt sau ngày diễn ra sự kiện.
- → Kết quả bước: Danh sách nội dung đã kiểm chứng, loại trùng, sẵn sàng đưa vào thông báo.

**Bước 3. Đặt tiêu đề và viết mở đầu**
- Làm gì: Viết dòng "THÔNG BÁO" (in hoa, căn giữa) + tiêu đề vắn tắt sau "V/v" lấy từ `tieu_de`; viết dòng "Kính gửi" + `doi_tuong`; mở đầu 1–2 câu: nêu căn cứ/quyết định liên quan (nếu có) rồi đi thẳng vào nội dung ("...thông báo ... như sau:").
- Dùng input: `tieu_de`, `doi_tuong`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Tiêu đề không dài quá một dòng; mở đầu không kể lể dài dòng — thông báo càng vào việc nhanh càng tốt.
- → Kết quả bước: Phần tiêu đề + mở đầu hoàn chỉnh.

**Bước 4. Liệt kê nội dung theo chuẩn việc – ai – khi nào – ở đâu**
- Làm gì: Chuyển từng điểm trong `noi_dung` thành các mục đánh số 1., 2., 3...; mỗi mục phải trả lời đủ 4 câu hỏi: việc gì – ai thực hiện – khi nào – ở đâu; với thông báo yêu cầu thực hiện, mỗi mục ghi rõ đơn vị/cá nhân chịu trách nhiệm và hạn hoàn thành.
- Dùng input: `noi_dung`, `thoi_han`, `doi_tuong`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: xử lý sơ bộ theo quy trình · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Tránh câu bị động mập mờ ("sẽ được bố trí") — phải ghi rõ chủ thể thực hiện; thời gian ghi đầy đủ thứ, ngày/tháng/năm, giờ (nếu có).
- → Kết quả bước: Dự thảo nội dung đánh số, mỗi ý đủ 4 yếu tố.

**Bước 5. Viết kết thúc và dự thảo nơi nhận, chữ ký**
- Làm gì: Viết câu kết: với thông báo yêu cầu thực hiện — "Đề nghị các đơn vị, cá nhân nghiêm túc thực hiện./."; với thông báo thông tin — lời cảm ơn hoặc câu kết phù hợp; liệt kê nơi nhận ("- Như trên;" + "- Lưu: VT, [mã đơn vị]."); khối chữ ký theo `nguoi_ky` (ký thừa ủy quyền thì ghi "TL. HIỆU TRƯỞNG" + chức danh).
- Dùng input: `nguoi_ky`, `doi_tuong`.
- Vai trò: Chuyên viên Phòng HCTH · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Thông báo do Trưởng phòng ký phải có quyết định ủy quyền còn hiệu lực; nơi nhận phải bao phủ hết `doi_tuong` đã xác định ở Bước 1.
- → Kết quả bước: Phần kết thúc + nơi nhận + khối chữ ký hoàn chỉnh.

**Bước 6. Kiểm tra đối tượng, thời hạn, ngôn ngữ**
- Làm gì: Đối chiếu: nơi nhận có bao phủ hết đối tượng trong `doi_tuong` không; thời hạn trong nội dung có rõ và nhất quán với `thoi_han` không; đọc lại toàn văn kiểm tra ngôn ngữ dễ hiểu, không vòng vo, không thuật ngữ chuyên môn khó hiểu với đối tượng nhận; kiểm tra thể thức (quốc hiệu, số ký hiệu, ngày tháng).
- Dùng input: toàn bộ input (đối chiếu chéo).
- Vai trò: Chuyên viên Phòng HCTH (Trưởng phòng kiểm tra lại) · AI hỗ trợ: quét lỗi theo checklist · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: Đọc thử với góc nhìn của người nhận ít thông tin nhất (vd sinh viên năm nhất) — chỗ nào khó hiểu thì viết lại.
- → Kết quả bước: Báo cáo kiểm tra + danh sách chỗ cần sửa (nếu có), trả về bước tương ứng để chỉnh.

**Bước 7. Xuất bản thông báo trình duyệt**
- Làm gì: Ghép toàn bộ thành thông báo hoàn chỉnh ở định dạng markdown; chuyển cho thủ trưởng đơn vị ban hành duyệt (human gate) trước khi phát hành trên các kênh (website, email, bảng tin).
- Dùng input: toàn bộ.
- Vai trò: Chuyên viên Phòng HCTH chuẩn bị, Hiệu trưởng phê duyệt · AI hỗ trợ: tổng hợp hồ sơ, soạn phiếu trình/tờ trình đầy đủ · ⏱ ~15–30 phút chuẩn bị + chờ duyệt (ước tính)
- Lưu ý nghiệp vụ: Thông báo có thời hạn gấp nên ghi rõ giờ phát hành dự kiến để đơn vị truyền thông kịp đăng.
- → Kết quả bước: Thông báo hoàn chỉnh, sẵn sàng ban hành.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Nội dung cần thông báo"/] --> B1["Bước 1: Xác định mục đích, đối tượng và thời hạn"]
    B1 --> B2["Bước 2: Thu thập và kiểm chứng nội dung cần thông báo"]
    B2 --> B3["Bước 3: Đặt tiêu đề và viết mở đầu"]
    B3 --> B4["Bước 4: Liệt kê nội dung theo chuẩn việc, ai, khi nào, ở đâu"]
    B4 --> B5["Bước 5: Viết kết thúc và dự thảo nơi nhận, chữ ký"]
    B5 --> B6["Bước 6: Kiểm tra đối tượng, thời hạn, ngôn ngữ"]
    B6 --> B7["Bước 7: Xuất bản thông báo trình duyệt"]
    B7 --> HG["👤 Thủ trưởng duyệt thông báo"]
    HG --> OUT[["Thông báo ban hành"]]
```

## Đầu ra (Output)
- Thông báo hoàn chỉnh (markdown).

**Cấu trúc output chuẩn:** khung mẫu cố định của thông báo — các phần bắt buộc theo đúng thứ tự xuất hiện:
1. Tên trường + Quốc hiệu "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"
2. Tên đơn vị ban hành + Tiêu ngữ "Độc lập – Tự do – Hạnh phúc"
3. Số, ký hiệu thông báo (ký hiệu "TB"); địa danh, ngày tháng năm
4. Tên loại "THÔNG BÁO" (in hoa, căn giữa) + tiêu đề vắn tắt sau "V/v"
5. Dòng "Kính gửi" + đối tượng nhận
6. Mở đầu 1–2 câu: căn cứ/quyết định liên quan (nếu có), rồi đi thẳng vào nội dung
7. Nội dung: đánh số 1., 2., 3..., mỗi ý đủ việc gì – ai thực hiện – khi nào – ở đâu
8. Kết thúc: đề nghị các đơn vị/cá nhân nghiêm túc thực hiện (nếu là thông báo yêu cầu), kết bằng "./."
9. Nơi nhận
10. Khối chữ ký: chức danh người ký (+ ký hiệu TL. nếu ký thừa ủy quyền) + họ tên

## Checklist nghiệm thu

Tiêu chí đạt: tất cả các ô dưới đây được đánh dấu.

- [ ] Đủ các phần theo Cấu trúc output chuẩn: Tên trường + Quốc hiệu "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"; Tên đơn vị ban hành + Tiêu ngữ "Độc lập – Tự do – Hạnh phúc"; Số, ký hiệu thông báo (ký hiệu "TB"); địa danh, ngày tháng năm; Tên loại "THÔNG BÁO" (in hoa, căn giữa) + tiêu đề vắn tắt sau "V/v"; … (đủ 10 phần)
- [ ] Nội dung và số liệu trong output khớp đúng với Input đã cho (không thêm, bớt hay suy diễn)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức và định dạng theo Thông báo càng ngắn càng tốt
- [ ] Căn cứ pháp lý được trích dẫn đầy đủ và còn hiệu lực
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/duyệt trước khi phát hành
- [ ] Thông báo yêu cầu thực hiện bắt buộc phải có thời hạn rõ ràng
- [ ] Thông báo gửi "toàn thể" mà nội dung chỉ liên quan một nhóm sẽ gây nhiễu — thu hẹp đối tượng cho đúng
- [ ] Tránh câu bị động mập mờ ("sẽ được bố trí") — phải ghi rõ chủ thể thực hiện

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `tieu_de` | V/v nghỉ Tết Dương lịch năm 2027 |
| `doi_tuong` | Toàn thể cán bộ, viên chức và sinh viên |
| `noi_dung` | 1. Nghỉ 01 ngày: thứ Sáu, 01/01/2027. 2. Các đơn vị bố trí trực bảo vệ, PCCC. 3. Sinh viên ở KTX đăng ký ở lại (nếu có) tại Ban Quản lý KTX trước 28/12/2026. |
| `don_vi_ban_hanh` | Phòng Hành chính – Tổng hợp |
| `nguoi_ky` | Trưởng phòng (thừa ủy quyền Hiệu trưởng) |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A            CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
PHÒNG HÀNH CHÍNH – TỔNG HỢP              Độc lập – Tự do – Hạnh phúc
      Số: 98/TB-ĐHA-HCTH
                                                 Thành phố C, ngày 09 tháng 10 năm 2026

                          THÔNG BÁO
                   V/v nghỉ Tết Dương lịch năm 2027

Kính gửi: Toàn thể cán bộ, viên chức và sinh viên Trường Đại học A

Căn cứ Bộ luật Lao động và kế hoạch năm học 2026–2027, Nhà trường thông báo
lịch nghỉ Tết Dương lịch năm 2027 như sau:

1. Toàn trường nghỉ 01 ngày: thứ Sáu, ngày 01/01/2027.

2. Các đơn vị bố trí cán bộ trực, đảm bảo công tác bảo vệ, phòng cháy chữa cháy
trong thời gian nghỉ.

3. Sinh viên có nhu cầu ở lại ký túc xá trong dịp nghỉ đăng ký tại Ban Quản lý
ký túc xá trước ngày 28/12/2026.

Đề nghị các đơn vị, cá nhân nghiêm túc thực hiện./.

Nơi nhận:                                          TL. HIỆU TRƯỞNG
- Như trên;                                        TRƯỞNG PHÒNG
- Lưu: VT, HCTH.                                       [CHỜ KÝ]

                                                  ThS. Vũ Văn B
```

## Căn cứ & lưu ý
- Thông báo càng ngắn càng tốt; tránh văn hoa, vòng vo.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/soan-thong-bao`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
