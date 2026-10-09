---
name: tong-quan-tai-lieu-khoa-hoc
description: Tổng quan tài liệu khoa học (literature review) từ các tài liệu được cung cấp: trích xuất phương pháp/kết quả, lập ma trận so sánh, xác định khoảng trống nghiên cứu, trích dẫn chuẩn. Dùng chung cho mọi đơn vị làm nghiên cứu.
---

# Skill: Tổng quan tài liệu khoa học

## Khi nào dùng
Khi viết phần tổng quan nghiên cứu cho đề tài, luận văn/luận án, bài báo khoa học.
Dùng chung cho giảng viên, nghiên cứu viên, học viên cao học, NCS ở mọi khoa/phòng.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `cau_hoi_nghien_cuu` | Câu hỏi/mục tiêu nghiên cứu cần tổng quan | Có |
| `tai_lieu` | Danh sách tài liệu được phép dùng: tiêu đề, tác giả, năm, nguồn, file/tóm tắt | Có |
| `pham_vi` | Giới hạn năm xuất bản, loại nguồn (tạp chí, hội thảo...) | Không |
| `dinh_dang_trich_dan` | APA / IEEE / Vancouver... | Không (mặc định: APA) |

## Quy trình

**Bước 1. Trích xuất có cấu trúc từng tài liệu**
- Làm gì: Đọc từng tài liệu trong `tai_lieu`; trích: câu hỏi nghiên cứu, phương pháp, kết quả chính, hạn chế — kèm trích dẫn đầy đủ (tác giả, năm, nguồn); kiểm tra `pham_vi` (năm xuất bản, loại nguồn) để loại tài liệu ngoài phạm vi, ghi rõ lý do loại.
- Dùng input: `tai_lieu`, `pham_vi`, `cau_hoi_nghien_cuu`.
- Vai trò: Nhà nghiên cứu · AI hỗ trợ: trích xuất có cấu trúc từng tài liệu (câu hỏi, phương pháp, kết quả, hạn chế) · ⏱ ~20–40 phút (ước tính)
- Lưu ý nghiệp vụ: chỉ trích xuất từ tài liệu được cung cấp — TUYỆT ĐỐI không bịa thêm; thiếu thông tin ghi "không xác định"; giữ nguyên số liệu gốc, không diễn giải thêm.
- → Kết quả bước: Phiếu trích xuất có cấu trúc cho từng tài liệu.

**Bước 2. Lập ma trận literature**
- Làm gì: Dựng bảng ma trận: hàng = tài liệu, cột = phương pháp / dữ liệu / kết quả chính / hạn chế; điền nội dung từ phiếu trích xuất ở bước 1; kiểm tra mỗi ô đều có căn cứ trích dẫn rõ ràng.
- Dùng input: (phiếu trích xuất từ bước 1).
- Vai trò: Nhà nghiên cứu · AI hỗ trợ: dựng ma trận so sánh, đảm bảo mỗi ô có căn cứ trích dẫn · ⏱ ~15–25 phút (ước tính)
- Lưu ý nghiệp vụ: ma trận phải trung thực — không gom nhóm làm mờ khác biệt giữa các nghiên cứu; cột "hạn chế" là bắt buộc vì đó chính là nguồn của gap ở bước 4.
- → Kết quả bước: Ma trận so sánh tài liệu hoàn chỉnh.

**Bước 3. Tổng hợp xu hướng, đồng thuận, mâu thuẫn**
- Làm gì: Đọc ma trận theo chiều dọc từng cột: rút ra xu hướng chung, điểm các nghiên cứu đồng thuận, điểm mâu thuẫn; mỗi nhận định phải dẫn chiếu cụ thể tài liệu nào (tác giả, năm).
- Dùng input: `cau_hoi_nghien_cuu` (ma trận từ bước 2).
- Vai trò: Nhà nghiên cứu · AI hỗ trợ: tổng hợp xu hướng/đồng thuận/mâu thuẫn, mỗi nhận định dẫn chiếu tài liệu cụ thể · ⏱ ~15–25 phút (ước tính)
- Lưu ý nghiệp vụ: không suy diễn vượt quá dữ liệu trong ma trận; điểm mâu thuẫn phải nêu rõ cả hai phía, không "hòa giải" hộ nhà nghiên cứu.
- → Kết quả bước: Bản tổng hợp (xu hướng/đồng thuận/mâu thuẫn) có dẫn chiếu.

**Bước 4. Xác định gap nghiên cứu**
- Làm gì: Từ cột "hạn chế" và các điểm mâu thuẫn trong ma trận, liệt kê những câu hỏi chưa được trả lời; mỗi gap ghi rõ: dẫn từ tài liệu nào, vì sao là khoảng trống; sắp xếp theo mức độ liên quan đến `cau_hoi_nghien_cuu`.
- Dùng input: `cau_hoi_nghien_cuu` (ma trận từ bước 2, tổng hợp từ bước 3).
- Vai trò: Nhà nghiên cứu · AI hỗ trợ: xác định gap nghiên cứu dẫn từ tài liệu, sắp xếp theo liên quan đến câu hỏi nghiên cứu · ⏱ ~15–25 phút (ước tính)
- Lưu ý nghiệp vụ: gap phải dẫn từ tài liệu, không "nghĩ ra"; phân biệt gap thật với hạn chế đã được nghiên cứu khác lấp đầy.
- → Kết quả bước: Danh sách gap nghiên cứu có căn cứ.

**Bước 5. Dự thảo outline và danh mục trích dẫn**
- Làm gì: Dự thảo outline phần tổng quan bám theo ma trận + gap (mở đầu → các chủ đề → gap → hướng nghiên cứu); lập danh mục trích dẫn đầy đủ theo `dinh_dang_trich_dan` (mặc định APA); đối chiếu chéo: mọi trích dẫn trong outline đều có trong danh mục và ngược lại.
- Dùng input: `dinh_dang_trich_dan` (ma trận, tổng hợp, gap từ bước 2–4).
- Vai trò: Nhà nghiên cứu · AI hỗ trợ: dự thảo outline + danh mục trích dẫn theo định dạng, đối chiếu chéo hai chiều · ⏱ ~15–25 phút (ước tính)
- Lưu ý nghiệp vụ: kiểm tra kỹ chính tả tên tác giả, năm xuất bản — lỗi trích dẫn làm mất uy tín bài viết; outline chỉ là khung, không viết hộ nội dung phân tích sâu.
- → Kết quả bước: Outline phần tổng quan + danh mục trích dẫn chuẩn — sản phẩm cuối.
## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Tập tài liệu được cung cấp"/]
    B["Trích xuất có cấu trúc từng tài liệu"]
    C["Lập ma trận literature"]
    D["Tổng hợp đồng thuận, mâu thuẫn, xu hướng"]
    E["Xác định gap nghiên cứu"]
    F["Dự thảo outline + danh mục trích dẫn"]
    HG["👤 Nhà nghiên cứu kiểm tra từng trích dẫn"]
    G[/"Outline tổng quan + danh mục trích dẫn"/]
    A --> B --> C --> D --> E --> F --> HG --> G
```

## Đầu ra (Output)
- Ma trận so sánh tài liệu (bảng).
- Bản tổng hợp xu hướng/đồng thuận/mâu thuẫn/gap.
- Outline phần tổng quan kèm trích dẫn chuẩn.

**Cấu trúc output chuẩn:** khung mẫu CỐ ĐỊNH của sản phẩm chính (Bản tổng hợp tổng quan):
1. Câu hỏi nghiên cứu + phạm vi tổng quan (năm xuất bản, loại nguồn).
2. Ma trận so sánh tài liệu: hàng = tài liệu, cột = phương pháp / dữ liệu / kết quả chính / hạn chế.
3. Tổng hợp: xu hướng chung, điểm đồng thuận, điểm mâu thuẫn (kèm dẫn chiếu từng tài liệu).
4. Gap nghiên cứu: khoảng trống chưa được trả lời, dẫn từ tài liệu cụ thể.
5. Outline phần tổng quan + danh mục trích dẫn theo định dạng yêu cầu.

## Checklist nghiệm thu

- [ ] Output đầy đủ 5 phần theo Cấu trúc output chuẩn: câu hỏi nghiên cứu + phạm vi tổng quan; ma trận so sánh; tổng hợp; gap nghiên cứu; outline + danh mục trích dẫn.
- [ ] Chỉ tổng hợp từ tài liệu được cung cấp; mọi nhận định trong tổng hợp đều dẫn chiếu cụ thể tài liệu (tác giả, năm).
- [ ] TUYỆT ĐỐI không bịa trích dẫn: không tự tạo tên tác giả, năm, tạp chí, số liệu; thiếu thông tin ghi "không xác định".
- [ ] Mâu thuẫn được nêu rõ cả hai phía, không "hòa giải" hộ nhà nghiên cứu; gap dẫn từ tài liệu, phân biệt gap thật với hạn chế đã được nghiên cứu khác lấp đầy.
- [ ] Đối chiếu chéo: mọi trích dẫn trong outline đều có trong danh mục và ngược lại; chính tả tên tác giả, năm xuất bản chính xác.
- [ ] Đúng định dạng trích dẫn yêu cầu (APA/IEEE...); không tái tạo nguyên văn đoạn dài của tài liệu có bản quyền.
- [ ] Đã qua Human gate: nhà nghiên cứu/chủ nhiệm đề tài đã kiểm tra từng trích dẫn và từng kết luận tổng hợp.

> Tiêu chí đạt: tất cả các ô được đánh dấu.

## Ví dụ mô phỏng (dữ liệu giả lập)

> Tất cả tên tác giả, tài liệu, số liệu dưới đây đều là **giả lập**, minh họa cấu trúc output.

### Input mẫu

| Trường | Giá trị |
|---|---|
| `cau_hoi_nghien_cuu` | AI hỗ trợ đánh giá kết quả học tập sinh viên đại học có hiệu quả không? |
| `tai_lieu` | 4 bài báo giả lập (2019–2024) về AI trong đánh giá giáo dục |
| `dinh_dang_trich_dan` | APA |

### Output mẫu

```
BẢN TỔNG HỢP TỔNG QUAN TÀI LIỆU (giả lập — minh họa cấu trúc)

1. Câu hỏi nghiên cứu: AI hỗ trợ đánh giá kết quả học tập sinh viên đại học có hiệu quả không?
   Phạm vi: 4 bài báo giả lập (2019–2024) về AI trong đánh giá giáo dục; định dạng trích dẫn: APA.

2. ĐHA TRẬN SO SÁNH TÀI LIỆU

| Tài liệu (giả lập) | Phương pháp | Kết quả chính | Hạn chế |
|---|---|---|---|
| Nguyễn A. & Trần B. (2022) | Thực nghiệm, n=200 | AI chấm tự luận nhanh hơn 40%, độ đồng thuận với GV 0.82 | Chỉ 1 môn học |
| Lê C. (2023) | Khảo sát, n=500 | 72% SV hài lòng với feedback tự động | Thiếu nhóm đối chứng |
| Phạm D. et al. (2024) | Phân tích log LMS | Feedback tức thì giúp tăng 15% điểm quá trình | Dữ liệu 1 trường |
| Hoàng E. (2019) | Tổng quan | Cảnh báo thiên lệch khi dữ liệu huấn luyện không đại diện | Không thực nghiệm |

3. TỔNG HỢP: các nghiên cứu đồng thuận AI giúp tăng tốc và cá nhân hóa đánh giá
   (Nguyễn A. & Trần B., 2022; Lê C., 2023; Phạm D. et al., 2024); mâu thuẫn ở mức độ
   tin cậy khi thiếu kiểm chứng của giảng viên (Hoàng E., 2019).

4. GAP: thiếu nghiên cứu dài hạn về tác động đến năng lực tự đánh giá của SV
   (dẫn từ hạn chế của cả 4 tài liệu) — đây là khoảng trống đề tài có thể khai thác.

5. OUTLINE PHẦN TỔNG QUAN + DANH MỤC TRÍCH DẪN (APA):
   I. Mở đầu: bối cảnh AI trong đánh giá giáo dục
   II. AI hỗ trợ chấm và feedback tự động
   III. Mức độ tin cậy và thiên lệch của AI
   IV. Gap nghiên cứu và hướng đề xuất
   Danh mục: Nguyễn A. & Trần B. (2022); Lê C. (2023); Phạm D. et al. (2024); Hoàng E. (2019).
```

## Human gate (người kiểm duyệt)
- **Nhà nghiên cứu/chủ nhiệm đề tài** kiểm tra từng trích dẫn, từng kết luận tổng hợp
  trước khi đưa vào bài viết.
- Giảng viên hướng dẫn duyệt đối với luận văn/luận án.

## Giới hạn (guardrails)
- **TUYỆT ĐỐI không bịa trích dẫn**: không tự tạo tên tác giả, năm, tạp chí, số liệu không có
  trong tài liệu đầu vào. Nếu thiếu thông tin, ghi rõ "không xác định" thay vì suy đoán.
- Chỉ tổng hợp từ tài liệu người dùng cung cấp hoặc nguồn xác thực được; không trích dẫn
  từ trí nhớ.
- Tuân thủ bản quyền: không tái tạo nguyên văn đoạn dài của tài liệu có bản quyền;
  chỉ tóm tắt và trích dẫn ngắn.
- Không thay nhà nghiên cứu đưa ra kết luận khoa học cuối cùng.

## Căn cứ & lưu ý
- Chuẩn trích dẫn APA/IEEE theo yêu cầu của tạp chí/cơ sở đào tạo.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.
