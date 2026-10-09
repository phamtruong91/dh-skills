---
name: "quyet-dinh-cu-di-hoc"
description: "Soạn quyết định cử cán bộ, viên chức, giảng viên đi đào tạo, bồi dưỡng, tập huấn trong và ngoài nước. Dùng khi phòng Tổ chức – Cán bộ cử người đi học theo kế hoạch hoặc theo nhu cầu đột xuất, làm căn cứ chế độ, kinh phí."
---

# Quyết định cử cán bộ đi đào tạo / tập huấn

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




## Khi nào dùng
Khi cần cử cán bộ, viên chức, giảng viên đi học: đào tạo sau đại học, bồi dưỡng nghiệp vụ,
tập huấn chuyên môn, hội thảo khoa học trong và ngoài nước; làm căn cứ hưởng chế độ,
thanh toán kinh phí và quản lý thời gian công tác.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ho_ten` | Họ tên cán bộ được cử | Có |
| `chuc_vu` | Chức vụ, chức danh nghề nghiệp | Có |
| `don_vi` | Đơn vị công tác | Có |
| `khoa_hoc` | Tên khóa đào tạo / tập huấn / hội thảo | Có |
| `don_vi_to_chuc` | Cơ sở đào tạo / đơn vị tổ chức khóa học | Có |
| `thoi_gian` | Từ ngày ... đến ngày ... | Có |
| `dia_diem` | Nơi tổ chức | Có |
| `kinh_phi` | Kinh phí và nguồn chi trả (ngân sách / nguồn thu / tự túc một phần...) | Có |
| `can_cu` | Kế hoạch bồi dưỡng năm / công văn triệu tập / đề nghị của đơn vị | Có |
| `nguoi_ky` | Hiệu trưởng / Phó Hiệu trưởng | Có |

## Quy trình

**Bước 1. Kiểm tra điều kiện cử đi học**
- Làm gì: đối chiếu đề nghị cử đi học với kế hoạch bồi dưỡng năm của trường; xác nhận
đối tượng thuộc diện được cử (thuộc kế hoạch năm hoặc nhu cầu đột xuất có tờ trình hợp lệ);
kiểm tra thời gian đi học không trùng lịch giảng dạy/quản lý đã phân công, đã bố trí người
dạy thay hoặc người thay thế nhiệm vụ nếu cần.
- Dùng input: `ho_ten`, `chuc_vu`, `don_vi`, `thoi_gian`, `can_cu`.
- Vai trò: Chuyên viên Phòng TCCB (Trưởng phòng kiểm tra lại) · AI hỗ trợ: quét lỗi theo checklist · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: cử đi học trong thời gian giảng dạy mà không bố trí dạy thay là bẫy
thường gặp — phải có xác nhận của đơn vị quản lý cán bộ; trường hợp đột xuất ngoài kế
hoạch năm cần tờ trình nêu rõ lý do và được Ban Giám hiệu đồng ý trước.
- → Kết quả bước: phiếu kiểm tra điều kiện (đạt/không đạt từng tiêu chí + phương án
bố trí thay thế).

**Bước 2. Xác minh căn cứ cử đi học**
- Làm gì: thu thập và đối chiếu từng văn bản nêu trong `can_cu`: kế hoạch bồi dưỡng năm
đã phê duyệt (số, ngày ban hành, trích phần liên quan), công văn triệu tập của đơn vị
tổ chức (số, ngày, đối tượng triệu tập), tờ trình đề nghị của đơn vị quản lý cán bộ;
kiểm tra tên khóa học, đơn vị tổ chức, thời gian, địa điểm trong các văn bản có khớp
nhau không.
- Dùng input: `can_cu`, `khoa_hoc`, `don_vi_to_chuc`, `thoi_gian`, `dia_diem`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: đối chiếu chéo tự động · ⏱ ~20–30 phút (ước tính)
- Lưu ý nghiệp vụ: tên khóa học trên công văn triệu tập và trên tờ trình thường lệch nhau
vài chữ — phải thống nhất một tên chính thức để dùng trong quyết định; kiểm tra thời hạn
đăng ký/nộp hồ sơ của đơn vị tổ chức để quyết định được ký kịp thời.
- → Kết quả bước: bảng đối chiếu căn cứ (căn cứ | số, ngày văn bản | nội dung liên quan |
khớp/không khớp).

**Bước 3. Lập bảng đối chiếu thông tin cá nhân và chế độ**
- Làm gì: đối chiếu `ho_ten`, `chuc_vu`, `don_vi` với hồ sơ cán bộ (đúng chính tả họ tên,
đúng chức danh và đơn vị hiện tại); phân tích `kinh_phi`: tách các khoản (học phí, công tác
phí, lưu trú), xác định nguồn chi (ngân sách / nguồn thu / tự túc một phần) và kiểm tra
nguồn chi có được phép dùng cho mục đích này không.
- Dùng input: `ho_ten`, `chuc_vu`, `don_vi`, `kinh_phi`.
- Vai trò: Chuyên viên Phòng TCCB (Trưởng phòng kiểm tra lại) · AI hỗ trợ: lập bảng tính toán · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: chức danh trong quyết định phải là chức danh hiện tại (kiểm tra quyết
định bổ nhiệm gần nhất); kinh phí trong quyết định ghi cả số tiền bằng số và bằng chữ;
nếu tự túc một phần phải ghi rõ phần nào tự túc để tránh tranh chấp khi thanh toán.
- → Kết quả bước: bảng đối chiếu thông tin cá nhân và kinh phí đã xác minh.

**Bước 4. Soạn khung quyết định theo thể thức NĐ 30/2020**
- Làm gì: soạn phần mở đầu văn bản: Quốc hiệu – Tiêu ngữ, tên cơ quan ban hành, số và ký
hiệu văn bản, địa danh và ngày tháng năm; tên loại văn bản "QUYẾT ĐỊNH" kèm trích yếu;
chức danh người ký; phần căn cứ (mỗi căn cứ một dòng bắt đầu bằng "Căn cứ", sắp xếp từ
căn cứ thành lập trường → quy chế trường → kế hoạch bồi dưỡng năm → công văn triệu tập →
đề nghị của P. TCCB).
- Dùng input: `can_cu`, `nguoi_ky`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: số, ký hiệu lấy từ sổ đăng ký văn bản đi của Văn phòng (không tự đặt số
trùng); trích yếu ngắn gọn nêu đúng nội dung "Về việc cử cán bộ đi bồi dưỡng, tập huấn";
thẩm quyền ký: Hiệu trưởng hoặc Phó Hiệu trưởng được ủy quyền bằng văn bản.
- → Kết quả bước: khung quyết định (phần mở đầu + căn cứ) đúng thể thức.

**Bước 5. Soạn nội dung các Điều**
- Làm gì: viết các điều sau cụm "QUYẾT ĐỊNH:": Điều 1 — cử ông/bà nào (họ tên, chức vụ,
đơn vị) đi học khóa nào, đơn vị tổ chức nào, thời gian nào, địa điểm nào; Điều 2 — chế độ
được hưởng và kinh phí (số tiền bằng số + bằng chữ, nguồn chi); Điều 3 — các đơn vị, cá nhân
chịu trách nhiệm thi hành (P. TCCB, P. Tài chính – Kế toán, đơn vị quản lý, cá nhân được cử).
- Dùng input: `ho_ten`, `chuc_vu`, `don_vi`, `khoa_hoc`, `don_vi_to_chuc`, `thoi_gian`, `dia_diem`, `kinh_phi`.
- Vai trò: Chuyên viên Phòng TCCB · AI hỗ trợ: soạn dự thảo đúng thể thức · ⏱ ~20–45 phút (ước tính)
- Lưu ý nghiệp vụ: Điều 1 phải đầy đủ 5 yếu tố (ai – học gì – ai tổ chức – khi nào – ở đâu);
Điều 2 ghi nguồn chi cụ thể để P. Tài chính – Kế toán có căn cứ thanh toán; Điều 3 liệt kê
đủ đầu mối để không sót khâu theo dõi (đặc biệt là đơn vị quản lý trực tiếp của cán bộ).
- → Kết quả bước: dự thảo quyết định đầy đủ các Điều.

**Bước 6. Kiểm tra, soát lỗi và xuất bản**
- Làm gì: soát toàn văn: chính tả họ tên/chức vụ/đơn vị, thời gian – địa điểm – kinh phí
khớp với căn cứ đã xác minh ở Bước 2–3; kiểm tra thẩm quyền ký của `nguoi_ky`; hoàn thiện
mục Nơi nhận (các đơn vị/cá nhân ở Điều 3 + lưu VT, TCCB); lập danh sách giấy tờ kèm theo
cần chuẩn bị (công văn triệu tập, tờ trình đơn vị, trích lục kế hoạch bồi dưỡng).
- Dùng input: toàn bộ input (tổng soát), `nguoi_ky`.
- Vai trò: Chuyên viên Phòng TCCB (Trưởng phòng kiểm tra lại) · AI hỗ trợ: quét lỗi theo checklist · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: lỗi phổ biến nhất là họ tên/chức danh sai một chữ so với hồ sơ cán bộ —
quyết định sai tên không có giá trị làm căn cứ thanh toán; Nơi nhận phải có "Lưu: VT, TCCB"
để lưu hồ sơ cán bộ.
- → Kết quả bước: quyết định cử đi học hoàn chỉnh + danh sách giấy tờ kèm theo, sẵn sàng trình ký.

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    IN[/"Đề nghị cử đi học"/] --> A["Bước 1. Kiểm tra điều kiện cử đi học"]
    A --> B["Bước 2. Xác minh căn cứ cử đi học"]
    B --> C["Bước 3. Lập bảng đối chiếu thông tin cá nhân và chế độ"]
    C --> D["Bước 4. Soạn khung quyết định theo thể thức NĐ 30/2020"]
    D --> E["Bước 5. Soạn nội dung các Điều"]
    E --> F["Bước 6. Kiểm tra, soát lỗi và xuất bản"]
    F --> HG["👤 Hiệu trưởng ký quyết định"]
    HG --> OUT[["Quyết định cử đi học"]]
```

## Đầu ra (Output)
- Quyết định cử cán bộ đi đào tạo / tập huấn hoàn chỉnh.
- Ghi chú các giấy tờ kèm theo cần chuẩn bị (công văn triệu tập, tờ trình đơn vị...).

**Cấu trúc output chuẩn:** (Quyết định cử cán bộ đi đào tạo / tập huấn — theo thể thức NĐ 30/2020)
1. Quốc hiệu – Tiêu ngữ ("CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" / "Độc lập – Tự do – Hạnh phúc").
2. Tên cơ quan ban hành (Trường Đại học A).
3. Số, ký hiệu văn bản.
4. Địa danh, ngày tháng năm ban hành.
5. Tên loại văn bản "QUYẾT ĐỊNH" + trích yếu ("Về việc cử cán bộ đi bồi dưỡng, tập huấn").
6. Chức danh người ký (HIỆU TRƯỞNG TRƯỜNG ĐẠI HỌC A).
7. Phần căn cứ: mỗi căn cứ một dòng bắt đầu bằng "Căn cứ" (thành lập trường → quy chế
trường → kế hoạch bồi dưỡng năm → công văn triệu tập → xét đề nghị của P. TCCB).
8. Cụm "QUYẾT ĐỊNH:" và các Điều: Điều 1 (cử ai — họ tên, chức vụ, đơn vị — đi học khóa gì,
đơn vị tổ chức nào, thời gian nào, địa điểm nào); Điều 2 (chế độ được hưởng; kinh phí: số
tiền bằng số + bằng chữ, nguồn chi); Điều 3 (trách nhiệm thi hành của P. TCCB, P. Tài chính –
Kế toán, đơn vị quản lý, cá nhân được cử).
9. Nơi nhận (như Điều 3; lưu VT, TCCB).
10. Chữ ký (chức danh người ký + họ tên).

## Checklist nghiệm thu

Tiêu chí đạt: tất cả các ô dưới đây được đánh dấu.

- [ ] Đủ các phần theo Cấu trúc output chuẩn: Quốc hiệu – Tiêu ngữ ("CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" / "Độc l…; Tên cơ quan ban hành (Trường Đại học A).; Số, ký hiệu văn bản.; Địa danh, ngày tháng năm ban hành.; … (đủ 10 phần)
- [ ] Nội dung và số liệu trong output khớp đúng với Input đã cho (không thêm, bớt hay suy diễn)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức và định dạng theo Nghị định 30/2020/NĐ-CP về công tác văn thư (thể thức văn bản).
- [ ] Căn cứ pháp lý được trích dẫn đầy đủ và còn hiệu lực
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/duyệt trước khi phát hành
- [ ] Chức danh trong quyết định phải là chức danh hiện tại (kiểm tra quyết
- [ ] Điều 1 phải đầy đủ 5 yếu tố (ai – học gì – ai tổ chức – khi nào – ở đâu);

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**, không liên quan tổ chức/cá nhân có thật.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `ho_ten` | Đỗ Thị A |
| `chuc_vu` | Giảng viên |
| `don_vi` | Khoa Công nghệ thông tin |
| `khoa_hoc` | Khóa bồi dưỡng "Ứng dụng trí tuệ nhân tạo trong giảng dạy đại học" |
| `don_vi_to_chuc` | Học viện Công nghệ Bưu chính Viễn thông |
| `thoi_gian` | Từ ngày 20/10/2026 đến ngày 25/10/2026 |
| `dia_diem` | thành phố C |
| `kinh_phi` | 8.500.000 đồng từ nguồn thu sự nghiệp (học phí, công tác phí, lưu trú theo quy định) |
| `can_cu` | Kế hoạch bồi dưỡng năm 2026 (QĐ 95/QĐ-ĐHA-TCCB); Công văn triệu tập số 210/CV-HV ngày 01/10/2026 |
| `nguoi_ky` | Hiệu trưởng |

### Output mẫu

```
TRƯỜNG ĐẠI HỌC A            CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
                                             Độc lập – Tự do – Hạnh phúc
      Số: 156/QĐ-ĐHA-TCCB
                                                 Thành phố C, ngày 09 tháng 10 năm 2026

                            QUYẾT ĐỊNH
            Về việc cử cán bộ đi bồi dưỡng, tập huấn

                                    HIỆU TRƯỞNG
                          TRƯỜNG ĐẠI HỌC A

Căn cứ Quyết định số 12/QĐ-BGDĐT ngày 05/01/2020 của Bộ trưởng Bộ Giáo dục và Đào tạo
về việc thành lập Trường Đại học A;
Căn cứ Quy chế tổ chức và hoạt động của Trường Đại học A;
Căn cứ Kế hoạch đào tạo, bồi dưỡng cán bộ, viên chức năm 2026 ban hành kèm theo
Quyết định số 95/QĐ-ĐHA-TCCB ngày 09/10/2026 của Hiệu trưởng;
Căn cứ Công văn số 210/CV-HV ngày 01/10/2026 của Học viện Công nghệ Bưu chính
Viễn thông về việc triệu tập bồi dưỡng;
Xét đề nghị của Trưởng phòng Tổ chức – Cán bộ,

                                 QUYẾT ĐỊNH:

Điều 1. Cử bà Đỗ Thị A, Giảng viên Khoa Công nghệ thông tin, đi bồi dưỡng
khóa học "Ứng dụng trí tuệ nhân tạo trong giảng dạy đại học" do Học viện Công nghệ
Bưu chính Viễn thông tổ chức, từ ngày 20/10/2026 đến ngày 25/10/2026, tại thành phố C.

Điều 2. Bà Đỗ Thị A được hưởng chế độ theo quy định hiện hành. Kinh phí:
8.500.000 đồng (Tám triệu năm trăm nghìn đồng) chi từ nguồn thu sự nghiệp của
Nhà trường (học phí, công tác phí, tiền lưu trú).

Điều 3. Trưởng phòng Tổ chức – Cán bộ, Trưởng phòng Tài chính – Kế toán, Trưởng khoa
Công nghệ thông tin và bà Đỗ Thị A chịu trách nhiệm thi hành Quyết định này./.

Nơi nhận:                                                      HIỆU TRƯỞNG
- Như Điều 3;
- Lưu: VT, TCCB.                                                   [CHỜ KÝ]

                                                              TS. Trần Văn D
```

### Giấy tờ kèm theo cần chuẩn bị
- [ ] Công văn triệu tập của đơn vị tổ chức (bản sao)
- [ ] Tờ trình/đề nghị của đơn vị quản lý cán bộ
- [ ] Kế hoạch bồi dưỡng năm đã phê duyệt (trích lục phần liên quan)

## Căn cứ & lưu ý
- Nghị định 30/2020/NĐ-CP về công tác văn thư (thể thức văn bản).
- Luật Viên chức và các quy định về đào tạo, bồi dưỡng viên chức.
- Kiểm tra thời gian đi học không trùng lịch giảng dạy đã phân công; bố trí dạy thay nếu cần.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/quyet-dinh-cu-di-hoc`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
