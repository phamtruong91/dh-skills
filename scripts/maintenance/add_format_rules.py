"""Đưa quy tắc thể thức/bảng biểu vào skill (chạy lại an toàn).

1. Thêm mục "Thể thức và bảng biểu khi dựng file" vào references/quy-cach-dau-ra.md của mọi skill xuất Word/Excel.
2. Thêm một câu dẫn vào SKILL.md.
3. Bổ sung trường đầu vào còn thiếu cho 9 skill văn bản hành chính chính và gắn vào bước dùng chúng.
Dùng: python -X utf8 scripts/maintenance/add_format_rules.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MARK = "## Thể thức và bảng biểu khi dựng file"
SKILL_NOTE = "Khi dựng file Word/Excel, áp dụng mục “Thể thức và bảng biểu khi dựng file” trong quy cách đầu ra (cỡ chữ từng thành phần, bảng nhiều trang, số trang, phụ lục)."

BASE = """- Khổ A4; Times New Roman đen; nội dung canh đều hai lề, thụt đầu dòng 1 cm, cách đoạn tối thiểu 6 pt, giãn dòng từ đơn đến 1,5. Số trang chữ số Ả Rập, giữa lề trên, cỡ 13–14, không hiện ở trang đầu.
- Tiêu đề IN HOA ngắt dòng cân đối, không để một chữ rơi xuống dòng riêng; thiếu dữ liệu thì để trống theo mẫu.
- Bảng: bố cục cố định, tổng bề rộng không vượt vùng chữ; cột STT rộng tối thiểu 1,4 cm (để "STT" không tách dòng); cột STT, mã, lớp, ngày, đơn vị căn giữa, cột họ tên và nội dung dài căn trái, cột số tiền căn thống nhất cả cột; chữ cỡ 11–13 (khuyến nghị 12; 11 khi từ 7 cột).
- Dòng tiêu đề bảng đậm, nền xám nhạt, lặp ở đầu mỗi trang; mọi dòng cao tối thiểu như nhau, căn giữa theo chiều dọc, có khoảng đệm trên dưới; dòng không bị cắt giữa hai trang; STT liên tục từ 1; dòng tổng cộng ở cuối bảng.
- Danh sách hoặc bảng kèm theo là phụ lục: bắt đầu ở trang mới, ghi "Kèm theo ... số ... ngày ..." (để trống nếu chưa có), đánh số trang riêng từ 1. Khối chữ ký cùng trang với ít nhất một đoạn nội dung cuối.
- Mở file xem bố cục thực tế trước khi giao; kiểm tra tự động không thay việc này."""
HC = """- Phần đầu theo Phụ lục I Nghị định 30/2020: quốc hiệu 12–13 đậm hoa; tiêu ngữ viết "Độc lập - Tự do - Hạnh phúc" (gạch ngang), 13–14 đậm, có đường kẻ dưới; tên cơ quan chủ quản 12–13 hoa không đậm; tên cơ quan ban hành 12–13 hoa đậm, có đường kẻ dưới; số, ký hiệu cỡ 13; địa danh, ngày tháng năm 13–14 nghiêng; tên loại văn bản 13–14 hoa đậm; chức vụ người ký hoa đậm, họ tên đậm.
- Nhãn "Nơi nhận:" cỡ 12 đậm nghiêng (đặt định dạng cho cả đoạn); danh sách nơi nhận cỡ 11 thường. Tên cơ quan ở phần đầu không ngắt chữ giữa chừng: chia bề rộng hai cột cho đủ chỗ.
- Số chưa cấp và ngày chưa ký để dòng dấu chấm; không tự điền."""
XL = """- Dòng tiêu đề đậm, nền nhạt, cố định (freeze) khi bảng dài; bề rộng cột vừa chữ; số tiền có dấu phân cách hàng nghìn; ngày theo dd/mm/yyyy; giữ công thức, không dán giá trị thay công thức.
- Đặt vùng in và lặp dòng tiêu đề khi in; dữ liệu khác bản chất để ở sheet riêng; ô thiếu dữ liệu để trống, không ghi 0.
- Mở file kiểm tra công thức đã tính, không có lỗi `#`, định dạng hiển thị đúng trước khi giao."""

HEAD_FIELDS = [
    ("co_quan_chu_quan", "Tên cơ quan chủ quản trực tiếp (chỉ khi trường có cấp trên; trường tư thục thường không có)", "Không"),
    ("co_quan_ban_hanh", "Tên cơ quan ban hành văn bản (thường là trường), khác với đơn vị soạn thảo", "Có"),
    ("dia_danh", "Địa danh ghi ở dòng ngày tháng năm", "Có"),
    ("so_van_ban", "Số, ký hiệu văn bản đã được cấp (để trống nếu chưa cấp; không tự đặt)", "Không"),
]
NOI_NHAN = ("noi_nhan", "Danh sách nơi nhận, gồm cả nơi lưu (VT, đơn vị soạn)", "Có")
NGUOI_KY = ("nguoi_ky", "Chức danh, họ tên người ký; hình thức TM./KT./TL./TUQ. chỉ khi có căn cứ", "Có")
NGUOI_MOI = ("nguoi_duoc_moi", "Họ tên, chức danh từng người được mời (nếu có danh sách)", "Không")
HEAD_TXT = "Phần đầu văn bản lấy từ `co_quan_chu_quan` (nếu có), `co_quan_ban_hanh`, `dia_danh`, `so_van_ban` (để dòng dấu chấm nếu chưa cấp số)."
NN_TXT = "Nơi nhận lấy từ `noi_nhan`."
NK_TXT = "Khối ký lấy từ `nguoi_ky`."

HF = [f[0] for f in HEAD_FIELDS]
CFG = {
    "soan-cong-van": {"rows": HEAD_FIELDS, "steps": {3: (HF, HEAD_TXT)}},
    "soan-thong-bao": {"rows": HEAD_FIELDS + [NOI_NHAN], "steps": {3: (HF, HEAD_TXT), 5: (["noi_nhan"], NN_TXT)}},
    "soan-bien-ban-hop": {"rows": HEAD_FIELDS + [NOI_NHAN], "steps": {2: (HF, HEAD_TXT), 5: (["noi_nhan"], NN_TXT)}},
    "soan-to-trinh": {"rows": HEAD_FIELDS + [NOI_NHAN, NGUOI_KY], "steps": {5: (HF + ["noi_nhan", "nguoi_ky"], HEAD_TXT + " " + NN_TXT + " " + NK_TXT)}},
    "soan-giay-moi": {"rows": HEAD_FIELDS + [NOI_NHAN, NGUOI_MOI], "steps": {2: (["nguoi_duoc_moi"], "Dòng \"Kính mời\" lấy từ `nguoi_duoc_moi`; thiếu thì để dòng dấu chấm."),
                                                                          5: (HF + ["noi_nhan"], HEAD_TXT + " " + NN_TXT)}},
    "soan-quyet-dinh-hc": {"rows": HEAD_FIELDS + [NOI_NHAN], "steps": {4: (HF, HEAD_TXT), 5: (["noi_nhan"], NN_TXT)}},
    "soan-ke-hoach-ct": {"rows": HEAD_FIELDS + [NOI_NHAN, NGUOI_KY], "steps": {7: (HF + ["noi_nhan", "nguoi_ky"], HEAD_TXT + " " + NN_TXT + " " + NK_TXT)}},
    "quyet-dinh-cap-hoc-bong": {"rows": HEAD_FIELDS + [NOI_NHAN], "steps": {3: (HF + ["noi_nhan"], HEAD_TXT + " " + NN_TXT)}},
    "thong-bao-hoc-bong": {"rows": HEAD_FIELDS + [NOI_NHAN], "steps": {2: (HF + ["noi_nhan"], HEAD_TXT + " " + NN_TXT)}},
}


def add_inputs(name, cfg):
    p = ROOT / "skills" / name / "SKILL.md"
    t = p.read_text(encoding="utf-8")
    if "`co_quan_ban_hanh`" in t.split("## Quy trình")[0]:
        return False
    head, rest = t.split("## Quy trình", 1)
    rows = [r for r in cfg["rows"] if f"`{r[0]}`" not in head]
    last = [m for m in re.finditer(r"^\| `[^`]+` \|.*\|[ \t]*$", head, flags=re.M)][-1]
    ins = "\n".join(f"| `{f}` | {d} | {rq} |" for f, d, rq in rows)
    head = head[:last.end()] + "\n" + ins + head[last.end():]
    # gắn vào bước
    for n, (fields, txt) in cfg["steps"].items():
        m = re.search(rf"^\*\*Bước {n}\.[^\n]*\n", rest, flags=re.M)
        nxt = re.search(r"^\*\*Bước \d+\.", rest[m.end():], flags=re.M)
        end = m.end() + (nxt.start() if nxt else len(rest) - m.end())
        blk = rest[m.end():end]
        blk = re.sub(r"(- Làm gì:[^\n]*)", lambda x: x.group(1).rstrip() + " " + txt, blk, count=1)
        def add_f(x):
            line = x.group(0)
            extra = ", ".join(f"`{f}`" for f in fields if f"`{f}`" not in line)
            if not extra:
                return line
            return (line.rstrip().rstrip(".") + ", " + extra + ".") if "`" in line else line.rstrip() + " " + extra + "."
        blk = re.sub(r"- Dùng input:[^\n]*", add_f, blk, count=1)
        rest = rest[:m.end()] + blk + rest[end:]
    p.write_text(head + "## Quy trình" + rest, encoding="utf-8")
    return True


def main():
    m = json.loads((ROOT / "skills-manifest.json").read_text(encoding="utf-8"))["skills"]
    n_q = n_s = n_i = 0
    for s in m:
        name, fmt, prof = s["name"], s["default_output_format"], s["output_profile"]
        sd = ROOT / "skills" / name
        qp = sd / "references/quy-cach-dau-ra.md"
        if fmt in ("docx", "xlsx"):
            q = qp.read_text(encoding="utf-8")
            if MARK not in q:
                body = (XL if fmt == "xlsx" else BASE + ("\n" + HC if prof == "hanh-chinh" else ""))
                q = q.rstrip("\n") + f"\n\n{MARK}\n\n{body}\n"
                qp.write_text(q, encoding="utf-8")
                n_q += 1
            sp = sd / "SKILL.md"
            t = sp.read_text(encoding="utf-8")
            if SKILL_NOTE not in t:
                t = t.replace("## Quy cách đầu ra và thông tin thiếu\n", "## Quy cách đầu ra và thông tin thiếu\n" + SKILL_NOTE + " ", 1)
                sp.write_text(t, encoding="utf-8")
                n_s += 1
    for name, cfg in CFG.items():
        n_i += add_inputs(name, cfg)
    print(f"quy cách: {n_q}; SKILL.md: {n_s}; skill thêm đầu vào: {n_i}")


if __name__ == "__main__":
    main()
