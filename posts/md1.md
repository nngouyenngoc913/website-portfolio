## Bối Cảnh: Đi Tìm Điểm Chung Bằng Tư Duy Hệ Thống

Việc xây dựng hệ thống tài khoản kế toán theo mô hình Cây quyết định (Decision Tree) thực chất bắt nguồn từ nhu cầu cốt lõi: tìm kiếm các bối cảnh (context) giả định cho mọi trường hợp giao dịch có thể xảy ra trong doanh nghiệp.
1/ Assumption : double - entry (debit - credit)
2/ Evidence : TT 200 - Nguyên lí kế toán - Accounting docs (optional)
3/ Transaction : Lớp kế toán thực hành có sửa bài tập
4/ COA : chart of accounts

### Lý Do Nên Chuyển Đổi Phương Pháp Tư Duy
* **Tăng tính chính xác tuyệt đối:** Hệ thống định khoản dựa vào từ khóa (keywords) và các quy luật logic, giúp loại bỏ hoàn toàn thói quen làm việc theo cảm tính. 
* **Xây dựng Knowledge Database:** Mọi giao dịch, cách xử lý và quy tắc đều được lưu trữ thành một nền tảng dữ liệu vững chắc.
> **Tựu trung lại:** Lợi ích lớn nhất mà công nghệ này mang lại chính là Tốc độ - Khả năng nhận định - Tự động xây dựng mẫu hình - Dự báo các giao dịch tương lai.

**1/ Đặt biến**
const = const transactionTypes = [
{ type: "bán hàng", keywords: ["xuất kho", "bán hàng", "doanh thu"] },
{ type: "chi tiền", keywords: ["chi tiền", "tiền mặt", "ngân hàng"] },
{ type: "trả lương", keywords: ["trả lương", "lương", "334"] },
{ type: "nộp thuế", keywords: ["thuế gtgt", "nộp thuế", "333"] },
{ type: "tạm ứng", keywords: ["tạm ứng", "ứng trước"] },
{ type: "mua hàng hóa", keywords: ["mua", "hàng hóa", "156"] }

**2/ Transactions From TT200/2014 (TK đuôi 1→6)**
1.Bán hàng hóa/Dịch vụ thu ngay bằng tiền mặt** (kèm thuế GTGT, TTĐB, XK, BVMT)
2.**Nhận trợ cấp, trợ giá bằng tiền mặt** từ Ngân sách Nhà nước (NSNN)
3.Doanh thu hoạt động tài chính, thu nhập khác** bằng tiền mặt
4. Rút tiền gửi ngân hàng về nhập quỹ, xuất quỹ tiền mặt gửi vào tk ngân hàng**
5.Vay nhận bằng tiền mặt**
6.Thu hồi nợ phải thu, cho vay, ký cược, ký quỹ bằng tiền mặt**
**7.Bán các khoản đầu tư ngắn hạn, dài hạn thu bằng tiền mặt**
**8.Nhận được vốn góp của chủ sở hữu** bằng tiền mặt
**9.Nhận tiền của các bên trong hợp đồng hợp tác kinh doanh** không thành lập pháp nhân
**10.Thừa quỹ tiền mặt** phát hiện khi kiểm kê chưa rõ nguyên nhân
**11.Phát sinh doanh thu/thu nhập khác bằng ngoại tệ** là tiền mặt
**12.Thu nợ phải thu bằng ngoại tệ** (Nếu phát sinh **lãi tỷ giá**)
**13. Thu nợ phải thu bằng ngoại tệ** (Nếu phát sinh **lỗ tỷ giá**)
**14.Nhận trước tiền của người mua bằng ngoại tệ**
**15.Đánh giá lại ngoại tệ tăng giá** (Lãi tỷ giá tại BCTC)
**16.Đánh giá lại vàng tiền tệ phát sinh lãi**
**17.Xuất quỹ tiền mặt gửi vào TK Ngân hàng, ký quỹ, ký cược**
**18.Xuất quỹ tiền mặt mua chứng khoán, đầu tư dài hạn**
**19.Mua hàng tồn kho (KKTT), TSCĐ, XDCB** (Thuế GTGT được khấu trừ)
**20.Mua hàng tồn kho (KKTT), TSCĐ, XDCB** (Thuế GTGT không được khấu trừ)
**21.Mua hàng tồn kho (KKĐK)** (Thuế GTGT được khấu trừ)
**22.Mua hàng tồn kho (KKĐK)** (Thuế GTGT không được khấu trừ)
**23.Mua NVL sử dụng ngay** (Thuế GTGT được khấu trừ)
**24.Mua NVL sử dụng ngay** (Thuế GTGT không được khấu trừ)
**25.Thanh toán các khoản vay, nợ phải trả** (331, 333, 334, 335, 336, 338, 341)
**26.Chi quỹ tiền mặt cho hoạt động tài chính, hoạt động khác**
**27.Thiếu quỹ tiền mặt** phát hiện khi kiểm kê chưa rõ nguyên nhân
**28.Mua hàng hóa/dịch vụ bằng ngoại tệ** (Nếu phát sinh **lỗ tỷ giá**)
**29.Thanh toán nợ phải trả bằng ngoại tệ** (Nếu phát sinh **lỗ tỷ giá**)
**30.Thanh toán nợ phải trả bằng ngoại tệ** (Nếu phát sinh **lãi tỷ giá**)
**31.Trả trước tiền bằng ngoại tệ cho người bán** (Nếu phát sinh **lỗ tỷ giá**)
**32.Đánh giá lại ngoại tệ giảm giá** (Lỗ tỷ giá tại BCTC)
**33.Đánh giá lại vàng tiền tệ phát sinh lỗ**
**34.Bán các khoản đầu tư ngắn hạn/dài hạn** thu bằng tiền gửi ngân hàng
35.**Nhận ký quỹ, ký cược** của DN khác bằng tiền gửi ngân hàng.
36.**Bán các khoản đầu tư ngắn hạn/dài hạn** thu bằng tiền gửi ngân hàng
37.**Nhận được vốn góp của chủ sở hữu** bằng tiền
38.**Nhận tiền của các bên trong Hợp đồng Hợp tác Kinh doanh** (để trang trải hoạt động chung).
39.**Thu nợ phải thu bằng ngoại tệ** là TGNH
40.**Đánh giá lại ngoại tệ tăng giá** (Lãi tỷ giá tại BCTC), **Đánh giá lại vàng tiền tệ phát sinh lãi** (ghi nhận DTHĐTC).
41.**Thu hồi/Bán các khoản đầu tư ngắn hạn, dài hạn thu bằng tiền gửi ngân hàng**
**42.Thu hồi các khoản đầu tư nắm giữ đến ngày đáo hạn** (TK 128) khi đáo hạn
**43.Mua chứng khoán, cho vay hoặc đầu tư** vào công ty con, công ty liên doanh, liên kết... bằng tiền gửi ngân hàng
44.**Khi trả tiền mua trái phiếu nhận lãi trước**
**45.Khi trả tiền mua trái phiếu nhận lãi định kỳ hoặc lãi sau**
46.**Bán sản phẩm, hàng hoá, cung cấp dịch vụ chưa thu được ngay bằng tiền** (kể cả các khoản phải thu về tiền bán hàng xuất khẩu của bên giao ủy thác).
47.**Xác định số tiền khách hàng phải trả theo tiến độ kế hoạch** (Áp dụng cho hợp đồng xây dựng).
48.**Phản ánh giá trị khối lượng thực hiện hợp đồng xây dựng** được khách hàng xác nhận
49.**Khoản tiền thưởng** thu được từ khách hàng hoặc **khoản bồi thường** thu được từ khách hàng hay các bên khác (để bù đắp chi phí không bao gồm trong giá trị hợp đồng)
50.**Thanh toán bằng hàng (hàng đổi hàng)**.
51.**Thu hồi nợ phải thu** (từ khách hàng) bằng tiền mặt/tiền gửi ngân hàng
52.**Nhận được tiền thanh toán khối lượng công trình hoàn thành hoặc khoản ứng trước** từ khách hàng.
53.**Nhận trước tiền của người mua bằng ngoại tệ.**
**54.Thu nợ phải thu bằng ngoại tệ** (Nếu phát sinh **Lãi/lỗ tỷ giá hối đoái**).
55.**Kế toán hàng bán bị khách hàng trả lại, chiết khấu thương mại và giảm giá hàng bán**
**56.Chiết khấu thanh toán** phải trả cho người mua do người mua thanh toán hàng sớm
57.**Đánh giá lại số dư ngoại tệ giảm giá** so với Đồng Việt Nam
58.**Mua hàng tồn kho (KKTT), TSCĐ, XDCB, BĐSĐT** nếu thuế GTGT đầu vào được khấu trừ.
59.**Mua hàng tồn kho (KKĐK)** nếu thuế GTGT đầu vào được khấu trừ.
60.**Mua nguyên vật liệu/dịch vụ sử dụng ngay vào sản xuất, kinh doanh** nếu thuế GTGT đầu vào được khấu trừ.
61.**Mua hàng hóa giao bán ngay cho khách hàng** (không qua nhập kho), nếu thuế GTGT được khấu trừ.
62.**Nhập khẩu vật tư, hàng hoá, TSCĐ** (Thuế GTGT đầu vào được khấu trừ).
63.**Bù trừ lãi/lỗ tỷ giá** khi mua hàng hóa/dịch vụ thanh toán bằng ngoại tệ.
64.**Kết chuyển thuế GTGT đầu vào** để khấu trừ vào thuế GTGT đầu ra (cuối tháng).
65.**Hoàn nhập thuế GTGT đầu vào** (khi hàng đã mua và đã trả lại hoặc được giảm giá).
66.**Xác định thuế GTGT đầu vào không được khấu trừ** (khi hạch toán chung).
67.**Xác định thuế GTGT đầu vào không được khấu trừ** (khi hạch toán chung).
68.**Thuế GTGT đầu vào không được khấu trừ** do tài sản mua vào bị tổn thất (đã xác định được người chịu trách nhiệm).
69.**Thuế GTGT đầu vào của vật tư bị tổn thất** (chưa xác định được nguyên nhân, chờ xử lý).
70.**Thu được tiền hoàn thuế GTGT đầu vào** của hàng hóa, dịch vụ.
71.**Phí uỷ thác nhập khẩu** (được tính vào giá trị hàng nhập khẩu)
**72.Tạm ứng tiền hoặc vật tư** cho người lao động trong doanh nghiệp.
73.**Thu hồi nợ phải thu, cho vay, ký cược, ký quỹ bằng tiền mặt**
**74.Quyết toán khoản tạm ứng** khi thực hiện xong công việc được giao (bằng các chứng từ gốc đã được ký duyệt).
75.**Các khoản tạm ứng chi (hoặc sử dụng) không hết**, phải nhập lại quỹ/kho hoặc trừ vào lương của người nhận tạm ứng.
76.**Thu hồi nợ phải thu, cho vay, ký cược, ký quỹ bằng tiền mặt.**
**77.Mua nguyên liệu, vật liệu nhập kho** (Thuế GTGT được khấu trừ).
**78.Mua nguyên liệu, vật liệu nhập kho** (Thuế GTGT không được khấu trừ).
**79.Nguyên vật liệu nhập khẩu** (Bao gồm thuế nhập khẩu, TTĐB, BVMT phải nộp).
**80.Nguyên vật liệu mua đang đi đường** (chưa về kho cuối kỳ kế toán).
81.**Chi phí thu mua, bốc xếp, vận chuyển** nguyên vật liệu về kho.
82.**Nhập kho nguyên liệu, vật liệu thuê ngoài gia công, chế biến xong.**
**83.Nhập kho nguyên liệu, vật liệu thuê ngoài gia công, tự chế biến xong**
**84.Nguyên vật liệu thừa phát hiện khi kiểm kê** (chưa xác định được nguyên nhân).
85.**Xuất kho nguyên vật liệu sử dụng vào sản xuất, kinh doanh** (Ghi vào chi phí trực tiếp).
86.**Xuất kho nguyên vật liệu sử dụng cho hoạt động XDCB hoặc sửa chữa lớn TSCĐ**
**87.Xuất nguyên vật liệu đưa đi gia công, chế biến.**
**88.Xuất kho nguyên vật liệu để tự chế biến** (chưa hoàn thành)
89.**Xuất nguyên vật liệu góp vốn** vào công ty con, liên doanh, liên kết.
90.**Nguyên vật liệu trả lại cho người bán** hoặc được giảm giá sau khi nhập kho.
91.**Nguyên vật liệu hao hụt nằm trong phạm vi hao hụt cho phép**
**92.Nguyên vật liệu hao hụt, mất mát chưa xác định rõ nguyên nhân** (chờ xử lý).
93.**Ghi nhận giá vốn khi bán nguyên vật liệu, phế liệu** (thanh lý).
94.**Mua công cụ, dụng cụ nhập kho** (Thuế GTGT được khấu trừ).
95.**Mua công cụ, dụng cụ nhập kho** (Thuế GTGT không được khấu trừ).
96.**Công cụ, dụng cụ mua đang đi đường** (chưa về kho cuối kỳ kế toán).
97.**Công cụ, dụng cụ mua đang đi đường** (đã tạm tính tháng trước, nay về nhập kho).
98.**Nhập khẩu công cụ, dụng cụ** (tương tự như nguyên vật liệu nhập khẩu).
99.**Xuất công cụ, dụng cụ sử dụng** (Ghi tăng chi phí trả trước hoặc chi phí trực tiếp).
100.**Công cụ, dụng cụ trả lại cho người bán** hoặc được giảm giá.
101.**Công cụ, dụng cụ bị mất mát, hao hụt** (chờ xử lý)
102.**Kết chuyển chi phí nguyên liệu, vật liệu trực tiếp** đưa vào sản xuất, chế tạo sản phẩm.
103.**Kết chuyển chi phí nhân công trực tiếp** tham gia sản xuất, chế tạo sản phẩm.
104.**Kết chuyển chi phí sản xuất chung/Chi phí sử dụng máy thi công** phân bổ cho từng đối tượng chi phí.
105.**Nguyên vật liệu xuất thuê ngoài gia công, chế biến** (đối với bên giao gia công).
106.**Chi phí thuê ngoài gia công, chế biến** phát sinh
107.**Chi phí sửa chữa và bảo hành công trình** (Xây lắp) trước khi kết chuyển.
108.**Trị giá sản phẩm hỏng không sửa chữa được** và người gây ra thiệt hại phải bồi thường (chưa xác định được người chịu trách nhiệm).
109.**Kết chuyển giá thành sản phẩm thực tế nhập kho trong kỳ** (Thành phẩm).
110.**Kết chuyển giá thành thực tế dịch vụ đã hoàn thành** và được xác định là đã bán trong kỳ.
111.**Giá thành sản phẩm (điện, nước,...) sản xuất xong, tiêu thụ ngay** (không qua nhập kho).
112.**Giá thành sản phẩm sản xuất ra được sử dụng tiêu dùng nội bộ** ngay (không qua nhập kho).
113.**Trị giá sản phẩm phụ/phế liệu thu hồi** (Làm giảm chi phí sản xuất).
114.**Kết chuyển chi phí sản xuất chung cố định không phân bổ** (do sản lượng thấp hơn công suất bình thường).
115.**Kết chuyển chi phí nguyên vật liệu, nhân công vượt trên mức bình thường** (không được tính vào giá thành)
116.**Khi công việc sửa chữa bảo hành công trình xây lắp hoàn thành bàn giao** cho khách hàng.
117.**Bàn giao sản phẩm xây lắp hoàn thành chờ bán** (hoặc chưa bàn giao).
118.**Mua TSCĐ hữu hình** (Nếu thuế GTGT được khấu trừ).
119.**Mua TSCĐ hữu hình** (Nếu thuế GTGT không được khấu trừ).
120.**Nhận TSCĐ do đầu tư XDCB hoàn thành bàn giao.*
**121.Nhận TSCĐ biếu tặng, cấp trên cấp** (hoặc nhận vốn góp bằng TSCĐ)
122.**TSCĐ nhập khẩu** (Thuế GTGT đầu vào được khấu trừ).
123.**Nhận bàn giao công trình đã được quyết toán** (Chủ đầu tư - Xây lắp).
124.**Điều chỉnh tăng giá trị công trình** (Chủ đầu tư) do giá được quyết toán lớn hơn giá tạm tính
125.**Nhận chuyển giao quyền sở hữu tài sản thuê tài chính** (mua lại sau khi thuê hết một phần giá trị).=
126.**Thanh lý, nhượng bán TSCĐ, TSVH**
**127.Điều chuyển TSCĐ nội bộ** (cho đơn vị hạch toán phụ thuộc).
128.**Đánh giá lại TSCĐ** , TSVH (Nếu giảm nguyên giá).
129.**Góp vốn, đầu tư bằng TSCĐ, TSVH** (Khi xuất TSCĐ)
130.**Phát hiện thiếu TSCĐ hữu hình, TSVH** (chưa xác định rõ nguyên nhân, chờ xử lý).
131.**Điều chỉnh giảm giá trị công trình** (Chủ đầu tư) do giá được quyết toán nhỏ hơn giá tạm tính.
132.**Mua TSCĐ vô hình** (Nếu thuế GTGT được khấu trừ).
133.**Mua TSCĐ vô hình** (Nếu thuế GTGT không được khấu trừ).
134.**Nhận TSCĐ vô hình từ đầu tư XDCB hoàn thành**
135.**Mua TSCĐ vô hình** (Nếu thuế GTGT không được khấu trừ).
136.**Nhận TSCĐ vô hình từ đầu tư XDCB hoàn thành**
**137.Nhận TSCĐ vô hình biếu tặng, cấp trên cấp** (hoặc nhận vốn góp bằng TSCĐ).
138.**TSCĐ vô hình nhập khẩu** (Thuế GTGT đầu vào được khấu trừ).
139.**Phát sinh chi phí trực tiếp ban đầu** liên quan đến tài sản thuê tài chính trước khi nhận tài sản thuê (ví dụ: chi phí đàm phán, ký kết hợp đồng).
140.**Khi nhận TSCĐ thuê tài chính.**
**141.Thanh toán khoản thuế GTGT đầu vào không được khấu trừ** (Nếu thuế GTGT đầu vào không được khấu trừ, và việc thanh toán được thực hiện một lần ngay tại thời điểm ghi nhận TSCĐ thuê tài chính).
142.**Lỗ do bán và thuê lại tài sản** (Trường hợp giao dịch bán và thuê lại với giá thấp hơn giá trị còn lại của TSCĐ).
143.**Khi trả lại TSCĐ thuê tài chính** theo quy định của hợp đồng thuê cho bên cho thuê.
144.**Nhận chuyển giao quyền sở hữu tài sản thuê tài chính** (mua lại sau khi thuê hết một phần giá trị)
145.**Lãi do bán và thuê lại tài sản** (Trường hợp giao dịch bán và thuê lại với giá bán cao hơn giá trị còn lại của TSCĐ)
146.**Đầu tư mua cổ phiếu hoặc góp vốn dài hạn bằng tiền**
**147.Đầu tư bằng tài sản phi tiền tệ** (vật tư, hàng hoá, TSCĐ).
148.**Mua lại phần vốn góp bằng tài sản phi tiền tệ**
**149.Nhận cổ tức, lợi nhuận được chia bằng tài sản phi tiền tệ** (ngoại trừ trường hợp nhận cổ tức bằng cổ phiếu).
150.**Ghi tăng khoản đầu tư khác** do trao đổi TSCĐ.
151.**Ghi tăng khoản đầu tư khác** do trao đổi sản phẩm, hàng hoá.
152.**Đầu tư bằng tiền mặt/tiền gửi ngân hàng** (Giao dịch chi tiền để đầu tư).
153.**Bán/Thanh lý các khoản đầu tư ngắn hạn, dài hạn** thu bằng tiền mặt/tiền gửi ngân hàng
154.**Thanh lý, nhượng bán các khoản đầu tư khác bị lỗ.**
**155.Nhận cổ tức, lợi nhuận được chia cho giai đoạn trước ngày đầu tư**
156.**Nhận được cổ tức, lợi nhuận đã dùng để đánh giá lại giá trị khoản đầu tư** khi cổ phần hoá và ghi tăng vốn Nhà nước.
157.**Bán một phần khoản đầu tư** dẫn đến không còn ảnh hưởng đáng kể (Ngầm định cho TK 228).
158.**Xuất quỹ tiền mặt chi cho hoạt động đầu tư XDCB** (Nếu thuế GTGT đầu vào được khấu trừ).
159.**Xuất quỹ tiền mặt chi cho hoạt động đầu tư XDCB** (Nếu thuế GTGT đầu vào không được khấu trừ).
160.**Mua TSCĐ, chi cho hoạt động đầu tư XDCB bằng tiền gửi ngân hàng** (Ngầm định).
161.**Mua hàng hóa, dịch vụ thanh toán bằng ngoại tệ** cho hoạt động XDCB (Nếu phát sinh lỗ tỷ giá hối đoái).
162.**Mua hàng hóa, dịch vụ thanh toán bằng ngoại tệ** cho hoạt động XDCB (Nếu phát sinh lãi tỷ giá hối đoái).
163.**Nhận khối lượng xây lắp hoàn thành bàn giao của bên nhận thầu xây lắp** (Nếu thuế GTGT đầu vào được khấu trừ).
164.**Nhận khối lượng xây lắp hoàn thành bàn giao của bên nhận thầu xây lắp** (Nếu thuế GTGT đầu vào không được khấu trừ).
165,**Chi phí khác cho hoạt động đầu tư XDCB** (như vật tư, nhân công trực tiếp, chi phí chung, v.v.).
166.**Chi phí sửa chữa lớn TSCĐ** (Nếu đủ điều kiện vốn hóa và ghi tăng nguyên giá TSCĐ).
167.**Quyết toán bàn giao công trình XDCB hoàn thành** và đưa vào sử dụng là TSCĐ hữu hình.
168.**Quyết toán bàn giao công trình XDCB hoàn thành** và đưa vào sử dụng là TSCĐ vô hình.
169.**Điều chỉnh tăng giá trị công trình** (Chủ đầu tư) do giá được quyết toán lớn hơn giá tạm tính.
170.**Xử lý giá trị công trình bị hủy bỏ**
**171.Điều chỉnh giảm giá trị công trình** (Chủ đầu tư) do giá được quyết toán nhỏ hơn giá tạm tính.
172.**Mua vật tư, hàng hóa, TSCĐ nhập kho/đưa vào sử dụng** (Nếu thuế GTGT được khấu trừ).
173.**Mua vật tư, hàng hóa, TSCĐ nhập kho/đưa vào sử dụng** (Nếu thuế GTGT không được khấu trừ).
174.**Nhận khối lượng XDCB hoàn thành bàn giao** (Nếu thuế GTGT được khấu trừ).
175.**Nhận khối lượng XDCB hoàn thành bàn giao** (Nếu thuế GTGT không được khấu trừ).
176.**Mua vật tư, hàng hóa nhập khẩu** (Ghi nhận giá trị hàng hóa)
177.**Nhận dịch vụ cung cấp** (vận chuyển, điện, nước, quảng cáo, v.v.) chưa trả tiền (Nếu thuế GTGT được khấu trừ).
178.**Nhận dịch vụ cung cấp** chưa trả tiền (Nếu thuế GTGT không được khấu trừ).
179.**Xác định giá trị khối lượng xây lắp phải trả cho nhà thầu phụ** (đối với nhà thầu chính)
180.**Nợ phải trả người bán bằng ngoại tệ** (Lãi tỷ giá).
181.**Ứng trước tiền hoặc thanh toán số tiền phải trả cho người bán** bằng tiền mặt hoặc tiền gửi ngân hàng.
182.**Thanh toán nợ phải trả bằng ngoại tệ** (Lỗ tỷ giá).
183.**Trả trước tiền bằng ngoại tệ cho người bán.**
**184.Trả trước tiền bằng ngoại tệ cho người bán** (Lãi tỷ giá).
185.**Nhận lại tiền do người bán hoàn lại số tiền đã ứng trước** (vì không cung cấp được hàng hóa/dịch vụ).
186.**Nhận lại tiền do người bán hoàn lại số tiền đã ứng trước** (vì không cung cấp được hàng hóa/dịch vụ)
187.**Trả lại vật tư, hàng hoá** hoặc được người bán chấp thuận giảm giá do không đúng quy cách/phẩm chất.
188.**Được hưởng chiết khấu thanh toán** khi thanh toán nợ sớm.
189.**Xử lý nợ phải trả không tìm ra chủ nợ** hoặc chủ nợ không đòi.
190.**Đánh giá lại số dư ngoại tệ giảm giá** (Lỗ tỷ giá tại BCTC).
191.**Bán sản phẩm, hàng hóa, dịch vụ** (Thuế GTGT/TTĐB/XK/BVMT phải nộp).
192.**Nhận trợ cấp, trợ giá bằng tiền mặt từ NSNN.**
**193.Nhập khẩu vật tư, hàng hoá, TSCĐ** (Ghi nhận thuế nhập khẩu, TTĐB, BVMT phải nộp).
194.**Xác định số thuế GTGT đầu ra**
195.**Nộp các loại thuế, phí, lệ phí** (GTGT, TNDN, TTĐB, XK, v.v.) vào NSNN.
196.**Khấu trừ thuế GTGT đầu vào** (Cuối tháng).
197.**Điều chỉnh giảm số thuế phải nộp** do sai sót hoặc ưu đãi.
198.**Hoàn thuế** (Ngầm định cho thuế GTGT).
199.**Hoàn nhập thuế GTGT đầu vào** (Khi hàng trả lại).
(Source : Notebook LM)

**3/Double entry logic: **
w + z = x + y (Debit/Credit) -> 2 ways transactions
-> w//x+y//z=w+y//x+z (debit - debit)||(credit-credit)
cross sum : w+z=x+y (cross check : debit + credit = 0), cannot be negative
zero term : w//0+0//y=w//y=0//0
debit-credit balance : w+...+x=y+...+z
-> w//0+....+x//0+0//y + ....+0//z: zero-term

4/ Logic of opening accounts: 
PPE_End = PPE_Start + Additions + Acquisitions + FX + Revaluation - Depreciation - Impairment + Reversals - Disposal
Goodwill_End = Goodwill_Start + Recognition + FX + Transfers - Impairment - Disposal - Amortisation
Provisions_End = Provisions_Start + Additions - Used - Reversed + FX + Transfers
Shares_End = Shares_Start + ΔShares

Inventory :
I/ FIFO (First In, First Out):
COGS=Earliest purchase cost×Units soldCOGS=Earliest purchase cost×Units sold
Ending Inventory=Beginning+Purchases−Sales(valued at recent purchases)
Ending Inventory=Beginning+Purchases−Sales(valued at recent purchases)

II/ LIFO (Last In, First Out):
COGS=Most recent purchase cost×Units sold
Ending Inventory=Beginning+Purchases−Sales (valued at oldest purchases)

- AVC (Average Cost / Weighted Average):**
Weighted Price=(Prev Inv×Prev Price)+(Purchase×Purchase Price)
Total Units
Weighted Price=Total Units(Prev Inv×Prev Price)+(Purchase×Purchase Price)​COGS=Weighted Price×Units SoldCOGS=Weighted Price×Units Sold

III/ **Depreciation / Amortization:**
Monthly Depreciation=Cost/Useful Life (months)
If  allocated from start month:
Expense = Cost×Depreciation30×(Days used)
Expense month​= Depreciation​×(Days used) (n-t+1)
Net Book Value =Cost−AccDepNBV=Cost−AccDep
Depreciation (t) =NBV(t−1)×Rate of Depreciationt​=NBV(t−1​)×Rate
Deferred Tax
Total = sum (DeferredTaxAssets, DeferredTaxLiabilities)
and continue
OCI/FVOCI (Comprehensive income) = IS
Comprehensive Income = Revenues - Expenses + Gains - Losses
EquityT1 = EquityT0 + ProfitLoss + OCI + IssueOfEquity - DividendsPaid + Contributions - Distributions + Transfers + TreasuryShares + SubsidiaryChanges + ShareBasedPayments


