"""Kiểm tra hợp đồng đóng gói của bộ skill. Đây không phải chứng nhận tuân thủ pháp luật.

Chạy: python -X utf8 scripts/validate_skills.py
Kết quả: in JSON tóm tắt; thoát mã 1 nếu có lỗi, kèm tên skill và tên kiểm tra bị hỏng.
"""
from pathlib import Path
import json
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
STRICT_DIAGRAM = set(open(Path(__file__).with_name('nhom_rasoat_1.txt'), encoding='utf-8').read().split())
MAX_SKILL_BYTES = 25000  # chặn SKILL.md phình to trở lại
# Cặp skill dễ bị chọn nhầm: mô tả mỗi skill phải nêu tên skill còn lại.
CONFUSABLE = [
    ("quy-che-to-chuc-hoat-dong", "quy-che-to-chuc-hoat-dong-truong"),
    ("thong-bao-tuyen-sinh", "thong-bao-tuyen-sinh-sdh"),
    ("ke-hoach-nam-hoc", "ke-hoach-nam-hoc-truong"),
    ("bao-cao-tai-chinh", "bao-cao-cong-khai-tai-chinh"),
    ("so-lieu-3-cong-khai-dt", "bao-cao-3-cong-khai"),
    ("ke-hoach-kiem-toan-noi-bo", "ke-hoach-thanh-tra-nam"),
    ("quyet-dinh-khen-thuong-kl", "soan-quyet-dinh-hc"),
]
# Skill được phép nhắc "markdown" ngoài danh sách định dạng (có lý do nghiệp vụ).
MARKDOWN_OK = {"cau-truc-bai-bao-khoa-hoc"}


def read(p):
    return Path(p).read_text(encoding="utf-8")


def skill_checks(path, manifest, records):
    name = path.parent.name
    t = read(path)
    fm = yaml.safe_load(t.split("---", 2)[1])
    ui = yaml.safe_load(read(path.parent / "agents/openai.yaml"))["interface"]
    version = json.loads(read(path.parent / "references/version.json"))
    out = path.parent / version["output_reference"]
    output_text = read(out) if out.is_file() else ""
    owner = version.get("approval_owner")
    c = {}  # tên kiểm tra -> bool
    c["ten_thu_muc_khop_frontmatter"] = fm["name"] == name
    c["ten_hop_le"] = bool(re.fullmatch("[a-z0-9]+(?:-[a-z0-9]+)*", name)) and len(name) <= 64
    c["mo_ta_toi_da_1024"] = len(fm["description"]) <= 1024
    c["metadata_ui_hop_le"] = (25 <= len(ui["short_description"]) <= 64 and "$" + name in ui["default_prompt"]
                               and bool(ui["display_name"]))
    for h in ("## Quản trị phiên bản", "## Giới hạn và human gate", "## Định dạng và file đầu ra", "## Đầu ra"):
        c["co_muc:" + h] = h in t
    c["khong_ghi_da_ky"] = "(đã ký)" not in t and "[CHỜ KÝ]" not in t
    c["version_khop_manifest"] = version == records[name]
    c["version_dung_ban_manifest"] = version["version"] == manifest["version"]
    c["approval_owner_hop_le"] = owner is None or (isinstance(owner, str) and owner.strip() != "")
    if version["legal_updates"]:
        c["co_phap_ly_md"] = (path.parent / "references/phap-ly.md").exists()
        c["co_quy_trinh_lich_su"] = (path.parent / "references/quy-trinh-lich-su.md").exists()
        c["co_nhan_can_xac_minh"] = "[CẦN XÁC MINH]" in t
    for link in re.findall(r"\]\((references/[^)]+)\)", t):
        c["lien_ket_ton_tai:" + link] = (path.parent / link).is_file()
    c["co_quy_tac_chung"] = (path.parent / "references/quy-tac-chung.md").is_file() and "references/quy-tac-chung.md" in t
    c["file_output_ton_tai"] = out.is_file()
    c["chinh_sach_thieu_du_lieu"] = version["missing_data_policy"] == "preserve-template-fill-spaces"
    c["khong_xuat_checklist"] = version["qa_attachments"] is False
    c["bat_buoc_xuat_file"] = version["output_delivery"] == "file-required"
    c["dinh_dang_mac_dinh_hop_le"] = (version["default_output_format"] in ("docx", "xlsx", "zip")
                                      and version["default_output_format"] in version["available_output_formats"]
                                      and len(version["available_output_formats"]) == len(set(version["available_output_formats"]))
                                      and "." + version["default_output_format"] in ui["default_prompt"])
    for h in ("## Cấu trúc sản phẩm của skill", "## Quy tắc giao văn bản", "## Bắt buộc xuất file"):
        c["output_co_muc:" + h] = h in output_text
    c["output_giu_cho_dien"] = "chừa chỗ điền đúng mẫu gốc" in output_text and "Không dùng dấu ba chấm" not in output_text
    for link in re.findall(r"\]\(([^)]+)\)", output_text):
        if not link.startswith(("https://", "http://")):
            c["lien_ket_output:" + link] = (out.parent / link).is_file()
    # --- Kiểm tra mới (1.3.2): mâu thuẫn nội bộ và chống phình ---
    c["dung_luong_skill_md"] = len(t.encode("utf-8")) <= MAX_SKILL_BYTES
    c["khong_buoc_xuat_checklist"] = not re.search(r"Kết quả bước:[^\n]*[Cc]hecklist[^\n]*đã đánh dấu", t)
    if "md" not in version["available_output_formats"] and name not in MARKDOWN_OK:
        c["khong_nhac_markdown_khi_khong_xuat_md"] = "markdown" not in t.lower()
    # --- Khóa kết quả khôi phục quy trình (1.3.2) ---
    c["khong_con_quy_trinh_rut_gon"] = "## Quy trình hiện hành" not in t and "## Quy trình cập nhật pháp lý" not in t
    c["co_it_nhat_3_buoc"] = len(re.findall(r"^\*\*Bước \d+\.", t, flags=re.M)) >= 3
    if (path.parent / "references/phap-ly.md").is_file():
        c["co_rang_buoc_phap_ly_trong_quy_trinh"] = "**Ràng buộc pháp lý khi thực hiện**" in t
    # --- Thể thức và bảng biểu (1.3.2) ---
    if version["default_output_format"] in ("docx", "xlsx"):
        c["co_muc_the_thuc_bang_bieu"] = "## Thể thức và bảng biểu khi dựng file" in output_text and "Thể thức và bảng biểu khi dựng file" in t
        if version["default_output_format"] == "docx":
            c["tieu_ngu_gach_ngang"] = "Độc lập – Tự do – Hạnh phúc" not in output_text
            if version["output_profile"] == "hanh-chinh":
                c["co_quy_tac_phan_dau_nd30"] = "Độc lập - Tự do - Hạnh phúc" in output_text and "Nơi nhận:" in output_text
    # --- Quy tắc biểu đồ cho skill báo cáo số liệu (1.3.3) ---
    chart_list = Path(__file__).with_name("chart_skills.txt")
    if chart_list.is_file() and name in chart_list.read_text(encoding="utf-8").split():
        c["co_quy_tac_bieu_do"] = "## Biểu đồ và hình trong báo cáo số liệu" in output_text and "Biểu đồ và hình trong báo cáo số liệu" in t
    # --- Khóa các lỗi mẫu đã sửa ở đợt rà soát nhóm 1 ---
    for line in re.findall(r"^- \[ \] Đúng thể thức và định dạng theo (.*)$", t, flags=re.M):
        c["muc_the_thuc_khong_cat_cut"] = not line.rstrip().endswith("…") and not re.search(
            r"\b(phải|nên|giúp|càng|thường)\b", line)
    if name in STRICT_DIAGRAM:  # sơ đồ phải khớp từng số bước của quy trình
        steps = set(re.findall(r"^\*\*Bước (\d+)\.", t, flags=re.M))
        mer = re.search(r"```mermaid(.*?)```", t, flags=re.S)
        c["so_do_khop_so_buoc"] = bool(mer) and steps <= set(re.findall(r"Bước (\d+)", mer.group(1)))
        c["ket_qua_buoc_khong_bao_cao_kiem_tra"] = "Kết quả bước: Báo cáo kiểm tra" not in t
    if "43/2023" in t:
        c["can_cu_thanh_tra_cap_nhat"] = "216/2025" in t and "84/2025" in t
    return c


def doc_checks():
    c = {}
    cap = re.sub(r"https?://\S+", "", read(ROOT / "docs/CAP_NHAT_PHAP_LY.md"))
    c["phap_ly_khong_dinh_chu"] = not re.search(r"[A-Za-zà-ỹÀ-Ỹ]\d{2,3}/\d{4}", cap)
    c["phap_ly_khong_nhan_so"] = not re.search(r"nhan-su-\d", cap)
    return c


def validate():
    manifest = json.loads(read(ROOT / "skills-manifest.json"))
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    records = {x["name"]: x for x in manifest["skills"]}
    errors = {}
    if not (len(skills) == manifest["count"] == len(records)):
        errors["_tong"] = {"so_luong_khop_manifest": False}
    descs = {}
    for p in skills:
        name = p.parent.name
        checks = skill_checks(p, manifest, records)
        descs[name] = yaml.safe_load(read(p).split("---", 2)[1])["description"]
        bad = [k for k, v in checks.items() if not v]
        if bad:
            errors[name] = bad
    for a, b in CONFUSABLE:
        for x, y in ((a, b), (b, a)):
            if x in descs and y not in descs[x]:
                errors.setdefault(x, []).append(f"mo_ta_phai_nhac:{y}")
    bad_docs = [k for k, v in doc_checks().items() if not v]
    if bad_docs:
        errors["_docs"] = bad_docs
    # Hồi quy cho các lỗi nghiệp vụ đã từng gặp.
    reg = {
        "soan-cong-van": ["TUQ. HIỆU TRƯỞNG", "không dùng chữ CV"],
    }
    for n, needles in reg.items():
        txt = read(ROOT / "skills" / n / "SKILL.md")
        miss = [x for x in needles if x not in txt]
        if miss:
            errors.setdefault(n, []).extend("hoi_quy:" + x for x in miss)
    pairs = [
        ("skills/soan-bien-ban-hop/references/quy-cach-dau-ra.md", ["Mẫu 1.9", "số, ký hiệu"]),
        ("skills/bao-cao-tai-chinh/references/quy-cach-dau-ra.md", ["B01/BCTC", "B02/BCTC", "B03/BCTC", "B04/BCTC"]),
        ("skills/chuan-bi-hop-hoi-dong-truong/SKILL.md", ["Không dùng để tổ chức hoạt động mới"]),
        ("skills/ke-hoach-mua-sam/SKILL.md", ["Không suy ra chỉ định thầu/mua sắm trực tiếp chỉ vì nhỏ lẻ hoặc cấp bách"]),
        ("skills/quyet-dinh-tot-nghiep/SKILL.md", ["Không tự triệu tập hội đồng lần nữa"]),
    ]
    for rel, needles in pairs:
        txt = read(ROOT / rel)
        miss = [x for x in needles if x not in txt]
        if miss:
            errors.setdefault(rel, []).extend("hoi_quy:" + x for x in miss)
    if "`thanh_vien`" in read(ROOT / "skills/chuan-bi-hop-hoi-dong-truong/references/quy-trinh-lich-su.md"):
        errors.setdefault("chuan-bi-hop-hoi-dong-truong", []).append("hoi_quy:thanh_vien")
    summary = {
        "version": manifest["version"],
        "skills": len(skills),
        "version_records": len(records),
        "targeted_legal_updates": sum(bool(x["legal_updates"]) for x in records.values()),
        "approval_owner_set": sum(1 for x in records.values() if x.get("approval_owner")),
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(validate())
