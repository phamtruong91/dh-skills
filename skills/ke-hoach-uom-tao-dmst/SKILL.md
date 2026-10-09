---
name: "ke-hoach-uom-tao-dmst"
description: "Lập kế hoạch chương trình ươm tạo đổi mới sáng tạo của Viện: tiêu chí tuyển chọn, lộ trình ươm tạo theo giai đoạn, nguồn lực hỗ trợ và KPI đầu ra. Dùng khi viện tổ chức các đợt ươm tạo startup/dự án khởi nghiệp."
---

# Kế hoạch ươm tạo ĐMST

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




## Khi nào dùng
Khi Viện ĐMST & CGCN tổ chức chương trình ươm tạo (startup sinh viên, giảng viên, dự án spin-off):
cần kế hoạch gồm tiêu chí tuyển chọn, lộ trình các giai đoạn, nguồn lực hỗ trợ và chỉ tiêu đầu ra.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_chuong_trinh` | Tên chương trình ươm tạo + đợt/năm | Có |
| `doi_tuong` | Sinh viên / giảng viên / startup ngoài / hỗn hợp | Có |
| `linh_vuc_uu_tien` | Các lĩnh vực ưu tiên (VD: AI, nông nghiệp thông minh...) | Không |
| `nguon_luc` | Mentor, phòng lab, vốn mồi, hỗ trợ pháp lý... hiện có | Có |
| `thoi_gian` | Thời gian mỗi giai đoạn và toàn chương trình | Có |
| `chi_tieu` | Số lượng dự án tuyển, tỷ lệ tốt nghiệp mong muốn | Không |

## Quy trình

**Bước 1. Xây dựng bộ tiêu chí tuyển chọn và thang điểm**
- Làm gì: Thiết kế bộ tiêu chí chấm thang 100 điểm: tính đổi mới sáng tạo, tính khả thi
  kỹ thuật, năng lực đội ngũ, tiềm năng thị trường, phù hợp lĩnh vực ưu tiên; mỗi tiêu
  chí có trọng số và rubric mô tả các mức điểm để giám khảo chấm nhất quán; đặt ngưỡng
  trúng tuyển.
- Dùng input: `ten_chuong_trinh`, `doi_tuong`, `linh_vuc_uu_tien`, `chi_tieu` (số lượng
  tuyển → mức ngưỡng điểm phù hợp).
- Vai trò: Hội đồng tuyển chọn · AI hỗ trợ: soạn bộ tiêu chí, thang điểm và rubric dự thảo · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: trọng số phải phản ánh mục tiêu chương trình (ươm tạo trong trường
  thì coi trọng tính đổi mới + đội ngũ hơn doanh thu tức thì); rubric phải cụ thể, tránh
  tiêu chí định tính chung chung khó chấm.
- → Kết quả bước: Bộ tiêu chí + thang điểm 100 + rubric chấm + ngưỡng trúng tuyển
  (dự thảo trình hội đồng ươm tạo duyệt).

**Bước 2. Thiết kế lộ trình ươm tạo theo giai đoạn**
- Làm gì: Chia chương trình thành 4 giai đoạn khớp `thoi_gian`: (1) Tuyển chọn — các mốc
  phát động/nhận hồ sơ/chấm/phỏng vấn/công bố; (2) Ươm tạo — hoàn thiện MVP, lịch đào tạo
  kỹ năng, mentor 1-1; (3) Tăng tốc — kết nối thị trường, tập gọi vốn; (4) Tốt nghiệp —
  demo day, đánh giá. Mỗi giai đoạn ghi: thời gian, mục tiêu đầu ra, tiêu chí "qua cửa"
  để sang giai đoạn tiếp theo.
- Dùng input: `thoi_gian`, `chi_tieu`, `doi_tuong`.
- Vai trò: Chuyên viên ươm tạo · AI hỗ trợ: thiết kế timeline 4 giai đoạn dự thảo, ban tổ chức chốt mốc và tiêu chí qua cửa · ⏱ 2–3 giờ (ước tính)
- Lưu ý nghiệp vụ: mỗi giai đoạn phải có "cửa kiểm tra" (gate) với tiêu chí rõ ràng —
  dự án không đạt thì dừng hỗ trợ hoặc kéo dài có điều kiện, tránh nuôi dự án không triển
  vọng; mốc thời gian phải chừa đệm cho tuyển chọn (thường 6–8 tuần).
- → Kết quả bước: Timeline chi tiết 4 giai đoạn (mốc thời gian, đầu ra, tiêu chí qua cửa).

**Bước 3. Phân bổ nguồn lực hỗ trợ**
- Làm gì: Từ `nguon_luc` hiện có: ghép mentor cho từng dự án theo lĩnh vực chuyên môn, lập
  lịch dùng lab/phòng làm việc chung, gói hỗ trợ pháp lý–kế toán (đăng ký doanh nghiệp,
  SHTT), thiết kế cơ chế giải ngân vốn mồi theo mốc (tỷ lệ % từng đợt gắn với KPI giai đoạn).
- Dùng input: `nguon_luc`, `chi_tieu` (số dự án tuyển → chia nguồn lực cho vừa).
- Vai trò: Chuyên viên ươm tạo · AI hỗ trợ: lập bảng phân bổ nguồn lực dự thảo, ban tổ chức xác nhận mentor và lịch lab · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: vốn mồi giải ngân theo mốc đạt được, không cấp một lần; mentor phải
  cam kết thời gian tối thiểu (VD: 2 giờ/tuần/dự án); kiểm tra tổng cam kết không vượt
  nguồn lực thực có.
- → Kết quả bước: Bảng phân bổ nguồn lực (ghép mentor–dự án, lịch lab, lịch giải ngân
  vốn mồi theo mốc).

**Bước 4. Thiết lập KPI và cơ chế đánh giá – tốt nghiệp**
- Làm gì: Đặt KPI đầu ra định lượng (số dự án tốt nghiệp, số MVP hoàn thiện, số dự án gọi
  được vốn, việc làm tạo ra) gắn với `chi_tieu`; thiết kế tiêu chí đánh giá cuối kỳ,
  format demo day (thành phần ban giám khảo, thang điểm), chính sách hỗ trợ sau ươm tạo
  (mạng lưới alumni, ưu đãi dùng lab).
- Dùng input: `chi_tieu`, `thoi_gian`.
- Vai trò: Hội đồng tuyển chọn · AI hỗ trợ: đề xuất KPI và quy chế đánh giá cuối kỳ · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: KPI phải đo được và có mốc thời gian; quy định rõ điều kiện "tốt
  nghiệp" so với "chưa đạt" và quyền lợi khác nhau của 2 nhóm.
- → Kết quả bước: Bộ KPI đầu ra + quy chế đánh giá cuối kỳ, demo day và tốt nghiệp.

**Bước 5. Tổng hợp thành văn bản kế hoạch và trình phê duyệt**
- Làm gì: Ghép kết quả các bước 1–4 thành văn bản kế hoạch hoàn chỉnh theo cấu trúc chuẩn;
  kiểm tra tính khả thi tổng thể (nguồn lực có đủ cho số dự án tuyển không, tổng vốn mồi
  cam kết có vượt ngân sách không); trình hội đồng ươm tạo và viện trưởng phê duyệt.
- Dùng input: `ten_chuong_trinh`, `doi_tuong` (tiêu đề, đối tượng chương trình).
- Vai trò: Viện trưởng · AI hỗ trợ: ghép văn bản và kiểm tra chéo tính khả thi · ⏱ 1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: kiểm tra chéo lần cuối — số mentor đủ cho số dự án, lịch lab không
  chồng chéo, mốc giải ngân khớp timeline; kế hoạch phải ban hành trước khi phát động
  tuyển chọn.
- → Kết quả bước: Văn bản kế hoạch chương trình ươm tạo hoàn chỉnh (trình phê duyệt).

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/Nhu cầu ươm tạo, nguồn lực hiện có/] --> B["Bước 1. Xây dựng bộ tiêu chí tuyển chọn và thang điểm"]
    B --> C["👤 Hội đồng ươm tạo duyệt bộ tiêu chí"]
    C --> D["Bước 2. Thiết kế lộ trình ươm tạo theo giai đoạn"]
    D --> E["Bước 3. Phân bổ nguồn lực hỗ trợ"]
    E --> F["Bước 4. Thiết lập KPI và cơ chế đánh giá - tốt nghiệp"]
    F --> G["Bước 5. Tổng hợp thành văn bản kế hoạch và trình phê duyệt"]
    G --> H["👤 Viện trưởng phê duyệt kế hoạch"]
    H --> I[/Kế hoạch chương trình ươm tạo/]
```

## Đầu ra (Output)
- Kế hoạch chương trình ươm tạo hoàn chỉnh: tiêu chí + thang điểm, timeline các giai đoạn,
  phân bổ nguồn lực, KPI.

**Cấu trúc output chuẩn** (văn bản kế hoạch chương trình ươm tạo — các phần theo đúng
thứ tự):
1. Tiêu đề: tên chương trình + đợt/năm; đơn vị tổ chức; thời gian thực hiện.
2. Đối tượng và lĩnh vực ưu tiên.
3. Tiêu chí tuyển chọn: thang điểm 100 (trọng số từng tiêu chí), rubric chấm, ngưỡng
   trúng tuyển.
4. Lộ trình ươm tạo: 4 giai đoạn (tuyển chọn, ươm tạo, tăng tốc, tốt nghiệp) — mỗi giai
   đoạn ghi mốc thời gian, đầu ra, tiêu chí "qua cửa".
5. Nguồn lực hỗ trợ: mentor, lab, vốn mồi (lịch giải ngân theo mốc), hỗ trợ pháp lý.
6. KPI đầu ra (định lượng, có mốc thời gian).
7. Đánh giá cuối kỳ, demo day và chính sách hỗ trợ sau ươm tạo.

## Checklist nghiệm thu

- [ ] Đủ 7 phần theo "Cấu trúc output chuẩn": tiêu đề, đối tượng và lĩnh vực ưu tiên, tiêu chí tuyển chọn, lộ trình 4 giai đoạn, nguồn lực hỗ trợ, KPI đầu ra, đánh giá cuối kỳ và hỗ trợ sau ươm tạo.
- [ ] Số liệu khớp với Input: số dự án tuyển, nguồn lực (mentor, lab, vốn mồi), thời gian.
- [ ] Không bịa đặt cam kết gọi vốn, cam kết đầu tư hay nguồn lực không có thật.
- [ ] Bộ tiêu chí thang 100 điểm có trọng số và rubric cụ thể cho từng mức điểm, ngưỡng trúng tuyển rõ ràng.
- [ ] Mỗi giai đoạn có "cửa kiểm tra" với tiêu chí qua cửa rõ ràng; dự án không đạt thì dừng hỗ trợ hoặc kéo dài có điều kiện.
- [ ] Tổng cam kết nguồn lực (mentor, lịch lab, vốn mồi giải ngân theo mốc) không vượt nguồn lực thực có.
- [ ] KPI định lượng được, có mốc thời gian; quy định rõ điều kiện tốt nghiệp so với chưa đạt và quyền lợi khác nhau.
- [ ] Kế hoạch ban hành trước khi phát động tuyển chọn.
- [ ] Đã qua Human gate: hội đồng ươm tạo duyệt bộ tiêu chí, viện trưởng phê duyệt kế hoạch và danh sách trúng tuyển.

Tiêu chí đạt = tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, tổ chức, số liệu dưới đây đều là **giả lập**.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `ten_chuong_trinh` | Vườn ươm A — Đợt 2/2026 |
| `doi_tuong` | Sinh viên và giảng viên Trường Đại học A |
| `linh_vuc_uu_tien` | AI ứng dụng, nông nghiệp thông minh, giáo dục số |
| `nguon_luc` | 12 mentor, 02 phòng lab, vốn mồi 500 triệu đồng, hỗ trợ pháp lý |
| `thoi_gian` | 9 tháng (T07/2026 – T03/2027) |
| `chi_tieu` | Tuyển 10 dự án, tối thiểu 6 dự án tốt nghiệp |

### Output mẫu (trích)

```
KẾ HOẠCH CHƯƠNG TRÌNH ƯƠM TẠO "VƯỜN ƯƠM A" — ĐỢT 2/2026
Đơn vị tổ chức: Viện ĐMST & CGCN — Trường Đại học A
Thời gian: 9 tháng (T07/2026 – T03/2027)

1. ĐỐI TƯỢNG VÀ LĨNH VỰC ƯU TIÊN
   - Đối tượng: sinh viên và giảng viên Trường Đại học A.
   - Lĩnh vực ưu tiên: AI ứng dụng, nông nghiệp thông minh, giáo dục số.

2. TIÊU CHÍ TUYỂN CHỌN (thang 100 điểm)
   - Tính đổi mới sáng tạo: 30 điểm
   - Tính khả thi kỹ thuật: 25 điểm
   - Năng lực đội ngũ: 20 điểm
   - Tiềm năng thị trường: 15 điểm
   - Phù hợp lĩnh vực ưu tiên: 10 điểm
   Ngưỡng trúng tuyển: ≥ 70 điểm.

3. LỘ TRÌNH ƯƠM TẠO
   - Giai đoạn 1 – Tuyển chọn (T07–T08/2026): phát động, nhận hồ sơ, chấm, phỏng vấn,
     công bố 10 dự án. Qua cửa: đạt ngưỡng 70 điểm.
   - Giai đoạn 2 – Ươm tạo (T09–T12/2026): hoàn thiện MVP, đào tạo kỹ năng, mentor 1-1
     hằng tuần. Qua cửa: có bản MVP chạy được.
   - Giai đoạn 3 – Tăng tốc (T01–T02/2027): kết nối thị trường, tập gọi vốn, hoàn thiện
     mô hình kinh doanh. Qua cửa: có kế hoạch kinh doanh và ít nhất 01 khách hàng thử nghiệm.
   - Giai đoạn 4 – Tốt nghiệp (T03/2027): demo day, đánh giá tốt nghiệp.

4. NGUỒN LỰC HỖ TRỢ
   - 12 mentor (mỗi dự án 01 mentor chính, cam kết 2 giờ/tuần); 02 phòng lab đặt lịch theo tuần.
   - Vốn mồi 500 triệu đồng, giải ngân theo mốc (30%-40%-30%) khi đạt KPI giai đoạn.
   - Hỗ trợ pháp lý: đăng ký doanh nghiệp, SHTT.

5. KPI ĐẦU RA
   - ≥ 6/10 dự án tốt nghiệp; ≥ 4 MVP hoàn thiện; ≥ 2 dự án gọi được vốn mồi tiếp theo.

6. ĐÁNH GIÁ CUỐI KỲ VÀ SAU ƯƠM TẠO
   - Demo day tháng 3/2027: ban giám khảo gồm hội đồng ươm tạo và nhà đầu tư khách mời,
     chấm thang 100 điểm; điều kiện tốt nghiệp: đạt ≥ 70 điểm và có MVP hoạt động được.
   - Hỗ trợ sau ươm tạo: tham gia mạng lưới alumni, ưu tiên đặt chỗ lab 12 tháng.
```

## Human gate (người kiểm duyệt)
- **Hội đồng ươm tạo** chấm tuyển chọn và đánh giá tốt nghiệp theo thang điểm đã duyệt.
- **Viện trưởng** phê duyệt danh sách trúng tuyển và quyết định giải ngân vốn mồi theo mốc.

## Giới hạn (guardrails)
- KHÔNG cam kết khả năng gọi vốn thành công cho dự án ươm tạo.
- KHÔNG quyết định đầu tư/góp vốn thay mặt nhà trường khi chưa có phê duyệt thẩm quyền.
- KHÔNG tiết lộ ý tưởng/dữ liệu của dự án này cho dự án khác khi chưa được đồng ý.

## Căn cứ & lưu ý
- Quy chế hoạt động vườn ươm/cơ sở ươm tạo của trường (nếu có); quy định quản lý vốn mồi.
- Mọi số liệu trong ví dụ đều giả lập.
- Không dùng tên thật của trường/cá nhân/tổ chức khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/ke-hoach-uom-tao-dmst`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
