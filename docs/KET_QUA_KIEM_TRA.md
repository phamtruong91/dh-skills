# Kết quả kiểm tra 1.3.2

Ngày: 2026-10-10. Thay thế bản 1.1.0.

## Kiểm tra tĩnh (`scripts/validate_skills.py`)

- 171/171 skill đạt; manifest, `version.json` và `SKILL.md` khớp nhau ở phiên bản 1.3.2.
- Kiểm tra mới: không còn bước kết quả "checklist đã đánh dấu"; không nhắc "markdown" ở skill không xuất `.md`; mỗi skill có `references/quy-tac-chung.md`; SKILL.md không quá 25 KB; 7 cặp skill dễ nhầm nêu tên nhau; căn cứ thanh tra không dùng NĐ 43/2023 mà thiếu NĐ 216/2025; tài liệu pháp lý không dính chữ.
- Thử hỏng có chủ đích trên bản sao: validator bắt 4/5 lỗi cố ý (lỗi còn lại là phép thử sai vì skill đó được phép xuất `.md`) và chấp nhận đúng khi gán `approval_owner`.

## Chạy thử bằng dữ liệu giả (`scripts/check_outputs.py`)

| Skill | File | Kết quả kiểm tra tự động | Phát hiện nghiệp vụ |
| --- | --- | --- | --- |
| `soan-cong-van` | `.docx`, 1 trang | Đạt | 4 |
| `ke-hoach-thanh-tra-nam` | `.docx`, 2 trang | Đạt | 6 |
| `pmo-quan-tri-du-an` | `.xlsx`, 4 sheet | Đạt (công thức tính lại bằng LibreOffice) | 7 |

Mỗi file được mở bằng thư viện thật, dựng trang bằng LibreOffice và xem lại bằng mắt. Chi tiết: `tests/results/*.findings.md`.

Thử hỏng có chủ đích: bộ kiểm tra đầu ra bắt được file đổi đuôi giả, nhãn "CHỜ KÝ", chữ "Checklist", số và ngày bịa, và việc điền % tiến độ khi thiếu minh chứng. Phép thử này làm lộ một lỗi của bộ kiểm tra (sập khi gặp file giả); đã sửa.

## Lỗi của skill do chạy thử phát hiện (đã sửa)

- `ke-hoach-thanh-tra-nam`: bắt "loại trừ trùng lịch thi/tuyển sinh" nhưng cuộc thanh tra thi, tuyển sinh phải diễn ra đúng lúc đó; cho phép tự đổi thời gian đã nhập.
- `pmo-quan-tri-du-an`: không có ngưỡng phân loại trạng thái; không đối chiếu tổng ngân sách.

## Còn tồn tại

- Chỉ 3/171 skill được chạy thử, và do cùng một AI vừa làm theo skill vừa viết kỳ vọng nên chưa phải kiểm tra độc lập.
- Mâu thuẫn chưa giải quyết: `ke-hoach-thanh-tra-nam` nêu "đơn vị lập" ở phần đầu trong khi quy tắc chung yêu cầu cơ quan ban hành là trường. Cần chủ skill quyết định.
- Phương pháp thanh tra mặc định theo lĩnh vực chưa được skill định nghĩa.
- Căn cứ thanh tra mới dựa trên nguồn thứ cấp; chưa đối chiếu Công báo. Các văn bản 2026 khác trong `docs/CAP_NHAT_PHAP_LY.md` không được mở lại trong lần rà soát này.
- Chưa có người phê duyệt nghiệp vụ hoặc pháp chế của trường.
