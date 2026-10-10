# Quy cách đầu ra — phan-tich-ket-qua-khao-sat

Loại sản phẩm: `nghiep-vu`.

## Bắt buộc xuất file

Sản phẩm cuối phải là file thực tế đã được tạo, có thể tải xuống và tiếp tục chỉnh sửa. Không dùng nội dung trong chat hoặc writing block thay file; không chờ người dùng nhắc “xuất file”. Nếu người dùng chỉ hỏi giải thích hoặc kiểm tra trạng thái, trả lời trong chat; nếu yêu cầu soạn, sửa, tổng hợp hoặc tạo sản phẩm nghiệp vụ thì phải xuất file. Nếu người dùng yêu cầu rõ chỉ trả nội dung trong chat, thực hiện đúng yêu cầu đó.

Ưu tiên định dạng người dùng chỉ định và mẫu bắt buộc của nghiệp vụ. Mặc định của skill được ghi dưới đây. Văn bản hành chính, báo cáo dạng văn bản, biên bản, thông báo, quyết định, tờ trình, hợp đồng, phiếu, đề cương và tài liệu nội dung xuất Word `.docx`; bảng tính, bảng theo dõi hoặc lịch dạng bảng xuất Excel `.xlsx`; gói skill xuất các file nguồn và `.zip`. PDF chỉ xuất khi người dùng yêu cầu hoặc mẫu yêu cầu. Bộ hồ sơ có nhiều văn bản phải tạo đủ file nghiệp vụ thành phần, có thể gom trong một ZIP khi phù hợp.

Trước khi giao: kiểm tra file tồn tại và mở/đọc được, đuôi file khớp định dạng thực, nội dung khớp dữ liệu, đúng mẫu, có chỗ điền thông tin thiếu và không kèm tài liệu kiểm tra đầu ra. Word/PDF cần xem lại bố cục bằng bộ dựng trang khi có; Excel cần kiểm tra sheet, công thức và vùng in. Chỉ xác nhận kiểm tra nào đã thực hiện. Nếu không xem trước được, nêu rõ trong tin nhắn giao file, không chèn ghi chú vào file.

Phản hồi cuối cung cấp liên kết tải file hoặc file đính kèm và một câu mô tả ngắn. Nếu công cụ xuất lỗi, sửa lỗi trong phạm vi được phép; nếu vẫn không tạo được định dạng yêu cầu, báo giới hạn và giữ nguồn, không tuyên bố đã xuất file hoặc tự đổi đuôi file. Không tự chuyển sang Markdown/chat để coi nhiệm vụ đã hoàn thành. Việc thiếu dữ liệu không ngăn tạo file với chỗ điền đúng mẫu gốc.

Định dạng mặc định của skill: **.xlsx**. Nếu yêu cầu gồm cả báo cáo thuyết minh, tạo thêm file Word cho báo cáo; không ghép báo cáo dài vào bảng tính.

## Định dạng bổ sung

Định dạng đầu ra có thể chọn theo sản phẩm/yêu cầu: .xlsx, .csv, .pdf, .png, .svg. Đọc mục “Định dạng bổ sung” trong quy cách đầu ra trước khi chọn.

Không giới hạn đầu ra vào định dạng mặc định. Chọn định dạng theo sản phẩm người dùng yêu cầu và công cụ thực tế: DOCX để sửa văn bản; PDF để đọc/in/công bố; XLSX để giữ sheet/công thức; CSV để trao đổi dữ liệu bảng; TXT/MD để giao nội dung thuần; HTML để giao nội dung web; JSON/YAML để giao dữ liệu hoặc cấu hình; PPTX để giao bài trình chiếu; PNG/SVG để giao biểu đồ; TEX/BIB để giao nguồn bài viết khoa học/danh mục trích dẫn; ZIP để gom bộ hồ sơ hoặc gói skill. Chỉ tạo định dạng bổ sung khi sản phẩm cần hoặc người dùng yêu cầu; danh sách định dạng là cách lựa chọn đầu ra, không cam kết mọi công cụ chuyển đổi đều có sẵn.

Markdown phải là file .md thật khi được yêu cầu, không phải đoạn Markdown trong chat. CSV/JSON không thay XLSX khi cần công thức/định dạng. PPTX phải có slide thực; PNG/SVG phải là biểu đồ hoặc hình thật. HTML không đồng nghĩa website đã được đăng. Skill kịch bản video chỉ giao kịch bản; MP4/âm thanh chỉ có thể giao khi người dùng yêu cầu sản xuất và có công cụ thực sự tạo được. Không đổi đuôi file hoặc gọi file mô tả là media đã hoàn thành.

## Quy tắc giao văn bản

File giao người dùng chỉ chứa sản phẩm nghiệp vụ được yêu cầu, trình bày như văn bản thực tế. Không ghép checklist nghiệm thu, bảng rà soát pháp lý, bảng truy nguyên nguồn, danh sách thiếu dữ liệu, phiếu kiểm duyệt, nhật ký AI hay giải thích cách tạo vào file. Những bước đối chiếu trong quy trình là công việc nội bộ, không phải tài liệu phải xuất. Không tạo thêm file kiểm tra nếu người dùng không yêu cầu.

Thiếu thông tin thì giữ nhãn trường/mục và chừa chỗ điền đúng mẫu gốc: giữ nguyên dòng dấu chấm (......), dấu gạch hoặc ô trống nếu mẫu sử dụng. Không tự thêm dấu chấm vào ô bảng mà mẫu để trống; không tự đổi dấu chấm của mẫu thành ô trống. Nếu chưa có mẫu, dùng dòng dấu chấm cho trường cần điền trên văn bản hành chính và để trống ô số liệu trong bảng. Dấu chấm là chỗ điền thông tin, không phải dữ liệu đã xác nhận. Không dùng mã trong ngoặc vuông, “chưa cung cấp”, “cần xác minh”, “chờ ký” hoặc số 0 thay dữ liệu thiếu. Giá trị 0 chỉ dùng khi nguồn xác nhận bằng 0; kết quả tính thiếu đầu vào cũng để trống. Không điền tên trường, tên người, số văn bản, ngày ban hành, điều khoản, nhận xét hoặc chữ ký từ ví dụ hay từ ngày chạy công cụ. Giữ phần đã có dữ liệu; để trống kết luận/xếp loại chưa đủ căn cứ. Không biến ô trống thành khẳng định đã đáp ứng điều kiện.

Tình trạng chưa ký/chưa duyệt được quản lý trong trao đổi hoặc hệ thống xử lý, không tự chèn nhãn “DỰ THẢO – CHỜ KIỂM DUYỆT” vào thân văn bản. Chỉ dùng dấu DỰ THẢO khi người dùng yêu cầu hoặc mẫu/quy trình có quy định. Khối chữ ký có chức vụ và họ tên nếu đã biết, chừa khoảng ký; không tạo chữ ký, dấu hoặc trạng thái đã duyệt.

Phụ lục nghiệp vụ (danh sách đối tượng, biểu số liệu, phiếu đánh giá, tài liệu theo mẫu) chỉ giữ khi mẫu pháp định/hồ sơ yêu cầu hoặc người dùng yêu cầu; không dùng phụ lục để chứa kiểm tra đầu ra. Bảng chi tiết có thể đưa vào nội dung chính nếu mẫu cho phép. Nếu yêu cầu trực tiếp là kiểm tra hồ sơ, thẩm định hoặc lập bảng theo dõi, bảng kết quả là sản phẩm chính; không kèm một checklist kiểm tra sản phẩm đó.

## Chọn mẫu và căn cứ

1. Xác định loại văn bản, cơ quan ban hành, đối tượng, ngày nghiệp vụ, loại hình trường và quy chế nội bộ từ nguồn. Các trường “bắt buộc” trong bảng đầu vào là trường cần cho hồ sơ hoàn chỉnh, không phải lý do dừng soạn khi người dùng muốn để trống.
2. Văn bản hành chính: dùng Điều 8, Điều 9 và Phụ lục I, II, III Nghị định 30/2020/NĐ-CP. Văn bản chuyên ngành: dùng nguyên mẫu đúng phụ lục, mã biểu, tên biểu, cột và người ký của văn bản chuyên ngành còn áp dụng. Mẫu nội bộ chỉ dùng trong phạm vi được phép, không đổi mẫu pháp định.
3. Đọc văn bản gốc, sửa đổi và chuyển tiếp tại ngày nghiệp vụ trước khi khẳng định mẫu hiện hành. Với skill có `phap-ly.md`, đọc tài liệu này; tư liệu lịch sử không phải mẫu hiện hành. Chưa xác minh được mẫu thì soạn phần khung có căn cứ, để trống phần chưa xác định và nêu giới hạn ngắn trong trao đổi; không tự ghi “chuẩn pháp luật” cho mẫu tự dựng.
4. Báo cáo của tổ chức Đảng dùng thể thức văn bản Đảng đang áp dụng; không mặc định dùng quốc hiệu và tiêu ngữ hành chính. Bài báo, giáo trình, FAQ, nội dung truyền thông, bảng theo dõi và phiếu khảo sát dùng cấu trúc chuyên môn phù hợp; không biến tất cả thành biên bản.

## Trình bày văn bản hành chính

Nguồn gốc để đối chiếu: [Nghị định 30/2020/NĐ-CP và phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2020/03/30.signed.pdf). Các trị số sau áp dụng cho văn bản hành chính, không thay quy cách riêng của biểu chuyên ngành.

- A4 210 × 297 mm, thông thường chiều dọc; bảng biểu không tách thành phụ lục có thể dùng chiều ngang theo Phụ lục I. Lề trên/dưới 20–25 mm, trái 30–35 mm, phải 15–20 mm. Thiết lập mặc định khi không có mẫu: trên/dưới 20 mm, trái 30 mm, phải 15 mm.
- Times New Roman, Unicode TCVN 6909:2001, màu đen. Nội dung cỡ 13–14, canh đều hai lề; đầu dòng lùi 1–1,27 cm, cách đoạn tối thiểu 6 pt; giãn dòng từ đơn đến 1,5. Có thể dùng nội dung 13 pt, lùi 1 cm, cách đoạn 6 pt, giãn dòng 1,15.
- Quốc hiệu ở phía trên bên phải, in hoa đậm, cỡ 12–13. Tiêu ngữ cỡ 13–14, đậm, căn giữa dưới quốc hiệu, viết đúng “Độc lập - Tự do - Hạnh phúc”, có đường kẻ dưới. Hai dòng cách nhau dòng đơn.
- Bên trái: tên cơ quan chủ quản trực tiếp nếu có, rồi cơ quan ban hành; chữ hoa cỡ 12–13, tên cơ quan ban hành đậm và có đường kẻ dưới. Không tự coi phòng soạn thảo là cơ quan ban hành văn bản của trường.
- Số/ký hiệu cỡ 13, dưới cơ quan ban hành; địa danh/ngày tháng cỡ 13–14 nghiêng, dưới tiêu ngữ. Số chưa cấp để trống; không lấy số tiếp theo hoặc ngày hiện tại để điền. Ký hiệu theo loại văn bản và quy định của cơ quan; công văn không dùng chữ viết tắt loại “CV”.
- Văn bản có tên loại: tên loại chữ hoa đậm cỡ 13–14, căn giữa; trích yếu ở dòng dưới, đậm cùng cỡ. Trích yếu của thông báo, báo cáo, kế hoạch, tờ trình không bắt buộc mở đầu “V/v”. Công văn không có tiêu đề “CÔNG VĂN”; trích yếu cỡ 12–13, chữ thường, sau “V/v”, dưới số/ký hiệu.
- Chức vụ/quyền hạn người ký chữ hoa đậm cỡ 13–14; họ tên đậm cỡ 13–14. Chỉ dùng TM., KT., TL., TUQ. khi đúng tư cách và có căn cứ phân công/ủy quyền; không mặc định người ký thay hoặc thừa lệnh.
- Nơi nhận ở cuối bên trái: nhãn “Nơi nhận:” cỡ 12 nghiêng đậm, danh sách cỡ 11. Khối chữ ký ở cuối bên phải; biên bản bố trí chữ ký các bên theo mẫu. Số trang chữ số Ả Rập cỡ 13–14, giữa lề trên, không hiển thị trang đầu.
- Khi xuất DOCX/PDF, thiết lập thực các thuộc tính trên, bảng không tràn lề, hàng không bị cắt, khối ký không đứng một mình; đọc lại bản render trước giao file. Markdown chỉ biểu diễn nội dung, không chứng minh lề, phông, cỡ chữ hoặc phân trang đã đúng.

## Cấu trúc sản phẩm của skill

1. Tiêu đề báo cáo + đối tượng khảo sát + mục đích + năm thực hiện;

2. Phần I – Thông tin chung: số phiếu phát ra, số phiếu hợp lệ, tỷ lệ phản hồi (đánh giá đạt/không đạt yêu cầu), cơ cấu đối tượng (khóa/ngành/năm tốt nghiệp...);

3. Phần II – Kết quả chi tiết: bảng điểm trung bình từng câu hỏi (kèm so sánh kỳ trước nếu có, chênh lệch, xếp loại theo quy ước ≥ 4.0 tốt / 3.0–3.99 trung bình / < 3.0 cần cải thiện) và điểm trung bình chung;

4. Phần III – Nhận xét: điểm mạnh, điểm cần cải thiện nhất, xu hướng so với kỳ trước, ý kiến mở nổi bật (nhóm theo chủ đề, tỷ lệ %);

5. Phần IV – Đề xuất cải tiến: 03–05 đề xuất cụ thể, mỗi đề xuất gắn đơn vị thực hiện và thời hạn.

Cấu trúc này là hướng dẫn nội dung; nếu có mẫu chuyên ngành được áp dụng thì giữ nguyên mẫu. Các bảng điểm, kết luận, yêu cầu chỉnh sửa và kết quả kiểm tra thực tế của nghiệp vụ được giữ trong văn bản; không nhầm chúng với checklist tự kiểm tra của AI.

## Thể thức và bảng biểu khi dựng file

- Dòng tiêu đề đậm, nền nhạt, cố định (freeze) khi bảng dài; bề rộng cột vừa chữ; số tiền có dấu phân cách hàng nghìn; ngày theo dd/mm/yyyy; giữ công thức, không dán giá trị thay công thức.
- Đặt vùng in và lặp dòng tiêu đề khi in; dữ liệu khác bản chất để ở sheet riêng; ô thiếu dữ liệu để trống, không ghi 0.
- Mở file kiểm tra công thức đã tính, không có lỗi `#`, định dạng hiển thị đúng trước khi giao.

## Biểu đồ và hình trong báo cáo số liệu

**Khi nào vẽ**
- Chỉ vẽ khi có từ 3 giá trị trở lên cần so sánh hoặc theo dõi xu hướng, và mọi số đều có trong đầu vào hoặc tính được từ đầu vào. Không vẽ cho 1–2 con số.
- Không vẽ nhóm có mẫu quá nhỏ (khảo sát dưới 30 phiếu), số liệu chưa có minh chứng, hoặc để gợi ra kết luận mà dữ liệu không nói.
- Mỗi hình đi kèm một bảng cùng số liệu trong báo cáo. Số trong hình phải trùng số trong bảng (cùng cách làm tròn). Khi hai nguồn lệch nhau, giữ nguyên, nêu độ lệch ở mục hạn chế, không tự chọn số cho đẹp.

**Chọn loại biểu đồ**
- So sánh giữa các nhóm: cột. So sánh hai kỳ hoặc dự toán với thực hiện: cột ghép. Thang đo nhiều mức (Likert): cột xếp chồng 100%. Xu hướng từ 4 mốc thời gian trở lên: đường.
- Không dùng biểu đồ 3D. Biểu đồ tròn chỉ khi có không quá 5 phần và tổng là 100%.

**Trục, nhãn, màu**
- Cột bắt đầu từ 0. Ghi tên trục và đơn vị (điểm, %, triệu đồng, số công trình). Ghi số trên cột nếu không quá dày; nếu dày thì ghi trong bảng.
- Đường ngưỡng đánh giá vẽ bằng nét đứt, chú giải đặt ngoài vùng vẽ để không đè lên nhãn số.
- Phải phân biệt được khi in đen trắng: dùng độ đậm nhạt khác nhau kèm hoa văn, không dựa riêng vào màu. Chữ trong hình dùng Times New Roman hoặc phông tương đương, từ 8 pt trở lên khi in.

**Dữ liệu thiếu, chưa đủ kỳ, câu đảo**
- Thiếu dữ liệu: ghi “n/a” hoặc “chưa có minh chứng” đúng vị trí, không vẽ cột 0 và không cộng thiếu vào tổng.
- Năm chưa đủ (ví dụ đến 30/9): ghi mốc ngay trong nhãn trục và dòng Nguồn; không nhận xét tăng giảm so với năm đủ 12 tháng.
- Câu hỏi đảo mã hóa ngược trước khi tính và vẽ, ghi chú trong dòng Nguồn. Hai kỳ chỉ so sánh khi câu hỏi và thang đo giữ nguyên.

**Dựng trong Word**
- Ảnh PNG từ 150 dpi khi in (khuyến nghị 200), rộng 8–16 cm, căn giữa, không vượt vùng chữ.
- Dưới hình: dòng “Hình n. Tên hình” (cỡ 13, đậm, căn giữa), rồi dòng “Nguồn: …” (cỡ 13, nghiêng, căn giữa; ghi kỳ, phạm vi, ghi chú). Hình, chú thích và nguồn dính nhau để không tách trang. Số hình liên tục từ 1. Tên bảng ghi “Bảng n. …” đặt phía trên bảng.
- Văn bản thay thế (alt) của hình ghi số liệu theo dạng “nhãn=giá trị; …” kèm đơn vị, để người dùng đọc màn hình và để đối chiếu với bảng.
- Hình PNG không sửa được số. Nếu người dùng cần sửa, giao kèm file Excel có biểu đồ gốc, và nói rõ khi số liệu đổi thì phải vẽ lại hình.
- Số thập phân dùng một kiểu thống nhất trong cả văn bản (khuyến nghị dấu phẩy: 4,12); ngưỡng và ví dụ trong báo cáo viết cùng kiểu.

**Dựng trong Excel**
- Dùng biểu đồ gốc tham chiếu ô dữ liệu (không dán ảnh). Đặt biểu đồ bên dưới bảng, không đè lên dữ liệu.
- Đặt hướng in ngang, vừa chiều rộng một trang, đặt vùng in và lặp dòng tiêu đề, để bảng và biểu đồ không bị cắt giữa các trang.

**Trước khi giao**: mở file xem từng hình: nhãn không đè nhau, chữ không bị cắt, hình nằm cùng trang với chú thích, số khớp bảng. Kiểm tra tự động chỉ bắt được lỗi cấu trúc, không thay việc nhìn hình.

## Xuất PowerPoint (.pptx) khi được yêu cầu

- **Bộ slide là tài liệu trình bày, không thay văn bản gốc.** Không dùng quốc hiệu, nơi nhận, khối chữ ký của văn bản hành chính trên slide. Công văn, quyết định, báo cáo chính thức vẫn giao bằng .docx; nói rõ điều này trong phản hồi.
- **Xác định cách dùng**: trình chiếu trực tiếp (ít chữ, mỗi slide một ý, khoảng 1,5–2 phút mỗi slide, số slide không vượt số phút của bài nói) hay đọc trước (được nhiều chữ hơn, nhưng vẫn một ý mỗi slide). Chưa biết thì ghi giả định đã dùng.
- **Cấu trúc**: slide mở đầu, kết luận hoặc tóm tắt đặt trước, các phần nội dung, tồn tại hoặc điểm cần quyết, bước tiếp theo. Tiêu đề mỗi slide nêu kết luận (không quá 16 chữ, không dấu chấm cuối) và là ô tiêu đề thật của slide để có dàn ý và đọc được bằng trình đọc màn hình.
- **Cỡ chữ**: tiêu đề từ 28 pt, nội dung và chữ trong bảng từ 14 pt, nguồn và chú thích từ 11 pt. Không thu nhỏ chữ để nhét thêm; quá dày thì tách slide. Khi trình chiếu trực tiếp, mỗi slide không quá khoảng 85 chữ.
- **Số liệu và biểu đồ**: dùng biểu đồ gốc của PowerPoint (sửa được), không dán ảnh; áp dụng quy tắc biểu đồ trong quy cách này nếu có. Mỗi biểu đồ và mỗi số nổi bật có dòng “Nguồn”. Thiếu số liệu thì ghi “Chưa có số liệu”, không vẽ cột 0.
- **Dữ liệu lệch hoặc thiếu**: số liệu lệch nhau, mục tiêu không đo được, đơn vị chưa nộp báo cáo, thiếu định hướng của lãnh đạo: nói thẳng trên slide (ô “Cần rà lại”, “Chưa có số liệu”) và trong ghi chú. Không điền cho đẹp, không bịa chỉ tiêu, nguồn, tên sách.
- **Ghi chú người trình bày** trên mọi slide (từ 15 chữ): lời nói chính, nguồn, điểm cần thận trọng. Không đặt ghi chú vào ô chữ trên slide.
- **Trình bày**: một bảng màu, bố cục và vị trí tiêu đề nhất quán, lề từ 0,5 inch, chữ không đè nhau, không có slide toàn chữ khi có thể dùng số liệu hoặc hình. Các nhãn trục, cột, ô trong sơ đồ phải đủ để đọc mà không cần lời nói.
- **Trước khi giao**: chạy công cụ kiểm tra cấu trúc của kỹ năng pptx, xuất ảnh từng slide và xem: chữ không tràn khung, không đè nhau, số khớp nguồn. Kiểm tra tự động không thay việc xem ảnh.
