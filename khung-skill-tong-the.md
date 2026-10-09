# KHUNG SKILL TỔNG THỂ — Khung mẫu áp dụng chung cho mọi trường đại học Việt Nam

> **Mục đích:** khung mẫu đóng gói skill AI cho khối phòng ban trường đại học, có thể áp dụng
> nguyên trạng cho bất kỳ trường nào (đối chiếu mã phòng với `khung-phong-ban-chuan.md`).
>
> **Kiến trúc 2 tầng:**
> - **Tầng 1 — Skill lõi dùng chung (18 skill):** năng lực AI xuyên phòng ban, không phụ thuộc tên
>   gọi đơn vị. Mọi trường đều dùng được ngay.
> - **Tầng 2 — Skill nghiệp vụ theo phòng ban (128 skill):** chi tiết từng nghiệp vụ, gắn với mã
>   phòng chuẩn B1–B12, C1–C3, D1, A3. Khi gặp trường theo mô hình gộp, tra bảng mapping trong
>   `khung-phong-ban-chuan.md` để giao đúng đầu mối — không cần đóng gói lại.

---

## Chuẩn cấu trúc file SKILL.md (áp dụng cho mọi skill trong khung)

Mỗi skill = 1 thư mục `skills/<mã-skill>/SKILL.md` gồm 10 mục:

1. **Frontmatter**: `name` (mã skill), `description` (1–2 câu, nêu khi nào dùng)
2. **Khi nào dùng**
3. **Đầu vào (Input)**: bảng Trường | Mô tả | Bắt buộc
4. **Quy trình**: các bước chi tiết để thực hiện nghiệp vụ — mỗi bước gồm:
   - **Làm gì**: thao tác cụ thể, không chung chung;
   - **Dùng input**: trường dữ liệu nào của Input được dùng ở bước này;
   - **Vai trò**: nhân sự thực hiện bước này (chức danh/đơn vị cụ thể: chuyên viên, trưởng phòng,
     hiệu trưởng, hội đồng...) + cách AI hỗ trợ bước đó — kèm thời gian ước tính;
   - **Lưu ý nghiệp vụ**: quy tắc, điểm kiểm tra;
   - **→ Kết quả bước**: bán thành phẩm cụ thể của bước đó.
5. **Đầu ra (Output)**: danh sách sản phẩm + **Cấu trúc output chuẩn** (khung mẫu cố định
   của sản phẩm chính: các phần bắt buộc theo đúng thứ tự)
6. **Checklist nghiệm thu**: bộ tiêu chí đánh giá output đạt/không đạt (đủ phần theo cấu trúc
   chuẩn, số liệu khớp input, không bịa dữ liệu, đúng thể thức, đã qua human gate)
7. **Ví dụ mô phỏng**: Input mẫu + Output mẫu bằng **dữ liệu giả lập** (trường hư cấu
   "Trường Đại học A", nhân vật/số liệu hư cấu, ghi chú rõ giả lập) — Output mẫu phải
   tuân đúng **Cấu trúc output chuẩn** ở mục 5
8. **Human gate (người kiểm duyệt)**: ai phải duyệt ở bước nào trước khi output được dùng/phát hành
9. **Giới hạn (guardrails)**: những việc AI tuyệt đối KHÔNG được làm (không ra quyết định thay,
   không tự phát hành, không bịa số liệu/minh chứng/trích dẫn...)
10. **Căn cứ & lưu ý**: văn bản pháp lý liên quan

> Mô hình thực thi của mọi skill: **Input → từng bước quy trình (mỗi bước cho ra bán thành phẩm)
> → Output theo khung chuẩn**. Có input đầy đủ và làm đúng các bước thì cho ra output chuẩn —
> đúng như một quy trình nghiệp vụ thực tế.

> Mục 7–8 là chuẩn bắt buộc mới (học từ khung VNUIS), đang được bổ sung cho toàn bộ skill.

---

## TẦNG 1 — Skill lõi dùng chung (18 skill)

| Mã | Tên | Mô tả | Tần suất | Human gate | Giới hạn |
|----|-----|-------|----------|------------|----------|
| `ra-soat-du-thao-van-ban` | Rà soát dự thảo văn bản | Kiểm tra thể thức (NĐ 30/2020), logic, thuật ngữ, số liệu → bảng lỗi + bản sạch | ★★★ | Chuyên viên soạn + người ký duyệt | Không thay thẩm định pháp lý/chuyên môn cuối |
| `kiem-tra-day-du-ho-so` | Kiểm tra đầy đủ hồ sơ | Đối chiếu hồ sơ với checklist, nêu thiếu, gợi ý bổ sung | ★★ | Chuyên viên ra quyết định | Không tự phê duyệt/từ chối hồ sơ |
| `hop-nhat-bao-cao-don-vi` | Hợp nhất báo cáo nhiều đơn vị | Gộp báo cáo theo mẫu chung, loại trùng, gap log số liệu thiếu | ★★ | Đầu mối xác nhận số liệu | Không bịa số liệu; giữ liên kết nguồn |
| `executive-brief-trinh-lanh-dao` | Executive brief trình lãnh đạo | Tóm tắt nhiều nguồn → memo + bảng vấn đề cần quyết định | ★★ | Thư ký kiểm tra nguồn; lãnh đạo quyết | Không ra quyết định thay lãnh đạo |
| `chuan-bi-hop-va-action-tracker` | Chuẩn bị họp & theo dõi action | Brief trước họp, trích kết luận, action theo owner/deadline | ★★★ | Thư ký xác nhận kết luận và hạn | Không tự gửi lịch; không ghi đè biên bản |
| `faq-chinh-sach-co-trich-nguon` | Hỏi đáp chính sách có trích nguồn | Trả lời theo văn bản, nêu nguồn + ngày hiệu lực | ★★ | Đơn vị nghiệp vụ duyệt corpus | Không tư vấn ngoài chính sách; không dùng văn bản hết hiệu lực |
| `dich-thuat-song-ngu-va-thuat-ngu` | Dịch song ngữ & quản lý thuật ngữ | Dịch Việt–Anh, QA thuật ngữ theo glossary | ★★ | Biên tập song ngữ duyệt | Không thay phiên dịch pháp lý cuối |
| `quan-ly-phien-ban-tai-lieu` | Quản lý file & phiên bản | Index, phát hiện trùng/phiên bản, đề xuất taxonomy (chỉ đọc) | ★ | Chủ sở hữu thư mục duyệt | Không xóa/di chuyển/đổi tên tự động |
| `triage-case-sinh-vien` | Phân loại case sinh viên | Tóm tắt, phân loại, mức độ ưu tiên, dự thảo phản hồi | ★★ | Cán bộ xác nhận và liên hệ | Không tự gửi; không chẩn đoán tâm lý/y tế |
| `audit-tien-do-tot-nghiep` | Audit tiến độ tốt nghiệp | Đối chiếu bảng điểm với CTĐT, liệt kê học phần thiếu, giải thích | ★★ | Chuyên viên/hội đồng quyết | Không cập nhật hệ thống; ẩn danh dữ liệu |
| `tong-quan-tai-lieu-khoa-hoc` | Tổng quan tài liệu khoa học | Ma trận literature, so sánh phương pháp/kết quả, gap, trích dẫn chuẩn | ★★ | Nhà nghiên cứu kiểm tra | Không bịa trích dẫn; tuân thủ bản quyền |
| `theo-doi-grant-nghien-cuu` | Theo dõi grant nghiên cứu | Checklist điều kiện, outline đề xuất, tracker milestone/deliverable | ★ | PI/phòng KHCN duyệt | Không viết dữ liệu nghiên cứu giả |
| `phan-tich-chenh-lech-ngan-sach` | Phân tích chênh lệch ngân sách | Đối chiếu dự toán/thực hiện, variance, dự thảo giải trình | ★ | Kế toán/chủ tài khoản duyệt | Không tự điều chỉnh ngân sách |
| `tro-ly-giang-day` | Trợ lý giảng dạy | Lesson plan, học liệu, rubric, dự thảo feedback | ★★ | Giảng viên duyệt toàn bộ | Không chấm điểm cuối thay giảng viên |
| `helpdesk-cntt-triage` | Helpdesk CNTT | Phân loại ticket, dự thảo hướng xử lý, FAQ, báo cáo xu hướng | ★★ | Kỹ thuật viên kiểm thử | Không chạy lệnh/thay đổi hệ thống tự động |
| `ke-hoach-to-chuc-su-kien` | Kế hoạch tổ chức sự kiện | Timeline, checklist, RACI, kịch bản run-of-show, báo cáo sau sự kiện | ★ | Ban tổ chức duyệt | Không đặt dịch vụ/gửi thư tự động |
| `theo-doi-thay-doi-van-ban-phap-quy` | Theo dõi thay đổi văn bản pháp quy | So sánh văn bản cũ/mới, ma trận nghĩa vụ thay đổi, checklist cập nhật | ★ | Pháp chế/nghiệp vụ duyệt | Không đưa kết luận pháp lý cuối |
| `dong-goi-skill-tu-quy-trinh` | Đóng gói skill từ quy trình (meta) | Phân rã quy trình thực tế → process map, skill spec, test case | ☆ | Process owner nghiệm thu | Không đóng gói khi thiếu mẫu và tiêu chí kiểm thử |

---

## TẦNG 2 — Skill nghiệp vụ theo phòng ban (128 skill)

Chi tiết từng skill xem tại `skills/<mã-skill>/SKILL.md` và [chỉ mục](skills/README.md).
Các skill **mới bổ sung** (từ đối chiếu khung VNUIS) được đánh dấu ★.

### B1. Phòng Hành chính – Tổng hợp (12)
`soan-cong-van`, `soan-to-trinh`, `soan-thong-bao`, `lap-lich-cong-tac-tuan`, `soan-bien-ban-hop`, `soan-quyet-dinh-hc`, `soan-ke-hoach-ct`, `soan-giay-moi`, `phieu-trinh-ky`, `so-van-ban-di-den`, `kich-ban-khanh-tiet`, `bao-cao-tong-ket-vp`

### B2. Phòng Tổ chức – Cán bộ (16)
`quy-trinh-tuyen-dung`, `thong-bao-tuyen-dung`, `quy-trinh-bo-nhiem`, `quyet-dinh-dieu-dong`, `hop-dong-lam-viec`, `phieu-danh-gia-vien-chuc`, `bao-cao-danh-gia-vc`, `quyet-dinh-nang-luong`, `ke-hoach-boi-duong`, `quyet-dinh-cu-di-hoc`, `checklist-ho-so-gs-pgs`, `ho-so-de-nghi-khen-thuong`, `quyet-dinh-khen-thuong-kl`, `bao-cao-thi-dua`, `de-an-vi-tri-viec-lam`, `quy-che-to-chuc-hoat-dong`

### B3. Phòng Đào tạo (14)
`de-an-tuyen-sinh`, `thong-bao-tuyen-sinh`, `bao-cao-ket-qua-tuyen-sinh`, `de-an-mo-nganh`, `khung-chuong-trinh-dao-tao`, `ma-tran-chuan-dau-ra`, `de-cuong-chi-tiet-hoc-phan`, `ke-hoach-nam-hoc`, `lap-thoi-khoa-bieu`, `quy-che-dao-tao`, `quyet-dinh-hoc-vu`, `quyet-dinh-tot-nghiep`, `bao-cao-dao-tao-dinh-ky`, `so-lieu-3-cong-khai-dt`

### B4. Phòng Đào tạo Sau đại học (5)
`thong-bao-tuyen-sinh-sdh`, `ke-hoach-dao-tao-sdh`, `quyet-dinh-hoi-dong-bao-ve`, `bien-ban-bao-ve-luan-van`, `bao-cao-dao-tao-sdh`

### B5. Phòng Khảo thí và Đảm bảo chất lượng (12)
`quy-trinh-ngan-hang-de-thi`, `ke-hoach-to-chuc-thi`, `quyet-dinh-phan-cong-thi`, `bien-ban-phong-thi`, `quyet-dinh-phuc-khao`, `bao-cao-tu-danh-gia`, `checklist-minh-chung-kiem-dinh`, `ke-hoach-cai-tien-chat-luong`, `thiet-ke-phieu-khao-sat`, `phan-tich-ket-qua-khao-sat`, `phan-tich-ket-qua-thi`, `bao-cao-dbcl-nam`

### B6. Phòng KHCN và Hợp tác quốc tế (15)
`thong-bao-dang-ky-de-tai`, `thuyet-minh-de-tai-nckh`, `hop-dong-thuc-hien-de-tai`, `bao-cao-tien-do-de-tai`, `bao-cao-nghiem-thu-de-tai`, `ho-so-quyet-toan-de-tai`, `ho-so-cong-nhan-sang-kien`, `ho-so-dang-ky-shtt`, `cau-truc-bai-bao-khoa-hoc`, `ke-hoach-hoi-thao-khoa-hoc`, `ky-yeu-hoi-thao`, `soan-mou-moa`, `ke-hoach-doan-ra-vao`, `bao-cao-ket-qua-doan`, `bao-cao-khcn-nam`

### B7. Phòng Công tác sinh viên (10)
`thong-bao-hoc-bong`, `quyet-dinh-cap-hoc-bong`, `phieu-danh-gia-ren-luyen`, `tong-hop-diem-ren-luyen`, `quyet-dinh-ky-luat-sv`, `ke-hoach-tuan-shcd`, `ke-hoach-ngay-hoi-viec-lam`, `khao-sat-viec-lam-sv-tot-nghiep`, `bao-cao-ctsv-nam`, `noi-quy-ky-tuc-xa`

### B8. Phòng Tài chính – Kế toán (6)
`thong-bao-muc-thu-hoc-phi`, `lap-du-toan-nam`, `bao-cao-quyet-toan`, `bao-cao-tai-chinh`, `bao-cao-cong-khai-tai-chinh`, `checklist-chung-tu-thanh-toan`

### B9. Phòng Quản trị – Thiết bị (6)
`ke-hoach-mua-sam`, `ho-so-moi-thau`, `hop-dong-mua-sam`, `bien-ban-nghiem-thu-thiet-bi`, `bien-ban-kiem-ke-tai-san`, `ke-hoach-bao-tri-csvc`

### B10. Phòng Thanh tra và Pháp chế (4)
`ke-hoach-thanh-tra-nam`, `ket-luan-thanh-tra`, `quyet-dinh-giai-quyet-kn`, `tham-dinh-phap-ly-van-ban`

### B11. Phòng Truyền thông và Tuyển sinh (8) ★ mới
| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-truyen-thong-nam` | Kế hoạch truyền thông năm | Mục tiêu, thông điệp chủ đạo, kênh, lịch chiến dịch, KPI |
| `content-calendar-truyen-thong` | Content calendar | Lịch đăng bài tuần/tháng: chủ đề, format, kênh, người phụ trách |
| `bai-viet-truyen-thong` | Bài viết truyền thông | Bài website/fanpage theo brand voice, kèm checklist kiểm chứng facts |
| `kich-ban-video-truyen-thong` | Kịch bản video truyền thông | Kịch bản từng cảnh + lời thoại + yêu cầu hình ảnh |
| `press-kit-su-kien` | Press kit sự kiện | Thông cáo báo chí, fact sheet, ảnh, thông tin liên hệ |
| `faq-tuyen-sinh` | FAQ tuyển sinh | Hỏi đáp theo quy chế/đề án tuyển sinh, trích nguồn + năm áp dụng |
| `funnel-theo-doi-thi-sinh` | Funnel theo dõi thí sinh | Nhóm lead theo giai đoạn, checklist hồ sơ, báo cáo chuyển đổi |
| `campaign-brief-tuyen-sinh` | Campaign brief tuyển sinh | Brief chiến dịch: mục tiêu, đối tượng, thông điệp, kênh, ngân sách, KPI |

### B12. Trung tâm CNTT / Chuyển đổi số (3)
`ke-hoach-phat-trien-cntt`, `quy-che-an-toan-thong-tin`, `bao-cao-chuyen-doi-so`

### C1. Viện Đổi mới sáng tạo và Chuyển giao công nghệ (4) ★ mới
| Mã | Tên | Mô tả |
|----|-----|-------|
| `pmo-quan-tri-du-an` | Quản trị dự án (PMO) | Tracker tiến độ, issue/risk log, lessons learned theo dự án |
| `bao-cao-du-an-dinh-ky` | Báo cáo dự án định kỳ | Báo cáo cho khách hàng/đối tác: tiến độ, deliverable, KPI, vấn đề |
| `ho-so-chuyen-giao-cong-nghe` | Hồ sơ chuyển giao công nghệ | Định giá, điều khoản thương thảo, biên bản chuyển giao |
| `ke-hoach-uom-tao-dmst` | Kế hoạch ươm tạo ĐMST | Tiêu chí tuyển chọn, lộ trình ươm tạo, KPI đầu ra |

### C2. Thư viện – Trung tâm học liệu (2)
`ke-hoach-bo-sung-hoc-lieu`, `bao-cao-cong-tac-thu-vien`

### D1. Khoa / Bộ môn (4)
`phan-cong-giang-day`, `bien-soan-giao-trinh`, `bao-cao-tong-ket-khoa`, `ke-hoach-nckh-khoa`

### A3. Hội đồng Khoa học và Đào tạo (3) ★ mới
| Mã | Tên | Mô tả |
|----|-----|-------|
| `bien-ban-hop-hoi-dong-khdt` | Biên bản họp Hội đồng KH&ĐT | Diễn biến, ý kiến thành viên, biểu quyết theo từng nội dung |
| `nghi-quyet-hoi-dong-khdt` | Nghị quyết Hội đồng KH&ĐT | Quyết nghị về chương trình, đề tài, học hàm... |
| `phieu-lay-y-kien-hoi-dong` | Phiếu lấy ý kiến hội đồng | Phiếu xin ý kiến bằng văn bản khi không họp tập trung |

### Bổ sung từ đối chiếu HLU / TLU / HUP (14 skill ★ mới)

**C4. Trạm Y tế** (TLU; HUP gộp vào CTSV)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-y-te-hoc-duong` | Kế hoạch y tế học đường | Chăm sóc sức khỏe ban đầu, phòng chống dịch bệnh, vệ sinh trường học |
| `bao-cao-cong-tac-y-te` | Báo cáo công tác y tế | Báo cáo định kỳ: khám sức khỏe, dịch bệnh, BHYT |
| `ho-so-quan-ly-suc-khoe` | Hồ sơ quản lý sức khỏe | Sổ theo dõi sức khỏe CBVC/SV, hồ sơ BHYT |

**C7. Phân hiệu / Cơ sở đào tạo** (HLU, TLU) — ngoài 2 skill riêng, phân hiệu áp dụng thu nhỏ toàn bộ khung

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-hoat-dong-phan-hieu` | Kế hoạch hoạt động phân hiệu | Kế hoạch năm của phân hiệu theo khung trường mẹ |
| `bao-cao-tong-hop-phan-hieu` | Báo cáo tổng hợp phân hiệu | Báo cáo gửi trường mẹ: đào tạo, CTSV, tài chính, CSVC |

**B7 bổ sung — Công tác chính trị, tư tưởng** (TLU: Phòng Chính trị và CTSV)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-giao-duc-chinh-tri-tu-tuong` | Kế hoạch giáo dục chính trị, tư tưởng | Giáo dục chính trị cho CBVC/SV, sinh hoạt chuyên đề |
| `bao-cao-cong-tac-chinh-tri` | Báo cáo công tác chính trị | Báo cáo định kỳ công tác tư tưởng, tuyên truyền |

**B6 bổ sung — Tạp chí khoa học** (TLU, HUP)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `quan-tri-tap-chi-khoa-hoc` | Quản trị tạp chí khoa học | Quy trình bình duyệt, xuất bản số tạp chí, ISSN |

**C1 bổ sung — Dịch vụ KHCN** (TLU, HUP: viện/trung tâm tư vấn)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ho-so-hop-dong-dich-vu-khcn` | Hồ sơ hợp đồng dịch vụ KHCN | Hợp đồng tư vấn, chuyển giao dịch vụ, nghiệm thu dịch vụ |
| `bao-cao-dich-vu-khcn` | Báo cáo dịch vụ KHCN | Báo cáo hoạt động dịch vụ: doanh thu, khách hàng, dự án |

**C5. Trung tâm Nội trú** (TLU)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-tiep-nhan-quan-ly-noi-tru` | Kế hoạch tiếp nhận & quản lý nội trú | Tiếp nhận SV, phân phòng, an ninh, dịch vụ ăn ở, căng tin |

**C6. Cơ quan báo chí – Xuất bản** (HLU)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-hoat-dong-bao-chi` | Kế hoạch hoạt động báo chí | Kế hoạch xuất bản báo/tạp chí nội bộ theo kỳ |
| `bien-tap-xuat-ban-an-pham` | Biên tập & xuất bản ấn phẩm | Quy trình biên tập, chế bản, phát hành ấn phẩm |

**C3. Trung tâm thực hành nghề nghiệp** (HLU: Trung tâm Thực hành pháp luật)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-hoat-dong-trung-tam-thuc-hanh` | Kế hoạch trung tâm thực hành | Kế hoạch thực hành, thực tập mô phỏng theo ngành |

### Bổ sung từ đối chiếu HUST / HVNH (11 skill ★ mới) — chỉ phòng ban chức năng, chưa gồm khoa

**C9. Trung tâm Đào tạo liên tục / Trường bồi dưỡng** (HUST, HVNH)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-dao-tao-lien-tuc` | Kế hoạch đào tạo liên tục | Khảo sát nhu cầu, danh mục khóa ngắn hạn, lịch khai giảng, dự toán |
| `to-chuc-khoa-boi-duong-ngan-han` | Tổ chức khóa bồi dưỡng ngắn hạn | Kế hoạch chi tiết khóa học: giảng viên, học liệu, hậu cần, đánh giá |
| `cap-chung-chi-dao-tao-lien-tuc` | Cấp chứng chỉ đào tạo liên tục | Xét điều kiện hoàn thành, quyết định cấp chứng chỉ, sổ cấp |

**B13. Ban Xúc tiến đầu tư và Phát triển hạ tầng** (HUST)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-xuc-tien-dau-tu` | Kế hoạch xúc tiến đầu tư | Định hướng thu hút đầu tư, danh mục kêu gọi, đối tác mục tiêu |
| `ho-so-du-an-dau-tu-ha-tang` | Hồ sơ dự án đầu tư hạ tầng | Đề xuất dự án: mục tiêu, quy mô, tổng mức đầu tư, hiệu quả, tiến độ |
| `bao-cao-giam-sat-du-an-dau-tu` | Báo cáo giám sát dự án đầu tư | Theo dõi tiến độ, giải ngân, vướng mắc, kiến nghị |

**B10 bổ sung — Kiểm toán nội bộ** (HUST: Ban Thanh tra, Pháp chế và Kiểm toán nội bộ)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-kiem-toan-noi-bo` | Kế hoạch kiểm toán nội bộ | Kế hoạch năm: đối tượng, phạm vi, phương pháp kiểm toán |
| `bao-cao-kiem-toan-noi-bo` | Báo cáo kiểm toán nội bộ | Phát hiện, đánh giá rủi ro, kiến nghị khắc phục |

**B11 bổ sung — Thương hiệu & tư vấn tuyển sinh** (HUST, HVNH)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `ke-hoach-quan-tri-thuong-hieu` | Kế hoạch quản trị thương hiệu | Định vị thương hiệu, bộ nhận diện, giám sát hình ảnh, xử lý khủng hoảng truyền thông |
| `kich-ban-tu-van-tuyen-sinh` | Kịch bản tư vấn tuyển sinh & hướng nghiệp | Kịch bản tư vấn theo đối tượng (học sinh, phụ huynh), câu hỏi thường gặp, chuyển đổi |

**A1 bổ sung — Văn phòng Hội đồng trường** (HVNH)

| Mã | Tên | Mô tả |
|----|-----|-------|
| `chuan-bi-hop-hoi-dong-truong` | Chuẩn bị họp Hội đồng trường | Tài liệu họp, dự thảo nghị quyết, biên bản, theo dõi thực hiện nghị quyết |

### Skill dùng chung liên phòng ban (4)
`bao-cao-3-cong-khai`, `bao-cao-tong-ket-nam-truong`, `ke-hoach-nam-hoc-truong`, `quy-che-to-chuc-hoat-dong-truong`

---

## Tổng hợp số lượng

| Tầng | Số skill | Tình trạng |
|------|----------|------------|
| Tầng 1 — lõi dùng chung | 18 | Đang đóng gói |
| Tầng 2 — B1–B10, B12, C2, D1, dùng chung | 113 | Đã đóng gói xong |
| Tầng 2 — B11, C1, A3 (mới) | 15 | Đang đóng gói |
| Tầng 2 — bổ sung từ HLU/TLU/HUP (C3–C7, B6/B7/C1 bổ sung) | 14 | Đang đóng gói |
| Tầng 2 — bổ sung từ HUST/HVNH (C9, B13, B10/B11/A1 bổ sung) | 11 | Mới (chuẩn bị đóng gói) |
| **Tổng** | **171** | |

## Quy tắc mở rộng khung
1. Skill mới phải gắn được vào 1 trong 2 tầng và 1 mã phòng chuẩn (hoặc "dùng chung").
2. Mọi skill mới tuân thủ chuẩn 8 mục (bao gồm Human gate + Giới hạn) và dữ liệu giả lập.
3. Khi phát hiện nghiệp vụ đặc thù của một trường, đóng gói thành skill mới ở Tầng 2 và cập nhật khung.

### Quy ước dữ liệu demo (áp dụng toàn bộ skill)
- Tên trường: **Trường Đại học A** (viết tắt ĐHA trong số ký hiệu văn bản).
- Địa chỉ và thông tin cơ bản: đúng chuẩn định dạng (vd: Số 123, đường B, thành phố C; SĐT 0900 000 001; email ...@dha.edu.vn).
- Tên người: dạng ABC (vd: PGS.TS. Nguyễn Văn A).
- Tên tổ chức khác: dạng ABC (Học viện B, Công ty TNHH D...).
- Tên phòng ban: giữ nguyên theo Khung phòng ban chuẩn (Phòng Đào tạo, Phòng HCTH...).
- Tất cả đều là dữ liệu giả lập, không liên quan tổ chức/cá nhân có thật.
