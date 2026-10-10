// Thư viện thiết kế slide phong cách trường đại học (dùng chung cho tests/build_pptx.js).
// Bảng màu: xanh navy học thuật + vàng đồng làm điểm nhấn + xám xanh nhạt; phông Cambria (tiêu đề) và Calibri (nội dung).
// Không có thanh màu trang trí hay đường kẻ dưới tiêu đề. Nền trang tiêu đề là ảnh vẽ bằng SVG (không chứa chữ).
// Biểu tượng huy hiệu chỉ là hình trung tính: thay bằng logo thật của trường trong bố cục khi dùng thật.
const pptxgen = require("pptxgenjs");
const React = require("react");
const RDS = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");

const THEME = {
  name: "Dai hoc",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: { dk1: "1A2433", lt1: "FFFFFF", dk2: "0B2A4A", lt2: "F1F4F8", accent1: "1F4E8C", accent2: "B8902B", accent3: "2E7D6B", accent4: "6B7A90",
    accent5: "A23B3B", accent6: "5B8DB8", hlink: "1F4E8C", folHlink: "6B7A90" },
};
const K = { navy: "0B2A4A", blue: "1F4E8C", gold: "B8902B", green: "2E7D6B", slate: "6B7A90", red: "A23B3B", ink: "1A2433", panel: "F1F4F8", line: "D5DCE6", warn: "FBF1E1" };

const iconCache = {};
async function icon(name, color = "FFFFFF", size = 256) {
  const key = `${name}-${color}`;
  if (!iconCache[key]) {
    const svg = RDS.renderToStaticMarkup(React.createElement(fa[name], { color: "#" + color, size }));
    iconCache[key] = "image/png;base64," + (await sharp(Buffer.from(svg)).png().toBuffer()).toString("base64");
  }
  return iconCache[key];
}

async function backdrop(variant) {
  const rings = variant === "closing"
    ? `<circle cx="1450" cy="720" r="480" fill="#1F4E8C" fill-opacity="0.35"/><circle cx="1450" cy="720" r="350" fill="none" stroke="#B8902B" stroke-width="3"/><circle cx="1450" cy="720" r="270" fill="#0B2A4A" fill-opacity="0.5"/>`
    : `<circle cx="1470" cy="170" r="470" fill="#1F4E8C" fill-opacity="0.35"/><circle cx="1470" cy="170" r="340" fill="none" stroke="#B8902B" stroke-width="3"/><circle cx="1470" cy="170" r="260" fill="#0B2A4A" fill-opacity="0.45"/><circle cx="1470" cy="170" r="100" fill="#B8902B" fill-opacity="0.9"/>`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B2A4A"/><stop offset="1" stop-color="#14396B"/></linearGradient></defs><rect width="1600" height="900" fill="url(#g)"/>${rings}</svg>`;
  return "image/png;base64," + (await sharp(Buffer.from(svg)).png().toBuffer()).toString("base64");
}

// Huy hiệu trung tính (hai vòng tròn đồng tâm) cho góc trên trái trang tiêu đề.
async function crest() {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256"><circle cx="128" cy="128" r="120" fill="none" stroke="#B8902B" stroke-width="10"/><circle cx="128" cy="128" r="86" fill="#B8902B"/><circle cx="128" cy="128" r="46" fill="#0B2A4A"/></svg>`;
  return "image/png;base64," + (await sharp(Buffer.from(svg)).png().toBuffer()).toString("base64");
}

async function newDeck({ title, donVi, footer }) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
  pres.title = title;
  pres.author = donVi;
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const bgTitle = await backdrop("title");
  const bgClose = await backdrop("closing");
  const logo = await crest();
  const dark = (bg) => ({ background: { data: bg }, objects: [
    { image: { x: 0.6, y: 0.45, w: 0.55, h: 0.55, data: logo, altText: "Huy hiệu mẫu (thay bằng logo của trường)" } },
    { text: { text: donVi, options: { x: 1.3, y: 0.45, w: 6.0, h: 0.55, fontSize: 14, bold: true, color: "FFFFFF", valign: "middle", margin: 0 } } },
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.55, w: 6.6, h: 1.7, fontSize: 36, bold: true, color: "FFFFFF", valign: "bottom", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "sub", type: "body", x: 0.6, y: 3.45, w: 6.6, h: 1.2, fontSize: 18, color: "D6E2F0", valign: "top", align: "left", margin: 0 }, text: "" } },
  ] });
  pres.defineSlideMaster(Object.assign({ title: "TITLE" }, dark(bgTitle)));
  pres.defineSlideMaster(Object.assign({ title: "CLOSING" }, dark(bgClose)));
  pres.defineSlideMaster({
    title: "SECTION", background: { color: K.navy },
    objects: [
      { placeholder: { options: { name: "num", type: "body", x: 0.6, y: 1.2, w: 2.5, h: 1.6, fontSize: 80, bold: true, color: K.gold, fontFace: "Cambria", valign: "middle", align: "left", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "title", type: "title", x: 3.2, y: 1.2, w: 6.2, h: 1.6, fontSize: 34, bold: true, color: "FFFFFF", valign: "middle", align: "left", margin: 0 }, text: "" } },
    ],
  });
  pres.defineSlideMaster({
    title: "CONTENT", background: { color: "FFFFFF" },
    slideNumber: { x: 8.9, y: 5.17, w: 0.5, h: 0.3, fontSize: 11, color: K.slate, align: "right" },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.3, w: 8.8, h: 0.95, fontSize: 28, bold: true, color: K.navy, valign: "middle", align: "left", margin: 0 }, text: "" } },
      { text: { text: footer, options: { x: 0.6, y: 5.17, w: 6.5, h: 0.3, fontSize: 11, color: K.slate, valign: "middle", margin: 0 } } },
    ],
  });
  const D = { pres, n: 0, secs: new Set() };
  D.sec = (name) => { if (name && !D.secs.has(name)) { pres.addSection({ title: name }); D.secs.add(name); } };
  D.title = (title, sub, notes, section, master = "TITLE") => {
    D.sec(section); D.n++;
    const s = pres.addSlide({ masterName: master, sectionTitle: section });
    s.addText(title, { placeholder: "title" });
    s.addText(sub, { placeholder: "sub" });
    s.addNotes(notes);
    return s;
  };
  D.closing = (title, sub, notes, section) => D.title(title, sub, notes, section, "CLOSING");
  D.divider = (num, title, notes, section) => {
    D.sec(section); D.n++;
    const s = pres.addSlide({ masterName: "SECTION", sectionTitle: section });
    s.addText(num, { placeholder: "num" });
    s.addText(title, { placeholder: "title" });
    s.addNotes(notes);
    return s;
  };
  D.content = (title, notes, section) => {
    D.sec(section); D.n++;
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
    s.addText(title, { placeholder: "title" });
    s.addNotes(notes);
    return s;
  };
  return D;
}

function source(s, text) {
  s.addText(text, { x: 0.6, y: 4.83, w: 8.8, h: 0.3, fontSize: 11, italic: true, color: K.slate, isTextBox: true, margin: 0, valign: "middle", objectName: "nguon" });
}

// Thẻ số liệu: ô tròn biểu tượng, số lớn, nhãn.
async function stat(s, x, y, w, h, iconName, big, label, color = K.blue) {
  s.addShape("roundRect", { x, y, w, h, fill: { color: K.panel }, line: { color: K.panel }, rectRadius: 0.08, objectName: "the" });
  s.addShape("ellipse", { x: x + 0.25, y: y + 0.25, w: 0.6, h: 0.6, fill: { color }, line: { color }, objectName: "o-bieu-tuong" });
  s.addImage({ data: await icon(iconName), x: x + 0.4, y: y + 0.4, w: 0.3, h: 0.3, altText: "Biểu tượng minh họa", objectName: "bieu-tuong" });
  s.addText(big, { x: x + 0.25, y: y + 1.0, w: w - 0.5, h: 0.85, fontSize: 40, bold: true, color, fontFace: "Cambria", isTextBox: true, margin: 0, valign: "middle", objectName: "so-lieu" });
  s.addText(label, { x: x + 0.25, y: y + 1.9, w: w - 0.5, h: h - 2.05, fontSize: 16, color: K.ink, isTextBox: true, margin: 0, valign: "top", objectName: "nhan" });
}

// Khung nhận xét: tiêu đề nhỏ + các ý ngắn; tone "warn" cho điểm cần rà lại.
async function panel(s, x, y, w, h, heading, items, tone = "info", iconName) {
  const warn = tone === "warn";
  s.addShape("roundRect", { x, y, w, h, fill: { color: warn ? K.warn : K.panel }, line: { color: warn ? K.gold : K.panel, pt: warn ? 1 : 0.5 }, rectRadius: 0.08, objectName: warn ? "luu-y" : "nhan-xet" });
  let ty = y + 0.2;
  if (iconName) {
    s.addImage({ data: await icon(iconName, warn ? K.red : K.blue), x: x + 0.2, y: ty + 0.02, w: 0.3, h: 0.3, altText: "Biểu tượng", objectName: "bieu-tuong" });
  }
  s.addText(heading, { x: x + (iconName ? 0.6 : 0.2), y: ty, w: w - (iconName ? 0.8 : 0.4), h: 0.36, fontSize: 18, bold: true, color: warn ? K.red : K.navy, isTextBox: true, margin: 0, valign: "middle", objectName: "nhan-xet-tieu-de" });
  s.addText(items.map((t, i) => ({ text: t, options: { bullet: items.length > 1, breakLine: i < items.length - 1, fontSize: 16, color: K.ink, paraSpaceAfter: 8 } })),
    { x: x + 0.2, y: ty + 0.5, w: w - 0.4, h: h - 0.8, isTextBox: true, margin: 0, valign: "top", objectName: "nhan-xet-chu" });
}

const CHART = { catAxisLabelFontSize: 12, valAxisLabelFontSize: 12, dataLabelFontSize: 12, legendFontSize: 12, catAxisLabelColor: K.ink, valAxisLabelColor: K.ink, dataLabelColor: K.ink,
  valGridLine: { color: "E3E8EF", size: 0.5 }, catGridLine: { style: "none" }, showValue: true, legendPos: "b", valAxisTitleFontSize: 12, valAxisLineShow: false, catAxisLineShow: true };

// Thẻ đánh số: vòng tròn số + tiêu đề + mô tả.
function numbered(s, x, y, w, h, n, head, body, color = K.blue) {
  s.addShape("roundRect", { x, y, w, h, fill: { color: K.panel }, line: { color: K.panel }, rectRadius: 0.08, objectName: "the" });
  s.addShape("ellipse", { x: x + 0.25, y: y + (h - 0.65) / 2, w: 0.65, h: 0.65, fill: { color }, line: { color }, objectName: "so-thu-tu" });
  s.addText(String(n), { x: x + 0.25, y: y + (h - 0.65) / 2, w: 0.65, h: 0.65, fontSize: 22, bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0, fontFace: "Cambria", objectName: "so-thu-tu-chu" });
  const runs = [{ text: head, options: { bold: true, fontSize: 18, color: K.navy, breakLine: !!body } }];
  if (body) runs.push({ text: body, options: { fontSize: 14, color: "46536A" } });
  s.addText(runs, { x: x + 1.15, y: y + 0.08, w: w - 1.4, h: h - 0.16, isTextBox: true, margin: 0, valign: "middle", objectName: "the-chu" });
}

function table(s, rows, opts = {}) {
  const fs = opts.fontSize || 14;
  delete opts.fontSize;
  const head = rows[0].map((t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: K.navy }, fontSize: fs, valign: "middle" } }));
  const body = rows.slice(1).map((r, ri) => r.map((t, c) => ({ text: t, options: { fontSize: fs, color: K.ink, valign: "middle", bold: c === 0, fill: { color: ri % 2 === 0 ? "FFFFFF" : K.panel } } })));
  s.addTable([head, ...body], Object.assign({ x: 0.6, y: 1.45, w: 8.8, border: { type: "solid", pt: 0.75, color: K.line }, margin: [0.06, 0.1, 0.06, 0.1], objectName: "bang" }, opts));
}

const vn = (x, nd = 1) => x.toFixed(nd).replace(".", ",");
const money = (n) => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ".");

module.exports = { THEME, K, icon, newDeck, source, stat, panel, CHART, numbered, table, vn, money };
