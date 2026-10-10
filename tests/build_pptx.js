// Thử các skill có thể xuất PowerPoint bằng dữ liệu GIẢ (cố định, lặp lại được).
// Đóng vai "AI làm theo SKILL.md" (không phải AI độc lập): dựng bằng pptxgenjs, biểu đồ gốc (sửa được trong PowerPoint).
// Dùng: node tests/build_pptx.js   (cần pptxgenjs và kỹ năng pptx ở /mnt/skills/public/pptx)
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");
const { applyTheme } = require("/mnt/skills/public/pptx/scripts/apply_theme.js");

const HERE = __dirname;
const OUT = path.join(HERE, "outputs");
const SAMPLES = path.join(HERE, "samples");
const RESULTS = path.join(HERE, "results");
for (const d of [OUT, SAMPLES, RESULTS]) fs.mkdirSync(d, { recursive: true });
const NOTE = "Dữ liệu GIẢ để thử. Tên trường, người, số liệu đều là mẫu.";

const THEME = {
  name: "Thu nghiem",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: { dk1: "1B1F2A", lt1: "FFFFFF", dk2: "0F3D3E", lt2: "EEF3F2", accent1: "0F6E6E", accent2: "D9822B", accent3: "5B8DB8",
    accent4: "7A8B8B", accent5: "B5473A", accent6: "3E7C4F", hlink: "0F6E6E", folHlink: "7A8B8B" },
};

function newDeck(title) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
  pres.title = title;
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;
  pres.defineSlideMaster({
    title: "TITLE", background: { color: "0F3D3E" },
    slideNumber: undefined,
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.5, w: 8.8, h: 1.5, fontSize: 36, bold: true, color: "FFFFFF", valign: "bottom", align: "left", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "sub", type: "body", x: 0.6, y: 3.2, w: 8.8, h: 1.0, fontSize: 18, color: "CFE3E1", valign: "top", align: "left", margin: 0 }, text: "" } },
    ],
  });
  pres.defineSlideMaster({
    title: "CONTENT", background: { color: "FFFFFF" },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.3, w: 9.0, h: 0.95, fontSize: 28, bold: true, color: "0F3D3E", valign: "middle", align: "left", margin: 0 }, text: "" } },
    ],
  });
  return pres;
}

function ensureSection(pres, section) {
  pres._secs = pres._secs || new Set();
  if (section && !pres._secs.has(section)) {
    pres.addSection({ title: section });
    pres._secs.add(section);
  }
}
function titleSlide(pres, title, sub, notes, section) {
  ensureSection(pres, section);
  const s = pres.addSlide({ masterName: "TITLE", sectionTitle: section });
  s.addText(title, { placeholder: "title", align: "left" });
  s.addText(sub, { placeholder: "sub", align: "left" });
  s.addNotes(notes);
  return s;
}
function contentSlide(pres, title, notes, section) {
  ensureSection(pres, section);
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
  s.addText(title, { placeholder: "title", align: "left" });
  s.addNotes(notes);
  return s;
}
function source(s, text) {
  s.addText(text, { x: 0.5, y: 5.05, w: 9.0, h: 0.35, fontSize: 11, italic: true, color: "5A6666", isTextBox: true, margin: 0, objectName: "nguon" });
}
function stat(s, x, y, w, big, label, accent) {
  s.addShape("roundRect", { x, y, w, h: 1.9, fill: { color: "EEF3F2" }, line: { color: "EEF3F2" }, rectRadius: 0.1, objectName: "the" });
  s.addText(big, { x: x + 0.15, y: y + 0.15, w: w - 0.3, h: 0.9, fontSize: 40, bold: true, color: accent || "0F6E6E", fontFace: "Cambria", isTextBox: true, margin: 0, valign: "middle", objectName: "so-lieu" });
  s.addText(label, { x: x + 0.15, y: y + 1.05, w: w - 0.3, h: 0.75, fontSize: 14, color: "1B1F2A", isTextBox: true, margin: 0, valign: "top", objectName: "nhan" });
}
const CHART_BASE = { catAxisLabelFontSize: 12, valAxisLabelFontSize: 12, dataLabelFontSize: 12, legendFontSize: 12, catAxisLabelColor: "1B1F2A", valAxisLabelColor: "1B1F2A",
  dataLabelColor: "1B1F2A", valGridLine: { color: "D9E0DF", size: 0.5 }, catGridLine: { style: "none" }, showValue: true, legendPos: "b", valAxisTitleFontSize: 12, catAxisTitleFontSize: 12,
  valAxisLineShow: false };
function bullets(items, size = 18) {
  return items.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < items.length - 1, fontSize: size, paraSpaceAfter: 8, color: "1B1F2A" } }));
}
function table(s, rows, opts) {
  const head = rows[0].map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: "0F3D3E" }, fontSize: 14, valign: "middle" } }));
  const body = rows.slice(1).map((r) => r.map((t, c) => ({ text: t, options: { fontSize: 14, color: "1B1F2A", valign: "middle", bold: c === 0 } })));
  s.addTable([head, ...body], Object.assign({ x: 0.5, y: 1.45, w: 9.0, border: { type: "solid", pt: 0.75, color: "B8C4C3" }, margin: [0.06, 0.1, 0.06, 0.1], objectName: "bang" }, opts));
}
async function save(pres, name, input, expect, findings) {
  const file = path.join(OUT, `${name}.pptx`);
  await pres.writeFile({ fileName: file });
  await applyTheme(file, THEME);
  fs.writeFileSync(path.join(SAMPLES, `${name}.input.json`), JSON.stringify(Object.assign({ _ghi_chu: NOTE }, input), null, 1));
  fs.writeFileSync(path.join(SAMPLES, `${name}.expect.json`), JSON.stringify(Object.assign({ skill: name, output: `${name}.pptx`, kind: "pptx" }, expect), null, 1));
  fs.writeFileSync(path.join(RESULTS, `${name}.findings.md`), `# Phát hiện khi chạy thử xuất PowerPoint: ${name} (dữ liệu giả)\n\n${findings}`);
  console.log("đã tạo", file);
}
const vn = (x, nd = 1) => x.toFixed(nd).replace(".", ",");
const money = (n) => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ".");

// =====================================================================
// 1. bao-cao-tong-ket-nam-truong -> bộ slide hội nghị tổng kết
// =====================================================================
async function deckTongKet() {
  const nganh = [["Công nghệ thông tin", 600, 571], ["Kinh tế", 500, 462], ["Ngoại ngữ", 400, 352], ["Luật", 300, 257]];
  const chiTieu = nganh.reduce((a, r) => a + r[1], 0), nhapHoc = nganh.reduce((a, r) => a + r[2], 0);
  const tn = [["2022–2023", 78], ["2023–2024", 81], ["2024–2025", 84]];
  const chi = [["Lương và phụ cấp", 210000], ["Đào tạo", 98500], ["Cơ sở vật chất", 60000], ["Khác", 30000]];
  const tongChi = chi.reduce((a, r) => a + r[1], 0);
  const input = {
    nam_hoc: "2025–2026", co_so: "Trường Đại học Mẫu A", thoi_gian_trinh_bay_phut: 20,
    bao_cao_don_vi: { dao_tao: { tuyen_sinh: nganh.map(([n, a, b]) => ({ nganh: n, chi_tieu: money(a), nhap_hoc: money(b) })),
        ty_le_tot_nghiep_dung_han_phan_tram: { "2022–2023": 78, "2023–2024": 81, "2024–2025": 84, "2025–2026": null }, nhan_xet_khai_bao: "Tăng 8 điểm phần trăm so với 2022–2023" },
      tai_chinh: { thu_trieu_dong: money(412000), chi_theo_nhom_trieu_dong: chi.map(([n, v]) => ({ nhom: n, so_tien: money(v) })), tong_chi_khai_bao_trieu_dong: money(400000) },
      cong_tac_sinh_vien: null,
      ton_tai: [["Cơ sở vật chất giảng đường chưa đáp ứng giờ cao điểm", "Số phòng học không tăng trong khi quy mô tăng"], ["Tỷ lệ nhập học Luật còn thấp", "Chưa có kênh tư vấn riêng cho ngành"], ["Báo cáo đơn vị nộp chậm", "Chưa có mốc nộp thống nhất"]] },
    dinh_huong_chung: null,
  };
  const pres = newDeck("Tổng kết năm học 2025–2026");
  titleSlide(pres, "Tổng kết năm học 2025–2026", "Hội nghị tổng kết · Trường Đại học Mẫu A (tên mẫu)",
    "Mở đầu: nêu phạm vi báo cáo gồm đào tạo, tài chính, tồn tại và phương hướng. Báo cáo của Phòng Công tác sinh viên chưa nhận được nên phần này chưa trình bày.", "Mở đầu");
  let s = contentSlide(pres, "Năm học 2025–2026 nhập học đạt 91,2% chỉ tiêu", "Ba con số cần nhớ: tỷ lệ nhập học theo chỉ tiêu, tỷ lệ tốt nghiệp đúng hạn năm gần nhất có số liệu, và tổng thu. Mọi số lấy từ báo cáo các đơn vị.", "Kết quả");
  stat(s, 0.5, 1.5, 2.85, `${vn((100 * nhapHoc) / chiTieu)}%`, `nhập học ${money(nhapHoc)} trên chỉ tiêu ${money(chiTieu)}`);
  stat(s, 3.575, 1.5, 2.85, "84%", "tốt nghiệp đúng hạn, năm học 2024–2025 (năm gần nhất có số liệu)", "D9822B");
  stat(s, 6.65, 1.5, 2.85, `${money(412000)}`, "triệu đồng tổng thu năm học", "0F6E6E");
  source(s, "Nguồn: báo cáo Phòng Đào tạo và Phòng Kế hoạch – Tài chính, năm học 2025–2026");
  s = contentSlide(pres, "Ngành Luật nhập học thấp nhất so với chỉ tiêu", "So sánh chỉ tiêu và nhập học theo ngành. Luật đạt 85,7%, Ngoại ngữ 88,0%, Kinh tế 92,4%, Công nghệ thông tin 95,2%.", "Kết quả");
  s.addChart(pres.charts.BAR, [{ name: "Chỉ tiêu", labels: nganh.map((r) => r[0]), values: nganh.map((r) => r[1]) }, { name: "Nhập học", labels: nganh.map((r) => r[0]), values: nganh.map((r) => r[2]) }],
    Object.assign({}, CHART_BASE, { x: 0.5, y: 1.35, w: 9.0, h: 3.6, barDir: "col", barGrouping: "clustered", chartColors: ["B8C4C3", "0F6E6E"], showLegend: true, showValAxisTitle: true, valAxisTitle: "Số sinh viên", valAxisMinVal: 0, objectName: "bieu-do" }));
  source(s, "Nguồn: báo cáo Phòng Đào tạo, năm học 2025–2026");
  s = contentSlide(pres, "Tốt nghiệp đúng hạn tăng 6 điểm phần trăm sau hai năm", "Từ 78% lên 84%. Lưu ý: nhận xét trong đầu vào nêu chênh lệch 8 điểm, nhưng tính lại 84 trừ 78 là 6 điểm; slide dùng số tính lại. Năm học 2025–2026 chưa xét tốt nghiệp nên chưa có số liệu, không ghi 0.", "Kết quả");
  s.addChart(pres.charts.LINE, [{ name: "Tốt nghiệp đúng hạn", labels: tn.map((r) => r[0]), values: tn.map((r) => r[1]) }],
    Object.assign({}, CHART_BASE, { x: 0.5, y: 1.35, w: 6.2, h: 3.6, chartColors: ["0F6E6E"], lineSize: 3, lineDataSymbolSize: 9, showLegend: false, showValAxisTitle: true, valAxisTitle: "% sinh viên", valAxisMinVal: 60, valAxisMaxVal: 100, objectName: "bieu-do" }));
  s.addText([{ text: "2025–2026", options: { bold: true, breakLine: true, fontSize: 18 } }, { text: "Chưa có số liệu: năm học chưa xét tốt nghiệp", options: { fontSize: 16 } }],
    { x: 7.0, y: 1.9, w: 2.5, h: 1.6, color: "1B1F2A", isTextBox: true, margin: 0, valign: "top", objectName: "ghi-chu" });
  source(s, "Nguồn: báo cáo Phòng Đào tạo. Năm học 2025–2026 chưa có số liệu");
  s = contentSlide(pres, "Lương và phụ cấp chiếm hơn một nửa chi", "Cơ cấu chi theo nhóm, đơn vị triệu đồng. Tổng các nhóm là 398.500 triệu đồng, trong khi báo cáo khai tổng chi 400.000 triệu đồng; chênh 1.500 triệu đồng chưa giải thích, đề nghị Phòng Kế hoạch – Tài chính rà lại trước hội nghị.", "Kết quả");
  s.addChart(pres.charts.BAR, [{ name: "Chi", labels: chi.map((r) => r[0]), values: chi.map((r) => r[1]) }],
    Object.assign({}, CHART_BASE, { x: 0.5, y: 1.35, w: 6.0, h: 3.6, barDir: "bar", chartColors: ["0F6E6E"], showLegend: false, showValAxisTitle: true, valAxisTitle: "Triệu đồng", dataLabelFormatCode: "#,##0", valAxisMinVal: 0, objectName: "bieu-do" }));
  s.addShape("roundRect", { x: 6.8, y: 1.9, w: 2.7, h: 2.1, fill: { color: "FBEEDD" }, line: { color: "D9822B", pt: 1 }, rectRadius: 0.1, objectName: "luu-y" });
  s.addText([{ text: "Cần rà lại", options: { bold: true, breakLine: true, fontSize: 16 } }, { text: `Cộng các nhóm: ${money(tongChi)}. Báo cáo khai: ${money(400000)}.`, options: { fontSize: 14 } }],
    { x: 6.95, y: 2.0, w: 2.4, h: 1.9, color: "1B1F2A", isTextBox: true, margin: 0, valign: "top", objectName: "luu-y-chu" });
  source(s, "Nguồn: báo cáo Phòng Kế hoạch – Tài chính, năm học 2025–2026 (đơn vị: triệu đồng)");
  s = contentSlide(pres, "Công tác sinh viên: đang chờ báo cáo của đơn vị", "Phòng Công tác sinh viên chưa gửi báo cáo, nên slide này chưa có nội dung. Không điền số liệu thay đơn vị; cập nhật khi nhận được.", "Kết quả");
  s.addShape("roundRect", { x: 1.5, y: 1.9, w: 7.0, h: 2.2, fill: { color: "EEF3F2" }, line: { color: "B8C4C3", pt: 1 }, rectRadius: 0.1, objectName: "cho-bao-cao" });
  s.addText("Chưa nhận được báo cáo của Phòng Công tác sinh viên. Nội dung sẽ được bổ sung khi có số liệu.", { x: 1.8, y: 2.1, w: 6.4, h: 1.8, fontSize: 20, color: "1B1F2A", isTextBox: true, margin: 0, valign: "middle", objectName: "cho-bao-cao-chu" });
  s = contentSlide(pres, "Ba tồn tại chính cần xử lý năm học tới", "Mỗi tồn tại đi kèm nguyên nhân do đơn vị nêu. Trình bày thẳng, không giảm nhẹ.", "Tồn tại và phương hướng");
  const tt = input.bao_cao_don_vi.ton_tai;
  tt.forEach(([a, b], i) => {
    const y = 1.45 + i * 1.18;
    s.addShape("ellipse", { x: 0.5, y: y + 0.1, w: 0.7, h: 0.7, fill: { color: "0F6E6E" }, line: { color: "0F6E6E" }, objectName: "so-thu-tu" });
    s.addText(String(i + 1), { x: 0.5, y: y + 0.1, w: 0.7, h: 0.7, fontSize: 20, bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "so-thu-tu-chu" });
    s.addText([{ text: a, options: { bold: true, breakLine: true, fontSize: 18 } }, { text: `Nguyên nhân: ${b}`, options: { fontSize: 14, color: "4A5656" } }],
      { x: 1.45, y, w: 8.0, h: 1.0, color: "1B1F2A", isTextBox: true, margin: 0, valign: "middle", objectName: "ton-tai" });
  });
  s = contentSlide(pres, "Phương hướng năm học tới: chờ định hướng của Ban Giám hiệu", "Đầu vào không có định hướng chung của Ban Giám hiệu, nên chưa nêu chỉ tiêu hay giải pháp mới. Chỉ ghi các việc hiển nhiên từ tồn tại; cập nhật khi có chỉ đạo.", "Tồn tại và phương hướng");
  s.addText(bullets(["Giải quyết ba tồn tại ở slide trước", "Chỉ tiêu và giải pháp: chờ định hướng của Ban Giám hiệu"], 20), { x: 0.5, y: 1.6, w: 9.0, h: 2.4, isTextBox: true, margin: 0, valign: "top", objectName: "noi-dung" });
  titleSlide(pres, "Trân trọng cảm ơn", "Trao đổi và góp ý", "Kết thúc phần trình bày. Dành thời gian cho các đơn vị góp ý, ghi nhận các ý kiến để bổ sung báo cáo công tác sinh viên và rà lại số liệu chi.", "Tồn tại và phương hướng");
  const expect = {
    must_contain: ["Tổng kết năm học 2025–2026", "91,2%", "tăng 6 điểm", "Chưa có số liệu", "Chưa nhận được báo cáo của Phòng Công tác sinh viên", "chờ định hướng"],
    must_not_contain: ["tăng 8 điểm", "Tăng 8 điểm", "400.000 triệu đồng tổng chi"],
    allowed_derived: [money(chiTieu), money(nhapHoc), money(tongChi), "1.500"],
    deck: { min_slides: 8, max_slides: 12, min_title_pt: 28, min_body_pt: 14, min_caption_pt: 11, max_words_per_slide: 85, notes_required: true, talk_minutes: 20,
      charts: [{ slide: 3, type: "bar", series: { "Chỉ tiêu": nganh.map((r) => r[1]), "Nhập học": nganh.map((r) => r[2]) } },
        { slide: 4, type: "line", series: { "Tốt nghiệp đúng hạn": tn.map((r) => r[1]) } }, { slide: 5, type: "bar", series: { "Chi": chi.map((r) => r[1]) } }] },
    traps: [{ id: "NHAN_XET_SAI_SO", mo_ta: "Đầu vào ghi tăng 8 điểm, tính lại 6 điểm" }, { id: "TONG_CHI_LECH", mo_ta: "Cộng nhóm 398.500, khai 400.000" },
      { id: "NAM_CHUA_CO_SO_LIEU", mo_ta: "Tốt nghiệp 2025–2026 chưa có: không ghi 0" }, { id: "DON_VI_CHUA_BAO_CAO", mo_ta: "Công tác sinh viên chưa nộp: không bịa" },
      { id: "THIEU_DINH_HUONG", mo_ta: "Không có định hướng BGH: không bịa chỉ tiêu" }, { id: "KHONG_PHAI_BAO_CAO_VAN_BAN", mo_ta: "Bộ slide không dùng thể thức văn bản hành chính" }],
  };
  const f = `- **NHAN_XET_SAI_SO**: đầu vào ghi "tăng 8 điểm phần trăm so với 2022–2023", nhưng 84 − 78 = 6. Tiêu đề slide dùng số tính lại (6); ghi chú người trình bày nêu rõ lệch.\n` +
    `- **TONG_CHI_LECH**: cộng các nhóm chi được ${money(tongChi)}, đầu vào khai 400.000 triệu đồng. Biểu đồ vẽ theo từng nhóm; slide có ô "Cần rà lại" nêu cả hai số, không tự chọn.\n` +
    `- **NAM_CHUA_CO_SO_LIEU**: tỷ lệ tốt nghiệp 2025–2026 là null; đường không có điểm thứ tư, bên cạnh ghi "Chưa có số liệu" (không ghi 0).\n` +
    `- **DON_VI_CHUA_BAO_CAO**: công tác sinh viên null; slide báo rõ chưa nhận được báo cáo, không điền. Câu hỏi mở: trong buổi trình bày thật, có nên bỏ hẳn slide này không? Đang giữ để người xem thấy phần còn thiếu.\n` +
    `- **THIEU_DINH_HUONG**: định hướng chung null; slide phương hướng chỉ nêu việc xử lý ba tồn tại và ghi chờ chỉ đạo.\n` +
    `- **KHONG_PHAI_BAO_CAO_VAN_BAN**: skill gốc mô tả báo cáo tổng kết là văn bản hành chính (quốc hiệu, nơi nhận, chữ ký). Bộ slide là tài liệu trình bày tách biệt, không có quốc hiệu/chữ ký; skill chưa nói rõ điều này (xem kết luận).\n`;
  await save(pres, "bao-cao-tong-ket-nam-truong", input, expect, f);
}

// =====================================================================
// 2. executive-brief-trinh-lanh-dao
// =====================================================================
async function deckBrief() {
  const input = {
    van_de: "Có nên nâng cấp hệ thống wifi giảng đường trong năm học này không, và theo phương án nào?", thoi_han_quyet_dinh: null,
    tieu_chi_quyet_dinh: ["Chi phí", "Thời gian triển khai", "Rủi ro", "Phù hợp chiến lược"],
    nguon_tai_lieu: ["Báo cáo khảo sát sinh viên học kỳ 1 năm học 2026–2027", "Báo giá NCC-01 (mẫu)"],
    so_lieu: { diem_wifi: "2,77", ty_le_y_kien_wifi: "33,3%", so_y_kien: "120/360", chi_phi_a: "1.200 triệu đồng" },
    phuong_an: [
      { ten: "A. Nâng cấp toàn bộ một lần", chi_phi: { gia_tri: "1.200 triệu", nguon: "Báo giá NCC-01" }, thoi_gian: { gia_tri: "4 tháng", nguon: "Báo giá NCC-01" }, rui_ro: { gia_tri: "Gián đoạn lịch học", nguon: "Ý kiến phòng Đào tạo" }, chien_luoc: { gia_tri: "Phù hợp kế hoạch CĐS", nguon: "Kế hoạch chuyển đổi số" } },
      { ten: "B. Nâng cấp theo hai giai đoạn", chi_phi: { gia_tri: "700 triệu (giai đoạn 1)", nguon: "Báo giá NCC-01" }, thoi_gian: { gia_tri: "2 tháng + 3 tháng", nguon: "Báo giá NCC-01" }, rui_ro: { gia_tri: "Giai đoạn 2 chưa có vốn", nguon: "Phòng Tài chính" }, chien_luoc: { gia_tri: null, nguon: null } },
      { ten: "C. Thuê dịch vụ trọn gói", chi_phi: { gia_tri: null, nguon: null }, thoi_gian: { gia_tri: "Chưa có báo giá", nguon: null }, rui_ro: { gia_tri: "Phụ thuộc nhà cung cấp", nguon: "Ý kiến phòng Quản trị" }, chien_luoc: { gia_tri: null, nguon: null } },
    ],
  };
  const pres = newDeck("Executive brief: nâng cấp wifi giảng đường");
  titleSlide(pres, "Nâng cấp wifi giảng đường: cần quyết định gì", "Executive brief · Thời hạn quyết định: chưa xác định",
    "Tài liệu dành cho lãnh đạo đọc trước cuộc họp. Vấn đề cần quyết định được nêu ở slide này; thời hạn quyết định chưa có trong đầu vào nên để trống.", "Brief");
  let s = contentSlide(pres, "Sinh viên chấm wifi thấp nhất trong các câu hỏi", "Bối cảnh: khảo sát học kỳ 1 năm học 2026–2027. Wifi đạt 2,77 điểm, là mức cần cải thiện theo quy ước dưới 3,0. Trong 360 phiếu có ý kiến mở, 120 phiếu nói về wifi.", "Brief");
  stat(s, 0.5, 1.5, 2.85, "2,77", "điểm trung bình câu 'Mạng wifi ổn định' (thang 1–5)", "B5473A");
  stat(s, 3.575, 1.5, 2.85, "33,3%", "ý kiến mở nói về wifi (120 trên 360)", "B5473A");
  stat(s, 6.65, 1.5, 2.85, "1.200", "triệu đồng, chi phí phương án A theo báo giá", "0F6E6E");
  source(s, "Nguồn: báo cáo khảo sát sinh viên học kỳ 1 năm học 2026–2027; báo giá NCC-01 (mẫu)");
  s = contentSlide(pres, "Ba phương án, nhưng mới đủ số liệu cho hai", "Ô để trống nghĩa là chưa có số liệu kèm nguồn. Không tự điền. Phương án C chưa có báo giá nên chưa so được chi phí; phương án B thiếu đánh giá về phù hợp chiến lược.", "Brief");
  const SHORT = { "Báo giá NCC-01": "NCC-01", "Ý kiến phòng Đào tạo": "P. Đào tạo", "Phòng Tài chính": "P. Tài chính", "Ý kiến phòng Quản trị": "P. Quản trị", "Kế hoạch chuyển đổi số": "KH chuyển đổi số" };
  const row = (k, lbl) => [lbl].concat(input.phuong_an.map((p) => (p[k].gia_tri ? `${p[k].gia_tri}` + (p[k].nguon ? ` (${SHORT[p[k].nguon] || p[k].nguon})` : "") : "Chưa có số liệu")));
  table(s, [["Tiêu chí", "A. Toàn bộ", "B. Hai giai đoạn", "C. Thuê dịch vụ"], row("chi_phi", "Chi phí"), row("thoi_gian", "Thời gian"), row("rui_ro", "Rủi ro"), row("chien_luoc", "Phù hợp chiến lược")],
    { colW: [1.8, 2.4, 2.4, 2.4], y: 1.4, rowH: [0.45, 0.75, 0.6, 0.75, 0.75] });
  source(s, "Nguồn: báo giá NCC-01 (mẫu), ý kiến các phòng. 'Chưa có số liệu' nghĩa là chưa có nguồn kèm theo");
  s = contentSlide(pres, "Những điều còn chưa rõ trước khi quyết định", "Thông tin thiếu và giả định đang dùng. Chưa lượng hóa được rủi ro gián đoạn lịch học và nhu cầu ngân sách giai đoạn 2.", "Brief");
  s.addText(bullets(["Chưa có báo giá phương án C", "Chưa đánh giá phù hợp chiến lược của phương án B", "Giai đoạn 2 của phương án B chưa có ngân sách", "Rủi ro gián đoạn lịch học của A chưa lượng hóa"], 20),
    { x: 0.5, y: 1.5, w: 9.0, h: 3.0, isTextBox: true, margin: 0, valign: "top", objectName: "noi-dung" });
  s = contentSlide(pres, "Hai câu hỏi lãnh đạo cần trả lời", "Khuyến nghị giữ trung lập và nêu căn cứ. Câu đầu chưa đủ căn cứ để khuyến nghị, vì thiếu số liệu của C và tiêu chí chiến lược của B.", "Brief");
  table(s, [["Câu hỏi", "Phương án", "Khuyến nghị trung lập và căn cứ"], ["Chọn phương án nào", "A, B hoặc C", "Chưa đủ căn cứ để khuyến nghị: thiếu báo giá C và đánh giá chiến lược của B"],
    ["Có triển khai giai đoạn 1 của B trước không", "Có / không", "Khả thi về chi phí và thời gian theo báo giá NCC-01; chưa có xác nhận ngân sách giai đoạn 2"]], { colW: [2.6, 1.8, 4.6], y: 1.5, rowH: [0.45, 1.0, 1.0] });
  source(s, "Nguồn: báo giá NCC-01 (mẫu), ý kiến phòng Tài chính");
  const expect = {
    must_contain: ["Chưa có số liệu", "Chưa đủ căn cứ để khuyến nghị", "chưa xác định", "2,77", "33,3%"], must_not_contain: ["nên chọn phương án", "Khuyến nghị chọn"],
    allowed_derived: ["1.200"],
    deck: { min_slides: 5, max_slides: 8, min_title_pt: 28, min_body_pt: 14, min_caption_pt: 11, max_words_per_slide: 95, notes_required: true, talk_minutes: 10, tables: [{ slide: 3, rows: 5, cols: 4, blank_text: "Chưa có số liệu", blank_cells: 3 }] },
    traps: [{ id: "THOI_HAN_TRONG", mo_ta: "Không có thời hạn quyết định: ghi chưa xác định" }, { id: "O_THIEU_NGUON", mo_ta: "Phương án B chiến lược, C chi phí/thời gian/chiến lược không có nguồn: để trống" },
      { id: "KHUYEN_NGHI_TRUNG_LAP", mo_ta: "Không đủ căn cứ: không chọn hộ phương án" }, { id: "MOI_SO_CO_NGUON", mo_ta: "Mỗi số liệu ghi nguồn" }],
  };
  const f = `- **THOI_HAN_TRONG**: không có thời hạn; slide đầu ghi "chưa xác định", không đặt hạn thay lãnh đạo.\n` +
    `- **O_THIEU_NGUON**: 3 ô (chi phí của C, chiến lược của B và C) hiển thị "Chưa có số liệu"; ô thời gian của C ghi "Chưa có báo giá"; bảng nêu rõ ngay trong chú thích nguồn.\n` +
    `- **KHUYEN_NGHI_TRUNG_LAP**: câu hỏi chọn phương án được trả lời "chưa đủ căn cứ để khuyến nghị" kèm lý do cụ thể thay vì chọn hộ A hoặc B.\n` +
    `- **MOI_SO_CO_NGUON**: ba số ở slide 2 có dòng Nguồn; mỗi ô bảng có tên nguồn trong ngoặc. Điểm yếu: bảng 4×3 chữ 14 pt khá dày, khó đọc nếu chiếu lên phòng họp; phù hợp đọc trước hơn trình chiếu.\n`;
  await save(pres, "executive-brief-trinh-lanh-dao", input, expect, f);
}

// =====================================================================
// 3. tro-ly-giang-day -> slide buổi học
// =====================================================================
async function deckGiangDay() {
  const hd = [["Khởi động: tình huống dự án trễ hạn", 10], ["Giảng: nhận diện và phân loại rủi ro", 25], ["Thực hành: lập ma trận rủi ro theo nhóm", 35], ["Thảo luận và phản hồi", 20], ["Tổng kết và bài tập", 10]];
  const tong = hd.reduce((a, r) => a + r[1], 0);
  const input = { de_cuong_hoc_phan: { ten: "Quản trị dự án", chuan_dau_ra: ["CĐR1: Nhận diện được rủi ro của dự án", "CĐR2: Đánh giá được mức độ rủi ro bằng ma trận xác suất – tác động", "CĐR3: Đề xuất được biện pháp ứng phó"] },
    chu_de_buoi_hoc: "Quản trị rủi ro dự án", trinh_do_sinh_vien: "Năm thứ ba", thoi_luong: 90,
    hoat_dong_de_xuat: hd.map(([t, p]) => ({ ten: t, phut: p })), ngoai_de_cuong: "Phân tích định lượng Monte Carlo", hoc_lieu: ["Giáo trình học phần (chương rủi ro)"] };
  const pres = newDeck("Quản trị rủi ro dự án");
  titleSlide(pres, "Quản trị rủi ro dự án", "Quản trị dự án · Buổi học 90 phút · Sinh viên năm thứ ba",
    "Chào lớp, nêu chủ đề và thời lượng buổi học 90 phút. Lưu ý cho giảng viên: tổng thời gian các hoạt động đề xuất là 100 phút, vượt 10 phút so với thời lượng; cần quyết định bớt hoạt động nào trước khi dạy.", "Buổi học");
  let s = contentSlide(pres, "Cuối buổi, bạn làm được ba việc", "Mục tiêu bám chuẩn đầu ra trong đề cương học phần. Không thêm mục tiêu ngoài đề cương.", "Buổi học");
  const cdr = input.de_cuong_hoc_phan.chuan_dau_ra;
  cdr.forEach((t, i) => {
    const y = 1.45 + i * 1.2;
    s.addShape("ellipse", { x: 0.5, y: y + 0.05, w: 0.75, h: 0.75, fill: { color: "0F6E6E" }, line: { color: "0F6E6E" }, objectName: "so-thu-tu" });
    s.addText(String(i + 1), { x: 0.5, y: y + 0.05, w: 0.75, h: 0.75, fontSize: 22, bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "so-thu-tu-chu" });
    s.addText(t.replace(/^CĐR\d: /, ""), { x: 1.5, y, w: 8.0, h: 0.85, fontSize: 20, color: "1B1F2A", isTextBox: true, margin: 0, valign: "middle", objectName: "muc-tieu" });
  });
  s = contentSlide(pres, "Buổi học gồm năm hoạt động", "Tiến trình theo thời gian. Thời lượng hiển thị đúng như đề xuất: 10, 25, 35, 20, 10 phút, tổng 100 phút. Cần giảng viên quyết định bớt 10 phút.", "Buổi học");
  const x0 = 0.5, W = 9.0; let acc = 0; const cols = ["5B8DB8", "0F6E6E", "D9822B", "3E7C4F", "7A8B8B"];
  hd.forEach(([t, p], i) => {
    const w = (W * p) / tong;
    s.addShape("rect", { x: x0 + (W * acc) / tong, y: 1.55, w: w - 0.04, h: 0.7, fill: { color: cols[i] }, line: { color: cols[i] }, objectName: "thanh-thoi-gian" });
    s.addText(`${p}'`, { x: x0 + (W * acc) / tong, y: 1.55, w: w - 0.04, h: 0.7, fontSize: 16, bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "thanh-thoi-gian-chu" });
    acc += p;
  });
  s.addText(bullets(hd.map(([t, p]) => `${t} (${p} phút)`), 16), { x: 0.5, y: 2.55, w: 9.0, h: 2.35, isTextBox: true, margin: 0, valign: "top", objectName: "noi-dung" });
  source(s, `Tổng các hoạt động: ${tong} phút; thời lượng buổi học: 90 phút`);
  s = contentSlide(pres, "Rủi ro là sự kiện có thể xảy ra và ảnh hưởng đến mục tiêu", "Khái niệm rủi ro: xác suất và tác động. Phân biệt rủi ro với vấn đề đã xảy ra. Hỏi sinh viên một ví dụ trong dự án tốt nghiệp của họ.", "Nội dung");
  s.addShape("roundRect", { x: 0.5, y: 1.6, w: 4.3, h: 2.4, fill: { color: "EEF3F2" }, line: { color: "EEF3F2" }, rectRadius: 0.1, objectName: "the" });
  s.addText([{ text: "Rủi ro", options: { bold: true, fontSize: 26, color: "0F6E6E", breakLine: true } }, { text: "Chưa xảy ra", options: { fontSize: 20, breakLine: true } }, { text: "Có xác suất và tác động", options: { fontSize: 20 } }],
    { x: 0.7, y: 1.8, w: 3.9, h: 2.0, isTextBox: true, margin: 0, valign: "top", color: "1B1F2A", objectName: "the-chu" });
  s.addShape("roundRect", { x: 5.2, y: 1.6, w: 4.3, h: 2.4, fill: { color: "FBEEDD" }, line: { color: "FBEEDD" }, rectRadius: 0.1, objectName: "the" });
  s.addText([{ text: "Vấn đề", options: { bold: true, fontSize: 26, color: "B5473A", breakLine: true } }, { text: "Đã xảy ra", options: { fontSize: 20, breakLine: true } }, { text: "Cần xử lý ngay", options: { fontSize: 20 } }],
    { x: 5.4, y: 1.8, w: 3.9, h: 2.0, isTextBox: true, margin: 0, valign: "top", color: "1B1F2A", objectName: "the-chu" });
  s = contentSlide(pres, "Ma trận rủi ro: xác suất nhân với tác động", "Giải thích cách đọc ma trận ba nhân ba. Ô góc trên bên phải là rủi ro cần ứng phó trước.", "Nội dung");
  const lv = [["Cao", "Trung bình", "Cao", "Rất cao"], ["Vừa", "Thấp", "Trung bình", "Cao"], ["Thấp", "Thấp", "Thấp", "Trung bình"]];
  const colr = { "Rất cao": "B5473A", "Cao": "D9822B", "Trung bình": "E6C36A", "Thấp": "9CC3A8" };
  const lab = ["Thấp", "Vừa", "Cao"];
  s.addText("Tác động →", { x: 0.5, y: 5.0, w: 9.0, h: 0.35, fontSize: 14, color: "4A5656", align: "center", isTextBox: true, margin: 0, objectName: "truc-x" });
  lv.forEach((r, i) => {
    s.addText(["Cao", "Vừa", "Thấp"][i], { x: 0.5, y: 1.7 + i * 0.95, w: 1.1, h: 0.9, fontSize: 14, color: "4A5656", valign: "middle", isTextBox: true, margin: 0, objectName: "truc-y" });
    [1, 2, 3].forEach((c) => {
      const v = r[c];
      s.addShape("rect", { x: 1.7 + (c - 1) * 2.6, y: 1.7 + i * 0.95, w: 2.5, h: 0.9, fill: { color: colr[v] }, line: { color: "FFFFFF", pt: 2 }, objectName: "o-ma-tran" });
      s.addText(v, { x: 1.7 + (c - 1) * 2.6, y: 1.7 + i * 0.95, w: 2.5, h: 0.9, fontSize: 18, bold: true, color: "1B1F2A", align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "o-ma-tran-chu" });
    });
  });
  ["Thấp", "Vừa", "Cao"].forEach((t, c) => s.addText(t, { x: 1.7 + c * 2.6, y: 4.58, w: 2.5, h: 0.35, fontSize: 14, color: "4A5656", align: "center", isTextBox: true, margin: 0, objectName: "truc-x-nhan" }));
  s.addText("Xác suất ↑", { x: 0.5, y: 1.3, w: 2.0, h: 0.3, fontSize: 14, color: "4A5656", isTextBox: true, margin: 0, objectName: "truc-y-nhan" });
  s = contentSlide(pres, "Nhóm lập ma trận cho dự án tốt nghiệp của mình", "Nhóm 4 người, 35 phút. Mỗi nhóm nêu ít nhất 5 rủi ro, xếp vào ma trận và đề xuất một biện pháp ứng phó cho rủi ro cao nhất.", "Hoạt động");
  s.addText(bullets(["Nêu ít nhất 5 rủi ro của dự án", "Xếp mỗi rủi ro vào ma trận", "Chọn rủi ro cao nhất, đề xuất biện pháp ứng phó"], 22), { x: 0.5, y: 1.6, w: 9.0, h: 2.6, isTextBox: true, margin: 0, valign: "top", objectName: "noi-dung" });
  s = contentSlide(pres, "Tóm tắt và bài tập", "Nhắc lại ba mục tiêu. Bài tập: hoàn thiện ma trận của nhóm. Nội dung ngoài đề cương học phần không đưa vào buổi này.", "Hoạt động");
  s.addText(bullets(["Nhận diện, đánh giá, ứng phó là ba bước", "Bài tập: hoàn thiện ma trận rủi ro của nhóm", "Học liệu: giáo trình học phần, chương rủi ro"], 22), { x: 0.5, y: 1.6, w: 9.0, h: 2.6, isTextBox: true, margin: 0, valign: "top", objectName: "noi-dung" });
  const expect = {
    must_contain: ["Cuối buổi, bạn làm được ba việc", "Tổng các hoạt động: 100 phút", "thời lượng buổi học: 90 phút", "Ma trận rủi ro"], must_not_contain: ["Monte Carlo", "Giáo trình Quản trị dự án của"],
    allowed_derived: ["100"], deck: { min_slides: 6, max_slides: 10, min_title_pt: 28, min_body_pt: 14, min_caption_pt: 11, max_words_per_slide: 85, notes_required: true, talk_minutes: 90 },
    traps: [{ id: "TONG_PHUT_VUOT", mo_ta: "Hoạt động cộng 100 phút, buổi học 90" }, { id: "NGOAI_DE_CUONG", mo_ta: "Monte Carlo không thuộc đề cương: không đưa vào" },
      { id: "HOC_LIEU_KHONG_BIA", mo_ta: "Chỉ ghi học liệu đầu vào cho, không bịa tác giả" }],
  };
  const f = `- **TONG_PHUT_VUOT**: các hoạt động đề xuất cộng ${tong} phút, buổi học 90 phút. Slide tiến trình giữ đúng số phút đầu vào và ghi tổng ở dòng Nguồn; ghi chú người trình bày nêu rõ cần bớt 10 phút. Không tự cắt hoạt động nào.\n` +
    `- **NGOAI_DE_CUONG**: "Phân tích định lượng Monte Carlo" không có trong chuẩn đầu ra nên không đưa vào slide, chỉ nhắc trong ghi chú.\n` +
    `- **HOC_LIEU_KHONG_BIA**: học liệu chỉ là "giáo trình học phần, chương rủi ro" theo đầu vào; không thêm tên sách, tác giả, năm.\n` +
    `- Ghi chú: skill nguồn có cấu trúc "kế hoạch buổi học" bằng văn bản, không nói gì về slide (số slide, cỡ chữ, ghi chú giảng); bộ slide này dựng theo quy tắc chung của kỹ năng pptx, cần bổ sung quy tắc vào skill.\n`;
  await save(pres, "tro-ly-giang-day", input, expect, f);
}

// =====================================================================
// 4. campaign-brief-tuyen-sinh
// =====================================================================
async function deckCampaign() {
  const kenh = [["Facebook Ads", 200], ["Tư vấn tại trường THPT", 150], ["Website và SEO", 90], ["Zalo OA", 80]];
  const tong = kenh.reduce((a, r) => a + r[1], 0);
  const input = { ten_chien_dich: "Tuyển sinh đợt 1 năm 2027 (tên mẫu)", thoi_gian: "01/02/2027–30/06/2027",
    muc_tieu: [{ noi_dung: "Số hồ sơ đăng ký xét tuyển", gia_tri: "1.500 hồ sơ", han: "30/06/2027" }, { noi_dung: "Tăng nhận diện thương hiệu", gia_tri: null, han: null }],
    doi_tuong: [{ nhom: "Học sinh lớp 12", kenh_hay_dung: "Facebook, Zalo", quan_tam: "Học phí, cơ hội việc làm" }, { nhom: "Phụ huynh", kenh_hay_dung: "Facebook", quan_tam: "Học phí, học bổng" }],
    thong_diep: { chinh: "Học thật, ra trường có việc", phu: ["Học bổng đầu vào", "Thực tập tại doanh nghiệp"], bang_chung: [{ thong_diep: "Học thật, ra trường có việc", so_lieu: null }, { thong_diep: "Học bổng đầu vào", so_lieu: "Học bổng cho 100 thí sinh đầu tiên" }] },
    ngan_sach_trieu_dong: kenh.map(([k, v]) => ({ kenh: k, so_tien: money(v) })), tong_ngan_sach_khai_bao_trieu_dong: money(500),
    kpi: [{ kenh: "Facebook Ads", kpi: "600 lead" }, { kenh: "Tư vấn tại trường THPT", kpi: "400 lead" }, { kenh: "Website và SEO", kpi: "300 lead" }, { kenh: "Zalo OA", kpi: null }], kpi_tong: "1.500 hồ sơ" };
  const pres = newDeck("Campaign brief tuyển sinh 2027");
  titleSlide(pres, "Tuyển sinh đợt 1 năm 2027", "Campaign brief · 01/02/2027–30/06/2027", "Giới thiệu chiến dịch và khoảng thời gian chạy. Đây là bản brief nội bộ, chưa phải kế hoạch chi tiết từng ngày.", "Brief");
  let s = contentSlide(pres, "Mục tiêu: 1.500 hồ sơ đăng ký trước 30/06/2027", "Mục tiêu đo được duy nhất trong đầu vào là số hồ sơ. Mục tiêu nhận diện thương hiệu chưa có con số nên chưa viết thành mục tiêu; cần bổ sung chỉ số và thời hạn.", "Brief");
  stat(s, 0.5, 1.5, 4.3, "1.500", "hồ sơ đăng ký xét tuyển, hạn 30/06/2027", "0F6E6E");
  s.addShape("roundRect", { x: 5.2, y: 1.5, w: 4.3, h: 1.9, fill: { color: "FBEEDD" }, line: { color: "D9822B", pt: 1 }, rectRadius: 0.1, objectName: "luu-y" });
  s.addText([{ text: "Chưa đo được", options: { bold: true, fontSize: 18, breakLine: true } }, { text: "Mục tiêu 'tăng nhận diện thương hiệu' chưa có chỉ số và thời hạn", options: { fontSize: 14 } }],
    { x: 5.35, y: 1.62, w: 4.0, h: 1.7, isTextBox: true, margin: 0, valign: "top", color: "1B1F2A", objectName: "luu-y-chu" });
  s = contentSlide(pres, "Hai nhóm đối tượng cùng dùng Facebook", "Học sinh lớp 12 dùng Facebook và Zalo, quan tâm học phí và cơ hội việc làm. Phụ huynh dùng Facebook, quan tâm học phí và học bổng.", "Brief");
  table(s, [["Nhóm", "Kênh hay dùng", "Mối quan tâm"], ["Học sinh lớp 12", "Facebook, Zalo", "Học phí, cơ hội việc làm"], ["Phụ huynh", "Facebook", "Học phí, học bổng"]], { colW: [2.4, 3.0, 3.6], y: 1.6, rowH: [0.5, 0.8, 0.8] });
  s = contentSlide(pres, "Thông điệp chính: học thật, ra trường có việc", "Thông điệp chính chưa có số liệu làm bằng chứng nên chỉ nêu như định hướng, không thêm con số. Thông điệp phụ về học bổng có căn cứ theo đầu vào.", "Brief");
  s.addText(bullets(["Chính: Học thật, ra trường có việc (chưa có số liệu bằng chứng)", "Phụ: Học bổng cho 100 thí sinh đầu tiên", "Phụ: Thực tập tại doanh nghiệp (chưa có số liệu bằng chứng)"], 20), { x: 0.5, y: 1.5, w: 9.0, h: 3.0, isTextBox: true, margin: 0, valign: "top", objectName: "noi-dung" });
  s = contentSlide(pres, "Facebook Ads chiếm phần lớn ngân sách", "Ngân sách theo kênh, triệu đồng. Cộng bốn kênh là 520 triệu đồng, trong khi đầu vào khai tổng 500 triệu đồng, lệch 20 triệu đồng chưa giải thích; không tự điều chỉnh kênh nào.", "Kế hoạch");
  s.addChart(pres.charts.BAR, [{ name: "Ngân sách", labels: kenh.map((r) => r[0]), values: kenh.map((r) => r[1]) }],
    Object.assign({}, CHART_BASE, { x: 0.5, y: 1.35, w: 6.0, h: 3.6, barDir: "bar", chartColors: ["0F6E6E"], showLegend: false, showValAxisTitle: true, valAxisTitle: "Triệu đồng", valAxisMinVal: 0, objectName: "bieu-do" }));
  s.addShape("roundRect", { x: 6.8, y: 1.9, w: 2.7, h: 2.1, fill: { color: "FBEEDD" }, line: { color: "D9822B", pt: 1 }, rectRadius: 0.1, objectName: "luu-y" });
  s.addText([{ text: "Cần rà lại", options: { bold: true, fontSize: 16, breakLine: true } }, { text: `Cộng kênh: ${tong}. Khai tổng: 500.`, options: { fontSize: 14 } }], { x: 6.95, y: 2.0, w: 2.4, h: 1.9, isTextBox: true, margin: 0, valign: "top", color: "1B1F2A", objectName: "luu-y-chu" });
  source(s, "Nguồn: dự kiến ngân sách theo kênh của đơn vị (đơn vị: triệu đồng)");
  s = contentSlide(pres, "Bốn pha: chuẩn bị, chạy, cao điểm, tổng kết", "Timeline theo bốn pha. Đầu vào chưa có ngày bắt đầu và kết thúc từng pha, người phụ trách và bàn giao, nên slide chỉ nêu pha và để trống mốc.", "Kế hoạch");
  ["Chuẩn bị", "Chạy", "Cao điểm", "Tổng kết"].forEach((p, i) => {
    s.addShape("rect", { x: 0.5 + i * 2.28, y: 1.8, w: 2.2, h: 1.0, fill: { color: ["5B8DB8", "0F6E6E", "D9822B", "7A8B8B"][i] }, line: { color: "FFFFFF" }, objectName: "pha" });
    s.addText(p, { x: 0.5 + i * 2.28, y: 1.8, w: 2.2, h: 1.0, fontSize: 20, bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "pha-chu" });
    s.addText("Mốc: ........", { x: 0.5 + i * 2.28, y: 2.95, w: 2.2, h: 0.6, fontSize: 14, color: "4A5656", align: "center", isTextBox: true, margin: 0, objectName: "moc" });
  });
  s = contentSlide(pres, "KPI: 1.500 hồ sơ, ba kênh đã có chỉ tiêu lead", "KPI tổng là 1.500 hồ sơ. Ba kênh đã có chỉ tiêu lead; Zalo OA chưa có KPI nên để trống. Chưa nêu tần suất báo cáo vì đầu vào không có.", "Kế hoạch");
  table(s, [["Kênh", "KPI"], ["Facebook Ads", "600 lead"], ["Tư vấn tại trường THPT", "400 lead"], ["Website và SEO", "300 lead"], ["Zalo OA", "Chưa có KPI"], ["Tổng", "1.500 hồ sơ"]], { colW: [5.0, 4.0], y: 1.4, rowH: [0.45, 0.55, 0.55, 0.55, 0.55, 0.55] });
  const expect = {
    must_contain: ["Mục tiêu: 1.500 hồ sơ", "Chưa đo được", "Cần rà lại", "Chưa có KPI", "Mốc: ........"], must_not_contain: ["tăng 20%", "tăng 30%"],
    allowed_derived: [money(tong)], deck: { min_slides: 6, max_slides: 10, min_title_pt: 28, min_body_pt: 14, min_caption_pt: 11, max_words_per_slide: 85, notes_required: true, talk_minutes: 15,
      charts: [{ slide: 5, type: "bar", series: { "Ngân sách": kenh.map((r) => r[1]) } }], tables: [{ slide: 7, rows: 6, cols: 2, blank_text: "Chưa có KPI", blank_cells: 1 }] },
    traps: [{ id: "NGAN_SACH_LECH", mo_ta: "Cộng kênh 520, khai tổng 500" }, { id: "MUC_TIEU_KHONG_DO_DUOC", mo_ta: "Nhận diện thương hiệu không có số: không viết thành mục tiêu SMART" },
      { id: "THONG_DIEP_THIEU_BANG_CHUNG", mo_ta: "Thông điệp chính không có số liệu: không bịa" }, { id: "KPI_THIEU", mo_ta: "Zalo OA không có KPI: để trống" }, { id: "TIMELINE_THIEU_MOC", mo_ta: "Không có mốc pha: dòng chấm" }],
  };
  const f = `- **NGAN_SACH_LECH**: cộng bốn kênh ${tong}, đầu vào khai 500 triệu đồng. Biểu đồ vẽ theo từng kênh; ô "Cần rà lại" nêu cả hai số.\n` +
    `- **MUC_TIEU_KHONG_DO_DUOC**: "tăng nhận diện thương hiệu" không có chỉ số, hạn; slide báo "chưa đo được", không tự bịa chỉ số.\n` +
    `- **THONG_DIEP_THIEU_BANG_CHUNG**: hai thông điệp thiếu số liệu bằng chứng được ghi chú rõ ngay trong dòng chữ.\n` +
    `- **KPI_THIEU**: Zalo OA không có KPI; bảng ghi "Chưa có KPI". Ba kênh còn lại cộng 1.300 lead, trong khi KPI tổng là 1.500 hồ sơ: hai đơn vị khác nhau (lead và hồ sơ) nên không so trực tiếp; skill nên nói rõ cách quy đổi lead sang hồ sơ.\n` +
    `- **TIMELINE_THIEU_MOC**: không có mốc từng pha, phụ trách, bàn giao; slide để dòng chấm "Mốc: ........".\n`;
  await save(pres, "campaign-brief-tuyen-sinh", input, expect, f);
}

(async () => {
  await deckTongKet();
  await deckBrief();
  await deckGiangDay();
  await deckCampaign();
})();
