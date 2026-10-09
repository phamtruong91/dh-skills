> Tư liệu thiết kế trước phiên bản 1.1.0. Các số lượng, mô hình quản trị và căn cứ pháp lý cũ không phải thông tin hiện hành. Đối chiếu README, skills-manifest.json và docs/CAP_NHAT_PHAP_LY.md trước áp dụng.

# Danh mục Skill triển khai cho các phòng ban trường Đại học Việt Nam

> Tổng hợp từ khảo sát cơ cấu tổ chức và chức năng nhiệm vụ các trường ĐH công lập Việt Nam
> (ĐHQG, Bách khoa, Kinh tế, Y Dược, Sư phạm, Ngân hàng...). Tên phòng ban có thể gộp/tách
> khác nhau giữa các trường, nhưng nghiệp vụ lõi giống nhau ~90%.
>
> Mỗi **Skill** = 1 năng lực AI có thể đóng gói (SKILL.md): nhận đầu vào → sinh văn bản / biểu mẫu /
> báo cáo đúng thể thức, kèm checklist quy trình và căn cứ pháp lý liên quan.
>
> **Thang tần suất sử dụng:**
> - ★★★ Rất cao — dùng hàng ngày / hàng tuần
> - ★★ Cao — dùng hàng tháng / mỗi học kỳ
> - ★ Trung bình — dùng hàng năm
> - ☆ Thấp — theo chu kỳ nhiều năm hoặc đột xuất

---

## 1. Phòng Hành chính – Tổng hợp (Văn phòng)

Phòng "xương sống" văn bản của trường — mọi văn bản đi/đến đều qua đây. Skill nhóm này **dùng chung cho toàn trường**.

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 1.1 | `soan-cong-van` | Soạn công văn đi đúng thể thức Nghị định 30/2020 (quốc hiệu, tiêu ngữ, số/ký hiệu, nơi nhận, chữ ký) | Nội dung + nơi nhận → Công văn hoàn chỉnh | ★★★ |
| 1.2 | `soan-to-trinh` | Soạn tờ trình xin chủ trương / phê duyệt của Ban Giám hiệu, Hội đồng trường | Nội dung đề xuất + căn cứ → Tờ trình | ★★★ |
| 1.3 | `soan-thong-bao` | Soạn thông báo nội bộ (lịch họp, nghỉ lễ, quy định mới...) | Nội dung → Thông báo | ★★★ |
| 1.4 | `lap-lich-cong-tac-tuan` | Tổng hợp lịch công tác tuần của Ban Giám hiệu từ đầu việc các đơn vị | Đầu việc các phòng/khoa → Lịch công tác tuần | ★★★ |
| 1.5 | `soan-quyet-dinh-hc` | Soạn quyết định hành chính (thành lập, ban hành văn bản, điều động...) | Căn cứ pháp lý + nội dung → Quyết định | ★★ |
| 1.6 | `soan-bien-ban-hop` | Soạn biên bản cuộc họp / hội nghị từ ghi chép | Ghi chép cuộc họp → Biên bản | ★★ |
| 1.7 | `soan-ke-hoach-ct` | Soạn kế hoạch công tác (tháng/quý/năm) | Mục tiêu + nhiệm vụ → Kế hoạch | ★★ |
| 1.8 | `soan-giay-moi` | Soạn giấy mời họp, hội nghị, lễ kỷ niệm | Nội dung + khách mời → Giấy mời | ★★ |
| 1.9 | `phieu-trinh-ky` | Lập phiếu trình ký văn bản trình lãnh đạo | Văn bản dự thảo → Phiếu trình | ★★ |
| 1.10 | `so-van-ban-di-den` | Template & quy trình quản lý sổ văn bản đi/đến, theo dõi xử lý | — → Sổ + quy trình | ★★ |
| 1.11 | `kich-ban-khanh-tiet` | Kịch bản lễ tân, khánh tiết cho sự kiện (khai giảng, kỷ niệm...) | Thông tin sự kiện → Kịch bản | ★ |
| 1.12 | `bao-cao-tong-ket-vp` | Báo cáo tổng kết công tác văn phòng định kỳ | Số liệu các mảng → Báo cáo | ★ |

## 2. Phòng Tổ chức – Cán bộ

Quản trị toàn bộ vòng đời viên chức. Nhiều quy trình chặt chẽ, rất hợp đóng gói Skill dạng checklist + bộ biểu mẫu.

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 2.1 | `quy-trinh-tuyen-dung` | Trọn gói quy trình tuyển dụng viên chức: kế hoạch → thông báo → hồ sơ → xét tuyển → quyết định → hợp đồng | Nhu cầu nhân sự → Bộ hồ sơ tuyển dụng | ★ |
| 2.2 | `thong-bao-tuyen-dung` | Soạn thông báo tuyển dụng (vị trí, tiêu chuẩn, hồ sơ, thời hạn) | Nhu cầu → Thông báo | ★ |
| 2.3 | `quy-trinh-bo-nhiem` | Checklist + soạn hồ sơ bổ nhiệm / bổ nhiệm lại / miễn nhiệm (tờ trình, phiếu tín nhiệm, quyết định) | Nhân sự → Bộ hồ sơ bổ nhiệm | ★★ |
| 2.4 | `quyet-dinh-dieu-dong` | Soạn quyết định điều động, luân chuyển, biệt phái | Thông tin → Quyết định | ★★ |
| 2.5 | `hop-dong-lam-viec` | Soạn hợp đồng làm việc / hợp đồng lao động | Thông tin NLĐ → Hợp đồng | ★ |
| 2.6 | `phieu-danh-gia-vien-chuc` | Phiếu đánh giá, xếp loại viên chức + hướng dẫn tiêu chí chấm | — → Phiếu + hướng dẫn | ★ |
| 2.7 | `bao-cao-danh-gia-vc` | Tổng hợp kết quả đánh giá viên chức toàn trường | Kết quả các đơn vị → Báo cáo | ★ |
| 2.8 | `quyet-dinh-nang-luong` | Soạn quyết định nâng lương, phụ cấp thâm niên, chuyển ngạch | Danh sách → Quyết định | ★★ |
| 2.9 | `ke-hoach-boi-duong` | Kế hoạch đào tạo, bồi dưỡng cán bộ năm | Nhu cầu → Kế hoạch | ★ |
| 2.10 | `quyet-dinh-cu-di-hoc` | Quyết định cử cán bộ đi đào tạo / tập huấn | Thông tin → Quyết định | ★ |
| 2.11 | `checklist-ho-so-gs-pgs` | Checklist hồ sơ xét công nhận GS/PGS + soạn báo cáo thẩm định | Hồ sơ → Checklist + báo cáo | ☆ |
| 2.12 | `ho-so-de-nghi-khen-thuong` | Hồ sơ đề nghị khen thưởng các cấp (tờ trình, báo cáo thành tích) | Thành tích → Bộ hồ sơ | ★ |
| 2.13 | `quyet-dinh-khen-thuong-kl` | Quyết định khen thưởng / kỷ luật viên chức | Hồ sơ → Quyết định | ★★ |
| 2.14 | `bao-cao-thi-dua` | Báo cáo tổng kết công tác thi đua, khen thưởng | Số liệu → Báo cáo | ★ |
| 2.15 | `de-an-vi-tri-viec-lam` | Xây dựng đề án vị trí việc làm của trường / đơn vị | Hiện trạng → Đề án | ☆ |
| 2.16 | `quy-che-to-chuc-hoat-dong` | Soạn quy chế tổ chức và hoạt động của đơn vị trực thuộc | Chức năng → Quy chế | ☆ |

## 3. Phòng Đào tạo (Quản lý đào tạo)

Phòng có khối lượng văn bản định kỳ lớn nhất trường (tuyển sinh, CTĐT, học vụ, tốt nghiệp).

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 3.1 | `de-an-tuyen-sinh` | Soạn đề án tuyển sinh hằng năm (chỉ tiêu, phương thức, tổ hợp, ngưỡng) | Số liệu → Đề án | ★ |
| 3.2 | `thong-bao-tuyen-sinh` | Soạn thông báo tuyển sinh theo từng phương thức xét tuyển | Đề án → Thông báo | ★★ |
| 3.3 | `bao-cao-ket-qua-tuyen-sinh` | Báo cáo kết quả tuyển sinh gửi Bộ GD&ĐT / cơ quan chủ quản | Số liệu → Báo cáo | ★ |
| 3.4 | `de-an-mo-nganh` | Soạn đề án mở ngành đào tạo (điều kiện đội ngũ, CSVC, chương trình, nhu cầu XH) | Hồ sơ → Đề án | ☆ |
| 3.5 | `khung-chuong-trinh-dao-tao` | Xây dựng khung chương trình đào tạo (mục tiêu, chuẩn đầu ra, cấu trúc) | Thông tin ngành → Khung CTĐT | ★ |
| 3.6 | `ma-tran-chuan-dau-ra` | Lập ma trận đối sánh chuẩn đầu ra học phần – chương trình (CLO–PLO) | Danh mục HP → Ma trận | ★ |
| 3.7 | `de-cuong-chi-tiet-hoc-phan` | Soạn đề cương chi tiết học phần (mục tiêu, nội dung, PPGD, đánh giá) | Thông tin HP → Đề cương | ★★ |
| 3.8 | `ke-hoach-nam-hoc` | Lập kế hoạch năm học (tiến độ đào tạo, lịch thi, nghỉ lễ) | Khung thời gian → Kế hoạch | ★ |
| 3.9 | `lap-thoi-khoa-bieu` | Lập thời khóa biểu học kỳ (xếp lớp, phòng, giảng viên) | Dữ liệu → TKB | ★★ |
| 3.10 | `quy-che-dao-tao` | Soạn / sửa đổi quy chế đào tạo theo quy định Bộ GD&ĐT | Dự thảo → Quy chế | ☆ |
| 3.11 | `quyet-dinh-hoc-vu` | Soạn quyết định cảnh báo học vụ / thôi học / bảo lưu / chuyển trường | Danh sách SV → Quyết định | ★★ |
| 3.12 | `quyet-dinh-tot-nghiep` | Soạn quyết định công nhận tốt nghiệp theo đợt | Danh sách → Quyết định | ★★ |
| 3.13 | `bao-cao-dao-tao-dinh-ky` | Báo cáo công tác đào tạo (học kỳ / năm học) | Số liệu → Báo cáo | ★★ |
| 3.14 | `so-lieu-3-cong-khai-dt` | Tổng hợp số liệu 3 công khai mảng đào tạo (quy mô, chất lượng) | Số liệu → Bảng tổng hợp | ★ |

## 4. Phòng Đào tạo Sau đại học

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 4.1 | `thong-bao-tuyen-sinh-sdh` | Thông báo tuyển sinh thạc sĩ / tiến sĩ | Chỉ tiêu → Thông báo | ★★ |
| 4.2 | `ke-hoach-dao-tao-sdh` | Kế hoạch đào tạo SĐH (tiến độ học viên / NCS) | — → Kế hoạch | ★ |
| 4.3 | `quyet-dinh-hoi-dong-bao-ve` | Quyết định thành lập hội đồng chấm luận văn / luận án | Danh sách → Quyết định | ★★ |
| 4.4 | `bien-ban-bao-ve-luan-van` | Biên bản bảo vệ luận văn thạc sĩ / luận án tiến sĩ | Kết quả → Biên bản | ★★ |
| 4.5 | `bao-cao-dao-tao-sdh` | Báo cáo đào tạo sau đại học hằng năm | Số liệu → Báo cáo | ★ |

## 5. Phòng Khảo thí & Đảm bảo chất lượng

Phòng "nặng" về báo cáo và quy trình kỹ thuật — Skill ở đây có giá trị cao vì liên quan trực tiếp đến kiểm định.

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 5.1 | `quy-trinh-ngan-hang-de-thi` | Quy trình xây dựng ngân hàng đề thi (thu thập – phản biện – phê duyệt – bảo mật) | — → Quy trình + biểu mẫu | ★ |
| 5.2 | `ke-hoach-to-chuc-thi` | Kế hoạch tổ chức kỳ thi kết thúc học phần / tốt nghiệp | Lịch → Kế hoạch | ★★ |
| 5.3 | `quyet-dinh-phan-cong-thi` | Quyết định phân công coi thi / chấm thi | Danh sách → Quyết định | ★★ |
| 5.4 | `bien-ban-phong-thi` | Biên bản phòng thi, biên bản bàn giao bài thi | — → Biên bản | ★★ |
| 5.5 | `quyet-dinh-phuc-khao` | Xử lý phúc khảo: tiếp nhận đơn → quyết định kết quả | Đơn → Quyết định | ★ |
| 5.6 | `bao-cao-tu-danh-gia` | Soạn báo cáo tự đánh giá cơ sở giáo dục / chương trình đào tạo theo bộ tiêu chí | Minh chứng → Báo cáo TĐG | ★ |
| 5.7 | `checklist-minh-chung-kiem-dinh` | Checklist + soạn minh chứng kiểm định theo từng tiêu chí / tiêu chuẩn | Tiêu chí → Bộ minh chứng | ★ |
| 5.8 | `ke-hoach-cai-tien-chat-luong` | Kế hoạch cải tiến chất lượng sau tự đánh giá / kiểm định | Khuyến nghị → Kế hoạch | ★ |
| 5.9 | `thiet-ke-phieu-khao-sat` | Thiết kế phiếu khảo sát SV / giảng viên / cựu SV / nhà tuyển dụng | Mục đích → Phiếu | ★ |
| 5.10 | `phan-tich-ket-qua-khao-sat` | Phân tích kết quả khảo sát, đề xuất cải tiến | Dữ liệu → Báo cáo phân tích | ★ |
| 5.11 | `phan-tich-ket-qua-thi` | Phân tích phổ điểm, độ khó – độ phân biệt của đề thi | Bảng điểm → Báo cáo | ★ |
| 5.12 | `bao-cao-dbcl-nam` | Báo cáo công tác đảm bảo chất lượng năm | Số liệu → Báo cáo | ★ |

## 6. Phòng Khoa học công nghệ & Hợp tác quốc tế

Mỏ Skill lớn nhất cho **trục Nghiên cứu** — vòng đời đề tài NCKH có thể tách thành chuỗi Skill.

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 6.1 | `thong-bao-dang-ky-de-tai` | Thông báo đăng ký đề tài NCKH các cấp | Kế hoạch → Thông báo | ★ |
| 6.2 | `thuyet-minh-de-tai-nckh` | Soạn thuyết minh đề tài NCKH (tính cấp thiết, mục tiêu, nội dung, phương pháp, kinh phí, tiến độ) | Ý tưởng → Thuyết minh | ★★ |
| 6.3 | `hop-dong-thuc-hien-de-tai` | Soạn hợp đồng thực hiện đề tài KHCN | Thuyết minh → Hợp đồng | ★ |
| 6.4 | `bao-cao-tien-do-de-tai` | Báo cáo tiến độ thực hiện đề tài (6 tháng / năm) | Tiến độ → Báo cáo | ★ |
| 6.5 | `bao-cao-nghiem-thu-de-tai` | Báo cáo tổng kết + biên bản nghiệm thu đề tài | Kết quả → Báo cáo + biên bản | ★★ |
| 6.6 | `ho-so-quyet-toan-de-tai` | Checklist + soạn hồ sơ thanh quyết toán kinh phí đề tài | Chứng từ → Bộ hồ sơ | ★ |
| 6.7 | `ho-so-cong-nhan-sang-kien` | Hồ sơ đề nghị công nhận sáng kiến kinh nghiệm | Mô tả → Hồ sơ | ★ |
| 6.8 | `ho-so-dang-ky-shtt` | Hồ sơ đăng ký sáng chế / giải pháp hữu ích | Giải pháp → Hồ sơ | ☆ |
| 6.9 | `cau-truc-bai-bao-khoa-hoc` | Hỗ trợ cấu trúc bài báo khoa học (tóm tắt, từ khóa, IMRaD, trích dẫn) | Bản thảo → Bài báo chuẩn | ★★ |
| 6.10 | `ke-hoach-hoi-thao-khoa-hoc` | Kế hoạch tổ chức hội thảo khoa học (cấp trường / quốc gia / quốc tế) | Chủ đề → Kế hoạch + thư mời | ★ |
| 6.11 | `ky-yeu-hoi-thao` | Biên tập kỷ yếu hội thảo khoa học | Bài viết → Kỷ yếu | ★ |
| 6.12 | `soan-mou-moa` | Soạn biên bản ghi nhớ / thỏa thuận hợp tác (song ngữ Việt–Anh) | Nội dung → MOU/MOA | ★ |
| 6.13 | `ke-hoach-doan-ra-vao` | Kế hoạch đoàn ra / đoàn vào (mục đích, thành phần, chương trình) | Thông tin → Kế hoạch | ★ |
| 6.14 | `bao-cao-ket-qua-doan` | Báo cáo kết quả đoàn công tác nước ngoài / đón đoàn | Diễn biến → Báo cáo | ★ |
| 6.15 | `bao-cao-khcn-nam` | Báo cáo khoa học công nghệ & hợp tác quốc tế hằng năm | Số liệu → Báo cáo | ★ |

## 7. Phòng Công tác sinh viên

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 7.1 | `thong-bao-hoc-bong` | Thông báo học bổng (khuyến khích, tài trợ, chính sách) | Tiêu chí → Thông báo | ★★ |
| 7.2 | `quyet-dinh-cap-hoc-bong` | Quyết định cấp học bổng / miễn giảm học phí | Danh sách → Quyết định | ★★ |
| 7.3 | `phieu-danh-gia-ren-luyen` | Phiếu đánh giá kết quả rèn luyện SV + hướng dẫn chấm | — → Phiếu + hướng dẫn | ★★ |
| 7.4 | `tong-hop-diem-ren-luyen` | Tổng hợp điểm rèn luyện toàn trường theo học kỳ | Kết quả khoa → Bảng tổng hợp | ★★ |
| 7.5 | `quyet-dinh-ky-luat-sv` | Quyết định khen thưởng / kỷ luật sinh viên | Biên bản → Quyết định | ★ |
| 7.6 | `ke-hoach-tuan-shcd` | Kế hoạch Tuần sinh hoạt công dân đầu khóa / đầu năm | Chủ đề → Kế hoạch + nội dung | ★ |
| 7.7 | `ke-hoach-ngay-hoi-viec-lam` | Kế hoạch ngày hội việc làm, kết nối doanh nghiệp | — → Kế hoạch | ★ |
| 7.8 | `khao-sat-viec-lam-sv-tot-nghiep` | Khảo sát + báo cáo tình trạng việc làm SV sau tốt nghiệp | Dữ liệu → Báo cáo | ★ |
| 7.9 | `bao-cao-ctsv-nam` | Báo cáo công tác sinh viên năm học | Số liệu → Báo cáo | ★ |
| 7.10 | `noi-quy-ky-tuc-xa` | Soạn nội quy ký túc xá, quy trình xét duyệt chỗ ở | — → Nội quy + quy trình | ★ |

## 8. Phòng Tài chính – Kế toán

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 8.1 | `thong-bao-muc-thu-hoc-phi` | Thông báo mức thu học phí / lệ phí năm học | Quyết định → Thông báo | ★★ |
| 8.2 | `lap-du-toan-nam` | Lập dự toán thu – chi ngân sách năm | Số liệu → Dự toán | ★ |
| 8.3 | `bao-cao-quyet-toan` | Báo cáo quyết toán ngân sách năm | Chứng từ → Báo cáo | ★ |
| 8.4 | `bao-cao-tai-chinh` | Lập báo cáo tài chính theo chế độ kế toán HCSN | Sổ sách → BCTC | ★ |
| 8.5 | `bao-cao-cong-khai-tai-chinh` | Báo cáo công khai tài chính (minh bạch ngân sách) | Số liệu → Báo cáo | ★ |
| 8.6 | `checklist-chung-tu-thanh-toan` | Checklist chứng từ thanh toán (lương, học bổng, đề tài, mua sắm) | — → Checklist | ★★ |

## 9. Phòng Quản trị – Thiết bị

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 9.1 | `ke-hoach-mua-sam` | Kế hoạch mua sắm trang thiết bị năm | Nhu cầu → Kế hoạch | ★ |
| 9.2 | `ho-so-moi-thau` | Soạn hồ sơ mời thầu / chào hàng cạnh tranh | Yêu cầu → HSMT | ★ |
| 9.3 | `hop-dong-mua-sam` | Soạn hợp đồng mua sắm thiết bị | Kết quả → Hợp đồng | ★ |
| 9.4 | `bien-ban-nghiem-thu-thiet-bi` | Biên bản nghiệm thu, bàn giao thiết bị | Thực tế → Biên bản | ★★ |
| 9.5 | `bien-ban-kiem-ke-tai-san` | Biên bản kiểm kê tài sản cố định | Sổ sách → Biên bản | ★ |
| 9.6 | `ke-hoach-bao-tri-csvc` | Kế hoạch bảo trì, sửa chữa cơ sở vật chất | Hiện trạng → Kế hoạch | ★ |

## 10. Phòng Thanh tra & Pháp chế

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 10.1 | `ke-hoach-thanh-tra-nam` | Kế hoạch thanh tra nội bộ năm (đào tạo, tuyển sinh, thi cử) | — → Kế hoạch | ★ |
| 10.2 | `ket-luan-thanh-tra` | Soạn kết luận thanh tra | Biên bản → Kết luận | ★ |
| 10.3 | `quyet-dinh-giai-quyet-kn` | Quyết định giải quyết khiếu nại / tố cáo | Hồ sơ → Quyết định | ☆ |
| 10.4 | `tham-dinh-phap-ly-van-ban` | Rà soát, cho ý kiến pháp lý đối với dự thảo văn bản nội bộ | Dự thảo → Ý kiến pháp lý | ★★ |

## 11. Trung tâm CNTT / Chuyển đổi số

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 11.1 | `ke-hoach-phat-trien-cntt` | Kế hoạch phát triển hạ tầng & phần mềm (SIS, LMS, tuyển sinh online) | Hiện trạng → Kế hoạch | ☆ |
| 11.2 | `quy-che-an-toan-thong-tin` | Soạn quy chế an toàn thông tin mạng | — → Quy chế | ☆ |
| 11.3 | `bao-cao-chuyen-doi-so` | Báo cáo hiện trạng & kết quả chuyển đổi số | Số liệu → Báo cáo | ★ |

## 12. Thư viện – Trung tâm học liệu

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 12.1 | `ke-hoach-bo-sung-hoc-lieu` | Kế hoạch bổ sung, số hóa học liệu | Nhu cầu → Kế hoạch | ★ |
| 12.2 | `bao-cao-cong-tac-thu-vien` | Báo cáo công tác thư viện (bạn đọc, vốn tài liệu) | Số liệu → Báo cáo | ★ |

## 13. Khoa / Bộ môn

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 13.1 | `phan-cong-giang-day` | Phân công giảng dạy học kỳ cho giảng viên / bộ môn | Danh mục HP → Bảng phân công | ★★ |
| 13.2 | `bien-soan-giao-trinh` | Hỗ trợ biên soạn giáo trình / bài giảng (đề cương, cấu trúc chương) | Đề cương HP → Khung giáo trình | ★ |
| 13.3 | `bao-cao-tong-ket-khoa` | Báo cáo tổng kết năm học của khoa | Số liệu → Báo cáo | ★ |
| 13.4 | `ke-hoach-nckh-khoa` | Kế hoạch NCKH cấp khoa (đề tài, bài báo, hội thảo) | — → Kế hoạch | ★ |

## 14. Skill dùng chung liên phòng ban

| # | Skill | Mô tả | Đầu vào → Đầu ra | Tần suất |
|---|-------|-------|------------------|----------|
| 14.1 | `bao-cao-3-cong-khai` | Báo cáo 3 công khai toàn trường (tổng hợp từ các phòng ban) | Số liệu các đơn vị → Báo cáo | ★ |
| 14.2 | `bao-cao-tong-ket-nam-truong` | Báo cáo tổng kết năm học toàn trường | Báo cáo đơn vị → Báo cáo | ★ |
| 14.3 | `ke-hoach-nam-hoc-truong` | Kế hoạch năm học toàn trường | Nhiệm vụ → Kế hoạch | ★ |
| 14.4 | `quy-che-to-chuc-hoat-dong-truong` | Quy chế tổ chức và hoạt động của trường | — → Quy chế | ☆ |

---

## 15. Xếp hạng Skill được sử dụng nhiều nhất

Dựa trên tần suất phát sinh nghiệp vụ thực tế tại các trường ĐH (văn bản hành chính phát sinh hàng ngày/tuần;
nghiệp vụ đào tạo – thi cử – học vụ theo chu kỳ học kỳ; báo cáo mang tính định kỳ bắt buộc).

### Nhóm ★★★ — Dùng hàng ngày / hàng tuần (ưu tiên triển khai đầu tiên)

| Hạng | Skill | Phòng ban | Vì sao dùng nhiều |
|------|-------|-----------|-------------------|
| 1 | `soan-cong-van` | Hành chính – Tổng hợp | Mọi giao dịch hành chính trong/ngoài trường đều cần công văn |
| 2 | `soan-to-trinh` | Hành chính – Tổng hợp (dùng chung) | Mọi đề xuất lên lãnh đạo đều qua tờ trình |
| 3 | `soan-thong-bao` | Hành chính – Tổng hợp (dùng chung) | Thông báo lịch họp, nghỉ lễ, quy định mới... liên tục |
| 4 | `lap-lich-cong-tac-tuan` | Hành chính – Tổng hợp | Làm mới mỗi tuần cho Ban Giám hiệu |
| 5 | `soan-bien-ban-hop` | Hành chính – Tổng hợp (dùng chung) | Mọi cuộc họp giao ban, hội đồng đều cần biên bản |

### Nhóm ★★ — Dùng hàng tháng / mỗi học kỳ (triển khai đợt 2)

| Hạng | Skill | Phòng ban |
|------|-------|-----------|
| 6 | `soan-quyet-dinh-hc` | Hành chính – Tổng hợp |
| 7 | `de-cuong-chi-tiet-hoc-phan` | Đào tạo / Khoa |
| 8 | `lap-thoi-khoa-bieu` | Đào tạo |
| 9 | `quyet-dinh-hoc-vu` | Đào tạo |
| 10 | `quyet-dinh-tot-nghiep` | Đào tạo |
| 11 | `ke-hoach-to-chuc-thi` | Khảo thí & ĐBCL |
| 12 | `quyet-dinh-phan-cong-thi` | Khảo thí & ĐBCL |
| 13 | `bien-ban-phong-thi` | Khảo thí & ĐBCL |
| 14 | `thuyet-minh-de-tai-nckh` | KHCN |
| 15 | `bao-cao-nghiem-thu-de-tai` | KHCN |
| 16 | `cau-truc-bai-bao-khoa-hoc` | KHCN |
| 17 | `thong-bao-hoc-bong` + `quyet-dinh-cap-hoc-bong` | CTSV |
| 18 | `phieu-danh-gia-ren-luyen` + `tong-hop-diem-ren-luyen` | CTSV |
| 19 | `phan-cong-giang-day` | Khoa / Bộ môn |
| 20 | `tham-dinh-phap-ly-van-ban` | Thanh tra & Pháp chế |
| 21 | `checklist-chung-tu-thanh-toan` | Tài chính – Kế toán |
| 22 | `bien-ban-nghiem-thu-thiet-bi` | Quản trị – Thiết bị |
| 23 | `quy-trinh-bo-nhiem` | Tổ chức – Cán bộ |
| 24 | `quyet-dinh-nang-luong` | Tổ chức – Cán bộ |
| 25 | `bao-cao-dao-tao-dinh-ky` | Đào tạo |

### Nhóm ★ — Bắt buộc theo chu kỳ năm (giá trị cao dù tần suất thấp hơn)

`de-an-tuyen-sinh`, `bao-cao-ket-qua-tuyen-sinh`, `bao-cao-3-cong-khai`, `bao-cao-tu-danh-gia`,
`checklist-minh-chung-kiem-dinh`, `bao-cao-khcn-nam`, `bao-cao-tai-chinh`, `ke-hoach-tuyen-dung`,
`phieu-danh-gia-vien-chuc`, `bao-cao-ctsv-nam`, `khao-sat-viec-lam-sv-tot-nghiep`.

---

## 16. Gợi ý lộ trình triển khai

- **Đợt 1 (nền tảng):** 5 skill ★★★ nhóm Văn bản hành chính — dùng chung toàn trường, ROI cao nhất vì
  tần suất cao và mọi phòng ban đều cần.
- **Đợt 2 (theo học kỳ):** skill Đào tạo + Khảo thí + CTSV — bám theo chu kỳ tuyển sinh → giảng dạy →
  thi cử → tốt nghiệp → học bổng.
- **Đợt 3 (chuyên sâu):** chuỗi skill vòng đời đề tài NCKH (6.1 → 6.6), skill kiểm định & tự đánh giá,
  skill tài chính – nhân sự.
- Mỗi Skill khi đóng gói gồm: **mô tả + đầu vào/đầu ra + template mẫu + checklist quy trình +
  căn cứ pháp lý** (Luật Giáo dục ĐH, NĐ 30/2020 về công tác văn thư, Thông tư 12/2017 về kiểm định...).

---
*Tổng: 113 Skill — 12 (HCTH) + 16 (TCCB) + 14 (Đào tạo) + 5 (SĐH) + 12 (KT&ĐBCL) + 15 (KHCN&HTQT) + 10 (CTSV) + 6 (TCKT) + 6 (QTTB) + 4 (TTPC) + 3 (CNTT) + 2 (Thư viện) + 4 (Khoa) + 4 (dùng chung). Toàn bộ đã được đóng gói thành SKILL.md tại `skills/<mã-skill>/` — xem [chỉ mục](skills/README.md).*
*File sơ đồ use case tương tác: `so-do-case-phong-ban.html` (cùng thư mục).*
