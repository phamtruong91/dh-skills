"""Làm sạch các skill vừa khôi phục: cụm viện dẫn thừa, mục thể thức cắt cụt, thêm ràng buộc pháp lý vào quy trình.

Chạy sau restore_procedures.py và label_diagrams.py. Chạy lại an toàn.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = "văn bản hiện hành nêu tại phap-ly.md"
MARK = "**Ràng buộc pháp lý khi thực hiện**"


def legal_notes(sdir):
    t = (sdir / "references/phap-ly.md").read_text(encoding="utf-8")
    notes = []
    for sec in re.split(r"\n(?=## )", t)[1:]:
        lines = sec.split("\n")
        title = lines[0][3:].strip()
        body = " ".join(l.strip() for l in lines[1:] if l.strip() and not l.strip().startswith("Nguồn:"))
        notes.append((title, body))
    return notes


EXTRA = [
    (r"điều kiện chung bám sát Điều 22 Luật Viên chức và", "điều kiện chung bám sát luật viên chức và nghị định hướng dẫn hiện hành, theo"),
    (r"theo Điều 22 Luật Viên chức", "theo luật viên chức hiện hành (xem phap-ly.md)"),
    (r"xuất bản đề án hoàn chỉnh dạng markdown", "xuất bản đề án hoàn chỉnh theo định dạng đầu ra của skill"),
    (r"ở định dạng markdown", "theo định dạng đầu ra của skill"),
    (r"dạng markdown", "theo định dạng đầu ra của skill"),
    (r" ?\(markdown\)", ""),
    (r"xuất hợp đồng markdown", "xuất hợp đồng theo định dạng đầu ra của skill"),
    (r"xuất văn bản markdown và lưu checklist vào hồ sơ", "xuất văn bản theo định dạng đầu ra của skill và lưu hồ sơ"),
    (r"hoàn chỉnh \[CHỜ KÝ\]\.", "hoàn chỉnh, sẵn sàng trình ký."),
    (r"checklist 5 lớp đã đánh dấu", "kết quả rà soát 5 lớp (giữ nội bộ, không xuất kèm file)"),
    (r"checklist kiểm tra đã đánh dấu", "kết quả đối chiếu nội bộ (không xuất kèm file)"),
    (r"\+ checklist kiểm tra\.", "+ kết quả đối chiếu nội bộ (không xuất kèm file)."),
    (r", sẵn sàng trình ký \+ checklist 5 lớp đã đánh dấu\.", ", sẵn sàng trình ký + kết quả rà soát 5 lớp (giữ nội bộ, không xuất kèm file)."),
    (r"checklist rà soát đã đánh dấu \+ danh sách điểm cần sửa", "kết quả đối chiếu nội bộ (không xuất kèm file) + danh sách điểm cần sửa"),
    (r"bộ hồ sơ nghiệm thu hoàn chỉnh đã ký \(Phần A \+ Phần B\)", "bộ hồ sơ nghiệm thu hoàn chỉnh (Phần A + Phần B), sẵn sàng trình ký"),
]


CAVEAT = ("- Các con số, thời hạn, số điều, số mức xếp loại, hệ số và mẫu biểu nêu trong các bước dưới đây được giữ từ quy trình gốc (trước cập nhật pháp lý); "
          "chỉ dùng khi đã đối chiếu đúng với căn cứ đã chọn, khác thì theo căn cứ. Danh sách điểm cần đối chiếu: docs/DIEM_CAN_DOI_CHIEU_PHAP_LY.md.\n")


def polish(path):
    sdir = path.parent
    t = path.read_text(encoding="utf-8")
    if "## Tư liệu đối chiếu" not in t or "Bản gốc trước cập nhật pháp lý" not in t:
        return False
    o = t
    t = t.replace(P + ", " + P, P).replace("văn bản " + P, P).replace(P + " năm 2017", P)
    t = re.sub(re.escape(P) + r"\s*(?:/|-)\s*20\d\d", P, t)
    t = re.sub(r"^- \[ \] Đúng thể thức và định dạng theo .*$",
               "- [ ] Đúng thể thức và cấu trúc theo references/quy-cach-dau-ra.md và căn cứ đã chọn tại references/phap-ly.md.",
               t, flags=re.M)
    # cấu trúc output chuẩn của bản gốc không còn là chuẩn: cấu trúc hiện hành nằm ở references/quy-cach-dau-ra.md
    def _cut(m):
        body = m.group(2)
        k = re.search(r"\*\*Cấu trúc output chuẩn", body)
        return m.group(1) + (body[:k.start()].rstrip() + "\n\n" if k else body) + m.group(3)
    t = re.sub(r"(## Đầu ra\n)(.*?)(File nghiệp vụ thực tế)", _cut, t, count=1, flags=re.S)
    t = re.sub(r"^- \[ \] [^\n]*[Cc]ấu trúc output chuẩn[^\n]*$",
               "- [ ] Đủ các phần và đúng bố cục theo cấu trúc tại references/quy-cach-dau-ra.md (không theo cấu trúc của bản gốc).", t, flags=re.M)
    for old, new in EXTRA:
        t = re.sub(old, new, t)
    if MARK in t and "được giữ từ quy trình gốc" not in t:
        t = t.replace("chưa kết luận tuân thủ.\n", "chưa kết luận tuân thủ.\n" + CAVEAT, 1)
    if MARK not in t:
        notes = legal_notes(sdir)
        if notes:
            block = MARK + " (trích references/phap-ly.md; đối chiếu toàn văn và hiệu lực tại ngày nghiệp vụ):\n" + \
                "\n".join(f"- {ti}: {bo}" for ti, bo in notes) + \
                "\n- Trước Bước 1: chọn căn cứ theo đối tượng, loại hình trường và chuyển tiếp; lập bảng văn bản / điều khoản / lý do áp dụng / bằng chứng. " \
                "Thiếu văn bản gốc hoặc điều khoản thì ghi nhận nội bộ [CẦN XÁC MINH] (không đưa vào file giao), để trống phần tương ứng, chưa kết luận tuân thủ.\n" + CAVEAT
            t = re.sub(r"(## Quy trình\n)", r"\1" + block.replace("\\", "\\\\") + "\n", t, count=1)
    if t != o:
        path.write_text(t, encoding="utf-8")
        return True
    return False


def main():
    n = 0
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        n += polish(p)
    print(n, "skill đã làm sạch")


if __name__ == "__main__":
    main()
