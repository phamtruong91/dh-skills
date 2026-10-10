// Thử các skill có thể xuất PowerPoint bằng dữ liệu GIẢ (cố định, lặp lại được), phong cách trường đại học.
// Đóng vai "AI làm theo SKILL.md" (không phải AI độc lập): dựng bằng pptxgenjs, biểu đồ gốc (sửa được trong PowerPoint).
// Dùng: node tests/build_pptx.js   (cần pptxgenjs, react-icons, sharp và kỹ năng pptx ở /mnt/skills/public/pptx)
const fs = require("fs");
const path = require("path");
const { applyTheme } = require("/mnt/skills/public/pptx/scripts/apply_theme.js");
const { THEME, K, icon, newDeck, source, stat, panel, CHART, numbered, table, vn, money } = require("./pptx_dai_hoc");

const HERE = __dirname;
const OUT = path.join(HERE, "outputs");
const SAMPLES = path.join(HERE, "samples");
const RESULTS = path.join(HERE, "results");
for (const d of [OUT, SAMPLES, RESULTS]) fs.mkdirSync(d, { recursive: true });
const NOTE = "Dữ liệu GIẢ để thử. Tên trường, người, số liệu đều là mẫu.";
const DONVI = "Trường Đại học Mẫu A (tên mẫu)";

async function save(D, name, input, expect, findings) {
  const file = path.join(OUT, `${name}.pptx`);
  await D.pres.writeFile({ fileName: file });
  await applyTheme(file, THEME);
  fs.writeFileSync(path.join(SAMPLES, `${name}.input.json`), JSON.stringify(Object.assign({ _ghi_chu: NOTE }, input), null, 1));
  fs.writeFileSync(path.join(SAMPLES, `${name}.expect.json`), JSON.stringify(Object.assign({ skill: name, output: `${name}.pptx`, kind: "pptx" }, expect), null, 1));
  fs.writeFileSync(path.join(RESULTS, `${name}.findings.md`), `# Phát hiện khi chạy thử xuất PowerPoint: ${name} (dữ liệu giả)\n\n${findings}`);
  console.log("đã tạo", file);
}
const DECK = { min_title_pt: 28, min_body_pt: 14, min_caption_pt: 11, max_words_per_slide: 85, notes_required: true };
const colChart = (D, s, type, series, extra = {}) => s.addChart(type, series, Object.assign({}, CHART, { objectName: "bieu-do" }, extra));

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
    nam_hoc: "2025–2026", co_so: DONVI, thoi_gian_trinh_bay_phut: 20,
    bao_cao_don_vi: { dao_tao: { tuyen_sinh: nganh.map(([n, a, b]) => ({ nganh: n, chi_tieu: money(a), nhap_hoc: money(b) })),
        ty_le_tot_nghiep_dung_han_phan_tram: { "2022–2023": 78, "2023–2024": 81, "2024–2025": 84, "2025–2026": null }, nhan_xet_khai_bao: "Tăng 8 điểm phần trăm so với 2022–2023" },
      tai_chinh: { thu_trieu_dong: money(412000), chi_theo_nhom_trieu_dong: chi.map(([n, v]) => ({ nhom: n, so_tien: money(v) })), tong_chi_khai_bao_trieu_dong: money(400000) },
      cong_tac_sinh_vien: null,
      ton_tai: [["Cơ sở vật chất giảng đường chưa đáp ứng giờ cao điểm", "Số phòng học không tăng trong khi quy mô tăng"], ["Tỷ lệ nhập học Luật còn thấp", "Chưa có kênh tư vấn riêng cho ngành"], ["Báo cáo đơn vị nộp chậm", "Chưa có mốc nộp thống nhất"]] },
    dinh_huong_chung: null,
  };
  const D = await newDeck({ title: "Tổng kết năm học 2025–2026", donVi: DONVI, footer: "Hội nghị tổng kết năm học 2025–2026" });
  const { pres } = D;
  D.title("Tổng kết năm học 2025–2026", "Hội nghị tổng kết toàn trường", "Mở đầu: nêu phạm vi báo cáo gồm đào tạo, tài chính, tồn tại và phương hướng. Báo cáo của Phòng Công tác sinh viên chưa nhận được nên phần này chưa trình bày số liệu.", "Mở đầu");
  let s = D.content("Nội dung chính của hội nghị", "Bốn phần: kết quả chính, đào tạo, tài chính, tồn tại và phương hướng. Công tác sinh viên sẽ bổ sung khi có báo cáo.", "Mở đầu");
  ["Kết quả chính của năm học", "Đào tạo: tuyển sinh và tốt nghiệp", "Tài chính và công tác sinh viên", "Tồn tại và phương hướng"].forEach((t, i) => numbered(s, 0.6, 1.45 + i * 0.85, 8.8, 0.72, i + 1, t, ""));
  s = D.content("Nhập học đạt 91,2% chỉ tiêu, tổng thu 412.000 triệu đồng", "Ba con số cần nhớ: tỷ lệ nhập học theo chỉ tiêu, tỷ lệ tốt nghiệp đúng hạn năm gần nhất có số liệu, và tổng thu. Mọi số lấy từ báo cáo các đơn vị.", "Kết quả");
  await stat(s, 0.6, 1.45, 2.8, 3.2, "FaUserGraduate", `${vn((100 * nhapHoc) / chiTieu)}%`, `nhập học ${money(nhapHoc)} trên chỉ tiêu ${money(chiTieu)}`, K.blue);
  await stat(s, 3.6, 1.45, 2.8, 3.2, "FaGraduationCap", "84%", "tốt nghiệp đúng hạn, năm học 2024–2025 (năm gần nhất có số liệu)", K.green);
  await stat(s, 6.6, 1.45, 2.8, 3.2, "FaCoins", money(412000), "triệu đồng tổng thu năm học", K.gold);
  source(s, "Nguồn: báo cáo Phòng Đào tạo và Phòng Kế hoạch – Tài chính, năm học 2025–2026");
  s = D.content("Luật có tỷ lệ nhập học thấp nhất trong bốn ngành", "So sánh chỉ tiêu và nhập học theo ngành. Luật đạt 85,7%, Ngoại ngữ 88,0%, Kinh tế 92,4%, Công nghệ thông tin 95,2%.", "Đào tạo");
  const slBar = D.n;
  colChart(D, s, pres.charts.BAR, [{ name: "Chỉ tiêu", labels: nganh.map((r) => r[0]), values: nganh.map((r) => r[1]) }, { name: "Nhập học", labels: nganh.map((r) => r[0]), values: nganh.map((r) => r[2]) }],
    { x: 0.6, y: 1.35, w: 5.9, h: 3.45, barDir: "col", barGrouping: "clustered", chartColors: ["B7C3D4", K.blue], showLegend: true, showValAxisTitle: true, valAxisTitle: "Số sinh viên", valAxisMinVal: 0 });
  await panel(s, 6.75, 1.45, 2.65, 3.3, "Nhận xét", ["Luật đạt 85,7% chỉ tiêu, thấp nhất", "Công nghệ thông tin đạt 95,2%, cao nhất"], "info", "FaChartBar");
  source(s, "Nguồn: báo cáo Phòng Đào tạo, năm học 2025–2026");
  s = D.content("Tốt nghiệp đúng hạn tăng 6 điểm phần trăm sau hai năm", "Từ 78% lên 84%. Lưu ý: nhận xét trong đầu vào nêu chênh lệch 8 điểm, nhưng tính lại 84 trừ 78 là 6 điểm; slide dùng số tính lại. Năm học 2025–2026 chưa xét tốt nghiệp nên chưa có số liệu, không ghi 0.", "Đào tạo");
  const slLine = D.n;
  colChart(D, s, pres.charts.LINE, [{ name: "Tốt nghiệp đúng hạn", labels: tn.map((r) => r[0]), values: tn.map((r) => r[1]) }],
    { x: 0.6, y: 1.35, w: 5.9, h: 3.45, chartColors: [K.blue], lineSize: 3, lineDataSymbolSize: 9, showLegend: false, showValAxisTitle: true, valAxisTitle: "% sinh viên", valAxisMinVal: 60, valAxisMaxVal: 100 });
  await panel(s, 6.75, 1.45, 2.65, 3.3, "Lưu ý", ["Tăng 6 điểm phần trăm so với 2022–2023", "2025–2026: chưa có số liệu vì chưa xét tốt nghiệp"], "info", "FaInfoCircle");
  source(s, "Nguồn: báo cáo Phòng Đào tạo. Năm học 2025–2026 chưa có số liệu");
  s = D.content("Lương và phụ cấp chiếm hơn một nửa tổng chi", "Cơ cấu chi theo nhóm, đơn vị triệu đồng. Tổng các nhóm là 398.500 triệu đồng, trong khi báo cáo khai tổng chi 400.000 triệu đồng; chênh 1.500 triệu đồng chưa giải thích, đề nghị Phòng Kế hoạch – Tài chính rà lại trước hội nghị.", "Tài chính");
  const slChi = D.n;
  colChart(D, s, pres.charts.BAR, [{ name: "Chi", labels: chi.map((r) => r[0]), values: chi.map((r) => r[1]) }],
    { x: 0.6, y: 1.35, w: 5.9, h: 3.45, barDir: "bar", chartColors: [K.blue], showLegend: false, showValAxisTitle: true, valAxisTitle: "Triệu đồng", dataLabelFormatCode: "#,##0", valAxisMinVal: 0 });
  await panel(s, 6.75, 1.45, 2.65, 3.3, "Cần rà lại", [`Cộng các nhóm: ${money(tongChi)}`, `Báo cáo khai: ${money(400000)}`, "Chênh 1.500 triệu đồng chưa giải thích"], "warn", "FaExclamationTriangle");
  source(s, "Nguồn: báo cáo Phòng Kế hoạch – Tài chính, năm học 2025–2026 (đơn vị: triệu đồng)");
  s = D.content("Công tác sinh viên: đang chờ báo cáo của đơn vị", "Phòng Công tác sinh viên chưa gửi báo cáo, nên slide này chưa có nội dung. Không điền số liệu thay đơn vị; cập nhật khi nhận được.", "Tài chính");
  s.addShape("roundRect", { x: 1.2, y: 1.6, w: 7.6, h: 2.6, fill: { color: K.panel }, line: { color: K.line, pt: 1 }, rectRadius: 0.1, objectName: "cho-bao-cao" });
  s.addImage({ data: await icon("FaHourglassHalf", K.slate), x: 1.6, y: 2.55, w: 0.7, h: 0.7, altText: "Biểu tượng chờ", objectName: "bieu-tuong" });
  s.addText("Chưa nhận được báo cáo của Phòng Công tác sinh viên. Nội dung sẽ được bổ sung khi có số liệu.", { x: 2.6, y: 1.9, w: 5.9, h: 2.0, fontSize: 20, color: K.ink, isTextBox: true, margin: 0, valign: "middle", objectName: "cho-bao-cao-chu" });
  s = D.content("Ba tồn tại chính cần xử lý trong năm học tới", "Mỗi tồn tại đi kèm nguyên nhân do đơn vị nêu. Trình bày thẳng, không giảm nhẹ.", "Tồn tại và phương hướng");
  input.bao_cao_don_vi.ton_tai.forEach(([a, b], i) => numbered(s, 0.6, 1.45 + i * 1.1, 8.8, 0.95, i + 1, a, `Nguyên nhân: ${b}`, K.red));
  s = D.content("Phương hướng năm học tới: chờ định hướng của Ban Giám hiệu", "Đầu vào không có định hướng chung của Ban Giám hiệu, nên chưa nêu chỉ tiêu hay giải pháp mới. Chỉ ghi các việc hiển nhiên từ tồn tại; cập nhật khi có chỉ đạo.", "Tồn tại và phương hướng");
  await panel(s, 0.6, 1.6, 4.2, 2.6, "Đã rõ", ["Xử lý ba tồn tại ở slide trước", "Rà lại số liệu chi và bổ sung báo cáo công tác sinh viên"], "info", "FaCheckCircle");
  await panel(s, 5.2, 1.6, 4.2, 2.6, "Chờ chỉ đạo", ["Chỉ tiêu năm học mới: chờ định hướng của Ban Giám hiệu", "Giải pháp trọng tâm: chờ định hướng của Ban Giám hiệu"], "warn", "FaHourglassHalf");
  D.closing("Trân trọng cảm ơn", "Trao đổi và góp ý", "Kết thúc phần trình bày. Dành thời gian cho các đơn vị góp ý, ghi nhận các ý kiến để bổ sung báo cáo công tác sinh viên và rà lại số liệu chi.", "Tồn tại và phương hướng");
  const expect = {
    must_contain: ["Tổng kết năm học 2025–2026", "91,2%", "tăng 6 điểm", "Tăng 6 điểm", "chưa có số liệu", "Chưa nhận được báo cáo của Phòng Công tác sinh viên", "chờ định hướng"],
    must_not_contain: ["tăng 8 điểm", "Tăng 8 điểm", "400.000 triệu đồng tổng chi"], allowed_derived: [money(chiTieu), money(nhapHoc), money(tongChi), "1.500"],
    deck: Object.assign({ min_slides: 8, max_slides: 12, talk_minutes: 20,
      charts: [{ slide: slBar, type: "bar", series: { "Chỉ tiêu": nganh.map((r) => r[1]), "Nhập học": nganh.map((r) => r[2]) } },
        { slide: slLine, type: "line", series: { "Tốt nghiệp đúng hạn": tn.map((r) => r[1]) } }, { slide: slChi, type: "bar", series: { "Chi": chi.map((r) => r[1]) } }] }, DECK),
    traps: [{ id: "NHAN_XET_SAI_SO", mo_ta: "Đầu vào ghi tăng 8 điểm, tính lại 6 điểm" }, { id: "TONG_CHI_LECH", mo_ta: "Cộng nhóm 398.500, khai 400.000" },
      { id: "NAM_CHUA_CO_SO_LIEU", mo_ta: "Tốt nghiệp 2025–2026 chưa có: không ghi 0" }, { id: "DON_VI_CHUA_BAO_CAO", mo_ta: "Công tác sinh viên chưa nộp: không bịa" },
      { id: "THIEU_DINH_HUONG", mo_ta: "Không có định hướng BGH: không bịa chỉ tiêu" }, { id: "KHONG_PHAI_BAO_CAO_VAN_BAN", mo_ta: "Bộ slide không dùng thể thức văn bản hành chính" }],
  };
  const f = `- **NHAN_XET_SAI_SO**: đầu vào ghi "tăng 8 điểm phần trăm so với 2022–2023", nhưng 84 − 78 = 6. Tiêu đề slide và khung "Lưu ý" dùng số tính lại (6); ghi chú người trình bày nêu rõ lệch.\n` +
    `- **TONG_CHI_LECH**: cộng các nhóm chi được ${money(tongChi)}, đầu vào khai 400.000 triệu đồng. Biểu đồ vẽ theo từng nhóm; khung "Cần rà lại" nêu cả hai số, không tự chọn.\n` +
    `- **NAM_CHUA_CO_SO_LIEU**: tỷ lệ tốt nghiệp 2025–2026 là null; đường không có điểm thứ tư, khung bên cạnh ghi "chưa có số liệu" (không ghi 0).\n` +
    `- **DON_VI_CHUA_BAO_CAO**: công tác sinh viên null; slide báo rõ chưa nhận được báo cáo, không điền. Câu hỏi mở: khi trình bày thật có nên bỏ slide này không? Đang giữ để người xem thấy phần còn thiếu.\n` +
    `- **THIEU_DINH_HUONG**: định hướng chung null; slide phương hướng chia "Đã rõ" và "Chờ chỉ đạo", không bịa chỉ tiêu.\n` +
    `- **KHONG_PHAI_BAO_CAO_VAN_BAN**: skill gốc mô tả báo cáo tổng kết là văn bản hành chính (quốc hiệu, nơi nhận, chữ ký). Bộ slide là tài liệu trình bày tách biệt, không có các phần đó.\n`;
  await save(D, "bao-cao-tong-ket-nam-truong", input, expect, f);
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
      { ten: "A. Nâng cấp toàn bộ một lần", chi_phi: { gia_tri: "1.200 triệu", nguon: "NCC-01" }, thoi_gian: { gia_tri: "4 tháng", nguon: "NCC-01" }, rui_ro: { gia_tri: "Gián đoạn lịch học", nguon: "P. Đào tạo" }, chien_luoc: { gia_tri: "Phù hợp kế hoạch CĐS", nguon: "KH chuyển đổi số" } },
      { ten: "B. Nâng cấp theo hai giai đoạn", chi_phi: { gia_tri: "700 triệu (giai đoạn 1)", nguon: "NCC-01" }, thoi_gian: { gia_tri: "2 tháng + 3 tháng", nguon: "NCC-01" }, rui_ro: { gia_tri: "Giai đoạn 2 chưa có vốn", nguon: "P. Tài chính" }, chien_luoc: { gia_tri: null, nguon: null } },
      { ten: "C. Thuê dịch vụ trọn gói", chi_phi: { gia_tri: null, nguon: null }, thoi_gian: { gia_tri: "Chưa có báo giá", nguon: null }, rui_ro: { gia_tri: "Phụ thuộc nhà cung cấp", nguon: "P. Quản trị" }, chien_luoc: { gia_tri: null, nguon: null } },
    ],
  };
  const D = await newDeck({ title: "Executive brief: nâng cấp wifi giảng đường", donVi: DONVI, footer: "Executive brief · Nâng cấp wifi giảng đường" });
  D.title("Nâng cấp wifi giảng đường: cần quyết định gì", "Executive brief cho lãnh đạo · Thời hạn quyết định: chưa xác định", "Tài liệu dành cho lãnh đạo đọc trước cuộc họp. Vấn đề cần quyết định được nêu ở slide này; thời hạn quyết định chưa có trong đầu vào nên để trống.", "Brief");
  let s = D.content("Sinh viên chấm wifi thấp nhất trong các câu hỏi khảo sát", "Bối cảnh: khảo sát học kỳ 1 năm học 2026–2027. Wifi đạt 2,77 điểm, là mức cần cải thiện theo quy ước dưới 3,0. Trong 360 phiếu có ý kiến mở, 120 phiếu nói về wifi.", "Brief");
  await stat(s, 0.6, 1.45, 2.8, 3.2, "FaWifi", "2,77", "điểm trung bình câu 'Mạng wifi ổn định' (thang 1–5)", K.red);
  await stat(s, 3.6, 1.45, 2.8, 3.2, "FaCommentDots", "33,3%", "ý kiến mở nói về wifi (120 trên 360 phiếu)", K.red);
  await stat(s, 6.6, 1.45, 2.8, 3.2, "FaCoins", "1.200", "triệu đồng, chi phí phương án A theo báo giá", K.blue);
  source(s, "Nguồn: báo cáo khảo sát sinh viên học kỳ 1 năm học 2026–2027; báo giá NCC-01 (mẫu)");
  s = D.content("Ba phương án, nhưng mới đủ số liệu để so sánh hai", "Ô để trống nghĩa là chưa có số liệu kèm nguồn. Không tự điền. Phương án C chưa có báo giá nên chưa so được chi phí; phương án B thiếu đánh giá về phù hợp chiến lược.", "Brief");
  const row = (k, lbl) => [lbl].concat(input.phuong_an.map((p) => (p[k].gia_tri ? `${p[k].gia_tri}` + (p[k].nguon ? ` (${p[k].nguon})` : "") : "Chưa có số liệu")));
  table(s, [["Tiêu chí", "A. Toàn bộ", "B. Hai giai đoạn", "C. Thuê dịch vụ"], row("chi_phi", "Chi phí"), row("thoi_gian", "Thời gian"), row("rui_ro", "Rủi ro"), row("chien_luoc", "Phù hợp chiến lược")],
    { colW: [1.9, 2.3, 2.3, 2.3], y: 1.4, rowH: [0.45, 0.75, 0.6, 0.75, 0.75] });
  const slBang1 = D.n;
  source(s, "Nguồn: báo giá NCC-01 (mẫu), ý kiến các phòng. 'Chưa có số liệu' nghĩa là chưa có nguồn kèm theo");
  s = D.content("Bốn điều còn chưa rõ trước khi quyết định", "Thông tin thiếu và giả định đang dùng. Chưa lượng hóa được rủi ro gián đoạn lịch học và nhu cầu ngân sách giai đoạn 2.", "Brief");
  ["Chưa có báo giá phương án C", "Chưa đánh giá phù hợp chiến lược của phương án B", "Giai đoạn 2 của phương án B chưa có ngân sách", "Rủi ro gián đoạn lịch học của A chưa lượng hóa"].forEach((t, i) => numbered(s, 0.6, 1.4 + i * 0.85, 8.8, 0.72, i + 1, t, "", K.gold));
  s = D.content("Hai câu hỏi lãnh đạo cần trả lời", "Khuyến nghị giữ trung lập và nêu căn cứ. Câu đầu chưa đủ căn cứ để khuyến nghị, vì thiếu số liệu của C và tiêu chí chiến lược của B.", "Brief");
  table(s, [["Câu hỏi", "Phương án", "Khuyến nghị trung lập và căn cứ"], ["Chọn phương án nào", "A, B hoặc C", "Chưa đủ căn cứ để khuyến nghị: thiếu báo giá C và đánh giá chiến lược của B"],
    ["Có triển khai giai đoạn 1 của B trước không", "Có / không", "Khả thi về chi phí và thời gian theo báo giá NCC-01; chưa có xác nhận ngân sách giai đoạn 2"]], { colW: [2.6, 1.8, 4.4], y: 1.5, rowH: [0.45, 1.0, 1.0] });
  source(s, "Nguồn: báo giá NCC-01 (mẫu), ý kiến phòng Tài chính");
  const expect = {
    must_contain: ["Chưa có số liệu", "Chưa đủ căn cứ để khuyến nghị", "chưa xác định", "2,77", "33,3%"], must_not_contain: ["nên chọn phương án", "Khuyến nghị chọn"], allowed_derived: ["1.200"],
    deck: Object.assign({ min_slides: 5, max_slides: 8, talk_minutes: 10, tables: [{ slide: slBang1, rows: 5, cols: 4, blank_text: "Chưa có số liệu", blank_cells: 3 }] }, DECK, { max_words_per_slide: 95 }),
    traps: [{ id: "THOI_HAN_TRONG", mo_ta: "Không có thời hạn quyết định: ghi chưa xác định" }, { id: "O_THIEU_NGUON", mo_ta: "Phương án B chiến lược, C chi phí/chiến lược không có nguồn: để trống" },
      { id: "KHUYEN_NGHI_TRUNG_LAP", mo_ta: "Không đủ căn cứ: không chọn hộ phương án" }, { id: "MOI_SO_CO_NGUON", mo_ta: "Mỗi số liệu ghi nguồn" }],
  };
  const f = `- **THOI_HAN_TRONG**: không có thời hạn; slide đầu ghi "chưa xác định", không đặt hạn thay lãnh đạo.\n` +
    `- **O_THIEU_NGUON**: 3 ô (chi phí của C, chiến lược của B và C) hiển thị "Chưa có số liệu"; ô thời gian của C ghi "Chưa có báo giá". Chú thích nguồn dưới bảng nói rõ nghĩa.\n` +
    `- **KHUYEN_NGHI_TRUNG_LAP**: câu hỏi chọn phương án được trả lời "chưa đủ căn cứ để khuyến nghị" kèm lý do cụ thể thay vì chọn hộ A hoặc B.\n` +
    `- **MOI_SO_CO_NGUON**: ba số ở slide 2 có dòng Nguồn; mỗi ô bảng có tên nguồn trong ngoặc. Điểm yếu: bảng 4×3 chữ 14 pt khá dày (khoảng 90 chữ), hợp đọc trước hơn trình chiếu; đã nới giới hạn chữ cho riêng bộ này (95).\n`;
  await save(D, "executive-brief-trinh-lanh-dao", input, expect, f);
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
  const D = await newDeck({ title: "Quản trị rủi ro dự án", donVi: DONVI, footer: "Quản trị dự án · Quản trị rủi ro dự án" });
  D.title("Quản trị rủi ro dự án", "Học phần Quản trị dự án · Buổi học 90 phút · Sinh viên năm thứ ba", "Chào lớp, nêu chủ đề và thời lượng buổi học 90 phút. Lưu ý cho giảng viên: tổng thời gian các hoạt động đề xuất là 100 phút, vượt 10 phút so với thời lượng; cần quyết định bớt hoạt động nào trước khi dạy.", "Buổi học");
  let s = D.content("Cuối buổi, bạn làm được ba việc", "Mục tiêu bám chuẩn đầu ra trong đề cương học phần. Không thêm mục tiêu ngoài đề cương.", "Buổi học");
  input.de_cuong_hoc_phan.chuan_dau_ra.forEach((t, i) => numbered(s, 0.6, 1.45 + i * 1.1, 8.8, 0.95, i + 1, t.replace(/^CĐR\d: /, ""), ""));
  s = D.content("Buổi học gồm năm hoạt động", "Tiến trình theo thời gian. Thời lượng hiển thị đúng như đề xuất: 10, 25, 35, 20, 10 phút, tổng 100 phút. Cần giảng viên quyết định bớt 10 phút.", "Buổi học");
  const cols = [K.blue, K.green, K.gold, "5B8DB8", K.slate]; let acc = 0;
  hd.forEach(([t, p], i) => {
    const w = (8.8 * p) / tong;
    s.addShape("rect", { x: 0.6 + (8.8 * acc) / tong, y: 1.45, w: w - 0.05, h: 0.65, fill: { color: cols[i] }, line: { color: cols[i] }, objectName: "thanh-thoi-gian" });
    s.addText(`${p}'`, { x: 0.6 + (8.8 * acc) / tong, y: 1.45, w: w - 0.05, h: 0.65, fontSize: 16, bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "thanh-thoi-gian-chu" });
    acc += p;
    s.addShape("ellipse", { x: 0.6, y: 2.4 + i * 0.46, w: 0.26, h: 0.26, fill: { color: cols[i] }, line: { color: cols[i] }, objectName: "cham-mau" });
    s.addText(`${t} (${p} phút)`, { x: 1.05, y: 2.35 + i * 0.46, w: 8.3, h: 0.36, fontSize: 16, color: K.ink, valign: "middle", isTextBox: true, margin: 0, objectName: "hoat-dong" });
  });
  source(s, `Tổng các hoạt động: ${tong} phút; thời lượng buổi học: 90 phút`);
  s = D.content("Rủi ro là sự kiện có thể xảy ra và ảnh hưởng đến mục tiêu", "Khái niệm rủi ro: xác suất và tác động. Phân biệt rủi ro với vấn đề đã xảy ra. Hỏi sinh viên một ví dụ trong dự án tốt nghiệp của họ.", "Nội dung");
  await panel(s, 0.6, 1.6, 4.2, 2.3, "Rủi ro", ["Chưa xảy ra", "Có xác suất và tác động"], "info", "FaCloudSun");
  await panel(s, 5.2, 1.6, 4.2, 2.3, "Vấn đề", ["Đã xảy ra", "Cần xử lý ngay"], "warn", "FaExclamationCircle");
  s = D.content("Ma trận rủi ro: xác suất nhân với tác động", "Giải thích cách đọc ma trận ba nhân ba. Ô góc trên bên phải là rủi ro cần ứng phó trước.", "Nội dung");
  const lv = [["Trung bình", "Cao", "Rất cao"], ["Thấp", "Trung bình", "Cao"], ["Thấp", "Thấp", "Trung bình"]];
  const colr = { "Rất cao": K.red, "Cao": "D9822B", "Trung bình": "E6C36A", "Thấp": "9CC3A8" };
  s.addText("Xác suất ↑", { x: 0.6, y: 1.3, w: 2.0, h: 0.3, fontSize: 14, color: K.slate, isTextBox: true, margin: 0, objectName: "truc-y-nhan" });
  lv.forEach((r, i) => {
    s.addText(["Cao", "Vừa", "Thấp"][i], { x: 0.6, y: 1.65 + i * 0.95, w: 1.0, h: 0.9, fontSize: 14, color: K.slate, valign: "middle", isTextBox: true, margin: 0, objectName: "truc-y" });
    r.forEach((v, c) => {
      s.addShape("rect", { x: 1.7 + c * 2.6, y: 1.65 + i * 0.95, w: 2.5, h: 0.9, fill: { color: colr[v] }, line: { color: "FFFFFF", pt: 2 }, objectName: "o-ma-tran" });
      s.addText(v, { x: 1.7 + c * 2.6, y: 1.65 + i * 0.95, w: 2.5, h: 0.9, fontSize: 18, bold: true, color: v === "Rất cao" ? "FFFFFF" : K.ink, align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "o-ma-tran-chu" });
    });
  });
  ["Thấp", "Vừa", "Cao"].forEach((t, c) => s.addText(t, { x: 1.7 + c * 2.6, y: 4.52, w: 2.5, h: 0.3, fontSize: 14, color: K.slate, align: "center", isTextBox: true, margin: 0, objectName: "truc-x-nhan" }));
  s.addText("Tác động →", { x: 1.7, y: 4.82, w: 7.7, h: 0.3, fontSize: 14, color: K.slate, align: "center", isTextBox: true, margin: 0, objectName: "truc-x" });
  s = D.content("Nhóm lập ma trận rủi ro cho dự án tốt nghiệp", "Nhóm 4 người, 35 phút. Mỗi nhóm nêu ít nhất 5 rủi ro, xếp vào ma trận và đề xuất một biện pháp ứng phó cho rủi ro cao nhất.", "Hoạt động");
  ["Nêu ít nhất 5 rủi ro của dự án", "Xếp mỗi rủi ro vào ma trận", "Chọn rủi ro cao nhất, đề xuất biện pháp ứng phó"].forEach((t, i) => numbered(s, 0.6, 1.45 + i * 1.1, 8.8, 0.95, i + 1, t, "", K.green));
  s = D.content("Ba điều cần nhớ và bài tập về nhà", "Nhắc lại ba mục tiêu. Bài tập: hoàn thiện ma trận của nhóm. Nội dung ngoài đề cương học phần không đưa vào buổi này.", "Hoạt động");
  await panel(s, 0.6, 1.6, 2.8, 2.5, "Ba bước", ["Nhận diện", "Đánh giá", "Ứng phó"], "info", "FaLayerGroup");
  await panel(s, 3.6, 1.6, 2.8, 2.5, "Bài tập", ["Hoàn thiện ma trận rủi ro của nhóm"], "info", "FaPenFancy");
  await panel(s, 6.6, 1.6, 2.8, 2.5, "Học liệu", ["Giáo trình học phần, chương rủi ro"], "info", "FaBook");
  D.closing("Hỏi và đáp", "Câu hỏi của lớp trước khi kết thúc buổi học", "Dành thời gian còn lại cho câu hỏi. Nhắc hạn nộp bài tập theo thông báo của giảng viên.", "Hoạt động");
  const expect = {
    must_contain: ["Cuối buổi, bạn làm được ba việc", "Tổng các hoạt động: 100 phút", "thời lượng buổi học: 90 phút", "Ma trận rủi ro"], must_not_contain: ["Monte Carlo", "Giáo trình Quản trị dự án của"], allowed_derived: ["100"],
    deck: Object.assign({ min_slides: 6, max_slides: 10, talk_minutes: 90 }, DECK),
    traps: [{ id: "TONG_PHUT_VUOT", mo_ta: "Hoạt động cộng 100 phút, buổi học 90" }, { id: "NGOAI_DE_CUONG", mo_ta: "Monte Carlo không thuộc đề cương: không đưa vào" }, { id: "HOC_LIEU_KHONG_BIA", mo_ta: "Chỉ ghi học liệu đầu vào cho, không bịa tác giả" }],
  };
  const f = `- **TONG_PHUT_VUOT**: các hoạt động đề xuất cộng ${tong} phút, buổi học 90 phút. Slide tiến trình giữ đúng số phút đầu vào và ghi tổng ở dòng Nguồn; ghi chú người trình bày nêu rõ cần bớt 10 phút. Không tự cắt hoạt động nào.\n` +
    `- **NGOAI_DE_CUONG**: "Phân tích định lượng Monte Carlo" không có trong chuẩn đầu ra nên không đưa vào slide; ghi chú chỉ nhắc chung "nội dung ngoài đề cương".\n` +
    `- **HOC_LIEU_KHONG_BIA**: học liệu chỉ là "giáo trình học phần, chương rủi ro" theo đầu vào; không thêm tên sách, tác giả, năm.\n` +
    `- Ghi chú: skill nguồn mô tả "kế hoạch buổi học" bằng văn bản, không nói gì về slide; bộ slide dựng theo mục "Xuất PowerPoint" mới thêm.\n`;
  await save(D, "tro-ly-giang-day", input, expect, f);
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
  const D = await newDeck({ title: "Campaign brief tuyển sinh 2027", donVi: DONVI, footer: "Campaign brief · Tuyển sinh đợt 1 năm 2027" });
  const { pres } = D;
  D.title("Tuyển sinh đợt 1 năm 2027", "Campaign brief · Thời gian chạy: 01/02/2027–30/06/2027", "Giới thiệu chiến dịch và khoảng thời gian chạy. Đây là bản brief nội bộ, chưa phải kế hoạch chi tiết từng ngày.", "Brief");
  let s = D.content("Mục tiêu: 1.500 hồ sơ đăng ký trước 30/06/2027", "Mục tiêu đo được duy nhất trong đầu vào là số hồ sơ. Mục tiêu nhận diện thương hiệu chưa có con số nên chưa viết thành mục tiêu; cần bổ sung chỉ số và thời hạn.", "Brief");
  await stat(s, 0.6, 1.45, 4.2, 3.2, "FaBullseye", "1.500", "hồ sơ đăng ký xét tuyển, hạn 30/06/2027", K.blue);
  await panel(s, 5.2, 1.45, 4.2, 3.2, "Chưa đo được", ["Mục tiêu 'tăng nhận diện thương hiệu' chưa có chỉ số và thời hạn", "Cần bổ sung trước khi duyệt"], "warn", "FaExclamationTriangle");
  s = D.content("Hai nhóm đối tượng cùng dùng Facebook", "Học sinh lớp 12 dùng Facebook và Zalo, quan tâm học phí và cơ hội việc làm. Phụ huynh dùng Facebook, quan tâm học phí và học bổng.", "Brief");
  await panel(s, 0.6, 1.6, 4.2, 2.4, "Học sinh lớp 12", ["Kênh hay dùng: Facebook, Zalo", "Quan tâm: học phí, cơ hội việc làm"], "info", "FaUserGraduate");
  await panel(s, 5.2, 1.6, 4.2, 2.4, "Phụ huynh", ["Kênh hay dùng: Facebook", "Quan tâm: học phí, học bổng"], "info", "FaUsers");
  s = D.content("Thông điệp chính: học thật, ra trường có việc", "Thông điệp chính chưa có số liệu làm bằng chứng nên chỉ nêu như định hướng, không thêm con số. Thông điệp phụ về học bổng có căn cứ theo đầu vào.", "Brief");
  s.addShape("roundRect", { x: 0.6, y: 1.45, w: 8.8, h: 1.4, fill: { color: K.navy }, line: { color: K.navy }, rectRadius: 0.08, objectName: "the-chinh" });
  s.addText("Học thật, ra trường có việc", { x: 0.9, y: 1.5, w: 8.2, h: 0.9, fontSize: 30, bold: true, color: "FFFFFF", fontFace: "Cambria", valign: "middle", isTextBox: true, margin: 0, objectName: "thong-diep-chinh" });
  s.addText("Thông điệp chính · chưa có số liệu bằng chứng", { x: 0.9, y: 2.4, w: 8.2, h: 0.35, fontSize: 14, color: "D6E2F0", valign: "middle", isTextBox: true, margin: 0, objectName: "thong-diep-ghi-chu" });
  await panel(s, 0.6, 3.05, 4.2, 1.65, "Phụ: học bổng", ["Học bổng cho 100 thí sinh đầu tiên"], "info");
  await panel(s, 5.2, 3.05, 4.2, 1.65, "Phụ: thực tập", ["Chưa có số liệu bằng chứng"], "warn");
  s = D.content("Facebook Ads chiếm phần lớn ngân sách", "Ngân sách theo kênh, triệu đồng. Cộng bốn kênh là 520 triệu đồng, trong khi đầu vào khai tổng 500 triệu đồng, lệch 20 triệu đồng chưa giải thích; không tự điều chỉnh kênh nào.", "Kế hoạch");
  const slNS = D.n;
  colChart(D, s, pres.charts.BAR, [{ name: "Ngân sách", labels: kenh.map((r) => r[0]), values: kenh.map((r) => r[1]) }],
    { x: 0.6, y: 1.35, w: 5.9, h: 3.45, barDir: "bar", chartColors: [K.blue], showLegend: false, showValAxisTitle: true, valAxisTitle: "Triệu đồng", valAxisMinVal: 0 });
  await panel(s, 6.75, 1.45, 2.65, 3.3, "Cần rà lại", [`Cộng bốn kênh: ${tong}`, "Khai tổng: 500", "Lệch 20 triệu đồng chưa giải thích"], "warn", "FaExclamationTriangle");
  source(s, "Nguồn: dự kiến ngân sách theo kênh của đơn vị (đơn vị: triệu đồng)");
  s = D.content("Bốn pha: chuẩn bị, chạy, cao điểm, tổng kết", "Timeline theo bốn pha. Đầu vào chưa có ngày bắt đầu và kết thúc từng pha, người phụ trách và bàn giao, nên slide chỉ nêu pha và để trống mốc.", "Kế hoạch");
  ["Chuẩn bị", "Chạy", "Cao điểm", "Tổng kết"].forEach((p, i) => {
    const x = 0.6 + i * 2.25;
    s.addShape("rect", { x, y: 1.7, w: 2.15, h: 1.0, fill: { color: [K.blue, K.green, K.gold, K.slate][i] }, line: { color: "FFFFFF" }, objectName: "pha" });
    s.addText(p, { x, y: 1.7, w: 2.15, h: 1.0, fontSize: 20, bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0, objectName: "pha-chu" });
    s.addText("Mốc: ........", { x, y: 2.85, w: 2.15, h: 0.4, fontSize: 14, color: K.slate, align: "center", isTextBox: true, margin: 0, objectName: "moc" });
    s.addText("Phụ trách: ........", { x, y: 3.25, w: 2.15, h: 0.4, fontSize: 14, color: K.slate, align: "center", isTextBox: true, margin: 0, objectName: "phu-trach" });
  });
  s = D.content("KPI: 1.500 hồ sơ, ba kênh đã có chỉ tiêu lead", "KPI tổng là 1.500 hồ sơ. Ba kênh đã có chỉ tiêu lead; Zalo OA chưa có KPI nên để trống. Chưa nêu tần suất báo cáo vì đầu vào không có.", "Kế hoạch");
  table(s, [["Kênh", "KPI"], ["Facebook Ads", "600 lead"], ["Tư vấn tại trường THPT", "400 lead"], ["Website và SEO", "300 lead"], ["Zalo OA", "Chưa có KPI"], ["Tổng", "1.500 hồ sơ"]], { colW: [5.2, 3.6], y: 1.4, rowH: [0.55, 0.55, 0.55, 0.55, 0.55, 0.55], fontSize: 18 });
  const slKPI = D.n;
  s = D.content("Năm điều cần bổ sung trước khi duyệt chiến dịch", "Danh sách thông tin còn thiếu để brief đủ điều kiện duyệt. Đây là các chỗ đang để trống, không tự điền.", "Kế hoạch");
  ["Chỉ số, thời hạn cho mục tiêu nhận diện", "Số liệu bằng chứng cho thông điệp chính", "Mốc, người phụ trách của bốn pha", "KPI của kênh Zalo OA", "Giải thích chênh 20 triệu đồng ở tổng ngân sách"].forEach((t, i) => numbered(s, 0.6, 1.35 + i * 0.7, 8.8, 0.6, i + 1, t, "", K.gold));
  const expect = {
    must_contain: ["Mục tiêu: 1.500 hồ sơ", "Chưa đo được", "Cần rà lại", "Chưa có KPI", "Mốc: ........"], must_not_contain: ["tăng 20%", "tăng 30%"], allowed_derived: [money(tong)],
    deck: Object.assign({ min_slides: 6, max_slides: 10, talk_minutes: 15, charts: [{ slide: slNS, type: "bar", series: { "Ngân sách": kenh.map((r) => r[1]) } }], tables: [{ slide: slKPI, rows: 6, cols: 2, blank_text: "Chưa có KPI", blank_cells: 1 }] }, DECK),
    traps: [{ id: "NGAN_SACH_LECH", mo_ta: "Cộng kênh 520, khai tổng 500" }, { id: "MUC_TIEU_KHONG_DO_DUOC", mo_ta: "Nhận diện thương hiệu không có số: không viết thành mục tiêu SMART" },
      { id: "THONG_DIEP_THIEU_BANG_CHUNG", mo_ta: "Thông điệp chính không có số liệu: không bịa" }, { id: "KPI_THIEU", mo_ta: "Zalo OA không có KPI: để trống" }, { id: "TIMELINE_THIEU_MOC", mo_ta: "Không có mốc pha: dòng chấm" }],
  };
  const f = `- **NGAN_SACH_LECH**: cộng bốn kênh ${tong}, đầu vào khai 500 triệu đồng. Biểu đồ vẽ theo từng kênh; khung "Cần rà lại" nêu cả hai số.\n` +
    `- **MUC_TIEU_KHONG_DO_DUOC**: "tăng nhận diện thương hiệu" không có chỉ số, hạn; slide báo "chưa đo được", không tự bịa chỉ số.\n` +
    `- **THONG_DIEP_THIEU_BANG_CHUNG**: thông điệp chính và thông điệp phụ về thực tập được ghi rõ là chưa có số liệu bằng chứng ngay trên slide.\n` +
    `- **KPI_THIEU**: Zalo OA không có KPI; bảng ghi "Chưa có KPI". Ba kênh còn lại cộng 1.300 lead, trong khi KPI tổng là 1.500 hồ sơ: hai đơn vị khác nhau (lead và hồ sơ) nên không so trực tiếp; skill nên nói rõ cách quy đổi lead sang hồ sơ.\n` +
    `- **TIMELINE_THIEU_MOC**: không có mốc, người phụ trách từng pha; slide để dòng chấm "Mốc: ........", "Phụ trách: ........". Slide cuối liệt kê năm điều cần bổ sung.\n`;
  await save(D, "campaign-brief-tuyen-sinh", input, expect, f);
}

(async () => {
  await deckTongKet();
  await deckBrief();
  await deckGiangDay();
  await deckCampaign();
})().catch((e) => { console.error(e); process.exit(1); });
