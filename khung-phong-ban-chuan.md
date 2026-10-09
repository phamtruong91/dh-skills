# KHUNG PHÒNG BAN CHUẨN — Áp dụng chung cho mọi trường đại học Việt Nam

> **Mục đích:** danh mục phòng ban tổng thể, chuẩn hóa để làm khung mẫu triển khai cho bất kỳ
> trường đại học nào tại Việt Nam.
>
> **Nguyên tắc thiết kế:**
> 1. Thực tế có 2 mô hình tổ chức: **tách chuyên sâu** (mỗi nghiệp vụ một phòng riêng) và
>    **gộp tinh gọn** (gộp nhiều nghiệp vụ vào một phòng, như VNUIS gộp Tài chính + CNTT vào
>    Phòng Tổ chức và Quản trị). Khung này lấy mô hình **tách đầy đủ nhất** làm chuẩn;
>    mọi biến thể gộp/tách đều mapping về phòng chuẩn.
> 2. Skill được đóng gói theo **nghiệp vụ**, gắn với phòng chuẩn → khi gặp trường theo mô hình
>    gộp, chỉ cần tra bảng mapping là biết skill nào thuộc phòng nào, không phải làm lại.
> 3. Tên gọi cụ thể từng trường có thể khác (VD: "Phòng Đào tạo" / "Phòng Quản lý đào tạo"),
>    nhưng mã phòng (B1–B12...) và nghiệp vụ là cố định.

---

## Khối A — Lãnh đạo và Hội đồng

| Mã | Đơn vị | Chức năng (1 dòng) |
|----|--------|--------------------|
| A1 | Hội đồng trường | Cơ quan quyết định chiến lược, phê duyệt quy chế, giám sát hoạt động |
| A2 | Ban Giám hiệu | Hiệu trưởng + các Phó Hiệu trưởng; điều hành toàn bộ hoạt động |
| A3 | Hội đồng Khoa học và Đào tạo | Tư vấn chuyên môn về đào tạo, KHCN; quyết nghị học hàm, chương trình |
| A4 | Các hội đồng tư vấn khác | Tuyển sinh, thi đua–khen thưởng, kỷ luật, xét tốt nghiệp... (hoạt động theo vụ việc) |

## Khối B — Phòng chức năng (chuẩn 12 phòng)

| Mã | Phòng chuẩn | Chức năng (1 dòng) | Biến thể thường gặp |
|----|-------------|--------------------|---------------------|
| B1 | Phòng Hành chính – Tổng hợp | Văn thư, văn bản, lịch công tác, khánh tiết, con dấu | — (hầu như trường nào cũng có) |
| B2 | Phòng Tổ chức – Cán bộ | Tuyển dụng, bổ nhiệm, đánh giá, lương, đào tạo bồi dưỡng, thi đua khen thưởng | Có trường gộp thêm Tài chính, CNTT (mô hình VNUIS) |
| B3 | Phòng Đào tạo | Tuyển sinh ĐH, CTĐT, học vụ, tốt nghiệp, văn bằng | Trường nhỏ gộp thêm SĐH, CTSV |
| B4 | Phòng Đào tạo Sau đại học | Tuyển sinh và quản lý đào tạo thạc sĩ / tiến sĩ | Thường gộp vào B3 |
| B5 | Phòng Khảo thí và Đảm bảo chất lượng | Ngân hàng đề thi, tổ chức thi, tự đánh giá, kiểm định | Có trường gộp với Thanh tra |
| B6 | Phòng KHCN và Hợp tác quốc tế / Hợp tác phát triển | Đề tài NCKH, SHTT, tạp chí, hội thảo, MOU, đoàn ra/vào | Có trường tách HTQT riêng |
| B7 | Phòng Công tác sinh viên | Học bổng, rèn luyện, kỷ luật SV, KTX, việc làm | Có trường gộp vào B3 |
| B8 | Phòng Tài chính – Kế toán | Thu học phí, dự toán/quyết toán, BCTC, công khai tài chính | Có trường gộp vào B2 |
| B9 | Phòng Quản trị – Thiết bị | Mua sắm/đấu thầu, tài sản, bảo trì, phòng học–PTN | Tên gọi: Quản trị, CSVC, Thiết bị... |
| B10 | Phòng Thanh tra và Pháp chế | Thanh tra nội bộ, giải quyết KNTC, thẩm định pháp lý; có trường thêm Kiểm toán nội bộ (HUST) | Có trường gộp vào B5 |
| B11 | Phòng Truyền thông và Tuyển sinh | Thương hiệu & quản trị thương hiệu, nội dung truyền thông, tư vấn tuyển sinh & hướng nghiệp, tuyển sinh theo chiến dịch | Có trường: tuyển sinh thuộc B3, truyền thông thuộc B1; HUST tách Ban Tuyển sinh–Hướng nghiệp và Phòng Truyền thông & Quản trị thương hiệu |
| B12 | Trung tâm CNTT / Chuyển đổi số | Hạ tầng, SIS/LMS, ATTT, dữ liệu dùng chung | Có thể là phòng hoặc trung tâm; có trường gộp vào B2; HUST tách Trung tâm Mạng thông tin và Trung tâm Chuyển đổi số |
| B13 | Ban Xúc tiến đầu tư và Phát triển hạ tầng | Xúc tiến đầu tư, quản lý dự án đầu tư hạ tầng, giám sát dự án | Mới thấy ở HUST; trường khác có thể giao Phòng Quản trị (B9) |

## Khối C — Đơn vị trực thuộc

| Mã | Đơn vị | Chức năng (1 dòng) |
|----|--------|--------------------|
| C1 | Viện Đổi mới sáng tạo và Chuyển giao công nghệ | ĐMST, chuyển giao công nghệ, quản trị dự án, ươm tạo; các viện/trung tâm dịch vụ KHCN, tư vấn |
| C2 | Thư viện – Trung tâm học liệu | Học liệu, số hóa, CSDL, phục vụ bạn đọc (có trường gộp với CNTT) |
| C3 | Trung tâm thực hành nghề nghiệp | Thực hành, thực tập theo ngành đào tạo (VD: thực hành pháp luật, mô phỏng...) |
| C4 | Trạm Y tế | Chăm sóc sức khỏe ban đầu, y tế học đường, phòng chống dịch bệnh (có trường gộp vào CTSV) |
| C5 | Trung tâm Nội trú / Ban Quản lý ký túc xá | Quản lý KTX tập trung: tiếp nhận, an ninh, dịch vụ ăn ở (có trường giao Phòng CTSV) |
| C6 | Cơ quan báo chí – Xuất bản | Báo/tạp chí nội bộ, xuất bản ấn phẩm của trường |
| C7 | Phân hiệu / Cơ sở đào tạo | Đơn vị trực thuộc tại địa phương khác; vận hành thu nhỏ toàn bộ khung (đào tạo, CTSV, hành chính...) |
| C8 | Các trung tâm khác | Ngoại ngữ, đào tạo quốc tế, khảo thí độc lập, tư vấn tâm lý, dịch vụ & hỗ trợ... (tùy trường) |
| C9 | Trung tâm Đào tạo liên tục / Trường bồi dưỡng | Đào tạo ngắn hạn, bồi dưỡng cán bộ theo nhu cầu xã hội/ngành, cấp chứng chỉ (HUST, HVNH) |

## Khối D — Đơn vị đào tạo

| Mã | Đơn vị | Chức năng (1 dòng) |
|----|--------|--------------------|
| D1 | Khoa / Viện đào tạo | Giảng dạy, NCKH, quản lý SV, cố vấn học tập |
| D2 | Bộ môn | Đơn vị chuyên môn trực thuộc khoa |

---

## Bảng mapping biến thể → phòng chuẩn (tra cứu khi triển khai trường mới)

| Nếu trường gộp/tách thế này... | Skill áp dụng của phòng chuẩn |
|---|---|
| Không có B4 (SĐH gộp vào Đào tạo) | Dùng skill nhóm B3 + 5 skill SĐH |
| Không có B7 (CTSV gộp vào Đào tạo) | Dùng skill nhóm B3 + 10 skill CTSV |
| B8 + CNTT gộp vào B2 (mô hình VNUIS) | Dùng skill B2 + B8 + B12, giao cho một đầu mối |
| Không có B10 (Thanh tra gộp vào ĐBCL) | Dùng skill B5 + 4 skill thanh tra |
| Không có B11 (tuyển sinh thuộc B3) | Skill tuyển sinh (B3) + skill truyền thông (nhóm B11 mới) giao B1/B3 phối hợp |
| B12 là trung tâm (không phải phòng) | Skill nhóm B12 giữ nguyên, đổi đầu mối |
| Phòng Tài chính - Quản trị (HLU: gộp tài chính + CSVC) | Dùng skill B8 + B9, một đầu mối |
| Trung tâm CNTT và Thư viện (HLU: gộp IT + thư viện) | Dùng skill B12 + C2, một đầu mối |
| Phòng Tổ chức - Hành chính (HLU, HUP: gộp TC + HC) | Dùng skill B1 + B2, một đầu mối |
| Phòng HCTH gồm Thanh tra + Pháp chế (TLU) | Dùng skill B1 + B10, một đầu mối |
| Phòng Chính trị và CTSV (TLU) | Dùng skill B7 + 2 skill công tác chính trị mới |
| Phòng Công tác HVSV - Y tế (HUP: gộp CTSV + y tế) | Dùng skill B7 + 3 skill y tế (C4) |
| Trung tâm Thông tin - Thư viện (HUP) | Dùng skill B12 + C2 |
| Tạp chí khoa học thuộc Phòng KHCN (TLU, HUP) | Dùng skill `quan-tri-tap-chi-khoa-hoc` (B6) |
| Viện/trung tâm dịch vụ KHCN, tư vấn (TLU, HUP) | Dùng skill nhóm C1 + 2 skill dịch vụ KHCN |
| Phân hiệu / cơ sở địa phương (HLU, TLU) | Áp dụng thu nhỏ toàn bộ khung + 2 skill riêng (C7) |
| HUST dùng "Ban" thay "Phòng" | Mapping tên: Văn phòng ĐH→B1, Ban Tổ chức–Nhân sự→B2, Ban Tài chính–Kế hoạch→B8, Ban CTSV→B7, Ban Hợp tác đối ngoại→B6, Ban Đào tạo→B3, Ban KH–CN→B6, Ban Cơ sở vật chất→B9, Ban Quản lý chất lượng→B5 |
| Ban Tuyển sinh – Hướng nghiệp tách riêng (HUST) | Dùng skill B11 (nhóm tuyển sinh + hướng nghiệp) |
| Phòng Truyền thông & Quản trị thương hiệu (HUST); Phòng Tư vấn tuyển sinh & PT thương hiệu (HVNH) | Dùng skill B11 (nhóm truyền thông + thương hiệu + tư vấn) |
| Ban Xúc tiến đầu tư & PT hạ tầng (HUST) | Phòng chuẩn mới B13; trường không có thì giao B9 |
| Kiểm toán nội bộ trong Ban Thanh tra (HUST) | Dùng 2 skill kiểm toán nội bộ mới (B10) |
| Trung tâm Đào tạo liên tục (HUST); Trường Đào tạo bồi dưỡng cán bộ (HVNH) | Đơn vị mới C9; 3 skill riêng |
| Văn phòng Hội đồng trường (HVNH) | Thuộc A1; 1 skill chuẩn bị họp HĐ trường |
| Viện Đào tạo quốc tế / Viện NCKH (HVNH); Ban QLDA (HUST) | Mapping về C8 / C1 |

**Quy trình áp dụng khung cho một trường mới:**
1. Khảo sát sơ đồ tổ chức thực tế của trường.
2. Tra bảng mapping → mỗi phòng thực tế ánh xạ về 1..n phòng chuẩn.
3. Kích hoạt các skill của phòng chuẩn tương ứng — không cần đóng gói lại.
4. Chỉ đóng gói bổ sung nếu trường có nghiệp vụ đặc thù ngoài khung.
