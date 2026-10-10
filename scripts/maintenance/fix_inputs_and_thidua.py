"""Sửa đầu vào mồ côi/không có trong bảng ở một số skill và chuyển bao-cao-thi-dua sang dạng Bước chuẩn. Chạy lại an toàn."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOG = []


def ed(skill, old, new, why):
    p = ROOT / "skills" / skill / "SKILL.md"
    t = p.read_text(encoding="utf-8")
    if old in t and new not in t:
        p.write_text(t.replace(old, new, 1), encoding="utf-8")
        LOG.append((skill, why))
    elif old not in t and new not in t:
        print("KHÔNG TÌM THẤY:", skill, old[:60])


def main():
    ed("bao-cao-cong-khai-tai-chinh", "| `nam_hoc` / `nam_tai_chinh` | Năm học / năm tài chính công khai | Có |",
       "| `nam_hoc` | Năm học công khai (khi công khai theo năm học) | Có (một trong hai) |\n| `nam_tai_chinh` | Năm tài chính công khai (khi công khai theo năm tài chính) | Có (một trong hai) |",
       "Tách hai trường đầu vào dính nhau")
    ed("bao-cao-tai-chinh", "| `nguoi_lap` / `ke_toan_truong` / `nguoi_ky` |",
       "| `nguoi_lap` |", "Tách ba trường đầu vào dính nhau")
    p = ROOT / "skills/bao-cao-tai-chinh/SKILL.md"
    t = p.read_text(encoding="utf-8")
    m = re.search(r"\| `nguoi_lap` \|([^\n]*)\n", t)
    if m and "`ke_toan_truong` |" not in t:
        rest = m.group(1)
        new = ("| `nguoi_lap` | Người lập báo cáo | Có |\n| `ke_toan_truong` | Kế toán trưởng | Có |\n"
               "| `nguoi_ky` | Thủ trưởng đơn vị ký báo cáo | Có |\n")
        t = t.replace(m.group(0), new, 1)
        t = t.replace("- Dùng input: `nguoi_lap` / `ke_toan_truong` / `nguoi_ky`,", "- Dùng input: `nguoi_lap`, `ke_toan_truong`, `nguoi_ky`,")
        p.write_text(t, encoding="utf-8")
        LOG.append(("bao-cao-tai-chinh", "Tách ba trường đầu vào dính nhau"))
    ed("campaign-brief-tuyen-sinh", "- Dùng input: toàn bộ bán thành phẩm Bước 1–6.", "- Dùng input: `ten_chien_dich` (tên brief), toàn bộ bán thành phẩm Bước 1–6.",
       "Gắn input ten_chien_dich vào bước hoàn thiện brief")
    ed("de-an-mo-nganh", "- Dùng input: `minh_chung`, `don_vi_chu_tri`, toàn bộ kết quả các bước trên.",
       "- Dùng input: `minh_chung`, `don_vi_chu_tri`, `ma_nganh` (ghi mã ngành nếu đã xác định, chưa có thì để dòng dấu chấm), toàn bộ kết quả các bước trên.",
       "Gắn input ma_nganh vào bước hoàn thiện hồ sơ")
    ed("hop-dong-lam-viec", "- Dùng input: toàn bộ input đã thu thập ở các bước 1–3.", "- Dùng input: `cong_viec` (điều khoản công việc) và toàn bộ input đã thu thập ở các bước 1–3.",
       "Gắn input cong_viec vào bước soạn điều khoản")
    ed("khung-chuong-trinh-dao-tao", "- Dùng input: `ten_nganh`, `muc_tieu_dao_tao`, `don_vi_xay_dung`.",
       "- Dùng input: `ten_nganh`, `ma_nganh` (nếu có), `trinh_do`, `muc_tieu_dao_tao`, `don_vi_xay_dung`.", "Gắn input ma_nganh, trinh_do vào Bước 1")
    ed("khung-chuong-trinh-dao-tao", "- Dùng input: `tong_tin_chi`, `khoi_kien_thuc`.",
       "- Dùng input: `tong_tin_chi`, `khoi_kien_thuc`, `thoi_gian_dao_tao` (số học kỳ để phân bổ tín chỉ; thiếu thì dùng mặc định ghi ở bảng đầu vào).",
       "Gắn input thoi_gian_dao_tao vào Bước 3")
    ed("pmo-quan-tri-du-an", "**Bước 3. Phân loại trạng thái và cập nhật tracker**", "**Bước 3. Phân loại trạng thái và cập nhật tracker**", "")
    p = ROOT / "skills/pmo-quan-tri-du-an/SKILL.md"
    t = p.read_text(encoding="utf-8")
    old = "- Dùng input: `workplan`, `ky_bao_cao`."
    seg = t.split("**Bước 3.")[1].split("**Bước 4.")[0]
    if old in seg and "nguong_trang_thai" not in seg.split("Dùng input")[1].split("\n")[0]:
        t = t.replace("**Bước 3." + seg, "**Bước 3." + seg.replace(old, "- Dùng input: `workplan`, `ky_bao_cao`, `nguong_trang_thai` (nếu có).", 1), 1)
        p.write_text(t, encoding="utf-8")
        LOG.append(("pmo-quan-tri-du-an", "Gắn input nguong_trang_thai vào Bước 3"))
    p = ROOT / "skills/ra-soat-du-thao-van-ban/SKILL.md"
    t = p.read_text(encoding="utf-8")
    seg = t.split("**Bước 1.")[1].split("**Bước 2.")[0]
    if "`muc_do`" not in seg:
        new = seg.replace("- Dùng input: `du_thao`, `loai_van_ban`.", "- Dùng input: `du_thao`, `loai_van_ban`, `muc_do` (nhanh: chỉ Bước 1 và Bước 5; kỹ: đủ Bước 1–5; thiếu thì mặc định kỹ).", 1)
        t = t.replace("**Bước 1." + seg, "**Bước 1." + new, 1)
        p.write_text(t, encoding="utf-8")
        LOG.append(("ra-soat-du-thao-van-ban", "Gắn input muc_do vào Bước 1"))
    thi_dua()
    for s, w in LOG:
        print(s, "-", w)


def thi_dua():
    p = ROOT / "skills/bao-cao-thi-dua/SKILL.md"
    t = p.read_text(encoding="utf-8")
    if "**Bước 1." in t:
        return
    a = t.index("## Quy trình\n")
    b = t.index("## Đầu ra\n")
    VT = "Chuyên viên Văn phòng/Phòng Thi đua (đơn vị tổng hợp)"
    steps = [
        ("Kiểm tra kỳ, thời điểm chốt và nguồn từng dòng",
         "Kiểm tra từng dòng số liệu có kỳ, thời điểm chốt và nguồn; dòng thiếu quyết định hoặc xác nhận thì ghi nhận nội bộ [CHƯA XÁC NHẬN] (không đưa vào file giao) và không tính vào kết quả đã ban hành.",
         "`ky_bao_cao`, `quyet_dinh_khen_thuong`, `bao_cao_don_vi`",
         "Mọi con số phải truy được về quyết định/hồ sơ và người xác nhận.",
         "Danh sách dòng số liệu hợp lệ + danh sách dòng chưa xác nhận (nội bộ)."),
        ("Đối chiếu số liệu đơn vị với quyết định",
         "Lập bảng số liệu nguồn / số liệu báo cáo / chênh lệch / người cần xác nhận. Không tự chọn một nguồn khi có mâu thuẫn.",
         "`quyet_dinh_khen_thuong`, `bao_cao_don_vi`",
         "Chênh lệch chưa giải trình được thì giữ ở bảng nội bộ, không đưa vào báo cáo.",
         "Bảng đối chiếu (nội bộ) + danh sách cần bổ sung."),
        ("Tổng hợp số lượng theo danh hiệu, hình thức và đơn vị",
         "Tổng hợp theo loại danh hiệu, hình thức khen thưởng và đơn vị; giữ tách biệt tập thể/cá nhân và đã được tặng/đang đề nghị. Tránh đếm trùng người hay hồ sơ; không cộng các đại lượng khác đơn vị tính.",
         "kết quả Bước 1–2, `ho_so_dang_trinh`",
         "Hồ sơ đang đề nghị không được cộng vào kết quả đã được tặng.",
         "Bảng thống kê đã tách các nhóm."),
        ("Tính biến động so với kỳ trước",
         "Chỉ tính biến động khi có dữ liệu kỳ trước cùng phạm vi. Nếu mẫu số bằng 0 hoặc không có dữ liệu thì để trống, ghi không tính được; không tự đặt tỷ lệ tăng/giảm.",
         "kết quả Bước 3, `so_lieu_ky_truoc`",
         "So sánh khác phạm vi (đơn vị, loại danh hiệu) là so sánh sai.",
         "Bảng biến động hoặc ghi chú không tính được."),
        ("Soạn báo cáo",
         "Soạn báo cáo gồm kết quả đã xác nhận, vấn đề đối chiếu còn mở và nhiệm vụ kỳ tới đã được cung cấp. Chỉ trình bày nhận xét từ `nhan_xet_da_duyet` và phương hướng từ `phuong_huong_da_duyet`, ghi rõ nguồn.",
         "kết quả Bước 3–4, `nhan_xet_da_duyet`, `phuong_huong_da_duyet`, `thong_tin_trinh_ky`",
         "Không suy đoán nguyên nhân hay thành tích cá nhân; không thêm nhận xét khi thiếu dữ liệu.",
         "Dự thảo báo cáo đúng bố cục."),
        ("Kiểm tra nguồn truy nguyên và chuyển duyệt",
         "Kiểm tra mỗi số liệu và phát biểu có nguồn truy nguyên; xuất báo cáo hoàn chỉnh về bố cục, để trống dữ liệu thiếu; bảng đối chiếu và vấn đề cần xác nhận chỉ dùng nội bộ. Cán bộ phụ trách xác nhận nội dung; người có thẩm quyền quyết định ký/phát hành.",
         "toàn bộ input, `thong_tin_trinh_ky`",
         "Không tự gửi, công bố, ký hoặc đánh dấu đã duyệt.",
         "Báo cáo hoàn chỉnh, sẵn sàng chuyển cán bộ phụ trách kiểm tra."),
    ]
    out = "## Quy trình\n\n"
    for i, (ti, lg, inp, ln, kq) in enumerate(steps, 1):
        role = VT if i < 6 else f"{VT} chuẩn bị; cán bộ phụ trách xác nhận; người có thẩm quyền duyệt"
        out += (f"**Bước {i}. {ti}**\n- Làm gì: {lg}\n- Dùng input: {inp}.\n- Vai trò: {role} · AI hỗ trợ: đối chiếu và tổng hợp số liệu, soạn dự thảo\n"
                f"- Lưu ý nghiệp vụ: {ln}\n- → Kết quả bước: {kq}\n\n")
    out += '''## Luồng quy trình

```mermaid
flowchart TD
    IN[/"Quyết định, báo cáo đơn vị"/] --> B1["Bước 1: Kiểm tra kỳ, thời điểm chốt và nguồn"]
    B1 --> B2["Bước 2: Đối chiếu số liệu với quyết định"]
    B2 --> C{"Đủ xác nhận?"}
    C -->|Chưa| D["Bảng cần bổ sung"]
    D --> B2
    C -->|Đủ| B3["Bước 3: Tổng hợp theo danh hiệu, hình thức, đơn vị"]
    B3 --> B4["Bước 4: Tính biến động so với kỳ trước"]
    B4 --> B5["Bước 5: Soạn báo cáo"]
    B5 --> B6["Bước 6: Kiểm tra nguồn và chuyển duyệt"]
    B6 --> HG["👤 Cán bộ phụ trách kiểm tra, người có thẩm quyền duyệt"]
    HG --> OUT[["Báo cáo thi đua, khen thưởng"]]
```

'''
    # đưa mục Đầu vào về dạng chuẩn tên "Đầu vào (Input)" không đổi; chỉ thay Quy trình + Luồng
    c = t.index("## Luồng quy trình\n")
    t = t[:a] + out + t[b:]
    p.write_text(t, encoding="utf-8")
    LOG.append(("bao-cao-thi-dua", "Chuyển quy trình sang dạng Bước chuẩn (Làm gì/Dùng input/Vai trò/Lưu ý/Kết quả), dùng hết 8 input, sơ đồ khớp bước"))


if __name__ == "__main__":
    main()
