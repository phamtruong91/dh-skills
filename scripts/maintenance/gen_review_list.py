"""Lập docs/DIEM_CAN_DOI_CHIEU_PHAP_LY.md: các dòng trong quy trình của skill đã khôi phục có con số, thời hạn, số điều, mức xếp loại, mẫu biểu
được giữ từ quy trình gốc và phải đối chiếu lại với căn cứ hiện hành. Công cụ lập danh sách cho người có chuyên môn, không kết luận đúng/sai."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAT = re.compile(r"(\d+\s*(?:tháng|ngày|năm|điều khoản|mức|bước|tín chỉ|%|giờ|bản)\b|Điều\s*\d+|[Mm]ẫu\s*\d+|hệ số|bậc \d|tối đa|tối thiểu|ít nhất|không quá|thời hạn)")
LEG = re.compile(r"(Luật|Nghị định|Thông tư|NĐ|TT|Quyết định|Bộ luật)\s*\d")


def main():
    out = ["# Điểm cần đối chiếu pháp lý trong các skill đã khôi phục quy trình\n",
           "Tài liệu này do công cụ tự lập (`scripts/maintenance/gen_review_list.py`). Mỗi dòng dưới đây nằm trong quy trình giữ từ bản gốc "
           "(trước cập nhật pháp lý) và có con số, thời hạn, số điều hoặc mẫu biểu. **Chưa kết luận đúng hay sai**: cán bộ pháp chế/chuyên môn "
           "đối chiếu với căn cứ trong `references/phap-ly.md` của từng skill và văn bản gốc tại ngày nghiệp vụ, rồi sửa SKILL.md nếu khác.\n"]
    total = 0
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        t = p.read_text(encoding="utf-8")
        if "được giữ từ quy trình gốc" not in t:
            continue
        body = t.split("## Quy trình\n", 1)[1].split("## Luồng quy trình", 1)[0]
        rows, step, cur = [], None, None
        bl = []
        for ln in body.split("\n"):
            m = re.match(r"\*\*Bước (\d+)\.", ln)
            if m:
                step = m.group(1)
                continue
            if ln.startswith("- "):
                bl.append([step, ln])
            elif ln.startswith(" ") and bl and ln.strip():
                bl[-1][1] += " " + ln.strip()
        for st, b_ in bl:
            if not b_.startswith(("- Làm gì", "- Lưu ý nghiệp vụ")):
                continue
            hits = list(PAT.finditer(b_))
            if not hits:
                continue
            names = sorted({h.group(0).strip() for h in hits})[:6]
            s0 = max(0, hits[0].start() - 90)
            rows.append((st, ", ".join(names), ("…" if s0 else "") + " ".join(b_[s0:s0 + 260].split())))
        out.append(f"## {p.parent.name} ({len(rows)} điểm)\n")
        for s, h, l in rows[:14]:
            out.append(f"- Bước {s} [{h}]: {l}")
        if len(rows) > 14:
            out.append(f"- … và {len(rows) - 14} dòng khác")
        out.append("")
        total += len(rows)
    out.insert(2, f"Tổng số dòng cần đối chiếu: {total}.\n")
    (ROOT / "docs/DIEM_CAN_DOI_CHIEU_PHAP_LY.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(total, "dòng")


if __name__ == "__main__":
    main()
