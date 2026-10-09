---
name: executive-brief-trinh-lanh-dao
description: Tóm tắt nhiều nguồn (báo cáo, tờ trình, bảng số liệu) thành executive brief 1–2 trang kèm decision memo và bảng "vấn đề cần quyết định", giúp lãnh đạo nắm nhanh và ra quyết định. Dùng chung cho mọi cấp lãnh đạo, mọi lĩnh vực trong trường.
---

# Skill: Executive brief trình lãnh đạo

## Khi nào dùng
Khi lãnh đạo cần quyết định một vấn đề phức tạp có nhiều nguồn thông tin: phê duyệt đề án,
chọn phương án đầu tư, xử lý vụ việc... Thay vì đọc cả chồng tài liệu, lãnh đạo chỉ đọc
brief 1–2 trang + bảng vấn đề cần quyết định.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `van_de` | Vấn đề cần quyết định (1 câu) | Có |
| `nguon_tai_lieu` | Danh sách nguồn: báo cáo, tờ trình, bảng số liệu, văn bản liên quan | Có |
| `tieu_chi_quyet_dinh` | Các tiêu chí lãnh đạo sẽ dùng để quyết (VD: chi phí, tiến độ, rủi ro, phù hợp chiến lược) | Có |
| `phuong_an_hien_co` | Các phương án đang được đề xuất (nếu đã có) | Không |
| `thoi_han_quyet_dinh` | Deadline cần ra quyết định | Không |

## Quy trình

**Bước 1. Kiểm kê nguồn tài liệu**
- Làm gì: liệt kê toàn bộ nguồn trong `nguon_tai_lieu`; kiểm tra mỗi nguồn có đủ thông tin trích dẫn
  (tên, số/ký hiệu, ngày); nêu rõ nguồn nào còn thiếu và ảnh hưởng của việc thiếu đó đến độ tin cậy của brief.
- Dùng input: `nguon_tai_lieu`, `van_de`.
- Vai trò: Thư ký lãnh đạo (hoặc chuyên viên đơn vị trình vấn đề) · AI hỗ trợ: kiểm kê nguồn, ghi nhận nguồn thiếu và mâu thuẫn · ⏱ ~10–20 phút (ước tính)
- Lưu ý nghiệp vụ: nguồn thiếu không được "bù" bằng suy đoán — phải ghi rõ trong brief; các nguồn mâu thuẫn
  nhau phải được ghi nhận ngay từ bước này để xử lý ở Bước 3–4.
- → Kết quả bước: danh mục nguồn (đủ/thiếu) + ghi chú ảnh hưởng của nguồn thiếu.

**Bước 2. Tóm tắt từng nguồn**
- Làm gì: mỗi nguồn tóm tắt 3–5 dòng: sự kiện chính, số liệu chính, kết luận/quan điểm của nguồn;
  giữ nguyên ý của nguồn, không trộn ý kiến cá nhân.
- Dùng input: `nguon_tai_lieu`.
- Vai trò: Thư ký lãnh đạo (hoặc chuyên viên đơn vị trình vấn đề) · AI hỗ trợ: tóm tắt từng nguồn 3–5 dòng, giữ nguyên ý và ghi nguồn số liệu · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: tóm tắt phải trung thành — không "làm mềm" số liệu bất lợi của bất kỳ phương án nào;
  mỗi số liệu ghi rõ lấy từ nguồn nào.
- → Kết quả bước: bộ tóm tắt từng nguồn (3–5 dòng/nguồn).

**Bước 3. So sánh phương án theo tiêu chí**
- Làm gì: lập bảng ma trận — hàng là các tiêu chí trong `tieu_chi_quyet_dinh`, cột là từng phương án
  trong `phuong_an_hien_co`; nếu chưa có phương án thì đề xuất các phương án hiển nhiên rút ra từ nguồn
  (làm / không làm / hoãn); mỗi ô điền đánh giá và ghi nguồn số liệu.
- Dùng input: `phuong_an_hien_co`, `tieu_chi_quyet_dinh`, bộ tóm tắt (Bước 2).
- Vai trò: Thư ký lãnh đạo (hoặc chuyên viên đơn vị trình vấn đề) · AI hỗ trợ: lập bảng ma trận so sánh phương án theo tiêu chí, mỗi ô có nguồn · ⏱ ~15–30 phút (ước tính)
- Lưu ý nghiệp vụ: ô nào không có số liệu thì ghi "chưa có số liệu", không bịa; mọi phương án phải được
  đánh giá trên cùng một bộ tiêu chí để so sánh công bằng.
- → Kết quả bước: bảng so sánh phương án theo tiêu chí (mỗi ô có nguồn).

**Bước 4. Nêu vấn đề còn mở, giả định và rủi ro**
- Làm gì: liệt kê thông tin chưa có, giả định đang phải dùng tạm, rủi ro chưa lượng hóa được;
  đánh giá mức độ ảnh hưởng của từng điểm mở đến quyết định.
- Dùng input: bộ tóm tắt (Bước 2), bảng so sánh (Bước 3).
- Vai trò: Thư ký lãnh đạo (hoặc chuyên viên đơn vị trình vấn đề) · AI hỗ trợ: liệt kê thông tin thiếu, giả định tạm dùng, rủi ro chưa lượng hóa · ⏱ ~10–20 phút (ước tính)
- Lưu ý nghiệp vụ: đây là phần bảo vệ lãnh đạo khỏi quyết định mù — phải trung thực, không giấu điểm yếu
  của phương án đang được "ưa thích".
- → Kết quả bước: danh sách vấn đề mở + giả định + rủi ro chưa lượng hóa.

**Bước 5. Lập bảng vấn đề cần quyết định**
- Làm gì: với mỗi điểm cần lãnh đạo chốt, viết một câu hỏi quyết định cụ thể; liệt kê các phương án;
  đưa khuyến nghị TRUNG LẬP kèm căn cứ (trích từ Bước 3–4); ghi `thoi_han_quyet_dinh` nếu có.
- Dùng input: `van_de`, bảng so sánh (Bước 3), vấn đề mở (Bước 4), `thoi_han_quyet_dinh`.
- Vai trò: Thư ký lãnh đạo (hoặc chuyên viên đơn vị trình vấn đề) · AI hỗ trợ: lập bảng vấn đề cần quyết định với khuyến nghị trung lập kèm căn cứ · ⏱ ~15–25 phút (ước tính)
- Lưu ý nghiệp vụ: khuyến nghị trung lập = trình bày cân bằng, luôn kèm căn cứ, cấm thiên vị phương án;
  câu hỏi phải đủ cụ thể để lãnh đạo trả lời được ngay, tránh câu hỏi chung chung.
- → Kết quả bước: bảng vấn đề cần quyết định (câu hỏi | phương án | khuyến nghị trung lập + căn cứ).

**Bước 6. Xuất brief và decision memo**
- Làm gì: viết executive brief tối đa 2 trang gồm: bối cảnh, số liệu chính, bảng so sánh rút gọn,
  vấn đề mở, bảng vấn đề cần quyết định; đính kèm decision memo — mẫu để lãnh đạo ghi: quyết định,
  người quyết định, ngày quyết định, ý kiến chỉ đạo.
- Dùng input: kết quả các Bước 1–5.
- Vai trò: Thư ký lãnh đạo (hoặc chuyên viên đơn vị trình vấn đề) · AI hỗ trợ: xuất brief tối đa 2 trang + decision memo có chỗ ký xác nhận · ⏱ ~15–25 phút (ước tính)
- Lưu ý nghiệp vụ: brief tốt = ngắn + đủ + trung thực; chi tiết đầy đủ để ở phụ lục nguồn, không nhồi
  vào brief; decision memo phải có chỗ ký/xác nhận của lãnh đạo.
- → Kết quả bước: executive brief (tối đa 2 trang) + decision memo.
## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Các nguồn tài liệu"/]
    B["Bước 1. Kiểm kê nguồn tài liệu"]
    C["Bước 2. Tóm tắt từng nguồn"]
    D["Bước 3. So sánh phương án theo tiêu chí"]
    E["Bước 4. Vấn đề mở, giả định, rủi ro"]
    F["Bước 5. Bảng vấn đề cần quyết định"]
    G["Bước 6. Xuất brief + decision memo"]
    HG["👤 Thư ký kiểm tra nguồn; lãnh đạo quyết định"]
    H[/"Executive brief + decision memo"/]
    A --> B --> C --> D --> E --> F --> G --> HG --> H
```

## Đầu ra (Output)
- Executive brief (1–2 trang).
- Decision memo (mẫu ghi quyết định).
- Bảng vấn đề cần quyết định (câu hỏi + phương án + khuyến nghị trung lập + căn cứ).

**Cấu trúc output chuẩn** (sản phẩm chính: Executive brief):
1. Tiêu đề: EXECUTIVE BRIEF + vấn đề cần quyết định (1 câu) + thời hạn quyết định.
2. Bối cảnh (3–5 dòng): vì sao vấn đề phát sinh, ai đề xuất.
3. Số liệu chính: các con số quyết định, mỗi số ghi nguồn.
4. So sánh phương án: bảng theo tiêu chí quyết định (mỗi ô có nguồn).
5. Vấn đề còn mở: thông tin thiếu, giả định đang dùng, rủi ro chưa lượng hóa.
6. Bảng vấn đề cần quyết định: câu hỏi | phương án | khuyến nghị trung lập + căn cứ.
7. Phụ lục: danh mục nguồn tài liệu.

## Checklist nghiệm thu

- [ ] Brief đầy đủ 7 phần theo Cấu trúc output chuẩn: tiêu đề + vấn đề 1 câu + thời hạn; bối cảnh (3–5 dòng); số liệu chính; bảng so sánh phương án; vấn đề còn mở; bảng vấn đề cần quyết định; phụ lục danh mục nguồn.
- [ ] Brief không quá 2 trang; chi tiết đầy đủ để ở phụ lục nguồn, không nhồi vào brief.
- [ ] Mọi số liệu khớp với Input; mỗi số ghi rõ nguồn; ô không có số liệu ghi "chưa có số liệu", không bịa.
- [ ] Khuyến nghị trung lập: trình bày cân bằng các phương án, luôn kèm căn cứ; không thiên vị phương án nào.
- [ ] Vấn đề mở, giả định, rủi ro chưa lượng hóa được nêu trung thực — không giấu điểm yếu của bất kỳ phương án nào.
- [ ] Decision memo có đủ ô: quyết định, người quyết định, ngày quyết định, ý kiến chỉ đạo, chỗ ký/xác nhận.
- [ ] Câu hỏi quyết định đủ cụ thể để lãnh đạo trả lời được ngay.
- [ ] Đã qua Human gate: thư ký/văn phòng lãnh đạo đã kiểm tra nguồn trích dẫn đầy đủ, chính xác, không sót nguồn quan trọng.

> Tiêu chí đạt: tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên trường, cá nhân, số liệu dưới đây đều là **giả lập**.
> Ví dụ: Ban Giám hiệu cần quyết định có đầu tư phòng lab AI mới không.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `van_de` | Có đầu tư xây dựng Phòng Lab AI dùng chung năm 2027 không? |
| `nguon_tai_lieu` | Tờ trình của Khoa CNTT (đề xuất 8 tỷ đồng); Báo cáo khảo sát nhu cầu (72% giảng viên ủng hộ); Báo cáo tài chính (ngân sách còn 12 tỷ); Biên bản họp Hội đồng KH&ĐT (ý kiến chia rẽ) |
| `tieu_chi_quyet_dinh` | Chi phí; nhu cầu sử dụng thực; khả năng huy động thêm nguồn; rủi ro công nghệ lạc hậu |
| `thoi_han_quyet_dinh` | Trước 30/11/2026 (để kịp kế hoạch năm) |

### Output mẫu

**EXECUTIVE BRIEF — Có đầu tư xây dựng Phòng Lab AI dùng chung năm 2027 không?** (thời hạn quyết định: trước 30/11/2026)

1. **Bối cảnh:** Khoa CNTT đề xuất đầu tư 8 tỷ đồng xây phòng lab AI dùng chung phục vụ đào tạo và nghiên cứu; Hội đồng KH&ĐT chưa thống nhất (7/13 phiếu thuận).
2. **Số liệu chính:** 72% giảng viên được khảo sát ủng hộ (n=180) *(nguồn: Báo cáo khảo sát nhu cầu)*; ngân sách đầu tư 2027 còn 12 tỷ *(nguồn: Báo cáo tài chính)*; đề xuất 8 tỷ *(nguồn: Tờ trình Khoa CNTT)*.
3. **So sánh phương án:**
| Tiêu chí | PA1: Đầu tư ngay 8 tỷ | PA2: Thuê dịch vụ cloud 2 tỷ/năm | PA3: Hoãn sang 2028 |
|---|---|---|---|
| Chi phí | 8 tỷ một lần | 2 tỷ/năm | 0 (năm nay) |
| Rủi ro lạc hậu | Cao (thiết bị 3–5 năm) | Thấp | — |
4. **Vấn đề còn mở:** chưa có khảo sát nhu cầu sinh viên; chưa có báo giá chi tiết thiết bị; chưa lượng hóa được chi phí vận hành PA1.
5. **Bảng vấn đề cần quyết định:**
| # | Câu hỏi quyết định | Phương án | Khuyến nghị (trung lập, kèm căn cứ) |
|---|---|---|---|
| 1 | Có đầu tư lab năm 2027? | Đầu tư / Thuê cloud / Hoãn | Cân nhắc PA2 nếu ưu tiên linh hoạt chi phí (căn cứ: rủi ro lạc hậu thiết bị, Hội đồng chưa đồng thuận) |
6. **Phụ lục nguồn:** Tờ trình Khoa CNTT; Báo cáo khảo sát nhu cầu (n=180); Báo cáo tài chính; Biên bản họp Hội đồng KH&ĐT.

## Human gate (người kiểm duyệt)
1. **Thư ký/văn phòng lãnh đạo**: kiểm tra nguồn trích dẫn trong brief có đầy đủ, chính xác;
   đảm bảo không sót nguồn quan trọng.
2. **Lãnh đạo**: là người DUY NHẤT ra quyết định; ghi quyết định vào decision memo.
3. Brief chỉ có giá trị tham khảo — không thay thế tờ trình, hồ sơ chính thức.

## Giới hạn (guardrails)
- KHÔNG ra quyết định thay lãnh đạo dưới bất kỳ hình thức nào.
- Khuyến nghị trong brief phải TRUNG LẬP, luôn kèm căn cứ; cấm thiên vị phương án.
- KHÔNG giấu rủi ro, thông tin bất lợi của bất kỳ phương án nào.
- KHÔNG bịa số liệu, trích dẫn; nguồn nào thiếu phải nêu rõ.

## Căn cứ & lưu ý
- Brief tốt = ngắn + đủ + trung thực. Tối đa 2 trang; chi tiết để ở phụ lục nguồn.
- Mọi ví dụ đều giả lập; không dùng tên thật của trường/cá nhân.
