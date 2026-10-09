---
name: "campaign-brief-tuyen-sinh"
description: "Soạn brief chiến dịch tuyển sinh: mục tiêu, đối tượng, thông điệp, kênh, ngân sách, KPI, timeline. Dùng trước mỗi đợt chiến dịch để thống nhất toàn nhóm và trình duyệt."
---

# Campaign brief tuyển sinh

## Kiểm soát áp dụng và phê duyệt

Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay dữ liệu bắt buộc. Hồ sơ có yếu tố pháp lý phải kèm văn bản gốc, tình trạng hiệu lực, điều khoản áp dụng và chuyển tiếp.

## Giới hạn và human gate

AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Mọi đầu ra mặc định là **DỰ THẢO – CHỜ KIỂM DUYỆT**; không đánh dấu đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước xử lý/chia sẻ dữ liệu cá nhân.




## Khi nào dùng
Trước mỗi đợt chiến dịch tuyển sinh (mở đợt, cao điểm, xét tuyển bổ sung...), khi cần một bản
brief thống nhất để cả nhóm triển khai và trình lãnh đạo phê duyệt.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_chien_dich` | Tên chiến dịch/đợt | Có |
| `thoi_gian` | Thời gian chạy chiến dịch | Có |
| `muc_tieu` | Mục tiêu cụ thể, đo được (lead, hồ sơ, nhập học) | Có |
| `doi_tuong` | Chân dung đối tượng (học sinh lớp 12 khu vực nào, phụ huynh...) | Có |
| `thong_diep` | Thông điệp chính + thông điệp phụ | Có |
| `kenh` | Kênh triển khai (paid + owned + earned) | Có |
| `ngan_sach` | Ngân sách dự kiến theo kênh | Có |
| `kpi` | KPI theo kênh và tổng | Có |

## Quy trình

**Bước 1. Xác định mục tiêu SMART và chốt chỉ tiêu**
- Làm gì: chuyển `muc_tieu` thành mục tiêu SMART (cụ thể, đo được, khả thi, liên quan, có thời hạn), gắn với chỉ tiêu tuyển sinh của đợt; chốt con số cuối (VD: 3.000 hồ sơ đợt 1) và mốc thời gian đo.
- Dùng input: `muc_tieu`, `thoi_gian`.
- Vai trò: Trưởng phòng Truyền thông – Tuyển sinh · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: mục tiêu phải bám chỉ tiêu tuyển sinh đã được duyệt; tránh mục tiêu mơ hồ kiểu "tăng nhận biết" mà không đo được.
- → Kết quả bước: Mục tiêu SMART đã chốt (con số + thời hạn đo).

**Bước 2. Vẽ chân dung đối tượng**
- Làm gì: từ `doi_tuong`, mô tả chi tiết từng nhóm: học sinh lớp 12 ở khu vực nào, dùng kênh nào hằng ngày, quan tâm điều gì khi chọn trường; phụ huynh: mối bận tâm (học phí, đầu ra, xa nhà).
- Dùng input: `doi_tuong`.
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~30–90 phút (ước tính)
- Lưu ý nghiệp vụ: chân dung càng cụ thể thì chọn kênh và thông điệp càng trúng; tách riêng học sinh và phụ huynh vì mối quan tâm khác nhau.
- → Kết quả bước: Bảng chân dung đối tượng (nhóm – đặc điểm – kênh hay dùng – mối quan tâm).

**Bước 3. Chốt thông điệp chính và thông điệp phụ**
- Làm gì: từ `thong_diep`, chốt 1 thông điệp chính (≤ 12 từ, dễ nhớ) + 2–3 thông điệp phụ; kiểm tra từng thông điệp có bằng chứng/số liệu trong đề án tuyển sinh không; rà soát theo brand voice trẻ trung, học thuật.
- Dùng input: `thong_diep`.
- Vai trò: Trưởng phòng Truyền thông – Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: không đưa thông điệp sai lệch so với đề án tuyển sinh đã ban hành; mỗi thông điệp phụ phải có số liệu chứng minh.
- → Kết quả bước: Bộ thông điệp đã chốt (1 chính + 2–3 phụ, kèm bằng chứng).

**Bước 4. Chọn kênh và phân bổ ngân sách**
- Làm gì: từ `kenh`, liệt kê kênh paid/owned/earned; ưu tiên kênh có tỉ lệ chuyển đổi tốt từ các đợt trước; phân bổ `ngan_sach` theo từng kênh (số tiền cụ thể); ghi vai trò của từng kênh trong phễu.
- Dùng input: `kenh`, `ngan_sach` + bộ thông điệp (Bước 3).
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: xử lý sơ bộ, tổng hợp · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: tổng phân bổ phải khớp 100% ngân sách được duyệt; không cam kết ngân sách vượt thẩm quyền.
- → Kết quả bước: Bảng kênh – ngân sách – vai trò (tổng khớp ngân sách duyệt).

**Bước 5. Lập timeline và phân công**
- Làm gì: chia 4 pha: chuẩn bị → chạy → cao điểm → tổng kết; gắn từng mốc vào `thoi_gian`; mỗi mốc ghi công việc, người phụ trách, sản phẩm bàn giao; đối chiếu timeline với lịch tuyển sinh chung của Bộ/trường.
- Dùng input: `thoi_gian` + bảng kênh – ngân sách (Bước 4).
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: mốc cao điểm phải trùng giai đoạn thí sinh quyết định (sau thi tốt nghiệp THPT); để dự phòng 5–7 ngày cho phê duyệt nội dung.
- → Kết quả bước: Timeline chi tiết (mốc – công việc – phụ trách – bàn giao).

**Bước 6. Thiết lập KPI và bảng theo dõi**
- Làm gì: từ `kpi`, chốt KPI tổng và KPI từng kênh; thiết kế bảng theo dõi hằng tuần (tuần – KPI kế hoạch – thực tế – chênh lệch – hành động); quy định ngưỡng cảnh báo (VD: đạt < 70% kế hoạch tuần → họp rà soát).
- Dùng input: `kpi` + mục tiêu SMART (Bước 1).
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: đối chiếu tự động, cảnh báo sai lệch, lập bảng biểu, định dạng · ⏱ ~30–60 phút (ước tính)
- Lưu ý nghiệp vụ: KPI phải đo được hằng tuần bằng dữ liệu thực (lead, hồ sơ), không dùng chỉ số cảm tính.
- → Kết quả bước: Bộ KPI đã chốt + mẫu bảng theo dõi hằng tuần.

**Bước 7. Kiểm tra tính tương xứng và hoàn thiện brief**
- Làm gì: kiểm tra tam giác mục tiêu – ngân sách – KPI có tương xứng không (ngân sách có đủ để đạt KPI không); rà soát toàn bộ brief: thông điệp bám đề án, timeline khớp lịch chung; tổng hợp thành văn bản brief hoàn chỉnh.
- Dùng input: toàn bộ bán thành phẩm Bước 1–6.
- Vai trò: Chuyên viên Phòng Truyền thông – Tuyển sinh · AI hỗ trợ: tổng hợp, chuẩn hóa dữ liệu, đối chiếu tự động, cảnh báo sai lệch · ⏱ ~1–2 giờ (ước tính)
- Lưu ý nghiệp vụ: nếu ngân sách không đủ đạt KPI thì hoặc giảm mục tiêu hoặc xin bổ sung — không để brief "thiếu tiền mà đòi kết quả".
- → Kết quả bước: Campaign brief hoàn chỉnh (sẵn sàng trình duyệt).

## Luồng quy trình (Workflow)

```mermaid
flowchart TD
    A[/"Chỉ tiêu tuyển sinh đợt"/] --> B["Bước 1. Xác định mục tiêu SMART và chốt chỉ tiêu"]
    B --> C["Bước 2. Vẽ chân dung đối tượng"]
    C --> D["Bước 3. Chốt thông điệp chính và phụ"]
    D --> E["Bước 4. Chọn kênh và phân bổ ngân sách"]
    E --> F["Bước 5. Lập timeline và phân công"]
    F --> G["Bước 6. Thiết lập KPI và bảng theo dõi"]
    G --> H["Bước 7. Kiểm tra tính tương xứng và hoàn thiện brief"]
    H --> HG["👤 Trưởng phòng → BGH phê duyệt"]
    HG --> I[["Campaign brief + bảng theo dõi KPI"]]
```

## Đầu ra (Output)
- Campaign brief hoàn chỉnh (markdown): mục tiêu, đối tượng, thông điệp, kênh, ngân sách, timeline, KPI.
- Bảng theo dõi KPI hằng tuần (mẫu).

**Cấu trúc output chuẩn** (khung mẫu cố định của sản phẩm chính — Campaign brief):
1. Tiêu đề (tên chiến dịch + thời gian chạy).
2. Mục tiêu SMART (con số + thời hạn đo).
3. Đối tượng (bảng chân dung: nhóm – đặc điểm – kênh hay dùng – mối quan tâm).
4. Thông điệp (1 chính + 2–3 phụ, kèm bằng chứng/số liệu).
5. Kênh và ngân sách (bảng: kênh – số tiền – vai trò trong phễu).
6. Timeline (4 pha: chuẩn bị – chạy – cao điểm – tổng kết; mốc – công việc – phụ trách – bàn giao).
7. KPI (KPI tổng, KPI từng kênh, tần suất báo cáo).
- Phụ lục: Mẫu bảng theo dõi KPI hằng tuần.

## Checklist nghiệm thu

- [ ] Đủ các phần theo "Cấu trúc output chuẩn": Tiêu đề (tên chiến dịch + thời gian chạy).; Mục tiêu SMART (con số + thời hạn đo).; Đối tượng (bảng chân dung; Thông điệp (1 chính + 2; Kênh và ngân sách (bảng; Timeline (4 pha; …
- [ ] Có đầy đủ sản phẩm: Campaign brief hoàn chỉnh (markdown): mục tiêu, đối tượng, thông điệp, kênh, ngân sách,…
- [ ] Có đầy đủ sản phẩm: Bảng theo dõi KPI hằng tuần (mẫu)
- [ ] Mọi số liệu, tên, ngày tháng trong output khớp với Input đã cung cấp (không thêm bớt, không suy đoán)
- [ ] Không bịa đặt số liệu, minh chứng, trích dẫn hay căn cứ
- [ ] Đúng thể thức, định dạng văn bản theo quy định hiện hành
- [ ] Căn cứ pháp lý nêu đầy đủ, còn hiệu lực tại thời điểm lập
- [ ] Đã qua Human gate: người có thẩm quyền đã kiểm tra/ký duyệt trước khi phát hành
- [ ] Mục tiêu phải bám chỉ tiêu tuyển sinh đã được duyệt
- [ ] Chân dung càng cụ thể thì chọn kênh và thông điệp càng trúng

> Tiêu chí đạt: tất cả các ô đều được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `ten_chien_dich` | Cao điểm tư vấn tuyển sinh đợt 1/2027 |
| `thoi_gian` | 01/03/2027 – 30/06/2027 |
| `muc_tieu` | 3.000 hồ sơ đăng ký (giả lập) |
| `doi_tuong` | Học sinh lớp 12 khu vực phía Bắc, phụ huynh |
| `thong_diep` | Chính: "A — Nơi tri thức gặp tương lai"; Phụ: học bổng, việc làm sau tốt nghiệp |
| `kenh` | Fanpage ads, TikTok, ngày hội tư vấn, website |
| `ngan_sach` | 350 triệu đồng (giả lập) |
| `kpi` | 5.000 lead; tỉ lệ lead→hồ sơ 60% |

### Output mẫu

```
CAMPAIGN BRIEF — Cao điểm tư vấn tuyển sinh đợt 1/2027
Thời gian chạy: 01/03/2027 – 30/06/2027
Trường Đại học A (dữ liệu giả lập)

1. MỤC TIÊU: 3.000 hồ sơ đăng ký (giả lập).
2. ĐỐI TƯỢNG: Học sinh lớp 12 khu vực phía Bắc và phụ huynh.
3. THÔNG ĐIỆP:
   - Chính: "A — Nơi tri thức gặp tương lai"
   - Phụ: học bổng đa dạng; 95% SV có việc làm sau 6 tháng (giả lập).
4. KÊNH & NGÂN SÁCH (giả lập):
   - Fanpage ads: 150 trđ | TikTok: 80 trđ | Ngày hội tư vấn: 70 trđ | Website/SEO: 50 trđ
5. TIMELINE:
   - T3: chuẩn bị nội dung, landing page | T4–T5: chạy cao điểm | T6: đẩy hồ sơ + tổng kết
6. KPI: 5.000 lead; tỉ lệ lead → hồ sơ ≥ 60%; báo cáo hằng tuần cho Trưởng phòng.

PHỤ LỤC: Mẫu bảng theo dõi KPI hằng tuần (Tuần | KPI kế hoạch | Thực tế |
Chênh lệch | Hành động) — ngưỡng cảnh báo: đạt < 70% kế hoạch tuần → họp rà soát.
```

## Human gate (người kiểm duyệt)
- Trưởng phòng duyệt brief trước khi trình.
- Ban Giám hiệu phê duyệt ngân sách chiến dịch.
- Không chạy chiến dịch khi chưa được phê duyệt.

## Giới hạn (guardrails)
- Không tự chạy quảng cáo, tự chi ngân sách.
- Không cam kết ngân sách vượt thẩm quyền.
- Không đưa thông điệp sai lệch so với đề án tuyển sinh đã ban hành.
- Không dùng hình ảnh, KOLs không rõ bản quyền/thỏa thuận.

## Căn cứ & lưu ý
- Brief phải bám đề án tuyển sinh và lịch tuyển sinh của Bộ GD&ĐT.
- Brand voice: trẻ trung, học thuật.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.1.0`; ngày cập nhật: `2026-10-09`.
- Kho nguồn: https://github.com/phamtruong91/dh-skills
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `78fd1d51b8acd1a724d9b9af6c488460bc7551ad`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/campaign-brief-tuyen-sinh`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
