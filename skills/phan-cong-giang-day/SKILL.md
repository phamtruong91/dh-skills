---
name: "phan-cong-giang-day"
description: "Lập bảng phân công giảng dạy học kỳ cho giảng viên của khoa/bộ môn trường đại học: căn cứ danh mục học phần, chuyên môn và định mức giờ giảng. Dùng đầu mỗi học kỳ."
---

# Phân công giảng dạy học kỳ

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




## Khi nào dùng
Khi bắt đầu mỗi học kỳ, khoa/bộ môn cần phân công giảng viên phụ trách các học phần,
lớp học phần theo thời khóa biểu dự kiến.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `hoc_ky` | Học kỳ, năm học (VD: học kỳ 1, năm học 2026–2027) | Có |
| `danh_muc_hoc_phan` | Bảng: mã HP, tên HP, số tín chỉ, số lớp, số SV/lớp | Có |
| `danh_sach_giang_vien` | Bảng: họ tên, học hàm/học vị, bộ môn, chuyên môn, định mức giờ/năm | Có |
| `dinh_muc_gio` | Định mức giờ giảng chuẩn theo chức danh | Không (mặc định theo quy định của trường) |

## Quy trình

**Bước 1. Tổng hợp khối lượng giảng dạy theo bộ môn**
- Làm gì: từ `danh_muc_hoc_phan`, tính tổng số giờ giảng cho từng học phần: giờ lý thuyết + giờ thực hành/thí nghiệm + giờ chấm thi, hướng dẫn (áp hệ số quy đổi giờ chuẩn hiện hành của trường); cộng dồn theo bộ môn; lập bảng "khối lượng giảng dạy học kỳ" gồm các cột: học phần (mã, tên) – số lớp – tổng giờ chuẩn.
- Dùng input: `danh_muc_hoc_phan`, `hoc_ky`.
- Vai trò: Trợ lý đào tạo Khoa · AI hỗ trợ: tính tổng giờ giảng theo học phần/bộ môn, áp hệ số quy đổi giờ chuẩn hiện hành · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: phải dùng đúng hệ số quy đổi giờ chuẩn hiện hành (VD: 1 tiết thực hành quy đổi bao nhiêu giờ chuẩn) — sai hệ số là sai toàn bộ bảng giờ vượt. Lớp ghép, lớp đông có hệ số riêng thì ghi chú rõ từng dòng.
- → Kết quả bước: bảng khối lượng giảng dạy học kỳ theo học phần/bộ môn (tổng giờ chuẩn cần phân công).

**Bước 2. Phân công giảng viên theo nguyên tắc**
- Làm gì: với từng học phần, chọn giảng viên từ `danh_sach_giang_vien` theo thứ tự ưu tiên: (1) đúng chuyên môn được đào tạo; (2) giảng viên cơ hữu còn dưới định mức giờ; (3) cân đối khối lượng giữa các bộ môn, tránh dồn việc; ghi lại lý do phân công cho từng trường hợp đặc biệt (trái chuyên môn, vượt định mức); nếu giảng viên cơ hữu không đủ, lập danh sách học phần cần mời thỉnh giảng.
- Dùng input: `danh_sach_giang_vien`, `dinh_muc_gio` (+ bảng khối lượng ở Bước 1).
- Vai trò: Trưởng bộ môn · AI hỗ trợ: đề xuất phương án phân công theo nguyên tắc ưu tiên, Trưởng bộ môn họp quyết định phân công · ⏱ 1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: không phân công vượt quá 150% định mức nếu chưa có thỏa thuận bằng văn bản với giảng viên. Giảng viên mới (chưa đủ 1 năm công tác) không giao học phần tốt nghiệp/khóa luận. Bẫy: dồn giờ "dễ" cho người quen, giờ "khó" cho người mới — trưởng bộ môn phải kiểm tra phân bổ công bằng.
- → Kết quả bước: phương án phân công sơ bộ (học phần – giảng viên – lý do) + danh sách học phần cần mời thỉnh giảng.

**Bước 3. Mời thỉnh giảng bổ sung (nếu cần)**
- Làm gì: với các học phần thiếu giảng viên cơ hữu, liên hệ giảng viên thỉnh giảng (ưu tiên người đã dạy tốt các kỳ trước, có lý lịch khoa học lưu tại Phòng TCCB); xác nhận khả năng nhận lớp và khung giờ giảng dạy; ký hợp đồng thỉnh giảng trước khi đưa tên vào bảng phân công chính thức.
- Dùng input: `danh_sach_giang_vien` (xác định phần việc còn thiếu) (+ danh sách cần thỉnh giảng ở Bước 2).
- Vai trò: Trưởng khoa · AI hỗ trợ: soạn dự thảo văn bản trình ký, kiểm tra thể thức · ⏱ 3–5 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: giảng viên thỉnh giảng chưa có hợp đồng thì KHÔNG đưa tên vào bảng phân công trình ký — tránh "treo" lớp khi người ta từ chối phút chót.
- → Kết quả bước: danh sách giảng viên thỉnh giảng đã ký hợp đồng/xác nhận nhận lớp.

**Bước 4. Lập bảng phân công chi tiết và tính giờ vượt định mức**
- Làm gì: lắp ráp bảng phân công chính thức gồm các cột: giảng viên – học phần (mã, tên) – lớp – số giờ (lý thuyết/thực hành) – ghi chú (giảng viên chính/trợ giảng/thỉnh giảng); tính tổng giờ chuẩn từng giảng viên trong học kỳ, cộng dồn với các kỳ trước để ra "lũy kế dự kiến cả năm"; tính giờ vượt định mức = lũy kế − định mức (nếu dương); lập bảng tổng hợp giờ giảng/giờ vượt định mức làm căn cứ thanh toán.
- Dùng input: `dinh_muc_gio` (+ phương án phân công ở Bước 2, danh sách thỉnh giảng ở Bước 3).
- Vai trò: Trưởng bộ môn · AI hỗ trợ: lắp bảng phân công và tính giờ vượt định mức, Trưởng bộ môn rà soát và xác nhận · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: giờ vượt định mức là căn cứ thanh toán tiền — tính sai là sai tiền lương. Đối chiếu tổng giờ trong bảng phân công với bảng khối lượng ở Bước 1: mọi giờ trong khối lượng đều phải có người nhận, không để giờ "vô chủ".
- → Kết quả bước: bảng phân công giảng dạy chi tiết + bảng tổng hợp giờ giảng/giờ vượt định mức theo giảng viên.

**Bước 5. Thẩm định, phê duyệt và gửi đơn vị liên quan**
- Làm gì: trưởng bộ môn rà soát (đúng chuyên môn, phân bổ công bằng, không sót giờ); trình trưởng khoa phê duyệt (human gate); gửi bảng đã duyệt cho Phòng Đào tạo (làm căn cứ xếp thời khóa biểu) và Phòng TCCB (làm căn cứ tính giờ giảng, thanh toán); lưu hồ sơ phân công.
- Dùng input: `hoc_ky` (+ 2 bảng ở Bước 4).
- Vai trò: Trưởng bộ môn · AI hỗ trợ: tổng hợp danh mục kiểm tra, đối chiếu hồ sơ · ⏱ 1–2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: phân công phải xong trước khi học kỳ bắt đầu ít nhất 02 tuần để giảng viên chuẩn bị bài giảng. Mọi thay đổi sau phê duyệt (đổi giảng viên, đổi lớp) phải làm văn bản điều chỉnh, không sửa tay trên bảng đã ký.
- → Kết quả bước: bảng phân công giảng dạy học kỳ đã phê duyệt, đã gửi Phòng Đào tạo và Phòng TCCB.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A["Bước 1: Tổng hợp khối lượng giảng dạy theo bộ môn"]
    B["Bước 2: Phân công giảng viên theo nguyên tắc"]
    C{"Giảng viên cơ hữu đủ?"}
    D["Bước 3: Mời thỉnh giảng bổ sung"]
    E["Bước 4: Lập bảng phân công chi tiết, tính giờ vượt"]
    HG["👤 Bước 5: Trưởng bộ môn rà soát, Trưởng khoa phê duyệt"]
    F["Gửi Phòng Đào tạo, Phòng TCCB"]
    O[/"Bảng phân công + bảng giờ vượt định mức"/]
    A --> B --> C
    C -->|Có| E
    C -->|Không| D --> E
    E --> HG --> F --> O
```

## Đầu ra (Output)
- Bảng phân công giảng dạy học kỳ hoàn chỉnh.
- Bảng tổng hợp giờ giảng / giờ vượt định mức theo giảng viên.

**Cấu trúc output chuẩn** (sản phẩm chính: Bảng phân công giảng dạy học kỳ):
1. Tiêu đề hành chính: tên trường – khoa, tên bộ môn.
2. Tên văn bản: "BẢNG PHÂN CÔNG GIẢNG DẠY" + học kỳ, năm học.
3. Bảng phân công chi tiết: các cột STT | Giảng viên | Học phần phụ trách (mã – tên HP) | Lớp | Số giờ (lý thuyết/thực hành) | Ghi chú (giảng viên chính/trợ giảng/thỉnh giảng).
4. Bảng tổng hợp giờ giảng: các cột Giảng viên | Định mức (giờ/năm) | Thực hiện học kỳ này | Lũy kế dự kiến cả năm | Giờ vượt định mức.
5. Ghi chú về giờ vượt định mức và căn cứ thanh toán.
6. Ngày lập văn bản + chữ ký Trưởng bộ môn và Trưởng khoa.

## Checklist nghiệm thu

- [ ] Đủ các phần của "Cấu trúc output chuẩn": bảng phân công chi tiết + bảng tổng hợp giờ giảng/giờ vượt định mức.
- [ ] Học phần, lớp, số giờ trong bảng phân công khớp với Input (`danh_muc_hoc_phan`, `danh_sach_giang_vien`).
- [ ] Mọi giờ trong bảng khối lượng đều có giảng viên nhận; không có giờ "vô chủ".
- [ ] Không phân công vượt quá 150% định mức nếu chưa có thỏa thuận bằng văn bản với giảng viên.
- [ ] Giờ vượt định mức tính đúng công thức và hệ số quy đổi giờ chuẩn hiện hành.
- [ ] Đúng thể thức: ngày lập văn bản, chữ ký Trưởng bộ môn và Trưởng khoa.
- [ ] Đã qua Human gate: Trưởng khoa đã phê duyệt; bảng đã gửi Phòng Đào tạo và Phòng TCCB.
- [ ] Giảng viên mới (chưa đủ 1 năm công tác) không được giao học phần tốt nghiệp/khóa luận.
- [ ] Giảng viên thỉnh giảng trong bảng đã có hợp đồng/xác nhận nhận lớp.
- [ ] Mọi thay đổi sau phê duyệt đều có văn bản điều chỉnh, không sửa tay trên bảng đã ký.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `hoc_ky` | Học kỳ 1, năm học 2026–2027 |
| `danh_muc_hoc_phan` | 08 học phần, 22 lớp (xem bảng mẫu) |
| `danh_sach_giang_vien` | 06 giảng viên Bộ môn Khoa học máy tính |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A – KHOA CÔNG NGHỆ THÔNG TIN
BỘ MÔN KHOA HỌC MÁY TÍNH

BẢNG PHÂN CÔNG GIẢNG DẠY
Học kỳ 1, năm học 2026–2027

| STT | Giảng viên | Học phần phụ trách | Lớp | Số giờ (LT/TH) | Ghi chú |
|---|---|---|---|---|---|
| 1 | TS. Phạm Văn B | CNTT101 – Nhập môn lập trình | K5A, K5B | 90 (45/45) | GV chính |
| 2 | TS. Phạm Văn B | CNTT305 – Trí tuệ nhân tạo | K3A | 45 (30/15) | GV chính |
| 3 | ThS. Bùi Thị B | CNTT101 – Nhập môn lập trình | K5C | 45 (22/23) | GV chính |
| 4 | ThS. Bùi Thị B | CNTT210 – Cơ sở dữ liệu | K4A, K4B | 90 (45/45) | GV chính |
| 5 | TS. Đỗ Thị C | CNTT305 – Trí tuệ nhân tạo | K3B | 45 (30/15) | GV chính |
| 6 | ThS. Trần Văn D | CNTT210 – Cơ sở dữ liệu | K4C | 45 (22/23) | Trợ giảng |
| 7 | ThS. Đặng Văn B | CNTT150 – Tin học đại cương | K6A–K6D | 120 (60/60) | Thỉnh giảng |

TỔNG HỢP GIỜ GIẢNG (giờ chuẩn)

| Giảng viên | Định mức (giờ/năm) | Thực hiện HK1 | Lũy kế dự kiến cả năm | Vượt định mức |
|---|---|---|---|---|
| TS. Phạm Văn B | 270 | 135 | 270 | 0 |
| ThS. Bùi Thị B | 270 | 135 | 280 | +10 |
| TS. Đỗ Thị C | 270 | 45 | 180 | 0 |
| ThS. Trần Văn D | 270 | 45 | 200 | 0 |
| ThS. Trần Văn D | 270 | 45 | 200 | 0 |

Ghi chú: giờ vượt định mức của ThS. Bùi Thị B (+10 giờ) được thanh toán
theo quy chế chi tiêu nội bộ.

Thành phố C, ngày 09 tháng 10 năm 2026

Trưởng bộ môn              Trưởng khoa
(ký, họ tên)               (ký, họ tên)
```

## Căn cứ & lưu ý
- Quy định về chế độ làm việc của giảng viên (Thông tư 20/2020/TT-BGDĐT); quy chế chi
  tiêu nội bộ của Trường Đại học A (giả lập).
- Phân công phải xong trước khi học kỳ bắt đầu ít nhất 02 tuần để giảng viên chuẩn bị.
- Giảng viên thỉnh giảng phải có hợp đồng và lý lịch khoa học lưu tại Phòng TCCB.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/phan-cong-giang-day`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
