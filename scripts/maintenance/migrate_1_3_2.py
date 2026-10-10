"""Di chuyển bộ skill từ 1.3.1 lên 1.3.2 (chạy một lần, có thể chạy lại an toàn).

Việc làm:
1. Nén 3 mục lặp lại ở 171 SKILL.md; giữ bản đầy đủ trong references/quy-tac-chung.md.
   Phần đặc thù của từng skill (nếu có) được giữ nguyên trong SKILL.md.
2. Nén mục "Quản trị phiên bản" thành con trỏ tới references/version.json.
3. Sửa các câu tự mâu thuẫn (kết quả bước "checklist"; nhắc "markdown" khi mặc định là Word/Excel).
4. Nâng phiên bản trong manifest và 171 version.json.

Dùng: python -X utf8 scripts/maintenance/migrate_1_3_2.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NEW_VERSION = "1.3.2"
BASELINE_COMMIT = "d2a835f00b0dbbafa13a66d56551a4f3102311ac"

QC_FULL = None  # đọc từ skill thực tế để so khớp chính xác
QC_SHORT = (
    "Đọc [quy cách và cấu trúc sản phẩm](references/quy-cach-dau-ra.md) trước khi soạn/xuất. "
    "File giao chỉ gồm sản phẩm nghiệp vụ được yêu cầu; kiểm tra nội bộ không xuất kèm. "
    "Thiếu thông tin thì giữ nguyên trường/mục và chỗ điền theo mẫu gốc (dòng dấu chấm, dấu gạch hoặc ô trống); "
    "không tự điền dữ liệu mẫu, số 0, mã chờ xác minh hay dòng chờ ký. "
    "Mẫu chuyên ngành còn áp dụng được ưu tiên về cấu trúc, mã biểu và người ký. "
    "Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md)."
)
KS_SHORT = (
    "Trước khi chạy, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu`, `nguoi_kiem_duyet`; "
    "chỉ hỏi thông tin liên quan nghiệp vụ, không dùng giá trị giả định thay dữ liệu bắt buộc. "
    "Đối chiếu căn cứ pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng và chuyển tiếp. "
    "Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md)."
)
GH_SHORT = (
    "AI hỗ trợ chuẩn bị và đối chiếu; cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. "
    "Không đánh dấu đã ký, đã duyệt, đã công bố khi chưa có chứng cứ. "
    "Dữ liệu sinh viên, sức khỏe, nhân sự, tài chính chỉ dùng theo mục đích và phân quyền, che thông tin định danh khi dùng ví dụ (Luật 91/2025/QH15, hiệu lực 01/01/2026); "
    "không tải dữ liệu lên dịch vụ ngoài khi chưa có quyền. "
    "Bản đầy đủ: [quy tắc chung](references/quy-tac-chung.md)."
)

H_QC = "## Quy cách đầu ra và thông tin thiếu"
H_KS = "## Kiểm soát áp dụng và phê duyệt"
H_GH = "## Giới hạn và human gate"
H_QT = "## Quản trị phiên bản"

# Bản đầy đủ chuẩn (đúng như trong 1.3.1) để nhận diện phần lặp lại.
KS_COMMON = (
    "Trước khi chạy quy trình, xác định `ngay_ap_dung`, `loai_hinh_truong`, `quy_che_noi_bo`, `nguon_du_lieu` "
    "và `nguoi_kiem_duyet`. Chỉ yêu cầu thông tin có liên quan đến nghiệp vụ; không dùng giá trị giả định thay "
    "dữ liệu bắt buộc. Đối chiếu nội bộ hồ sơ có yếu tố pháp lý với văn bản gốc, hiệu lực, điều khoản áp dụng "
    "và chuyển tiếp; không tự đính kèm bảng kiểm tra vào file giao."
)
GH_COMMON = (
    "AI hỗ trợ chuẩn bị và đối chiếu. Cán bộ phụ trách kiểm tra dữ liệu/căn cứ, người có thẩm quyền duyệt và ký. "
    "Văn bản soạn chưa được coi là đã ban hành; không tự chèn nhãn trạng thái kiểm duyệt vào file giao; không đánh dấu "
    "đã ký, đã duyệt hoặc đã công bố nếu chưa có chứng cứ. Dữ liệu sinh viên, sức khỏe, nhân sự và tài chính phải hạn chế "
    "theo mục đích, phân quyền và che thông tin định danh khi dùng ví dụ. Không tải dữ liệu lên dịch vụ ngoài khi chưa có "
    "quyền. Kiểm tra Luật 91/2025/QH15 về bảo vệ dữ liệu cá nhân (hiệu lực 01/01/2026) và quy định áp dụng trước "
    "xử lý/chia sẻ dữ liệu cá nhân."
)


def get_section(text, heading):
    m = re.search(re.escape(heading) + r"\n(.*?)(?=\n## |\Z)", text, re.S)
    return m


def replace_section(text, heading, new_body):
    m = get_section(text, heading)
    start, end = m.start(), m.end()
    return text[:start] + heading + "\n" + new_body.strip("\n") + "\n" + text[end:]


# Sửa câu mâu thuẫn: (skill, mẫu cũ, mẫu mới). Mẫu regex chạy trên toàn SKILL.md của skill.
CHECKLIST_OUT_OLD = "Checklist kiểm tra đã đánh dấu + danh sách lỗi cần sửa (nếu có), trả về bước tương ứng để chỉnh."
CHECKLIST_OUT_NEW = (
    "Kết quả đối chiếu thể thức (giữ nội bộ, không xuất kèm file) + danh sách lỗi cần sửa (nếu có), "
    "trả về bước tương ứng để chỉnh."
)
MARKDOWN_SKILLS = [
    "bao-cao-kiem-toan-noi-bo", "campaign-brief-tuyen-sinh", "content-calendar-truyen-thong", "faq-tuyen-sinh",
    "funnel-theo-doi-thi-sinh", "ke-hoach-hoi-thao-khoa-hoc", "ke-hoach-kiem-toan-noi-bo",
    "ke-hoach-quan-tri-thuong-hieu", "ke-hoach-thanh-tra-nam", "ke-hoach-truyen-thong-nam", "ket-luan-thanh-tra",
    "kich-ban-tu-van-tuyen-sinh", "kich-ban-video-truyen-thong", "lap-lich-cong-tac-tuan",
    "quyet-dinh-giai-quyet-kn", "tham-dinh-phap-ly-van-ban",
]


def fix_markdown_mentions(text):
    text = text.replace("(markdown, sẵn sàng trình ký)", "(sẵn sàng trình ký)")
    text = text.replace("hoàn chỉnh (markdown), sẵn sàng trình ký", "hoàn chỉnh, sẵn sàng trình ký")
    text = text.replace("(bảng markdown)", "(dạng bảng)")
    text = text.replace("Dựng bảng markdown với", "Dựng bảng với")
    text = text.replace(" (markdown)", "")
    return text


def main():
    manifest_path = ROOT / "skills-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    log = {"slimmed": 0, "unique_kept": [], "checklist_fixed": [], "markdown_fixed": []}

    for rec in manifest["skills"]:
        name = rec["name"]
        sdir = ROOT / "skills" / name
        skill_md = sdir / "SKILL.md"
        text = skill_md.read_text(encoding="utf-8")
        original = text
        already = (sdir / "references" / "quy-tac-chung.md").exists()

        # 1. Bản đầy đủ -> references/quy-tac-chung.md (chỉ tạo lần đầu, từ nội dung 1.3.1)
        if not already:
            parts = ["# Quy tắc chung của skill (bản đầy đủ)\n",
                     "Tài liệu này giữ nguyên các quy tắc dùng chung đã rút gọn trong SKILL.md. "
                     "Khi có khác biệt giữa SKILL.md và tài liệu này, áp dụng quy tắc chặt hơn.\n"]
            for h in (H_QC, H_KS, H_GH):
                m = get_section(text, h)
                if m:
                    parts.append(f"{h}\n{m.group(1).strip()}\n")
            (sdir / "references" / "quy-tac-chung.md").write_text("\n".join(parts), encoding="utf-8")

            # 1b. Nén các mục trong SKILL.md
            m = get_section(text, H_QC)
            text = replace_section(text, H_QC, QC_SHORT)

            body = get_section(text, H_KS).group(1).strip()
            if body.startswith(KS_COMMON):
                text = replace_section(text, H_KS, KS_SHORT + body[len(KS_COMMON):])
            else:
                log["unique_kept"].append(f"{name}:{H_KS}")

            body = get_section(text, H_GH).group(1).strip()
            if body == GH_COMMON:
                text = replace_section(text, H_GH, GH_SHORT)
            elif body.endswith(GH_COMMON):
                text = replace_section(text, H_GH, body[: -len(GH_COMMON)].rstrip() + "\n\n" + GH_SHORT)
            else:
                log["unique_kept"].append(f"{name}:{H_GH}")

        # 2. Quản trị phiên bản -> con trỏ
        approval = rec.get("approval_owner") or "**chưa chỉ định**"
        qt = (
            f"- Phiên bản gói `{NEW_VERSION}` (cập nhật 2026-10-10); hồ sơ đầy đủ tại [references/version.json](references/version.json).\n"
            f"- Người phê duyệt nghiệp vụ: {approval}. Trạng thái: dự thảo nghiệp vụ; kiểm tra pháp lý trước thực thi. "
            "Ngày cập nhật không đồng nghĩa mọi văn bản đã được rà soát toàn văn.\n"
            "- Giấy phép theo LICENSE của kho (bản quyền CES Global). Lịch sử thay đổi: CHANGELOG.md."
        )
        text = replace_section(text, H_QT, qt)

        # 3. Sửa mâu thuẫn
        if CHECKLIST_OUT_OLD in text:
            text = text.replace(CHECKLIST_OUT_OLD, CHECKLIST_OUT_NEW)
            log["checklist_fixed"].append(name)
        old_hb = "Kết quả bước: checklist kiểm tra đã đánh dấu (đủ 6 mục, thể thức, số liệu, nơi nhận)."
        if old_hb in text:
            text = text.replace(old_hb, "Kết quả bước: kết quả đối chiếu nội bộ (đủ 6 mục, thể thức, số liệu, nơi nhận); không xuất kèm file.")
            log["checklist_fixed"].append(name)
        if name in MARKDOWN_SKILLS:
            fixed = fix_markdown_mentions(text)
            if fixed != text:
                log["markdown_fixed"].append(name)
            text = fixed

        if text != original:
            skill_md.write_text(text, encoding="utf-8")
            log["slimmed"] += 1

        # 4. Nâng phiên bản
        rec["version"] = NEW_VERSION
        rec["source_commit"] = BASELINE_COMMIT
        (sdir / "references" / "version.json").write_text(
            json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    manifest["version"] = NEW_VERSION
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(log, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
