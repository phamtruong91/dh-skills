"""Khôi phục quy trình đầy đủ cho các skill đang chỉ có "Quy trình hiện hành" 4 bước chung chung.

Nguồn: references/quy-trinh-lich-su.md (nghiệp vụ gốc: đầu vào, các bước, sơ đồ, checklist, căn cứ).
Nguyên tắc:
- Giữ nguyên nghiệp vụ gốc (bước, vai trò, lưu ý, kết quả bước).
- Viện dẫn văn bản đã bị thay thế được đổi thành "văn bản hiện hành đã chọn (xem references/phap-ly.md)";
  KHÔNG tự viết nội dung biểu mẫu/điều khoản của văn bản mới.
- Bỏ phần "Ví dụ mô phỏng" (dữ liệu giả lập) khỏi SKILL.md; bản gốc vẫn còn ở quy-trinh-lich-su.md.
Chạy lại an toàn: bỏ qua skill đã khôi phục.
Dùng: python -X utf8 scripts/maintenance/restore_procedures.py [--skill ten ...]
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POINTER = "văn bản hiện hành nêu tại phap-ly.md"

SUP = re.compile(
    r"(?:Thông tư|TT)\s*(?:số\s*)?(?:36/2017(?:/TT-BGDĐT)?|08/2021(?:/TT-BGDĐT)?|17/2021(?:/TT-BGDĐT)?|08/2022(?:/TT-BGDĐT)?"
    r"|02/2022(?:/TT-BGDĐT)?|12/2017(?:/TT-BGDĐT)?|21/2019(?:/TT-BGDĐT)?|107/2017(?:/TT-BTC)?|36\b)"
    r"|(?:Nghị định|NĐ)\s*(?:số\s*)?(?:115/2020(?:/NĐ-CP)?|204/2004(?:/NĐ-CP)?|90/2020(?:/NĐ-CP)?)")


def sections(text):
    parts = re.split(r"^(## .+)$", text, flags=re.M)
    head = parts[0]
    return head, {parts[i].strip(): parts[i + 1].strip("\n") for i in range(1, len(parts) - 1, 2)}, [parts[i].strip() for i in range(1, len(parts) - 1, 2)]


def clean(s):
    return SUP.sub(POINTER, s)


def bullets(block):
    """Tách danh sách gạch đầu dòng có dòng nối tiếp."""
    items, cur = [], None
    for ln in block.split("\n"):
        if ln.startswith("- "):
            if cur is not None:
                items.append(cur)
            cur = ln
        elif cur is not None and ln.strip():
            cur += "\n" + ln
        elif ln.strip():
            items.append(ln)
    if cur is not None:
        items.append(cur)
    return items


def restore(name):
    sdir = ROOT / "skills" / name
    md = sdir / "SKILL.md"
    text = md.read_text(encoding="utf-8")
    if "## Quy trình hiện hành" not in text and "## Quy trình cập nhật pháp lý" not in text:
        return None
    leg = (sdir / "references/quy-trinh-lich-su.md").read_text(encoding="utf-8")
    _, ls, _ = sections(leg)
    head, cs, order = sections(text)

    khi = ls["## Khi nào dùng"]
    inp = ls["## Đầu vào (Input)"]
    qt = ls["## Quy trình"]
    wf = ls["## Luồng quy trình (Workflow)"]
    out_l = ls["## Đầu ra (Output)"].split("**Cấu trúc output chuẩn**")[0].strip()
    ck = ls["## Checklist nghiệm thu"]
    cc = ls["## Căn cứ & lưu ý"]

    # checklist -> mục kiểm tra nội bộ
    items = [ln for ln in ck.split("\n") if ln.startswith("- [ ]")]
    items = [clean(i) for i in items]
    ck_new = ("Các tiêu chí sau dùng để tự đối chiếu; không sao chép vào file xuất. Mục thiếu dữ liệu được để trống, "
              "không đánh dấu đã đạt hoặc đã duyệt.\n\n" + "\n".join(items))
    # căn cứ & lưu ý: bỏ gạch đầu dòng chỉ viện dẫn văn bản cũ
    cc_items = bullets(cc)
    kept = [i for i in cc_items if not SUP.search(i)]
    dropped = len(cc_items) - len(kept)
    if dropped:
        kept.insert(0, "- Căn cứ hiện hành: xem [căn cứ và điều kiện áp dụng](references/phap-ly.md); phải đối chiếu văn bản gốc, hiệu lực và chuyển tiếp tại ngày nghiệp vụ.")
    cc_new = "\n".join(kept)

    qt_new = clean(qt)
    wf_new = clean(wf)
    inp_new = clean(inp)
    khi_new = clean(khi)

    kiem_soat = cs["## Kiểm soát áp dụng và phê duyệt"]
    kiem_soat = re.sub(r"Phần quy trình lịch sử ở cuối chỉ để đối chiếu, không dùng làm chỉ dẫn hiện hành\.",
                       "Quy trình dưới đây giữ nghiệp vụ từ bản gốc; mọi viện dẫn văn bản, mẫu biểu, điều khoản phải theo căn cứ đã chọn trong phap-ly.md, "
                       "không theo văn bản cũ.", kiem_soat)
    dau_ra = cs["## Đầu ra"]
    if out_l:
        dau_ra = out_l + "\n\n" + dau_ra

    new = head.rstrip("\n") + "\n\n"
    def sec(h, b):
        return f"{h}\n{b.strip()}\n\n"
    new += sec("## Định dạng và file đầu ra", cs["## Định dạng và file đầu ra"])
    new += sec("## Quy cách đầu ra và thông tin thiếu", cs["## Quy cách đầu ra và thông tin thiếu"])
    new += sec("## Kiểm soát áp dụng và phê duyệt", kiem_soat)
    new += sec("## Giới hạn và human gate", cs["## Giới hạn và human gate"])
    new += sec("## Khi nào dùng", khi_new)
    new += sec("## Đầu vào (Input)", inp_new)
    new += sec("## Quy trình", qt_new)
    new += sec("## Luồng quy trình (Workflow)", wf_new)
    new += sec("## Đầu ra", dau_ra)
    new += sec("## Kiểm tra nội bộ trước khi giao", ck_new)
    new += sec("## Căn cứ & lưu ý", cc_new)
    new += sec("## Tư liệu đối chiếu",
               "Bản gốc trước cập nhật pháp lý (kèm ví dụ giả lập) lưu tại `references/quy-trinh-lich-su.md`, chỉ để đối chiếu hồ sơ lịch sử; "
               "không dùng căn cứ, mẫu hay số liệu trong đó làm chỉ dẫn hiện hành.")
    new += sec("## Quản trị phiên bản", cs["## Quản trị phiên bản"])
    md.write_text(new.rstrip("\n") + "\n", encoding="utf-8")
    return {"cite_replaced": len(SUP.findall(leg.split("## Ví dụ mô phỏng")[0])), "can_cu_bullets_dropped": dropped,
            "checklist_items": len(items)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", nargs="*")
    a = ap.parse_args()
    log = {}
    for d in sorted((ROOT / "skills").iterdir()):
        if a.skill and d.name not in a.skill:
            continue
        if (d / "references/quy-trinh-lich-su.md").exists():
            r = restore(d.name)
            if r:
                log[d.name] = r
    print(json.dumps(log, ensure_ascii=False, indent=1))
    print(len(log), "skill đã khôi phục")


if __name__ == "__main__":
    main()
