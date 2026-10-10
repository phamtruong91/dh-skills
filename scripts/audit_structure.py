"""Quét cấu trúc và tính nhất quán nội bộ của từng SKILL.md (không đánh giá nội dung pháp lý).

Chạy: python -X utf8 scripts/audit_structure.py [--skill ten-skill ...] [--json]
Mã lỗi trả về luôn 0; đây là công cụ rà soát, không phải cổng chặn. Cổng chặn là validate_skills.py.

Mã vấn đề:
  M01 thiếu mục bắt buộc            M02 mô tả không có "Dùng khi"      M03 mô tả quá dài (>400 ký tự)
  I01 đầu vào bị bỏ rơi (không bước nào dùng)   I02 bước dùng input không có trong bảng đầu vào
  I03 không có bảng đầu vào         S01 bước đánh số không liên tục     S02 bước thiếu trường (Làm gì/Dùng input/Vai trò/Kết quả bước)
  S03 không có bước nào             W01 sơ đồ không khớp số bước        W02 không có sơ đồ
  C01 checklist trống               O01 mục Đầu ra thiếu liên kết quy cách
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["## Định dạng và file đầu ra", "## Quy cách đầu ra và thông tin thiếu", "## Kiểm soát áp dụng và phê duyệt",
            "## Giới hạn và human gate", "## Khi nào dùng", "## Đầu ra", "## Quản trị phiên bản"]


def sections(t):
    parts = re.split(r"^(## .+)$", t, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def audit(path):
    t = path.read_text(encoding="utf-8")
    name = path.parent.name
    fm = yaml.safe_load(t.split("---", 2)[1])
    sec = sections(t)
    heads = list(sec)
    issues = []

    def add(code, msg):
        issues.append({"ma": code, "chi_tiet": msg})

    for h in REQUIRED:
        if h not in sec:
            add("M01", f"thiếu mục {h}")
    if not any(h.startswith("## Đầu vào") for h in heads):
        add("I03", "không có mục Đầu vào")
    if not any(k in fm["description"] for k in ("Dùng khi", "Dùng để", "Dùng cho")):
        add("M02", "mô tả không nói khi nào dùng")
    if len(fm["description"]) > 400:
        add("M03", f"mô tả dài {len(fm['description'])} ký tự")

    # bảng đầu vào
    inp_key = next((h for h in heads if h.startswith("## Đầu vào")), None)
    inputs = {}
    if inp_key:
        for row in re.findall(r"^\|\s*`([^`]+)`\s*\|(.*)$", sec[inp_key], flags=re.M):
            cells = [c.strip() for c in row[1].split("|")]
            req = cells[-2] if len(cells) >= 2 else ""
            inputs[row[0]] = req
    # quy trình
    q_key = next((h for h in heads if h.startswith("## Quy trình") and "lịch sử" not in h.lower()), None)
    body = sec.get(q_key, "")
    steps = list(re.finditer(r"^\*\*Bước (\d+)\.\s*(.*?)\*\*", body, flags=re.M))
    nums = [int(m.group(1)) for m in steps]
    if not steps:
        add("S03", "không tìm thấy bước nào")
    elif nums != list(range(1, len(nums) + 1)):
        add("S01", f"bước đánh số {nums}")
    used = set()
    for i, m in enumerate(steps):
        blk = body[m.end(): steps[i + 1].start() if i + 1 < len(steps) else len(body)]
        miss = [lbl for lbl, pat in (("Làm gì", r"- Làm gì:"), ("Dùng input", r"- Dùng input:"), ("Vai trò", r"- Vai trò:"),
                                      ("Kết quả bước", r"- → Kết quả bước:")) if not re.search(pat, blk)]
        if miss:
            add("S02", f"Bước {m.group(1)} thiếu: {', '.join(miss)}")
        mi = re.search(r"- Dùng input:(.*?)(?=\n- |\Z)", blk, flags=re.S)
        if mi:
            refs = set(re.findall(r"`([^`]+)`", mi.group(1)))
            used |= refs
            for r in sorted(refs - set(inputs)):
                if inputs:
                    add("I02", f"Bước {m.group(1)} dùng `{r}` không có trong bảng đầu vào")
    if inputs:
        for f_, req in inputs.items():
            if f_ not in used:
                add("I01", f"đầu vào `{f_}` ({req or '?'}) không bước nào dùng")
    # sơ đồ
    wf_key = next((h for h in heads if "Luồng quy trình" in h or "Workflow" in h), None)
    if not wf_key:
        add("W02", "không có sơ đồ luồng")
    else:
        mer = re.findall(r"Bước (\d+)", sec[wf_key])
        if steps and set(map(int, mer)) != set(nums):
            add("W01", f"sơ đồ nhắc bước {sorted(set(map(int, mer)))} nhưng quy trình có {nums}")
    # checklist, đầu ra
    ck = next((h for h in heads if h.startswith("## Kiểm tra nội bộ")), None)
    if ck and not re.search(r"- \[ \]", sec[ck]):
        add("C01", "checklist nội bộ không có mục nào")
    if "## Đầu ra" in sec and "references/quy-cach-dau-ra.md" not in sec["## Đầu ra"]:
        add("O01", "mục Đầu ra không dẫn tới quy cách đầu ra")
    return name, issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", nargs="*")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = {}
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        if a.skill and p.parent.name not in a.skill:
            continue
        n, iss = audit(p)
        res[n] = iss
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0
    from collections import Counter
    c = Counter(i["ma"] for v in res.values() for i in v)
    print(f"{len(res)} skill; {sum(1 for v in res.values() if v)} skill có vấn đề")
    for k, v in sorted(c.items()):
        print(f"  {k}: {v}")
    for n, v in res.items():
        for i in v:
            print(f"{n}\t{i['ma']}\t{i['chi_tiet']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
