---
name: "ma-tran-chuan-dau-ra"
description: "Lập ma trận đối sánh chuẩn đầu ra học phần (CLO) với chuẩn đầu ra chương trình (PLO) theo mức I – R – M, kiểm tra mỗi PLO có ít nhất một học phần đạt mức M và rà soát học phần thừa/thiếu. Dùng khi thẩm định, rà soát hoặc kiểm định chương trình đào tạo."
---

# Lập ma trận đối sánh chuẩn đầu ra học phần – chương trình (CLO–PLO)

## Định dạng và file đầu ra
Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .xlsx, .csv, .pdf. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

**Phải tạo file thực tế để tải xuống, không chỉ trả nội dung trong chat.** Định dạng mặc định của skill: **.xlsx**. Nếu yêu cầu gồm cả báo cáo thuyết minh, tạo thêm file Word cho báo cáo; không ghép báo cáo dài vào bảng tính. Không chờ người dùng yêu cầu xuất file lần nữa. Ưu tiên định dạng người dùng chỉ định; đọc quy tắc xuất file tại references/quy-cach-dau-ra.md.

## Quy cách đầu ra và thông tin thiếu
Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục). Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Khi người dùng yêu cầu bộ slide (.pptx), đọc mục “Xuất PowerPoint (.pptx) khi được yêu cầu” trong quy cách đầu ra.

## Kiểm soát áp dụng và phê duyệt
Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

Nếu có cập nhật pháp lý dưới đây, đọc [căn cứ và điều kiện áp dụng](references/phap-ly.md) trước khi làm. Quy trình dưới đây giữ nghiệp vụ từ bản gốc; mọi viện dẫn văn bản, mẫu biểu, điều khoản phải theo căn cứ đã chọn trong phap-ly.md, không theo văn bản cũ.

## Giới hạn và human gate
AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md).

## Khi nào dùng
Khi cần kiểm tra tính liên kết giữa các học phần và chuẩn đầu ra của chương trình đào tạo:
lập ma trận CLO–PLO, đánh giá mức độ đóng góp của từng học phần, phát hiện PLO chưa được
học phần nào "đạt được" (mức M) hoặc học phần không đóng góp vào PLO nào.

## Đầu vào (Input)
| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_nganh` | Tên ngành / chương trình đào tạo | Có |
| `plo` | Danh sách chuẩn đầu ra chương trình (PLO1, PLO2...) kèm nội dung tóm tắt | Có |
| `hoc_phan` | Danh sách học phần: mã, tên, và các CLO của từng học phần | Có |
| `nguong_kiem_tra` | Quy tắc kiểm tra (mặc định: mỗi PLO có ít nhất 1 học phần mức M) | Không |

## Quy trình
**Ràng buộc pháp lý khi thực hiện** (trích references/phap-ly.md; đối chiếu toàn văn và hiệu lực tại ngày nghiệp vụ):
- Thông tư 54/2026/TT-BGDĐT, hiệu lực 30/06/2026: Phân loại xây dựng chương trình, chuẩn đầu ra hay mở ngành; yêu cầu chuẩn ngành/trình độ, trạng thái chương trình và ngày tiếp nhận hồ sơ. Đọc toàn văn và điều khoản chuyển tiếp trước khi đổi chuẩn/mẫu; chưa xác minh toàn văn thì ghi điều kiện chưa xác nhận, không tự đặt thời hạn chuyển đổi.
- Trước Bước 1: chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi nhận nội bộ [CẦN XÁC MINH] (không đưa vào file giao), để trống phần tương ứng, chưa kết luận tuân thủ.
- Các con số, thời hạn, số điều, số mức xếp loại, hệ số và mẫu biểu nêu trong các bước dưới đây được giữ từ quy trình gốc (trước cập nhật pháp lý); chỉ dùng khi đã đối chiếu đúng với căn cứ đã chọn, khác thì theo căn cứ. Danh sách điểm cần đối chiếu: docs/DIEM_CAN_DOI_CHIEU_PHAP_LY.md.

**Bước 1. Liệt kê PLO của chương trình đào tạo**
- Làm gì: đưa toàn bộ chuẩn đầu ra chương trình từ `plo` thành các cột của ma trận; mỗi cột
  ghi số hiệu và nội dung tóm tắt từng PLO; kiểm tra danh sách PLO khớp với PLO đã ban hành
  trong khung CTĐT (đủ số lượng, đúng nội dung, đúng thứ tự đánh số).
- Dùng input: `ten_nganh`, `plo`.
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: chuẩn hóa danh sách PLO, đối chiếu bản PLO đang hiệu lực · ⏱ ~20 phút (ước tính)
- Lưu ý nghiệp vụ: bẫy thường gặp là dùng bản PLO cũ (chưa cập nhật sau lần rà soát CTĐT
  gần nhất) — phải lấy đúng bản PLO đang có hiệu lực; thiếu một PLO trong ma trận đồng nghĩa
  với PLO đó không được kiểm tra.
- → Kết quả bước: danh sách PLO đã chuẩn hóa (số hiệu + nội dung tóm tắt), sẵn sàng làm
  tiêu đề cột của ma trận.

**Bước 2. Liệt kê CLO của từng học phần**
- Làm gì: với mỗi học phần trong `hoc_phan`, lập một hàng của ma trận; ghi mã, tên học phần
  và toàn bộ các chuẩn đầu ra học phần (CLO) đã xác định trong đề cương chi tiết; kiểm tra
  mỗi CLO đều có ghi đóng góp vào PLO nào (thông tin này là đầu vào cho Bước 3).
- Dùng input: `hoc_phan`, `ten_nganh`.
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: tổng hợp danh sách CLO, kiểm tra đề cương đã thông qua · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: CLO phải lấy từ đề cương chi tiết đã được khoa thông qua, không lấy từ
  bản nháp; học phần nào chưa có CLO thì ghi chú "chưa xác định CLO" và đưa vào danh sách
  cần bổ sung — không được bỏ qua.
- → Kết quả bước: danh sách học phần (mỗi hàng kèm các CLO), sẵn sàng làm hàng của ma trận.

**Bước 3. Đánh dấu mức đóng góp I – R – M**
- Làm gì: với mỗi ô giao giữa học phần (hàng) và PLO (cột), đánh dấu mức đóng góp dựa trên
  CLO của học phần: **I (Introduce – Giới thiệu)** khi học phần giới thiệu, làm quen nội dung
  của PLO; **R (Reinforce – Củng cố)** khi học phần củng cố, thực hành sâu hơn; **M (Master –
  Đạt được)** khi học phần giúp người học đạt được PLO ở mức thành thạo (thường gắn với đánh
  giá tổng hợp như đồ án, thực tập, khóa luận); để trống nếu học phần không đóng góp vào PLO đó.
- Dùng input: kết quả Bước 1 (danh sách PLO), kết quả Bước 2 (CLO từng học phần).
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: đánh dấu sơ bộ I/R/M từng ô giao học phần – PLO · ⏱ ~1 giờ (ước tính)
- Lưu ý nghiệp vụ: mức M không được gán tùy tiện — chỉ gán M khi học phần có hình thức đánh
  giá tổng hợp đo được PLO ở mức thành thạo; bẫy phổ biến là gán quá nhiều M để "đẹp" ma trận,
  đoàn kiểm định sẽ đối chiếu với đề cương và rubric đánh giá.
- → Kết quả bước: ma trận CLO–PLO hoàn chỉnh (hàng: học phần; cột: PLO; ô: I/R/M hoặc trống).

**Bước 4. Kiểm tra độ phủ từng PLO**
- Làm gì: áp dụng `nguong_kiem_tra` (mặc định: mỗi PLO có ít nhất 01 học phần ở mức M): đếm
  số học phần ở mỗi mức I/R/M cho từng PLO; lập bảng kiểm tra độ phủ; đánh dấu "Đạt" hoặc
  "Chưa đạt" kèm ghi chú (vd: PLO chỉ có mức I mà không có R/M là điểm yếu).
- Dùng input: `nguong_kiem_tra`, kết quả Bước 3 (ma trận đã đánh dấu).
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: tính bảng độ phủ PLO, kiểm tra kết luận đạt/chưa đạt · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: kiểm tra cả chiều ngược — không chỉ PLO thiếu M mà còn phát hiện PLO
  "quá tải" (quá nhiều học phần mức M cho một PLO đơn giản) gây lãng phí nguồn lực; ghi rõ
  học phần nào đang gánh mức M cho từng PLO.
- → Kết quả bước: bảng kiểm tra độ phủ từng PLO (số HP ở mỗi mức I/R/M, kết luận đạt/chưa đạt).

**Bước 5. Rà soát học phần "thừa" và PLO "thiếu"**
- Làm gì: từ ma trận Bước 3 và bảng phủ Bước 4, liệt kê học phần "thừa" (hàng trống toàn bộ —
  không đóng góp vào PLO nào) để xem xét loại bỏ hoặc điều chỉnh CLO; liệt kê PLO "thiếu"
  (chưa đạt ngưỡng kiểm tra) để đề xuất bổ sung/điều chỉnh học phần; với mỗi trường hợp ghi
  rõ nguyên nhân và phương án xử lý đề xuất.
- Dùng input: kết quả Bước 3, kết quả Bước 4.
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: liệt kê sơ bộ học phần thừa/PLO thiếu, đề xuất phương án xử lý · ⏱ ~30 phút (ước tính)
- Lưu ý nghiệp vụ: học phần "thừa" chưa chắc phải loại bỏ ngay — có thể do CLO viết chưa
  gắn đúng PLO, cần kiểm tra đề cương trước khi kết luận; PLO "thiếu" mức M là lỗi nghiêm
  trọng khi kiểm định, phải có phương án khắc phục cụ thể (bổ sung học phần hay nâng mức
  đánh giá của học phần hiện có).
- → Kết quả bước: danh sách học phần thừa và PLO thiếu kèm nguyên nhân và phương án xử lý
  đề xuất.

**Bước 6. Tổng hợp nhận xét và kiến nghị**
- Làm gì: viết nhận xét đánh giá tổng thể mức độ liên kết giữa học phần và PLO (điểm mạnh,
  điểm yếu); tổng hợp các kiến nghị điều chỉnh cụ thể từ Bước 5 (học phần nào cần sửa CLO,
  PLO nào cần bổ sung mức M, thời hạn thực hiện); trình Hội đồng rà soát CTĐT phê duyệt.
- Dùng input: kết quả Bước 4, kết quả Bước 5, `ten_nganh`.
- Vai trò: Hội đồng rà soát CTĐT phê duyệt; chuyên viên Phòng Đào tạo soạn dự thảo và kiểm tra · AI hỗ trợ: soạn dự thảo nhận xét và kiến nghị · ⏱ ~45 phút (ước tính)
- Lưu ý nghiệp vụ: kiến nghị phải cụ thể đến từng học phần và có thời hạn (không viết chung
  chung "cần rà soát lại"); nhận xét phải công bằng — nêu cả điểm mạnh của ma trận, không
  chỉ liệt kê lỗi.
- → Kết quả bước: bản nhận xét đánh giá và kiến nghị điều chỉnh, sẵn sàng trình Hội đồng
  rà soát CTĐT.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Input: PLO của CTĐT, CLO từng học phần"/] --> B1["Bước 1: Liệt kê PLO của chương trình đào tạo"]
    B1 --> B2["Bước 2: Liệt kê CLO của từng học phần"]
    B2 --> B3["Bước 3: Đánh dấu mức đóng góp I – R – M"]
    B3 --> B4["Bước 4: Kiểm tra độ phủ từng PLO"]
    B4 --> B5["Bước 5: Rà soát học phần "thừa" và PLO "thiếu""]
    B5 --> B6["Bước 6: Tổng hợp nhận xét và kiến nghị"]
    B6 --> HG["👤 Hội đồng rà soát CTĐT phê duyệt"]
    HG --> OUT[["Output: Ma trận CLO-PLO + Nhận xét"]]
```

## Đầu ra
- Ma trận CLO–PLO hoàn chỉnh dạng bảng (hàng: học phần; cột: PLO; ô: I/R/M).
- Bảng kiểm tra độ phủ từng PLO (số học phần ở mỗi mức I/R/M).
- Nhận xét đánh giá + kiến nghị điều chỉnh.

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao
Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Đủ các phần và đúng bố cục theo cấu trúc tại references/quy-cach-dau-ra.md (không theo cấu trúc của bản gốc).
- [ ] Danh sách PLO khớp bản đang có hiệu lực trong khung CTĐT (đủ số lượng, đúng nội dung, đúng thứ tự đánh số).
- [ ] CLO lấy từ đề cương chi tiết đã được khoa thông qua (không dùng bản nháp); học phần chưa có CLO được ghi chú bổ sung.
- [ ] Mức M chỉ gán khi học phần có hình thức đánh giá tổng hợp đo được PLO ở mức thành thạo; không gán M tùy tiện để "đẹp" ma trận.
- [ ] Mỗi PLO có ít nhất 01 học phần ở mức M theo ngưỡng kiểm tra đã chọn; học phần "thừa"/PLO "thiếu" được liệt kê đầy đủ kèm nguyên nhân và phương án xử lý.
- [ ] Kiến nghị cụ thể đến từng học phần, có thời hạn thực hiện; nhận xét nêu cả điểm mạnh, không chỉ liệt kê lỗi.
- [ ] Không bịa đặt CLO, mức đánh giá hay trích dẫn văn bản.
- [ ] Đã qua Human gate: Hội đồng rà soát CTĐT đã phê duyệt.

## Căn cứ & lưu ý
- Căn cứ hiện hành: xem [căn cứ và điều kiện áp dụng](references/phap-ly.md); phải đối chiếu văn bản gốc, hiệu lực và chuyển tiếp tại ngày nghiệp vụ.
- Ma trận CLO–PLO là minh chứng bắt buộc trong hồ sơ tự đánh giá và kiểm định CTĐT.
- Ký hiệu I/R/M là quy ước phổ biến; nếu trường dùng quy ước khác cần chú thích rõ trong ma trận.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Tư liệu đối chiếu
Bản gốc trước cập nhật pháp lý (kèm ví dụ giả lập) lưu tại `references/quy-trinh-lich-su.md`, chỉ để đối chiếu hồ sơ lịch sử; không dùng căn cứ, mẫu hay số liệu trong đó làm chỉ dẫn hiện hành.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
