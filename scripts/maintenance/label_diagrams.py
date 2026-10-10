"""Thêm nhãn "Bước N" vào các nút của sơ đồ quy trình khi sơ đồ không nêu số bước.

Ghép nút với bước theo độ giống tên (difflib); chỉ ghi khi mọi bước đều được ghép chắc chắn,
nếu không thì in danh sách để sửa tay. Dùng: python -X utf8 scripts/maintenance/label_diagrams.py [--apply]
"""
import argparse
import difflib
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NODE = re.compile(r'(\b[A-Za-z][A-Za-z0-9_]*)(\[\[|\[/|\[|\{|\(\[)"([^"]+)"(\]\]|/\]|\]|\}|\]\))')


def norm(s):
    s = unicodedata.normalize("NFC", s.lower())
    s = re.sub(r"^(bước\s*\d+\s*[.:]\s*)", "", s)
    return re.sub(r"[^\w\s]", " ", s)


REBUILD = False


def rebuild(path, t, m, body, steps, nodes):
    """Dựng lại sơ đồ tuyến tính từ tên các bước; giữ nhãn đầu vào, cổng người duyệt (👤) và đầu ra của sơ đồ cũ.
    Các nút rẽ nhánh của sơ đồ cũ không được giữ (điều kiện nằm trong nội dung bước)."""
    ins = [(lbl, shp) for _, _, lbl, shp in nodes if shp in ("[/",)]
    hg = next((lbl for _, _, lbl, _ in nodes if lbl.startswith("👤")), None)
    outs = [(lbl, shp) for _, _, lbl, shp in nodes if shp in ("[[",) or shp == "[/"]
    first = ins[0][0] if ins else "Đầu vào"
    last = outs[-1][0] if outs and outs[-1][0] != first else "Sản phẩm đầu ra"
    lines = ["flowchart TD", f'    IN[/"{first}"/] --> B1["Bước 1: {steps[0][1]}"]']
    for (n, ti), (n2, ti2) in zip(steps, steps[1:]):
        lines.append(f'    B{n} --> B{n2}["Bước {n2}: {ti2}"]')
    ln = steps[-1][0]
    if hg:
        lines.append(f'    B{ln} --> HG["{hg}"]')
        lines.append(f'    HG --> OUT[["{last}"]]')
    else:
        lines.append(f'    B{ln} --> OUT[["{last}"]]')
    new = "\n".join(lines) + "\n"
    if REBUILD_APPLY:
        path.write_text(t[:m.start(1)] + new + t[m.end(1):], encoding="utf-8")
    return "rebuilt"


REBUILD_APPLY = False


def process(path, apply):
    t = path.read_text(encoding="utf-8")
    m = re.search(r"```mermaid\n(.*?)```", t, flags=re.S)
    if not m:
        return "no-diagram"
    body = m.group(1)
    steps = re.findall(r"^\*\*Bước (\d+)\.\s*(.*?)\*\*", t, flags=re.M)
    if not steps:
        return "no-steps"
    if set(map(int, re.findall(r"Bước (\d+)", body))) >= {int(n) for n, _ in steps}:
        return "ok"
    nodes = [(mm.start(3), mm.end(3), mm.group(3), mm.group(2)) for mm in NODE.finditer(body)]
    # chỉ xét nút có chữ giống một bước
    cand = []
    for i, (s, e, label, shape) in enumerate(nodes):
        if shape in ("{",) or label.startswith(("👤",)) and False:
            continue
        for n, title in steps:
            r = difflib.SequenceMatcher(None, norm(label), norm(title)).ratio()
            cand.append((r, i, int(n)))
    cand.sort(reverse=True)
    used_n, used_i, assign = set(), set(), {}
    for r, i, n in cand:
        if r < 0.45 or n in used_n or i in used_i:
            continue
        assign[i] = n
        used_n.add(n)
        used_i.add(i)
    missing = [int(n) for n, _ in steps if int(n) not in used_n]
    if missing:
        return rebuild(path, t, m, body, steps, nodes) if REBUILD else f"manual: chưa ghép bước {missing}"
    out, last = [], 0
    for i, (s, e, label, shape) in enumerate(nodes):
        out.append(body[last:s])
        if i in assign and not re.match(r"^(👤\s*)?Bước \d+", label):
            pre = "👤 " if label.startswith("👤") else ""
            label = pre + f"Bước {assign[i]}: " + label.replace("👤", "").strip()
        out.append(label)
        last = e
    out.append(body[last:])
    if apply:
        path.write_text(t[:m.start(1)] + "".join(out) + t[m.end(1):], encoding="utf-8")
    return "labelled"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--skill", nargs="*")
    ap.add_argument("--rebuild", action="store_true", help="dựng lại sơ đồ tuyến tính khi không ghép được")
    a = ap.parse_args()
    global REBUILD, REBUILD_APPLY
    REBUILD, REBUILD_APPLY = a.rebuild, a.apply
    from collections import Counter
    c = Counter()
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        if a.skill and p.parent.name not in a.skill:
            continue
        r = process(p, a.apply)
        c[r.split(":")[0]] += 1
        if r.startswith("manual"):
            print(p.parent.name, r)
    print(dict(c))


if __name__ == "__main__":
    main()
