---
name: "ke-hoach-to-chuc-thi"
description: "Lập kế hoạch tổ chức kỳ thi kết thúc học phần / thi tốt nghiệp của trường đại học: lịch thi, phân công nhiệm vụ, chuẩn bị đề thi – phòng thi, chấm thi và công bố kết quả. Dùng khi chuẩn bị mỗi kỳ thi trong năm học."
---

# Kế hoạch tổ chức kỳ thi

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
Khi cần lập kế hoạch tổng thể cho một kỳ thi: thi kết thúc học phần, thi tốt nghiệp,
thi tuyển sinh sau đại học.

## Đầu vào (Input)
| Trường | Mô tả | Bắt buộc |
|---|---|---|
| `ky_thi` | Tên kỳ thi (VD: thi kết thúc học phần học kỳ 1 năm học 2026–2027) | Có |
| `thoi_gian` | Thời gian diễn ra (từ ngày – đến ngày) | Có |
| `so_luong_thi_sinh` | Số lượng thí sinh dự kiến | Có |
| `danh_muc_mon_thi` | Danh sách học phần thi (mã HP, tên HP, hình thức thi) | Có |
| `don_vi_phoi_hop` | Các phòng/khoa tham gia (Đào tạo, Khảo thí, Thanh tra, Quản trị...) | Không |
| `nguoi_ky` | Hiệu trưởng / Phó Hiệu trưởng phụ trách đào tạo | Có |

## Quy trình
**Ràng buộc pháp lý khi thực hiện** (trích references/phap-ly.md; đối chiếu toàn văn và hiệu lực tại ngày nghiệp vụ):
- Thông tư 56/2026/TT-BGDĐT, hiệu lực 07/07/2026: Yêu cầu khóa tuyển sinh, chương trình, ngày áp dụng và quy chế đào tạo nội bộ. Đối chiếu điều khoản chuyển tiếp trong toàn văn trước khi chọn quy tắc; không tự áp dụng quy định mới hồi tố cho mọi khóa. Không dùng điều/khoản, thang điểm hoặc điều kiện tốt nghiệp cũ như quy định hiện hành nếu chưa đối chiếu.
- Trước Bước 1: chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. Thiếu văn bản gốc hoặc điều khoản thì ghi nhận nội bộ [CẦN XÁC MINH] (không đưa vào file giao), để trống phần tương ứng, chưa kết luận tuân thủ.
- Các con số, thời hạn, số điều, số mức xếp loại, hệ số và mẫu biểu nêu trong các bước dưới đây được giữ từ quy trình gốc (trước cập nhật pháp lý); chỉ dùng khi đã đối chiếu đúng với căn cứ đã chọn, khác thì theo căn cứ. Danh sách điểm cần đối chiếu: docs/DIEM_CAN_DOI_CHIEU_PHAP_LY.md.

**Bước 1. Xác định quy mô kỳ thi**
- Làm gì: Thu thập từ Phòng Đào tạo: danh sách sinh viên đủ điều kiện dự thi theo từng học phần, danh mục học phần thi (mã HP, tên HP, hình thức thi), khung thời gian học vụ; từ Phòng Khảo thí & ĐBCL: số phòng thi khả dụng, số cán bộ có thể huy động. Tổng hợp thành bảng quy mô: tổng số thí sinh, số học phần, số ca thi ước tính, số phòng thi cần dùng, số lượt cán bộ coi/chấm thi cần huy động.
- Dùng input: `ky_thi`, `thoi_gian`, `so_luong_thi_sinh`, `danh_muc_mon_thi`, `don_vi_phoi_hop`.
- Vai trò: Chuyên viên Phòng Đào tạo & Phòng Khảo thí & ĐBCL · AI hỗ trợ: tổng hợp bảng quy mô sơ bộ từ số liệu các đơn vị, đối chiếu danh sách thí sinh · ⏱ ~2 giờ (ước tính)
- Lưu ý nghiệp vụ: kiểm tra các học phần có hình thức thi đặc thù (vấn đáp, thực hành, thi trên máy) để bố trí ca thi và phòng thi riêng; số thí sinh phải khớp giữa danh sách học vụ và danh sách đăng ký thi.
- → Kết quả bước: Bảng tổng hợp quy mô kỳ thi (số thí sinh, số học phần, số ca thi, nhu cầu phòng thi và nhân sự).

**Bước 2. Lập lịch thi chi tiết**
- Làm gì: Xếp từng học phần vào ca thi – ngày thi – phòng thi cụ thể: học phần đông sinh viên thi trước; không xếp 02 học phần có chung sinh viên trong cùng một ca bằng cách đối chiếu danh sách sinh viên đăng ký từng học phần; chốt lịch, trình lãnh đạo duyệt và công bố trên hệ thống học vụ/cổng thông tin trước ít nhất 07 ngày so với ngày thi đầu tiên.
- Dùng input: `thoi_gian`, `danh_muc_mon_thi`, `so_luong_thi_sinh`.
- Vai trò: Chuyên viên Phòng Đào tạo · AI hỗ trợ: xếp lịch sơ bộ theo quy tắc không trùng ca, rà soát trùng ca học phần của cùng sinh viên · ⏱ ~4 giờ (ước tính)
- Lưu ý nghiệp vụ: bẫy thường gặp — sinh viên học lại/học cải thiện đăng ký nhiều học phần rất dễ bị trùng ca; mọi thay đổi lịch sau công bố phải thông báo lại bằng văn bản đến sinh viên và các đơn vị.
- → Kết quả bước: Dự thảo lịch thi chi tiết (Phụ lục 01) đã rà soát không trùng lịch thí sinh.

**Bước 3. Phân công nhiệm vụ**
- Làm gì: Căn cứ số ca thi và số phòng thi, lập danh sách cán bộ coi thi (02 cán bộ/phòng/ca), cán bộ chấm thi theo từng học phần, cán bộ thanh tra độc lập, thư ký hội đồng; gửi văn bản đề nghị các khoa cử cán bộ; tổng hợp danh sách, kiểm tra không phân công cán bộ có người thân dự thi vào học phần đó; ban hành quyết định phân công kèm theo kế hoạch.
- Dùng input: `don_vi_phoi_hop`, `nguoi_ky`.
- Vai trò: Phòng Khảo thí & ĐBCL (tổng hợp, rà soát), Hiệu trưởng/Phó Hiệu trưởng ký ban hành · AI hỗ trợ: lập bảng phân công sơ bộ, kiểm tra xung đột lợi ích trong danh sách · ⏱ ~1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: cán bộ coi thi phải được phổ biến quy chế thi trước kỳ thi; tránh phân công 01 cán bộ coi 02 ca liên tiếp quá sức; cán bộ chấm thi phải đúng chuyên môn học phần.
- → Kết quả bước: Quyết định phân công nhiệm vụ + bảng phân công chi tiết (Phụ lục 02).

**Bước 4. Chuẩn bị đề thi**
- Làm gì: Rút đề từ ngân hàng đề thi theo đúng ma trận đề đã duyệt (tỷ lệ nhận biết/thông hiểu/vận dụng); in sao đủ số lượng theo số thí sinh từng ca (+ dự phòng 5%); niêm phong từng túi đề, lập biên bản niêm phong; bàn giao đề thi cho trưởng điểm thi/trưởng ca trước giờ thi có biên bản giao nhận; toàn bộ quá trình bảo mật tuyệt đối.
- Dùng input: `danh_muc_mon_thi`, `so_luong_thi_sinh`.
- Vai trò: Cán bộ khảo thí (Phòng Khảo thí & ĐBCL) · AI hỗ trợ: kiểm tra ma trận đề, thống kê số lượng in sao theo từng ca trước khi niêm phong · ⏱ ~2 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: đề dự phòng niêm phong riêng, chỉ mở khi có sự cố; mọi khâu in sao phải có người giám sát, không để đề thi ra khỏi khu vực bảo mật; kiểm tra số lượng đề theo từng ca trước khi niêm phong.
- → Kết quả bước: Bộ đề thi đã niêm phong + biên bản niêm phong/bàn giao đề thi.

**Bước 5. Chuẩn bị cơ sở vật chất**
- Làm gì: Khảo sát thực tế và chốt danh sách phòng thi đủ tiêu chuẩn (ánh sáng, bàn ghế, đồng hồ treo tường, khoảng cách chống quay cóp); chuẩn bị hệ thống âm thanh gọi giờ, tủ thuốc/y tế trực, phương án an ninh trật tự và điện dự phòng; dán sơ đồ phòng thi và danh sách thí sinh trước mỗi phòng trước ngày thi 01 ngày.
- Dùng input: `thoi_gian`, `don_vi_phoi_hop`.
- Vai trò: Cán bộ Phòng Quản trị – Thiết bị (phối hợp Phòng Khảo thí & ĐBCL) · AI hỗ trợ: tổng hợp checklist tiêu chuẩn phòng thi, lập danh sách phòng dự kiến từ cơ sở dữ liệu CSVC · ⏱ ~1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: kiểm tra thực tế từng phòng trước kỳ thi 02 ngày; phòng thi trắc nghiệm cần bố trí giãn cách chỗ ngồi; chuẩn bị phòng thi dự phòng cho trường hợp phát sinh.
- → Kết quả bước: Biên bản kiểm tra cơ sở vật chất + sơ đồ bố trí phòng thi.

**Bước 6. Tổ chức coi thi**
- Làm gì: Tổ chức họp phổ biến quy chế thi cho toàn bộ cán bộ coi thi trước ca thi đầu tiên; giám sát việc gọi thí sinh vào phòng, kiểm tra giấy tờ tùy thân, phát đề đúng giờ; xử lý vi phạm quy chế tại chỗ đúng thẩm quyền (khiển trách/cảnh cáo/đình chỉ) và lập biên bản vi phạm; tổng hợp tình hình từng ca thi báo cáo ban chỉ đạo kỳ thi.
- Dùng input: `ky_thi`, `don_vi_phoi_hop`.
- Vai trò: Cán bộ coi thi · AI hỗ trợ: chuẩn bị tài liệu phổ biến quy chế trước ca thi, tổng hợp tình hình từng ca sau khi thi · ⏱ theo lịch thi (ước tính)
- Lưu ý nghiệp vụ: cán bộ coi thi không được mang thiết bị điện tử vào phòng thi; mọi trường hợp đình chỉ thi phải báo ngay trưởng ban chỉ đạo; biên bản vi phạm phải có chữ ký xác nhận của thí sinh.
- → Kết quả bước: Biên bản phòng thi từng ca + báo cáo nhanh tình hình coi thi.

**Bước 7. Chấm thi – nhập điểm – phúc khảo**
- Làm gì: Thu bài thi về kho tập trung, rọc phách trước khi chấm; tổ chức chấm tập trung tại Phòng Khảo thí (bài tự luận chấm 02 vòng độc lập, chênh lệch điểm xử lý theo quy chế); nhập điểm vào hệ thống quản lý học vụ, đối chiếu số bài/số điểm, kiểm tra ngẫu nhiên 10% số bài sau nhập; công bố điểm; tiếp nhận đơn phúc khảo trong thời hạn quy định, tổ chức chấm phúc khảo và ban hành quyết định công nhận kết quả.
- Dùng input: `danh_muc_mon_thi`, `so_luong_thi_sinh`.
- Vai trò: Hội đồng chấm thi / Cán bộ chấm thi · AI hỗ trợ: nhập điểm vào hệ thống, đối chiếu số bài/số điểm, cảnh báo điểm bất thường · ⏱ ~5–7 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: người chấm vòng 2 không được biết điểm vòng 1; kiểm tra điểm bất thường (điểm liệt hàng loạt, điểm cao bất thường) trước khi công bố.
- → Kết quả bước: Bảng điểm chính thức + quyết định công nhận kết quả phúc khảo (nếu có).

**Bước 8. Lưu trữ – báo cáo**
- Làm gì: Đóng gói, niêm phong bài thi theo từng học phần; lưu trữ bài thi và bảng điểm gốc theo thời hạn quy định của trường; lập báo cáo tổng kết kỳ thi (quy mô, kỷ luật thi, kết quả, tồn tại, kiến nghị); trình lãnh đạo ký duyệt và lưu hồ sơ kỳ thi.
- Dùng input: `ky_thi`, `nguoi_ky`.
- Vai trò: Phòng Khảo thí & ĐBCL (lập báo cáo), Lãnh đạo trường ký duyệt · AI hỗ trợ: soạn dự thảo báo cáo tổng kết từ số liệu kỳ thi · ⏱ ~1 ngày làm việc (ước tính)
- Lưu ý nghiệp vụ: báo cáo tổng kết kỳ thi là minh chứng kiểm định cho tiêu chí về công tác khảo thí — phải lưu đầy đủ, mã hóa theo quy tắc của trường.
- → Kết quả bước: Hồ sơ kỳ thi đã lưu trữ + báo cáo tổng kết kỳ thi.

## Luồng quy trình (Workflow)
```mermaid
flowchart TD
    IN[/"Input: quy mô kỳ thi, danh mục học phần, thời gian"/]
    A["Bước 1. Xác định quy mô kỳ thi"]
    B["Bước 2. Lập lịch thi chi tiết"]
    C{"Lịch thi có trùng không?"}
    D["Bước 3. Phân công nhiệm vụ"]
    HG["👤 Lãnh đạo duyệt lịch và phân công"]
    E["Bước 4. Chuẩn bị đề thi"]
    F["Bước 5. Chuẩn bị cơ sở vật chất"]
    G["Bước 6. Tổ chức coi thi"]
    H["Bước 7. Chấm thi, nhập điểm, phúc khảo"]
    I["Bước 8. Lưu trữ, báo cáo"]
    OUT[/"Output: Kế hoạch tổ chức kỳ thi"/]
    IN --> A --> B --> C
    C -->|Có| B
    C -->|Không| D --> HG --> E --> F --> G --> H --> I --> OUT
```

## Đầu ra
- Văn bản kế hoạch tổ chức kỳ thi hoàn chỉnh.
- Phụ lục: lịch thi chi tiết + bảng phân công nhiệm vụ.

File nghiệp vụ thực tế theo định dạng mặc định ở đầu skill hoặc định dạng người dùng yêu cầu, kèm liên kết tải trong phản hồi cuối.

Sản phẩm nghiệp vụ hoàn chỉnh theo [quy cách và cấu trúc](references/quy-cach-dau-ra.md), giữ các trường chưa có dữ liệu ở trạng thái trống. Không xuất kèm checklist/phụ lục kiểm tra đầu ra.

## Kiểm tra nội bộ trước khi giao
Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, không đánh dấu đã đạt hoặc đã duyệt.

- [ ] Đủ các phần và đúng bố cục theo cấu trúc tại references/quy-cach-dau-ra.md (không theo cấu trúc của bản gốc).
- [ ] Số liệu trong kế hoạch khớp với Input: tổng số thí sinh, số học phần, khung thời gian (`ky_thi`, `thoi_gian`, `so_luong_thi_sinh`, `danh_muc_mon_thi`).
- [ ] Không bịa đặt số liệu thí sinh, học phần, phòng thi, nhân sự coi/chấm thi.
- [ ] Đúng thể thức văn bản hành chính theo Nghị định 30/2020/NĐ-CP.
- [ ] Căn cứ pháp lý (văn bản hiện hành nêu tại phap-ly.md, quy chế thi của trường) đầy đủ, còn hiệu lực.
- [ ] Đã qua Human gate: người có thẩm quyền theo quy trình đã duyệt.
- [ ] Lịch thi không trùng ca đối với sinh viên đăng ký nhiều học phần (kể cả học lại/học cải thiện); công bố trước ít nhất 07 ngày so với ngày thi đầu tiên.
- [ ] Cán bộ chấm thi đúng chuyên môn học phần; không phân công cán bộ có người thân dự thi vào học phần đó.
- [ ] Đề thi rút đúng ma trận đề đã duyệt, in sao đủ số lượng (+ dự phòng 5%), niêm phong từng túi đề, có biên bản niêm phong/bàn giao.

## Căn cứ & lưu ý
- Căn cứ hiện hành: xem [căn cứ và điều kiện áp dụng](references/phap-ly.md); phải đối chiếu văn bản gốc, hiệu lực và chuyển tiếp tại ngày nghiệp vụ.
- Quy chế thi kết thúc học phần của Trường Đại học A (giả lập).
- Lịch thi phải công bố sớm để sinh viên chủ động ôn tập; mọi thay đổi lịch thi phải thông báo lại.
- Không dùng tên thật của trường/cá nhân khi mô phỏng.

## Tư liệu đối chiếu
Bản gốc trước cập nhật pháp lý (kèm ví dụ giả lập) lưu tại `references/quy-trinh-lich-su.md`, chỉ để đối chiếu hồ sơ lịch sử; không dùng căn cứ, mẫu hay số liệu trong đó làm chỉ dẫn hiện hành.

## Quản trị phiên bản
- Phiên bản gói `1.3.2` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).
- Người phê duyệt nghiệp vụ: **chưa chỉ định**. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.
- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md.
