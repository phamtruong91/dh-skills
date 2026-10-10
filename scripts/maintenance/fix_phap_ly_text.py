"""Sửa lỗi dính chữ/thiếu tên văn bản trong references/phap-ly.md của các skill. Chạy lại an toàn."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBS = [
    (r"^## (23[35]/2026/NĐ-CP)", r"## Nghị định \1"),
    (r"(Luật|Nghị định|Thông tư|Nghị quyết|NĐ|TT|NQ|Điều|điểm|khoản|Khoản|Điểm)(?=\d)", r"\1 "),
    (r"(?<=\d)(Điều|khoản|điểm|Luật|NĐ|TT)", r" \1"),
    (r"LuậtViênChức", "Luật Viên chức"),
    (r"LuậtViên chức", "Luật Viên chức"),
    (r"BộGDĐT", "Bộ GDĐT"),
    (r"(Luật)(?=[A-ZĐ][a-zà-ỹ])", r"\1 "),
    (r"giữ (\d)", r"giữ \1"),
]


def main():
    n = 0
    for p in sorted((ROOT / "skills").glob("*/references/phap-ly.md")):
        t = o = p.read_text(encoding="utf-8")
        for pat, rep in SUBS:
            t = re.sub(pat, rep, t, flags=re.M)
        t = t.replace("Luật Viên chức 2010 2010", "Luật Viên chức 2010")
        if t != o:
            p.write_text(t, encoding="utf-8")
            n += 1
    print(n, "phap-ly.md đã sửa")


if __name__ == "__main__":
    main()
