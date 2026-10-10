---
name: "ke-hoach-to-chuc-su-kien"
description: "Kế hoạch tổ chức sự kiện trong trường đại học: timeline ngược, checklist theo giai đoạn, phân công RACI, kịch bản run-of-show chi tiết, dự toán và mẫu báo cáo sau sự kiện. Dùng chung cho mọi đơn vị."
---

# Kế hoạch tổ chức sự kiện

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
Khi tổ chức hội nghị, hội thảo, lễ khai giảng/bế giảng, ngày hội việc làm, lễ kỷ niệm...
Dùng chung cho mọi phòng/khoa/trung tâm — không phụ thuộc tên đơn vị.

## Đầu vào (Input)

| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ten_su_kien` | Tên sự kiện | Có |
| `muc_tieu` | Mục tiêu, kết quả mong đợi | Có |
| `quy_mo` | Số lượng khách/dại biểu dự kiến, đối tượng | Có |
| `thoi_gian` | Ngày giờ tổ chức | Có |
| `dia_diem` | Địa điểm dự kiến | Có |
| `ngan_sach` | Ngân sách dự kiến (nếu có) | Không |
| `don_vi_phoi_hop` | Các đơn vị/cá nhân phối hợp | Không |

## Quy trình

**Bước 1. Lập timeline ngược**
- Làm gì: lấy `thoi_gian` làm ngày T, lùi lại các mốc T-30, T-14, T-7, T-3, T-1; mỗi mốc
  ghi rõ việc phải hoàn thành; kiểm tra các mốc có rơi vào cuối tuần/ngày lễ không
  để điều chỉnh sớm.
- Dùng input: `thoi_gian`, `ten_su_kien`, `quy_mo`
- Vai trò: Trưởng ban tổ chức · AI hỗ trợ: lập timeline ngược từ ngày T, kiểm tra cuối tuần/ngày lễ · ⏱ ~10–15 phút (ước tính)
- Lưu ý nghiệp vụ: việc phụ thuộc lẫn nhau phải xếp đúng thứ tự (VD chốt danh sách
  doanh nghiệp trước khi in backdrop có logo); mốc T-1 chỉ dành cho kiểm tra lần cuối,
  không xếp việc mới.
- → Kết quả bước: "timeline ngược" (mốc thời gian + việc phải xong ở mỗi mốc).

**Bước 2. Lập checklist theo giai đoạn**
- Làm gì: chi tiết hóa timeline thành checklist theo 6 giai đoạn: chuẩn bị → truyền thông
  → hậu cần → đón tiếp → diễn ra → tổng kết; mỗi đầu việc ghi đầu mối thực hiện
  và deadline cụ thể.
- Dùng input: kết quả bước 1 (timeline ngược), `don_vi_phoi_hop`, `dia_diem`
- Vai trò: Đơn vị chủ trì sự kiện (Ban tổ chức) · AI hỗ trợ: chi tiết hóa checklist 6 giai đoạn, gán đầu mối và deadline · ⏱ ~20–30 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi đầu việc phải có đúng một đầu mối (tránh "cả làng cùng làm,
  không ai chịu"); deadline của checklist phải khớp với mốc timeline ở bước 1.
- → Kết quả bước: "checklist công việc theo giai đoạn" (việc + đầu mối + deadline).

**Bước 3. Phân công RACI**
- Làm gì: với từng đầu việc trong checklist (bước 2), xác định R (người thực hiện),
  A (người chịu trách nhiệm cuối), C (tham vấn), I (được thông báo).
- Dùng input: kết quả bước 2 (checklist), `don_vi_phoi_hop`
- Vai trò: Trưởng ban tổ chức (chốt người chịu trách nhiệm cuối — A) · AI hỗ trợ: gợi ý phân công RACI · ⏱ ~20–30 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi đầu việc chỉ có đúng một A; A nên là trưởng ban tổ chức hoặc
  người có thẩm quyền quyết; không để đầu việc nào thiếu A.
- → Kết quả bước: "bảng phân công RACI".

**Bước 4. Dựng kịch bản run-of-show**
- Làm gì: chi tiết từng khung giờ trong ngày diễn ra: nội dung, người điều hành/MC,
  yêu cầu âm thanh–ánh sáng, ghi chú rủi ro và phương án dự phòng.
- Dùng input: `thoi_gian`, `dia_diem`, `quy_mo`, kết quả bước 2–3
- Vai trò: Đơn vị chủ trì sự kiện (Ban tổ chức) · AI hỗ trợ: dựng kịch bản run-of-show từng khung giờ, ghi rủi ro và phương án dự phòng · ⏱ ~20–30 phút (ước tính)
- Lưu ý nghiệp vụ: mỗi khung giờ phải có người điều hành cụ thể; ghi rõ thiết bị dự
  phòng (mic, máy chiếu) cho các tiết mục quan trọng; tính thời gian chuyển cảnh
  và dự phòng trễ giờ.
- → Kết quả bước: "kịch bản run-of-show chi tiết" (giờ + nội dung + điều hành +
  ghi chú rủi ro).

**Bước 5. Lập dự toán**
- Làm gì: từ checklist (bước 2) và kịch bản (bước 4), liệt kê từng hạng mục chi phí
  (số lượng × đơn giá ước tính) + khoản dự phòng; tổng hợp và đối chiếu với `ngan_sach`
  (nếu có).
- Dùng input: `ngan_sach`, kết quả bước 2, 4
- Vai trò: Đơn vị chủ trì sự kiện (lấy báo giá thực tế, đối chiếu ngân sách) · AI hỗ trợ: lập bảng dự toán ước tính từ checklist và kịch bản · ⏱ ~30 phút–1 giờ (ước tính)
- Lưu ý nghiệp vụ: mọi số liệu chỉ là ước tính — đơn vị phải lấy báo giá thực tế;
  không cam kết chi vượt thẩm quyền; khoản dự phòng thường để 10–15% tổng.
- → Kết quả bước: "bảng dự toán kinh phí" (hạng mục + số tiền + tổng).

**Bước 6. Soạn mẫu báo cáo sau sự kiện**
- Làm gì: soạn mẫu báo cáo gồm: số lượng tham dự thực tế, kết quả so với `muc_tieu`,
  vấn đề phát sinh, bài học kinh nghiệm; để trống các ô để điền sau khi sự kiện diễn ra.
- Dùng input: `muc_tieu`, `quy_mo`, kết quả bước 1–5
- Vai trò: Đơn vị chủ trì sự kiện (Ban tổ chức) · AI hỗ trợ: soạn mẫu báo cáo sau sự kiện, gắn trường đối chiếu mục tiêu · ⏱ ~10–15 phút (ước tính)
- Lưu ý nghiệp vụ: mẫu phải có trường đối chiếu kết quả với mục tiêu ban đầu để đánh giá
  hiệu quả; mục bài học kinh nghiệm là bắt buộc để cải tiến lần tổ chức sau.
- → Kết quả bước: "mẫu báo cáo tổng kết sau sự kiện" → cùng các sản phẩm trước tạo
  Output cuối.
## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    A[/"Mục tiêu, quy mô, ngân sách sự kiện"/]
    B["Bước 1. Lập timeline ngược T-30 đến T-1"]
    C["Bước 2. Lập checklist theo giai đoạn"]
    D["Bước 3. Phân công RACI từng đầu việc"]
    E["Bước 4. Dựng kịch bản run-of-show từng khung giờ"]
    F["Bước 5. Lập dự toán theo checklist"]
    K["Bước 6. Soạn mẫu báo cáo sau sự kiện"]
    HG["👤 Trưởng ban tổ chức duyệt kế hoạch/dự toán/kịch bản"]
    H[["Kế hoạch + kịch bản + dự toán + mẫu báo cáo"]]
    A --> B --> C --> D --> E --> F --> K --> HG --> H
```

## Đầu ra

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao

- [ ] Bố cục khớp mẫu áp dụng và cấu trúc tại references/quy-cach-dau-ra.md.
- [ ] Timeline ngược tính từ `thoi_gian`; các mốc không rơi vào cuối tuần/ngày lễ (hoặc đã điều chỉnh); việc phụ thuộc nhau xếp đúng thứ tự; mốc T-1 chỉ dành cho kiểm tra lần cuối.
- [ ] Checklist: mỗi đầu việc có đúng một đầu mối và deadline cụ thể; deadline khớp với mốc timeline.
- [ ] RACI: mỗi đầu việc có đúng một A (người chịu trách nhiệm cuối), không đầu việc nào thiếu A.
- [ ] Run-of-show: mỗi khung giờ có nội dung, người điều hành/MC, yêu cầu âm thanh–ánh sáng, ghi chú rủi ro và phương án dự phòng; đã tính thời gian chuyển cảnh và dự phòng trễ giờ.
- [ ] Dự toán liệt kê từng hạng mục (số lượng × đơn giá ước tính) + khoản dự phòng 10–15%; tổng đã đối chiếu với `ngan_sach`.
- [ ] Mẫu báo cáo sau sự kiện có trường đối chiếu kết quả với mục tiêu ban đầu và mục bài học kinh nghiệm bắt buộc.
- [ ] Mọi số liệu dự toán là ước tính — đơn vị đã lấy báo giá thực tế; không cam kết chi vượt thẩm quyền.
- [ ] Đã qua Human gate: trưởng ban tổ chức duyệt kế hoạch, dự toán, kịch bản trước khi triển khai.

> Tiêu chí đạt: tất cả các ô được đánh dấu.

## Human gate (người kiểm duyệt)
- **Trưởng ban tổ chức / thủ trưởng đơn vị chủ trì** duyệt kế hoạch, dự toán, kịch bản
  trước khi triển khai.
- Ban Giám hiệu duyệt đối với sự kiện cấp trường hoặc có khách mời cấp cao.

## Giới hạn (guardrails)
- Không tự đặt dịch vụ (địa điểm, catering, âm thanh...) hay ký hợp đồng thay.
- Không tự gửi thư mời, thông báo cho khách mời/đại biểu.
- Không cam kết ngân sách vượt thẩm quyền của đơn vị.
- Mọi số liệu dự toán là ước tính — đơn vị phải lấy báo giá thực tế.

## Căn cứ & lưu ý
- Theo quy chế tổ chức sự kiện và quy chế chi tiêu nội bộ của trường.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Quản trị phiên bản

- Phiên bản gói: `1.3.1`; ngày cập nhật: `2026-10-10`.
- Kho nguồn: https://github.com/phamtruong91/university-skills-framework
- Người duy trì trên GitHub: `phamtruong91` (Phạm Văn Trường). Người phê duyệt nghiệp vụ: **chưa chỉ định**.
- Commit nguồn trước cập nhật: `346719e6b0318ed034b4b016703f79733aa575e7`. Commit chứa phiên bản này xem bằng `git log -1 -- skills/ke-hoach-to-chuc-su-kien`; không tự gán SHA chưa tạo.
- Giấy phép: theo LICENSE của kho; bản quyền CES Global.
- Lịch sử 1.1.0: bổ sung metadata giao diện, kiểm soát áp dụng, quản trị phiên bản.
- Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
