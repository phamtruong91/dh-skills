---
name: "phan-tich-chenh-lech-ngan-sach"
description: "Phân tích chênh lệch ngân sách bằng cách đối chiếu dự toán với thực hiện theo từng mục: tính variance, đánh dấu vượt ngưỡng, phân loại nguyên nhân, dự thảo giải trình. Dùng chung cho mọi đơn vị có ngân sách. Dùng khi cuối quý/năm hoặc cần giải trình chênh lệch giữa dự toán và thực hiện."
---

# Phân tích chênh lệch ngân sách

## Định dạng và file đầu ra

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .xlsx, .csv, .pdf, .png, .svg. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.xlsx**. Nếu yêu cầu gồm cả báo cáo thuyết minh, tạo thêm file Word cho báo cáo; không ghép báo cáo dài vào bảng tính. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Khi báo cáo có số liệu cần so sánh hoặc nêu xu hướng, đọc mục “Biểu đồ và hình trong báo cáo số liệu” trong quy cách đầu ra trước khi vẽ.

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Cuối quý/năm hoặc khi cần giải trình chênh lệch giữa dự toán được giao và thực hiện.
Dùng chung cho Phòng Tài chính – Kế toán, các phòng/khoa/trung tâm, chủ tài khoản —
không phụ thuộc tên đơn vị.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `du_toan` | Dự toán theo từng mục chi (mã mục, tên mục, số tiền) | Có |
| `thuc_hien` | Số thực hiện theo từng mục chi | Có |
| `ky_bao_cao` | Quý/năm báo cáo | Có |
| `nguong_canh_bao` | Ngưỡng chênh lệch cần giải trình, VD: ±10% | Không (mặc định: 10%) |
| `chung_tu_lien_quan` | Chứng từ/giải trình sơ bộ của đơn vị (nếu có) | Không |

## Quy trình

**Bước 1. Validate và đối chiếu mã mục**
- Làm gì: đối chiếu danh sách mã mục chi giữa `du_toan` và `thuc_hien`; kiểm tra trùng mã,
  tên mục ghi khác nhau hai bên, mục có ở một bên mà thiếu ở bên kia; kiểm tra số liệu
  âm hoặc bất thường cần xác minh lại.
- Dùng input: `du_toan`, `thuc_hien`
- Vai trò: Kế toán phụ trách · AI hỗ trợ: đối chiếu mã mục hai bên, phát hiện trùng/lệch tên/thiếu dữ liệu · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: cùng một mục nhưng ghi khác tên (VD "VPP" và "Văn phòng phẩm") là lỗi
  phổ biến — chuẩn hóa tên trước khi đối chiếu; tuyệt đối không tự bịa số liệu cho mục thiếu.
- → Kết quả bước: "bảng khớp mã mục" (danh sách mục khớp đầy đủ + danh sách mục thiếu
  dữ liệu một bên cần đơn vị bổ sung).

**Bước 2. Tính chênh lệch từng mục**
- Làm gì: với mỗi mục đã khớp ở bước 1, tính chênh lệch tuyệt đối (thực hiện − dự toán)
  và tương đối (% = tuyệt đối ÷ dự toán × 100); tính thêm dòng tổng toàn bộ.
- Dùng input: `du_toan`, `thuc_hien`
- Vai trò: Kế toán phụ trách · AI hỗ trợ: tính chênh lệch tuyệt đối, tương đối và dòng tổng từng mục · ⏱ ~10–15 phút (ước tính)
- Lưu ý nghiệp vụ: giữ nguyên số liệu gốc, không làm tròn gây sai tổng; tỷ lệ % chỉ có
  ý nghĩa khi dự toán > 0 — mục dự toán = 0 mà có thực hiện thì ghi "phát sinh mới",
  không chia cho 0.
- → Kết quả bước: "bảng variance thô" (dự toán / thực hiện / chênh lệch / tỷ lệ %
  từng mục + dòng tổng).

**Bước 3. Đánh dấu mục vượt ngưỡng**
- Làm gì: so sánh |tỷ lệ %| của từng mục với `nguong_canh_bao` (mặc định 10% khi đơn vị
  không quy định); các mục vượt ngưỡng được gắn cờ "cần giải trình"; xếp hạng các mục
  vượt theo mức độ chênh lệch để ưu tiên giải trình.
- Dùng input: `nguong_canh_bao`, `ky_bao_cao`
- Vai trò: Kế toán phụ trách · AI hỗ trợ: so tỷ lệ % với ngưỡng cảnh báo, gắn cờ và xếp hạng mục vượt ngưỡng · ⏱ ~5–10 phút (ước tính)
- Lưu ý nghiệp vụ: chênh lệch âm lớn (chi chưa tới, giải ngân chậm) cũng phải giải trình
  như chênh lệch dương; ngưỡng mặc định chỉ dùng khi đơn vị không có quy định riêng.
- → Kết quả bước: "danh sách mục vượt ngưỡng cần giải trình" (kèm mức vượt và thứ tự
  ưu tiên).

**Bước 4. Phân loại nguyên nhân**
- Làm gì: với từng mục vượt ngưỡng ở bước 3, đọc `chung_tu_lien_quan` và thông tin đơn vị
  cung cấp, phân loại nguyên nhân: khách quan (giá thị trường biến động, phát sinh nhiệm
  vụ do cấp trên giao) hay chủ quan (lập dự toán chưa sát, chi vượt kế hoạch, quản lý
  lỏng lẻo); mục không đủ căn cứ thì ghi rõ "cần đơn vị giải trình thêm".
- Dùng input: `chung_tu_lien_quan`, `du_toan`, `thuc_hien`
- Vai trò: Kế toán phụ trách · AI hỗ trợ: phân loại sơ bộ nguyên nhân khách quan/chủ quan từ chứng từ, liệt kê mục chưa rõ để xác nhận · ⏱ ~30 phút–1 giờ (ước tính)
- Lưu ý nghiệp vụ: chỉ ghi nguyên nhân có chứng từ hoặc thông tin đối chứng — không suy
  đoán, không "làm đẹp" lý do; nguyên nhân khách quan phải kèm căn cứ cụ thể (số công văn,
  quyết định giao nhiệm vụ...).
- → Kết quả bước: "bảng phân loại nguyên nhân" (mục vượt → nguyên nhân khách quan /
  chủ quan / chưa rõ + căn cứ kèm theo).

**Bước 5. Dự thảo giải trình**
- Làm gì: soạn văn bản giải trình theo cấu trúc sản phẩm tại references/quy-cach-dau-ra.md: ghép bảng variance (bước 2),
  danh sách mục vượt ngưỡng (bước 3), viết giải trình từng mục dựa trên bảng phân loại
  nguyên nhân (bước 4), thêm đề xuất điều chỉnh (bổ sung dự toán, dùng nguồn tiết kiệm...)
  nếu cần, trình bày để chủ tài khoản duyệt.
- Dùng input: kết quả các bước 2–4, `ky_bao_cao`
- Vai trò: Kế toán phụ trách · AI hỗ trợ: soạn dự thảo giải trình theo cấu trúc chuẩn để trình chủ tài khoản duyệt · ⏱ ~30–45 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi mục vượt ngưỡng phải có đủ 3 yếu tố — con số chênh lệch, nguyên nhân
  đã phân loại, đề xuất xử lý (hoặc ghi "chưa đề xuất"); dùng ngôn ngữ văn bản hành chính,
  dẫn chiếu kỳ báo cáo và chứng từ.
- → Kết quả bước: "dự thảo văn bản giải trình chênh lệch ngân sách" (sản phẩm chính,
  chuyển sang Human gate).
## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Dự toán + số liệu thực hiện"/]
    B["Bước 1. Validate và đối chiếu mã mục"]
    C["Bước 2. Tính chênh lệch từng mục"]
    D["Bước 3. Đánh dấu mục vượt ngưỡng"]
    E{"Có mục vượt ngưỡng?"}
    F["Bước 4. Phân loại nguyên nhân khách quan/chủ quan"]
    G["Bước 5. Dự thảo giải trình"]
    HG["👤 Kế toán kiểm tra số liệu; chủ tài khoản duyệt"]
    H[["Bảng phân tích + dự thảo giải trình"]]
    A --> B --> C --> D --> E
    E -->|Có| F --> G --> HG
    E -->|Không| HG
    HG --> H
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Bảng variance khớp đúng `du_toan` / `thuc_hien`: số liệu giữ nguyên không làm tròn sai tổng; mục dự toán = 0 mà có thực hiện ghi "phát sinh mới", không chia cho 0.
- [ ] Đã đánh dấu đầy đủ các mục vượt `nguong_canh_bao` (kể cả chênh lệch âm lớn — giải ngân chậm — cũng phải giải trình).
- [ ] Mỗi mục vượt ngưỡng có đủ 3 yếu tố: con số chênh lệch, nguyên nhân đã phân loại, đề xuất xử lý (hoặc ghi "chưa đề xuất").
- [ ] Nguyên nhân kèm chứng từ/căn cứ cụ thể (số công văn, quyết định giao nhiệm vụ); mục chưa rõ nguyên nhân ghi "cần đơn vị giải trình thêm" — không suy đoán, không bịa số liệu.
- [ ] Văn bản dùng ngôn ngữ hành chính, dẫn chiếu kỳ báo cáo và chứng từ; mục còn thiếu dữ liệu một bên đã được đơn vị bổ sung.
- [ ] Đã qua Human gate: kế toán kiểm tra tính đúng đắn của số liệu; chủ tài khoản duyệt trước khi gửi cấp trên.

> Tiêu chí đạt: tất cả các ô được đánh dấu.

## Human gate (người kiểm duyệt)
- **Kế toán phụ trách** kiểm tra tính đúng đắn của số liệu đối chiếu.
- **Chủ tài khoản / thủ trưởng đơn vị** duyệt bản giải trình trước khi gửi cấp trên.
- Phòng Tài chính – Kế toán (hoặc đơn vị tương đương) là đầu mối tổng hợp cuối.

## Giới hạn (guardrails)
- Không tự điều chỉnh số liệu dự toán/thực hiện; mọi con số lấy nguyên từ đầu vào.
- Không thực hiện bút toán, thanh toán hay chuyển nguồn ngân sách.
- Không suy đoán nguyên nhân vượt/chưa đạt ngoài chứng từ và thông tin được cung cấp —
  mục chưa rõ nguyên nhân phải ghi "cần đơn vị giải trình thêm".
- Không bịa số liệu để "làm đẹp" báo cáo.

## Căn cứ & lưu ý
- Theo chế độ kế toán hành chính sự nghiệp và quy chế chi tiêu nội bộ của trường.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
