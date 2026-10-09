# University AI Skills Framework

**Khung Skill AI cho phòng ban trường đại học** — bộ **khung mẫu chuẩn** gồm **171 skill AI** bao phủ nghiệp vụ của các phòng ban trong trường đại học Việt Nam — áp dụng chung cho mọi trường, không phụ thuộc mô hình tổ chức cụ thể.

Mỗi skill là một **quy trình nghiệp vụ thực thi được**: có Input đầy đủ và làm đúng các bước thì cho ra Output theo khung chuẩn. Vai trò chính trong mỗi bước là **nhân sự** (chức danh/đơn vị cụ thể); AI đóng vai trò hỗ trợ.

## Cấu trúc repo

```
.
├── README.md                        # Tài liệu này
├── khung-skill-tong-the.md          # Chuẩn skill tổng thể: kiến trúc 2 tầng, cấu trúc 10 mục,
│                                    # mô hình thực thi, quy ước dữ liệu demo
├── khung-phong-ban-chuan.md         # Khung phòng ban chuẩn (mã A1–A4, B1–B13, C1–C9, D1–D2)
│                                    # + bảng mapping biến thể tổ chức các trường
├── danh-muc-skill-phong-ban-dh.md   # Danh mục skill theo phòng ban (bản tổng hợp ban đầu)
├── so-do-case-phong-ban.html        # Sơ đồ use case tương tác giữa các phòng ban
├── docs/
│   └── Khung_Skill_AI_phong_ban_truong_dai_hoc.docx   # File Word giới thiệu chi tiết
│                                                      # (kèm Bộ tài liệu CES Agent Workspace)
└── skills/
    ├── README.md                    # Chỉ mục toàn bộ 171 skill
    └── <ma-skill>/
        └── SKILL.md                 # 1 skill = 1 file độc lập
```

## Kiến trúc 2 tầng

| Tầng | Số lượng | Nội dung |
|------|----------|----------|
| Tầng 1 — Skill lõi dùng chung | 18 | Rà soát văn bản, kiểm tra hồ sơ, hợp nhất báo cáo, tóm tắt trình lãnh đạo, FAQ chính sách, dịch thuật, quản lý phiên bản, helpdesk CNTT... |
| Tầng 2 — Skill nghiệp vụ theo phòng ban | 153 | Bao phủ vòng đời nghiệp vụ của từng phòng/ban: lập kế hoạch → soạn thảo → tổ chức thực hiện → kiểm tra/giám sát → báo cáo/tổng kết |

## Chuẩn cấu trúc một skill (10 mục)

1. Thông tin định danh (mã skill, mô tả)
2. Khi nào dùng
3. Đầu vào (Input) — bảng Trường / Mô tả / Bắt buộc
4. Quy trình — từng bước chi tiết: **làm gì** · dùng input nào · **vai trò nhân sự + cách AI hỗ trợ** · thời gian ước tính · lưu ý nghiệp vụ · **→ kết quả bước**
5. Luồng quy trình (Workflow) — sơ đồ Mermaid: các bước, điểm rẽ nhánh, Human gate
6. Đầu ra (Output) + **Cấu trúc output chuẩn** (khung cố định)
7. Checklist nghiệm thu (6–10 tiêu chí)
8. Ví dụ mô phỏng — Input mẫu + Output mẫu (dữ liệu giả lập)
9. Human gate / Giới hạn (theo từng skill)
10. Căn cứ & lưu ý (căn cứ pháp lý)

## Quy ước dữ liệu demo

Tất cả ví dụ trong bộ skill dùng dữ liệu **giả lập, chuẩn theo mẫu** (dạng ABC), không liên quan tổ chức/cá nhân có thật:

- Trường: **Trường Đại học A** (viết tắt ĐHA trong số ký hiệu văn bản)
- Người / tổ chức khác: **Nguyễn Văn A**, **Học viện B**, **Công ty TNHH D**...
- Địa chỉ: **Số 123, đường B, thành phố C** (đúng chuẩn định dạng)
- Liên hệ: SĐT `0900 000 001`, email `...@dha.edu.vn`
- Tên phòng ban: giữ nguyên theo Khung phòng ban chuẩn

## Khung phòng ban chuẩn

Mã hóa 4 khối: **A** (Lãnh đạo & hội đồng) · **B** (13 phòng/ban chức năng) · **C** (đơn vị trực thuộc, sự nghiệp, dịch vụ) · **D** (đơn vị đào tạo). Khung bao phủ cả mô hình tách chuyên sâu và mô hình gộp tinh gọn, kèm bảng mapping biến thể (hệ "Ban" của Bách khoa, các mô hình gộp của Luật/Dược/Thủy lợi, Học viện Ngân hàng...). Chi tiết tại `khung-phong-ban-chuan.md`.

## Cơ sở xây dựng

- Khảo sát cơ cấu tổ chức, chức năng nhiệm vụ nhiều trường ĐH Việt Nam (VNUIS, ĐH Luật Hà Nội, ĐH Dược Hà Nội, ĐH Thủy lợi, ĐH Bách khoa Hà Nội, Học viện Ngân hàng...)
- Đối chiếu khung phân rã nhiệm vụ AI tham khảo của Trường Quốc tế – ĐHQGHN
- Căn cứ pháp lý: Luật Giáo dục đại học, Nghị định 30/2020/NĐ-CP (công tác văn thư), Thông tư 08/2021/TT-BGDĐT (quy chế đào tạo), các thông tư về kiểm định chất lượng và quản lý tài chính đơn vị sự nghiệp công lập

## Sử dụng

Mỗi thư mục `skills/<ma-skill>/SKILL.md` là một skill độc lập, đọc trực tiếp được. Xem chỉ mục tại [`skills/README.md`](skills/README.md).

## Giấy phép

**Dual license** — xem file `LICENSE`:
- **Cộng đồng**: CC BY-SA 4.0 — mọi người được tự do dùng, sửa, chia sẻ (kể cả thương mại);
  mọi bản cải tiến/phái sinh phải được chia sẻ lại dưới cùng giấy phép.
- **Thương mại**: CES Global (chủ sở hữu bản quyền) được phân phối nội dung dưới điều khoản
  thương mại riêng, bao gồm đóng gói vào nền tảng CES Agent Workspace cho thuê theo tháng.
