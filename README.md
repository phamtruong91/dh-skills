# University AI Skills Framework

**Bộ 171 skill AI phục vụ nghiệp vụ và quản trị trường đại học Việt Nam.**

Chuẩn hóa cách chuẩn bị văn bản, xử lý hồ sơ, tổng hợp số liệu, điều phối công việc, nghiên cứu và giảng dạy. Mỗi skill xác định dữ liệu đầu vào, quy trình, sản phẩm cần giao, định dạng file và trách nhiệm kiểm duyệt.

[![Version](https://img.shields.io/badge/version-1.3.1-1f4e79)](CHANGELOG.md)
[![Skills](https://img.shields.io/badge/skills-171-256D4A)](skills/README.md)
[![License](https://img.shields.io/badge/license-CC_BY--SA_4.0-555555)](LICENSE)

[Danh mục skill](skills/README.md) · [Quy cách đầu ra](docs/QUY_CACH_DAU_RA.md) · [Manifest](skills-manifest.json) · [Nhật ký thay đổi](CHANGELOG.md)

| Quy mô | Giá trị |
| --- | ---: |
| Phiên bản nội dung | **1.3.1** |
| Ngày cập nhật bộ skill | **10/10/2026** |
| Tổng số skill | **171** |
| Skill lõi dùng chung | **18** |
| Skill nghiệp vụ | **153** |
| Định dạng đầu ra được khai báo | **15** |

## Những điểm chính của phiên bản 1.3.1

- **Giao file thực tế:** khi được yêu cầu tạo sản phẩm nghiệp vụ, skill phải tạo file tải được và cung cấp liên kết ngay, không chờ yêu cầu xuất file lần nữa.
- **Chọn định dạng theo sản phẩm:** phân biệt định dạng mặc định với định dạng bổ sung; ưu tiên yêu cầu trực tiếp của người dùng và biểu mẫu áp dụng.
- **Giữ chỗ điền đúng mẫu:** thông tin chưa có được chừa bằng dòng dấu chấm, dấu gạch hoặc ô trống theo mẫu gốc. Không tự điền số 0, ngày chạy, số văn bản, chữ ký hoặc dữ liệu ví dụ.
- **File giao chỉ chứa sản phẩm nghiệp vụ:** không tự kèm checklist nghiệm thu, phụ lục kiểm tra, nhật ký AI hoặc bảng truy nguyên nguồn. Phụ lục nghiệp vụ bắt buộc theo mẫu vẫn được giữ.
- **Có kiểm soát chất lượng và thẩm quyền:** kiểm tra nguồn, cấu trúc, định dạng và khả năng mở file; người có thẩm quyền xác nhận nội dung trước khi ký, phát hành hoặc công bố.

Các thay đổi này áp dụng cho toàn bộ 171 skill. Xem [CHANGELOG](CHANGELOG.md) để đối chiếu các mốc cập nhật.

## Phạm vi nghiệp vụ

| Nhóm công việc | Sản phẩm điển hình | Skill tham khảo |
| --- | --- | --- |
| Hành chính và văn thư | Công văn, thông báo, biên bản, tờ trình, quyết định | [Soạn công văn](skills/soan-cong-van/SKILL.md), [Soạn biên bản](skills/soan-bien-ban-hop/SKILL.md) |
| Nhân sự và tổ chức | Hồ sơ tuyển dụng, hợp đồng, đánh giá viên chức | [Tuyển dụng](skills/quy-trinh-tuyen-dung/SKILL.md), [Hợp đồng làm việc](skills/hop-dong-lam-viec/SKILL.md) |
| Tuyển sinh và đào tạo | Thông báo tuyển sinh, đề cương, chương trình, lịch học | [Tuyển sinh sau đại học](skills/thong-bao-tuyen-sinh-sdh/SKILL.md), [Đề cương học phần](skills/de-cuong-chi-tiet-hoc-phan/SKILL.md) |
| Sinh viên và đảm bảo chất lượng | Hồ sơ học bổng, kết quả rèn luyện, báo cáo tự đánh giá | [Thông báo học bổng](skills/thong-bao-hoc-bong/SKILL.md), [Tự đánh giá](skills/bao-cao-tu-danh-gia/SKILL.md) |
| Tài chính, tài sản và mua sắm | Dự toán, báo cáo tài chính, kế hoạch mua sắm, kiểm kê | [Lập dự toán](skills/lap-du-toan-nam/SKILL.md), [Báo cáo tài chính](skills/bao-cao-tai-chinh/SKILL.md) |
| Nghiên cứu và hợp tác | Thuyết minh đề tài, tổng quan tài liệu, hồ sơ chuyển giao | [Thuyết minh đề tài](skills/thuyet-minh-de-tai-nckh/SKILL.md), [Tổng quan tài liệu](skills/tong-quan-tai-lieu-khoa-hoc/SKILL.md) |
| Truyền thông và điều phối | Bài viết, lịch nội dung, kịch bản, bảng theo dõi dự án | [Lịch nội dung](skills/content-calendar-truyen-thong/SKILL.md), [Quản trị dự án](skills/pmo-quan-tri-du-an/SKILL.md) |

Bộ skill gồm hai tầng: **18 skill lõi** hỗ trợ công việc dùng chung và **153 skill nghiệp vụ** gắn với chức năng phòng ban, khoa, viện, trung tâm. Đơn vị triển khai có thể điều chỉnh đầu mối theo cơ cấu thực tế của trường. Xem [danh mục theo phòng ban](skills/README.md) và [khung phòng ban](khung-phong-ban-chuan.md).

## File đầu ra và lựa chọn định dạng

### Định dạng mặc định

| Định dạng | Công dụng | Số skill |
| --- | --- | ---: |
| `.docx` | Văn bản, báo cáo dạng văn bản, hồ sơ, phiếu và tài liệu nội dung | **150** |
| `.xlsx` | Bảng tính, lịch dạng bảng, ma trận và bảng theo dõi | **20** |
| `.zip` | Đóng gói skill cùng các file nguồn và tài nguyên liên quan | **1** |

Đây là mặc định khi người dùng chưa chỉ định định dạng. Mỗi skill có danh sách lựa chọn riêng; không phải mọi skill đều xuất tất cả các định dạng dưới đây.

### Các định dạng được lựa chọn theo sản phẩm

| Nhóm | Định dạng | Khi sử dụng |
| --- | --- | --- |
| Văn bản | `.docx`, `.pdf` | Biên tập; đọc, in hoặc công bố theo yêu cầu |
| Bảng tính và dữ liệu bảng | `.xlsx`, `.csv` | Giữ sheet, công thức; trao đổi dữ liệu bảng |
| Trình chiếu | `.pptx` | Tạo bài trình chiếu khi yêu cầu cần slide thực tế |
| Nội dung thuần và nội dung web | `.txt`, `.md`, `.html` | Giao nội dung văn bản, Markdown hoặc HTML dưới dạng file |
| Dữ liệu và cấu hình | `.json`, `.yaml` | Giao dữ liệu có cấu trúc hoặc cấu hình gói skill |
| Biểu đồ | `.png`, `.svg` | Xuất biểu đồ theo yêu cầu của nhóm phân tích |
| Nguồn khoa học và trích dẫn | `.tex`, `.bib` | Giao nguồn LaTeX hoặc danh mục trích dẫn |
| Đóng gói | `.zip` | Gom bộ hồ sơ hoặc gói skill |

Các trường `default_output_format` và `available_output_formats` trong [manifest](skills-manifest.json) là nguồn đối chiếu theo từng skill. Định dạng bổ sung chỉ được tạo khi sản phẩm cần hoặc người dùng yêu cầu và có công cụ thực tế để xuất đúng định dạng.

**Quy tắc giao file:**

- File phải tồn tại, đọc được và có nội dung đúng định dạng; không đổi đuôi để giả lập kết quả.
- Nội dung trong chat dùng để trao đổi hoặc giải thích; không thay file khi nhiệm vụ yêu cầu tạo sản phẩm. Yêu cầu rõ chỉ trả nội dung trong chat vẫn được tôn trọng.
- Bộ hồ sơ gồm nhiều văn bản phải có đủ file thành phần; chỉ gom ZIP khi phù hợp.
- Chỉ xác nhận các kiểm tra đã thực hiện. Nếu không xem trước được Word/PDF hoặc không tạo được định dạng yêu cầu, thông báo giới hạn trong tin nhắn giao kết quả.
- Skill viết kịch bản video giao **kịch bản**. MP4 hoặc âm thanh cần yêu cầu sản xuất và công cụ thực sự tạo được media; HTML cũng không tự đồng nghĩa website đã được đăng.

## Cách sử dụng

1. **Chọn skill:** tìm trong [danh mục](skills/README.md), đọc phạm vi, đầu vào và định dạng của `SKILL.md`.
2. **Cung cấp nguồn:** gửi yêu cầu, dữ liệu, mẫu của trường và quy chế có liên quan. Thông tin chưa có được chừa chỗ đúng mẫu.
3. **Thực hiện và xuất file:** nạp cả thư mục skill vào nền tảng hỗ trợ, hoặc cung cấp `SKILL.md` cùng các tài liệu được liên kết. Nền tảng cần có công cụ tạo định dạng yêu cầu.
4. **Kiểm tra và trình ký:** đối chiếu nội dung với nguồn, hoàn thiện trường còn thiếu và thực hiện phê duyệt theo quy trình của đơn vị.

### Ví dụ yêu cầu

```text
Dùng skill thong-bao-tuyen-sinh-sdh để soạn thông báo
tuyển sinh sau đại học cho Trường Đại học Quốc tế.

Tổng chỉ tiêu: 03 người.
Mẫu và kế hoạch tuyển sinh: tài liệu đính kèm, nếu có.
Thông tin chưa cung cấp: giữ dấu chấm hoặc ô trống theo mẫu gốc.
Đầu ra: file Word .docx có thể tải về và chỉnh sửa.
Không kèm checklist hay phụ lục kiểm tra đầu ra.
```

Với ví dụ này, file Word phải được tạo ngay; ngành, trình độ, phân bổ chỉ tiêu, thời gian, căn cứ và người ký chưa có thì chừa chỗ. Không tự chọn ngành hoặc phân bổ tổng chỉ tiêu vào ngành chưa được xác nhận.

### Tải bộ skill

Chọn **Code → Download ZIP** trên GitHub hoặc tải bằng Git:

```bash
git clone https://github.com/phamtruong91/university-skills-framework.git
cd university-skills-framework
```

Khi cài một skill, giữ nguyên thư mục và các tài nguyên được liên kết. Repository chứa hướng dẫn và tài nguyên nghiệp vụ; việc chạy công cụ, tạo file hoặc kết nối hệ thống phụ thuộc nền tảng sử dụng.

## Quy trình thực hiện

```mermaid
flowchart LR
    A["Yêu cầu và nguồn"] --> B["Chọn skill và mẫu áp dụng"]
    B --> C["Soạn nội dung; chừa chỗ thông tin thiếu"]
    C --> D["Tạo file theo định dạng yêu cầu"]
    D --> E["Kiểm tra nội dung và file"]
    E --> F["Giao file tải được"]
    F --> G["Đơn vị hoàn thiện và phê duyệt"]
```

Việc đối chiếu và kiểm tra diễn ra trong quá trình làm. File giao chỉ chứa sản phẩm được yêu cầu. Nếu nhiệm vụ trực tiếp là kiểm tra hồ sơ hoặc thẩm định, bảng kết quả nghiệp vụ là sản phẩm chính; không thêm một checklist tự kiểm tra sản phẩm đó.

## Mẫu biểu, dữ liệu và phê duyệt

Văn bản hành chính được hướng dẫn theo Nghị định 30/2020/NĐ-CP; văn bản chuyên ngành dùng đúng mẫu, mã biểu và cấu trúc còn áp dụng. Văn bản Đảng, tài liệu khoa học, truyền thông và bảng theo dõi có quy cách riêng theo loại sản phẩm.

- Chọn căn cứ theo đối tượng, thời điểm nghiệp vụ, loại hình trường và điều khoản chuyển tiếp.
- Giữ dấu chấm, dấu gạch hoặc ô trống đúng mẫu gốc khi thiếu dữ liệu; không tự ghi mã “CHỜ KÝ”, “CHƯA CUNG CẤP” trong bản giao.
- Chức vụ, họ tên và chữ ký được xử lý theo nguồn và thẩm quyền; không tạo chữ ký, dấu hay trạng thái đã duyệt.
- Chỉ xử lý dữ liệu cá nhân trong phạm vi được phép và cần thiết cho nghiệp vụ.

**Phạm vi rà soát:** bộ skill có cập nhật căn cứ/điều kiện pháp lý cho 58 skill từ đợt trước, cùng quy cách đầu ra cho toàn bộ 171 skill. Việc kiểm tra đóng gói không chứng nhận tất cả căn cứ, ngưỡng, thời hạn hoặc mẫu chuyên ngành đều đã được xác minh toàn văn. Đơn vị phải đối chiếu quy chế, thẩm quyền và pháp luật tại thời điểm sử dụng.

Xem [quy cách đầu ra](docs/QUY_CACH_DAU_RA.md), [đối chiếu pháp lý](docs/CAP_NHAT_PHAP_LY.md) và [quản trị phiên bản](GOVERNANCE.md). Các tài liệu thiết kế và quy trình lịch sử chỉ dùng tham khảo; khi có khác biệt, ưu tiên `SKILL.md`, quy cách đầu ra và manifest hiện hành. Skill hội đồng trường có giới hạn riêng theo loại hình trường và thời điểm áp dụng.

## Cấu trúc repository

```text
university-skills-framework/
├── README.md
├── skills-manifest.json
├── skills/
│   ├── README.md
│   └── <ten-skill>/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
│           ├── quy-cach-dau-ra.md
│           ├── version.json
│           └── phap-ly.md              # ở skill có tài liệu pháp lý riêng
├── docs/
│   ├── QUY_CACH_DAU_RA.md
│   └── CAP_NHAT_PHAP_LY.md
├── scripts/validate_skills.py
├── CHANGELOG.md
├── GOVERNANCE.md
└── LICENSE
```

Một số skill có thêm `assets/` hoặc tài liệu lịch sử phục vụ nghiệp vụ. Xem [khung đóng gói](khung-skill-tong-the.md) và [sơ đồ phòng ban](so-do-case-phong-ban.html) khi tùy chỉnh bộ skill.

## Kiểm tra và đóng góp

Trước khi gửi thay đổi, đồng bộ `SKILL.md`, quy cách đầu ra, metadata giao diện, hồ sơ phiên bản và manifest; kiểm tra tình huống đủ dữ liệu, thiếu dữ liệu và dữ liệu mâu thuẫn.

```bash
python -X utf8 scripts/validate_skills.py
```

Công cụ kiểm tra số lượng skill, cấu trúc YAML, metadata, phiên bản, liên kết tài nguyên và các yêu cầu đầu ra. Việc xác nhận chất lượng nội dung, mẫu biểu và bố cục file thực tế vẫn cần thực hiện theo nghiệp vụ.

Gửi pull request với mô tả sản phẩm được hỗ trợ, hành vi thay đổi và kết quả kiểm tra. Tham khảo [skill đóng gói từ quy trình](skills/dong-goi-skill-tu-quy-trinh/SKILL.md) để xây hoặc mở rộng skill.

## Giấy phép và quản trị

Bản quyền **CES Global, 2026**. Bộ tài liệu được phân phối theo giấy phép kép được quy định trong [LICENSE](LICENSE): giấy phép cộng đồng **CC BY-SA 4.0** và điều khoản thương mại riêng.

Người duy trì: [phamtruong91](https://github.com/phamtruong91). Phiên bản **1.3.1** là phiên bản nội dung của bộ skill; xem [CHANGELOG](CHANGELOG.md) và lịch sử Git để theo dõi thay đổi. Số phiên bản này không tự đồng nghĩa đã phát hành GitHub Release.
