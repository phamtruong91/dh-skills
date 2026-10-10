---
name: "quyet-dinh-hoc-vu"
description: "Soạn quyết định xử lý học vụ sinh viên (cảnh báo học vụ, buộc thôi học, bảo lưu kết quả học tập, chuyển trường) đúng thể thức Nghị định 30/2020/NĐ-CP. Dùng khi kết thúc học kỳ/năm học cần xử lý học vụ theo quy chế đào tạo."
---

# Soạn quyết định xử lý học vụ

## Định dạng và file đầu ra
Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Nếu có cập nhật pháp lý dưới đây, đọc [căn cứ và điều kiện áp dụng](references/phap-ly.md) trước khi làm. Quy trình dưới đây giữ nghiệp vụ từ bản gốc; mọi viện dẫn văn bản, mẫu biểu, điều khoản phải theo căn cứ đã chọn trong phap-ly.md, không theo văn bản cũ.

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Khi kết thúc mỗi học kỳ hoặc năm học, cần rà soát kết quả học tập của sinh viên và ban hành
quyết định xử lý học vụ đối với các trường hợp: cảnh báo học vụ, buộc thôi học, cho phép
bảo lưu kết quả học tập, cho phép chuyển trường — theo quy chế đào tạo của trường.

## Đầu vào (Input)
| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `loai_xu_ly` | Cảnh báo học vụ / Buộc thôi học / Bảo lưu / Chuyển trường | Có |
| `hoc_ky` | Học kỳ, năm học áp dụng (ví dụ: Học kỳ 1 năm học 2026–2027) | Có |
| `danh_sach_sv` | Danh sách SV đủ điều kiện từng diện (mã SV, họ tên, lớp, ngành, lý do) | Có |
| `can_cu_quy_che` | Điều, khoản cụ thể của quy chế đào tạo áp dụng cho từng diện | Có |
| `bien_ban_hoi_dong` | Biên bản họp hội đồng xem xét xử lý học vụ (số, ngày họp, kết luận) | Có |
| `nguoi_ky` | Hiệu trưởng / Phó Hiệu trưởng phụ trách đào tạo | Có |
| `so_quyet_dinh` | Số quyết định (nếu đã cấp số; nếu chưa, để trống để điền khi ban hành) | Không |

## Quy trình
**Ràng buộc pháp lý khi thực hiện** (trích references/phap-ly.md; đối chiếu toàn văn và hiệu lực tại ngày nghiệp vụ):
- Thông tư 56/2026/TT-BGDĐT, hiệu lực 07/07/2026: Yêu cầu khóa tuyển sinh, chương trình, ngày áp dụng và quy chế đào tạo nội bộ. Đối chiếu điều khoản chuyển tiếp trong toàn văn trước khi chọn quy tắc; không tự áp dụng quy định mới hồi tố cho mọi khóa. Không dùng điều/khoản, thang điểm hoặc điều kiện tốt nghiệp cũ như quy định hiện hành nếu chưa đối chiếu.
- Trước Bước 1: chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi nhận nội bộ [CẦN XÁC MINH] (không đưa vào file giao), để trống phần tương ứng, chưa kết luận tuân thủ.

**Bước 1. Rà soát kết quả học tập của sinh viên**
- Làm gì: trích xuất từ hệ thống quản lý đào tạo của từng SV: điểm trung bình chung học kỳ/năm học,
  số tín chỉ đã tích lũy, số tín chỉ còn nợ, tổng thời gian đã học so với thời gian đào tạo tối đa;
  đối chiếu thêm hồ sơ kỷ luật (đình chỉ học tập) nếu có.
- Dùng input: `hoc_ky`, `danh_sach_sv`
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: trích xuất và đối chiếu số liệu tự động từ hệ thống · ⏱ ~45 phút (ước tính)
- Lưu ý nghiệp vụ: số liệu phải chốt tại thời điểm kết thúc học kỳ/năm học và ghi rõ thời điểm chốt
  để hội đồng đối chiếu; loại khỏi danh sách rà soát các SV đã bảo lưu/thôi học trước đó.
- → Kết quả bước: bảng số liệu kết quả học tập chi tiết từng SV (mã SV, họ tên, lớp, ngành,
  ĐTB học kỳ, tín chỉ tích lũy/nợ, thời gian đào tạo còn lại).

**Bước 2. Đối chiếu quy chế, phân loại diện xử lý**
- Làm gì: áp từng dòng số liệu ở Bước 1 vào các điều, khoản của quy chế đào tạo; phân loại SV vào
  4 diện: cảnh báo học vụ, buộc thôi học, bảo lưu, chuyển trường; ghi rõ điều, khoản áp dụng cho
  từng trường hợp.
- Dùng input: `danh_sach_sv`, `can_cu_quy_che`, `loai_xu_ly`
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: phân loại sơ bộ theo quy chế, cảnh báo trường hợp chưa khớp · ⏱ ~1 giờ (ước tính)
- Lưu ý nghiệp vụ: cảnh báo học vụ khi ĐTB học kỳ dưới ngưỡng quy định (thường < 2.00) hoặc nợ quá
  số tín chỉ cho phép; buộc thôi học khi vượt số lần cảnh báo quy định hoặc quá thời gian đào tạo
  tối đa; bảo lưu/chuyển trường chỉ áp dụng khi có đơn của SV với lý do chính đáng và đủ điều kiện;
  không gộp SV thuộc các diện khác nhau vào cùng một quyết định.
- → Kết quả bước: danh sách SV phân loại theo từng diện xử lý, kèm điều/khoản quy chế áp dụng
  cho từng trường hợp.

**Bước 3. Hội đồng xem xét, biểu quyết từng trường hợp**
- Làm gì: Phòng Đào tạo trình danh sách đã phân loại kèm hồ sơ minh chứng (bảng điểm, đơn của SV,
  hồ sơ kỷ luật) lên hội đồng xử lý học vụ; hội đồng họp, thảo luận và biểu quyết từng trường hợp;
  thư ký lập biên bản ghi kết luận từng trường hợp.
- Dùng input: `bien_ban_hoi_dong`, `danh_sach_sv`, `loai_xu_ly`
- Vai trò: Hội đồng xử lý học vụ · AI hỗ trợ: chuẩn bị tài liệu, tổng hợp hồ sơ minh chứng trước phiên họp · ⏱ ~1 buổi (ước tính)
- Lưu ý nghiệp vụ: đây là Human gate — chỉ các trường hợp được hội đồng thông qua mới được đưa
  vào quyết định; biên bản phải ghi rõ số, ngày họp và kết luận từng trường hợp; trường hợp không
  thông qua thì trả hồ sơ, rà soát lại từ Bước 2.
- → Kết quả bước: biên bản họp hội đồng xử lý học vụ (số, ngày họp, kết luận từng trường hợp) —
  căn cứ pháp lý bắt buộc của quyết định.

**Bước 4. Soạn quyết định theo thể thức NĐ 30/2020**
- Làm gì: soạn quyết định gồm: quốc hiệu – tiêu ngữ, tên cơ quan, số/ký hiệu quyết định, địa danh –
  ngày tháng năm ban hành, tên loại + trích yếu, phần căn cứ (quy chế đào tạo, biên bản hội đồng,
  đề nghị của Trưởng phòng Đào tạo), các điều khoản (Điều 1: xử lý đối với danh sách SV kèm theo;
  Điều 2: nghĩa vụ của SV; Điều 3: trách nhiệm thi hành), danh sách SV kèm theo, nơi nhận, chữ ký
  người có thẩm quyền.
- Dùng input: `loai_xu_ly`, `hoc_ky`, `danh_sach_sv`, `can_cu_quy_che`, `bien_ban_hoi_dong`,
  `nguoi_ky`, `so_quyet_dinh`
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: soạn dự thảo đúng thể thức NĐ 30/2020, kiểm tra căn cứ · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: kiểm tra thẩm quyền ký (Hiệu trưởng hoặc Phó Hiệu trưởng được ủy quyền);
  danh sách SV trong quyết định phải khớp 100% với biên bản hội đồng; nếu chưa cấp số quyết định
  thì để trống để điền khi ban hành.
- → Kết quả bước: dự thảo quyết định xử lý học vụ đúng thể thức NĐ 30/2020, kèm danh sách SV
  theo từng diện.

**Bước 5. Thông báo và lưu hồ sơ học vụ**
- Làm gì: gửi quyết định đã ký đến từng SV, cố vấn học tập, khoa quản lý SV và các đơn vị liên quan
  (Phòng CTSV; Phòng TC-KT nếu liên quan học phí/học bổng); cập nhật trạng thái học vụ vào hồ sơ
  SV trên hệ thống; lưu hồ sơ (quyết định + biên bản + minh chứng) theo quy định lưu trữ.
- Dùng input: `danh_sach_sv`, `loai_xu_ly`
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: soạn mẫu thông báo gửi SV và đơn vị liên quan · ⏱ ~1 giờ (ước tính)
- Lưu ý nghiệp vụ: đảm bảo SV được thông báo và biết quyền khiếu nại theo quy định; quyết định
  buộc thôi học phải lưu bản chính vào hồ sơ SV; cập nhật hệ thống ngay để các đơn vị liên quan
  đồng bộ trạng thái.
- → Kết quả bước: quyết định đã được gửi đến các bên liên quan; hồ sơ học vụ SV đã cập nhật và
  lưu trữ đầy đủ.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Input: KQ học tập, quy chế, danh sách SV"/]
    A["Bước 1: Rà soát kết quả học tập của sinh viên"]
    B["Bước 2: Đối chiếu quy chế, phân loại diện xử lý"]
    HG["👤 Bước 3: Hội đồng họp, biểu quyết từng trường hợp"]
    C{"Hội đồng thông qua?"}
    D["Trả hồ sơ, rà soát lại"]
    E["Bước 4: Soạn quyết định theo thể thức NĐ 30/2020"]
    F["Bước 5: Thông báo và lưu hồ sơ học vụ"]
    OUT[/"Output: Quyết định xử lý học vụ"/]

    IN --> A --> B --> HG --> C
    C -->|Không| D
    D --> B
    C -->|Có| E --> F --> OUT
```

## Đầu ra
- Quyết định xử lý học vụ hoàn chỉnh (đúng thể thức), kèm danh sách SV theo từng diện.
- Checklist kiểm tra: căn cứ pháp lý đầy đủ, danh sách khớp biên bản hội đồng, thẩm quyền ký, nơi nhận.

**Cấu trúc output chuẩn:** khung mẫu cố định của quyết định xử lý học vụ, các phần theo đúng thứ tự:
1. Phần đầu văn bản: quốc hiệu – tiêu ngữ; tên cơ quan ban hành; số, ký hiệu quyết định;
   địa danh, ngày tháng năm ban hành.
2. Tên loại và trích yếu: "QUYẾT ĐỊNH" + "Về việc…" (ghi rõ diện xử lý và học kỳ/năm học).
3. Thẩm quyền ban hành: chức danh người ký (HIỆU TRƯỞNG / KT. HIỆU TRƯỞNG – PHÓ HIỆU TRƯỞNG).
4. Phần căn cứ: quy chế đào tạo (điều, khoản cụ thể); biên bản họp hội đồng xử lý học vụ
   (số, ngày họp); đề nghị của Trưởng phòng Đào tạo.
5. Phần quyết định: Điều 1 (xử lý đối với các SV có tên trong danh sách kèm theo, ghi rõ
   diện xử lý và căn cứ điều khoản); Điều 2 (nghĩa vụ của SV sau xử lý); Điều 3 (trách nhiệm
   thi hành).
6. Phần cuối: nơi nhận; chữ ký, họ tên người ký.
7. Phụ lục kèm theo: danh sách SV theo từng diện (STT, mã SV, họ tên, lớp, ngành, ĐTB học kỳ, lý do).

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao
Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Đủ các phần theo "Cấu trúc output chuẩn": phần đầu văn bản; tên loại + trích yếu; thẩm quyền ban hành; phần căn cứ; 3 điều khoản quyết định; nơi nhận, chữ ký; phụ lục danh sách SV theo từng diện.
- [ ] Số liệu/nội dung trong output khớp với Input đã cho (mã SV, họ tên, lớp, ngành, ĐTB học kỳ, học kỳ áp dụng).
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn.
- [ ] Đúng thể thức văn bản hành chính theo Nghị định 30/2020/NĐ-CP (quốc hiệu, số/ký hiệu, nơi nhận, chữ ký).
- [ ] Căn cứ pháp lý đầy đủ, còn hiệu lực (văn bản hiện hành nêu tại phap-ly.md, quy chế đào tạo của trường, biên bản họp hội đồng).
- [ ] Đã qua Human gate: hội đồng xử lý học vụ đã họp, biểu quyết từng trường hợp; người có thẩm quyền (Hiệu trưởng/Phó Hiệu trưởng) đã ký duyệt.
- [ ] Không gộp SV thuộc các diện xử lý khác nhau vào cùng một quyết định; mỗi trường hợp ghi rõ điều/khoản quy chế áp dụng.
- [ ] Danh sách SV trong quyết định khớp 100% với biên bản họp hội đồng; SV đã bảo lưu/thôi học trước đó đã loại khỏi danh sách rà soát.
- [ ] SV đã được thông báo quyết định và biết quyền khiếu nại; quyết định buộc thôi học đã lưu bản chính vào hồ sơ SV.

## Căn cứ & lưu ý
- Căn cứ hiện hành: xem [căn cứ và điều kiện áp dụng](references/phap-ly.md); phải đối chiếu văn bản gốc, hiệu lực và chuyển tiếp tại ngày nghiệp vụ.
- Nghị định 30/2020/NĐ-CP về công tác văn thư (thể thức quyết định).
- Quyết định xử lý học vụ ảnh hưởng trực tiếp đến quyền lợi SV: phải có biên bản hội đồng,
  đảm bảo SV được thông báo và có quyền khiếu nại theo quy định.
- Khi mô phỏng không dùng tên thật của trường/cá nhân.

## Tư liệu đối chiếu
Bản gốc trước cập nhật pháp lý (kèm ví dụ giả lập) lưu tại `references/quy-trinh-lich-su.md`, chỉ để đối chiếu hồ sơ lịch sử; không dùng căn cứ, mẫu hay số liệu trong đó làm chỉ dẫn hiện hành.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
