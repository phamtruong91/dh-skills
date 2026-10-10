---
name: "ho-so-de-nghi-khen-thuong"
description: "Soạn bộ hồ sơ đề nghị khen thưởng các cấp (tờ trình, báo cáo thành tích cá nhân/tập thể, danh sách trích ngang). Dùng khi phòng Tổ chức – Cán bộ tổng hợp, hoàn thiện hồ sơ đề nghị khen thưởng gửi Hội đồng thi đua – khen thưởng các cấp."
---

# Hồ sơ đề nghị khen thưởng các cấp

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .docx, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.docx**. Nếu có bảng số liệu nghiệp vụ yêu cầu file bảng tính riêng, tạo thêm Excel theo yêu cầu; không tự tạo file kiểm tra. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu

Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm văn bản hoặc sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hoặc dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Các trường “bắt buộc” là điều kiện hoàn thiện hồ sơ, không ngăn việc soạn bản có chỗ chừa để điền. Mọi chỉ dẫn “để trống” trong skill được hiểu là không điền dữ liệu và giữ cách chừa chỗ của mẫu gốc, không phải xóa dấu chấm của mẫu.


## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu nội bộ hồ sơ có yếu tố pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp; không tự đính kèm bảng kiểm tra vào file giao.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Văn bản soạn chưa được coi là đã ban hành; không tự chèn nhãn trạng thái kiểm duyệt vào file giao; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.

## Khi nào dùng
Khi cần đề nghị khen thưởng cho cá nhân hoặc tập thể: Huân chương, Bằng khen của Thủ tướng,
Bằng khen Bộ/Giáo dục, Chiến sĩ thi đua, Giấy khen của Hiệu trưởng...; chuẩn bị tờ trình,
báo cáo thành tích và danh sách trích ngang gửi Hội đồng thi đua – khen thưởng cấp trên.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `doi_tuong` | Cá nhân / Tập thể | Có |
| `ho_ten_tap_the` | Họ tên cá nhân hoặc tên tập thể đề nghị | Có |
| `chuc_vu_don_vi` | Chức vụ, đơn vị công tác (cá nhân) / đơn vị chủ quản (tập thể) | Có |
| `hinh_thuc_khen` | Huân chương / Bằng khen Thủ tướng / Bằng khen Bộ / CSTĐ / Giấy khen... | Có |
| `cap_trinh` | Cấp trình (Hiệu trưởng / Bộ GD&ĐT / Thủ tướng Chính phủ...) | Có |
| `thanh_tich` | Tóm tắt thành tích nổi bật theo năm, có số liệu minh chứng | Có |
| `thoi_gian_xet` | Giai đoạn xét thành tích (vd: 2021–2026) | Có |
| `can_cu` | Quy định, tiêu chuẩn của hình thức khen thưởng tương ứng | Có |
| `nguoi_ky` | Hiệu trưởng / Chủ tịch Hội đồng TĐKT trường | Có |

## Quy trình

**Bước 1. Xác định hình thức và cấp khen thưởng phù hợp**
- Làm gì: căn cứ `thanh_tich` và `hinh_thuc_khen` đề xuất, đối chiếu với tiêu chuẩn của từng
hình thức trong Luật Thi đua, khen thưởng và văn bản hướng dẫn (Huân chương, Bằng khen Thủ
tướng, Bằng khen Bộ, Chiến sĩ thi đua, Giấy khen...); xác định `cap_trinh` có thẩm quyền
xét tặng; kiểm tra đối tượng chưa từng được tặng cùng hình thức cho cùng thành tích.
- Dùng input: `doi_tuong`, `hinh_thuc_khen`, `cap_trinh`, `thanh_tich`, `can_cu`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: phân tích input, xác định yêu cầu · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: bẫy thường gặp là đề nghị hình thức khen cao hơn tiêu chuẩn thành tích
thực tế (hồ sơ bị trả) hoặc đề nghị trùng hình thức đã được tặng cho cùng giai đoạn thành
tích; hình thức khen phải tương xứng và có tính kế thừa (không nhảy cóc từ Giấy khen lên
Huân chương).
- → Kết quả bước: phiếu xác định hình thức khen (hình thức đề nghị | tiêu chuẩn yêu cầu |
thành tích đối chiếu | kết luận phù hợp/không phù hợp).

**Bước 2. Thu thập, xác minh thành tích và minh chứng**
- Làm gì: thu thập chi tiết từng nội dung trong `thanh_tich` theo `thoi_gian_xet`: quá trình
công tác, thành tích từng năm (đề tài, bài báo, giải thưởng, sáng kiến, kết quả đánh giá
viên chức...), kèm minh chứng cho từng nội dung (quyết định nghiệm thu, bản sao bài báo,
quyết định công nhận danh hiệu...); kiểm tra giai đoạn xét liên tục, không trùng lặp thành
tích đã được khen ở cùng hình thức.
- Dùng input: `thanh_tich`, `thoi_gian_xet`, `ho_ten_tap_the`, `chuc_vu_don_vi`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: xử lý sơ bộ theo quy trình · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: mọi con số trong báo cáo thành tích (số đề tài, số bài báo, số NCS)
đều phải có minh chứng đối chiếu được; thành tích tập thể và cá nhân phải tách bạch
(không lấy thành tích tập thể ghi cho cá nhân); kiểm tra kết quả đánh giá viên chức các
năm trong giai đoạn xét (thường yêu cầu hoàn thành tốt nhiệm vụ trở lên).
- → Kết quả bước: bảng tổng hợp thành tích đã xác minh (năm | nội dung thành tích |
minh chứng kèm theo).

**Bước 3. Lập bảng đối chiếu tiêu chuẩn – thành tích**
- Làm gì: liệt kê từng tiêu chuẩn của hình thức khen đã xác định ở Bước 1, đối chiếu với
thành tích đã xác minh ở Bước 2, đánh dấu từng tiêu chí: Đạt / Chưa đạt / Cần làm rõ;
ghi rõ căn cứ pháp lý của từng tiêu chuẩn (`can_cu`).
- Dùng input: `hinh_thuc_khen`, `can_cu` + kết quả Bước 1–2.
- Vai trò: Chuyên viên Phòng TCCB (Trưởng phòng kiểm tra lại) · AI hỗ trợ: lập bảng tính toán · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: đây là bước quyết định hồ sơ có đủ điều kiện trình hay không — nếu có
tiêu chí chưa đạt phải dừng lại và báo lại đơn vị, không cố soạn hồ sơ; tiêu chí "cần làm
rõ" phải được xử lý dứt điểm trước khi sang bước soạn thảo.
- → Kết quả bước: bảng đối chiếu tiêu chuẩn – thành tích (tiêu chuẩn | yêu cầu |
thực tế | kết quả) + kết luận đủ/không đủ điều kiện trình.

**Bước 4. Soạn tờ trình đề nghị khen thưởng**
- Làm gì: soạn tờ trình theo thể thức NĐ 30/2020: Quốc hiệu – Tiêu ngữ, tên trường, số/ký
hiệu, địa danh ngày tháng, tên loại "TỜ TRÌNH" + trích yếu (Về việc đề nghị tặng...);
Kính gửi `cap_trinh`; phần căn cứ (Luật Thi đua, khen thưởng; quy định của cấp trình;
kết quả bình xét của Hội đồng TĐKT trường — số, ngày họp); nội dung đề nghị (tặng hình
thức gì cho ai — họ tên/tên tập thể, chức vụ, đơn vị — kèm tóm tắt thành tích); nêu rõ
có danh sách trích ngang và báo cáo thành tích kèm theo; câu kết trình cấp có thẩm quyền
xem xét, quyết định; Nơi nhận; `nguoi_ky` ký.
- Dùng input: `doi_tuong`, `ho_ten_tap_the`, `chuc_vu_don_vi`, `hinh_thuc_khen`, `cap_trinh`, `thanh_tich`, `nguoi_ky`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: trích yếu phải nêu đúng hình thức khen đề nghị; phần căn cứ bắt buộc có
kết quả bình xét của Hội đồng TĐKT trường (ngày họp, tỷ lệ bỏ phiếu) — thiếu căn cứ này
hồ sơ không hợp lệ; số lượng đề nghị trong tờ trình phải khớp tuyệt đối với danh sách
trích ngang.
- → Kết quả bước: dự thảo tờ trình đề nghị khen thưởng hoàn chỉnh.

**Bước 5. Soạn báo cáo thành tích cá nhân/tập thể**
- Làm gì: soạn báo cáo thành tích theo mẫu chuẩn: Quốc hiệu – Tiêu ngữ; tên báo cáo + hình
thức khen đề nghị; I. Sơ lược lý lịch (họ tên, chức vụ, đơn vị, trình độ — hoặc thông tin
tập thể); II. Thành tích đạt được trong `thoi_gian_xet` (trình bày theo năm hoặc theo nhóm
nội dung, nêu bật, có số liệu từ Bước 2); III. Các danh hiệu, hình thức khen thưởng đã được
tặng; lời cam đoan tính chính xác + chữ ký người báo cáo; phần xác nhận của thủ trưởng
đơn vị.
- Dùng input: `doi_tuong`, `ho_ten_tap_the`, `chuc_vu_don_vi`, `thanh_tich`, `thoi_gian_xet`, `hinh_thuc_khen`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: thành tích trình bày theo thứ tự ưu tiên (nổi bật nhất trước), số liệu
khớp với bảng tổng hợp ở Bước 2; mục III phải kê khai trung thực các khen thưởng đã nhận
(cơ quan xét đối chiếu để tránh khen trùng); báo cáo cá nhân do chính cá nhân ký và cam đoan.
- → Kết quả bước: dự thảo báo cáo thành tích hoàn chỉnh.

**Bước 6. Lập danh sách trích ngang**
- Làm gì: lập bảng trích ngang kèm tờ trình với các cột: TT, họ tên (hoặc tên tập thể),
chức vụ/đơn vị, tóm tắt thành tích (ngắn gọn, nêu số liệu chính), hình thức đề nghị;
kiểm tra số thứ tự, họ tên, hình thức đề nghị khớp với tờ trình (Bước 4) và báo cáo thành
tích (Bước 5).
- Dùng input: `ho_ten_tap_the`, `chuc_vu_don_vi`, `thanh_tich`, `hinh_thuc_khen`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: lập bảng tính toán · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: trích ngang là tài liệu cấp trên đọc đầu tiên — tóm tắt thành tích
không quá 2 dòng nhưng phải nêu được điểm nổi bật nhất; nếu nhiều đối tượng, sắp xếp theo
thứ tự ưu tiên đề nghị.
- → Kết quả bước: danh sách trích ngang đề nghị khen thưởng.

**Bước 7. Kiểm tra và xuất bản**
- Làm gì: soát toàn bộ hồ sơ: tiêu chuẩn hình thức khen khớp thành tích (kết quả Bước 3),
thời gian xét liên tục, minh chứng đầy đủ; họ tên/chức vụ/đơn vị thống nhất giữa tờ trình,
báo cáo thành tích và trích ngang; thẩm quyền trình đúng `cap_trinh`; thể thức văn bản
đúng NĐ 30/2020; `nguoi_ky` đúng thẩm quyền.
- Dùng input: toàn bộ input (tổng soát), `nguoi_ky`.
- Vai trò: Chuyên viên Phòng TCCB (Trưởng phòng kiểm tra lại) · AI hỗ trợ: quét lỗi theo checklist · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: lỗi phổ biến nhất là không thống nhất họ tên/chức danh giữa 3 tài liệu
(viết tắt ở trích ngang, viết đầy đủ ở tờ trình); kiểm tra lần cuối số lượng đối tượng
trong tờ trình = số dòng trong trích ngang = số báo cáo thành tích đính kèm.
- → Kết quả bước: bộ hồ sơ đề nghị khen thưởng hoàn chỉnh (tờ trình + báo cáo thành tích
+ danh sách trích ngang), sẵn sàng trình ký.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Thành tích cá nhân, tập thể"/] --> A["Bước 1. Xác định hình thức và cấp khen thưởng phù hợp"]
    A --> B["Bước 2. Thu thập, xác minh thành tích và minh chứng"]
    B --> C["Bước 3. Lập bảng đối chiếu tiêu chuẩn – thành tích"]
    C --> D["Bước 4. Soạn tờ trình đề nghị khen thưởng"]
    D --> E["Bước 5. Soạn báo cáo thành tích cá nhân, tập thể"]
    E --> F["Bước 6. Lập danh sách trích ngang"]
    F --> G["Bước 7. Kiểm tra và xuất bản"]
    G --> HG["👤 Hội đồng thi đua khen thưởng bỏ phiếu"]
    HG --> OUT[["Hồ sơ đề nghị khen thưởng hoàn chỉnh"]]
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Nội dung và số liệu trong output khớp đúng với Input đã cho (không thêm, bớt hay suy diễn)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức và định dạng theo Luật Thi đua, khen thưởng và các văn bản hướng dẫn thi hành.
- [ ] Căn cứ pháp lý được trích dẫn đầy đủ và còn hiệu lực
- [ ] Không coi bản soạn là đã ký/đã duyệt; việc phê duyệt thuộc người có thẩm quyền trước phát hành
- [ ] Trích yếu phải nêu đúng hình thức khen đề nghị

## Căn cứ & lưu ý
- Luật Thi đua, khen thưởng và các văn bản hướng dẫn thi hành.
- Quyết định 37/2018/QĐ-TTg về xét công nhận GS/PGS (tham chiếu khi thành tích liên quan
học hàm, học vị trong báo cáo thành tích).
- Nghị định 30/2020/NĐ-CP về công tác văn thư (thể thức văn bản).
- Thành tích phải có minh chứng, giai đoạn xét liên tục, không trùng lặp với thành tích
đã được khen thưởng ở cùng hình thức.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.3.1`; ngày cập nhật: `2026-10-10`.
- Kho nguồn: https://github.com/phamtruong91/university-skills-framework
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `346719e6b0318ed034b4b016703f79733aa575e7`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/ho-so-de-nghi-khen-thuong`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
