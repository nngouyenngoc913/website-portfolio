## Cách xây dựng quy trình tự động hoá vào trong workflow 
# Như thế nào gọi là tự động hoá ? Ý chỉ việc sử dụng các công cụ giúp hỗ trợ việc nhập/xuất dữ liệu nhanh chóng, 
ứng dụng các ứng dụng để khiến cho công việc được "tự động" 
# Vì sao tự động hoá lại được ưa chuộng ? 
- Gia tăng hiệu suất chính là tiết kiệm thời gian, tạo ra nhiều sản phẩm mà thời gian bỏ ra ngắn hơn
- Tự động hoá được coi là trend, nghĩa là ai cũng biết, ai cũng muốn tham gia, ai cũng muốn là người nắm bắt để
gia tăng năng lực cạnh tranh
- Vì tự động hoá là cách để kiểm soát lỗi sai

# Một số ứng dụng phổ biến và các case study 
1. N8N và double entry : giúp hỗ trợ xác định nhanh tài khoản, giúp hỗ trợ việc chiết xuất văn bản nghị định -> hỗ trợ
, cải thiện độ chính xác, hạn chế cảm tính, và nâng cao năng lực nghiệp vụ .
Chi tiết cách làm : https://trangtaichinhketoan.substack.com/publish/recipients/192158397
Goal : mục tiêu chính là giúp việc định khoản không còn là "hạn chế" phải nhớ tên định khoản, học vẹt, hoặc đơn giản hơn
là phải đọc cụm từ khoá

2.N8N ứng dụng trong việc xây dựng database , thư viện mở
Vì N8N khi thực hiện workflow phải lưu giữ 1 lượng lớn thông tin để có thể prompting chính xác, vì thế việc xây dựng 
những thông tin đó thành 1 KB (knowledge base) có thể giúp chúng ta tiết kiệm thời gian để phải lật lại tài liệu ghi nhớ
Chi tiết cách làm : Khi xây dựng một workflow về xử lí định khoản, chúng ta bắt buộc phải cho N8N nhận diện loại tk, loại
giao dịch, cách làm. Đây có thể được coi là một manual (hướng dẫn chi tiết) cách thức làm để một người "dù không biết gì"
cũng có thể tự làm 

3.N8N là thư kí cá nhân, hỗ trợ các công việc lặt vặt như tạo báo cáo thu - chi, viết email, ghi chép trên sheets, ....
N8N có chức năng kết nối Drive, Sheets, và hệ sinh thái Google nên chúng ta có thể nhờ N8N hỗ trợ truy cập vào, và sử dụng
các prompting để có thể "manipulate"

4. N8N có thể hỗ trợ công việc của 1 CS : nhờ việc liên kết với Facebook, thu thập thông tin các câu hỏi vào 1 bảng dữ liệu
, dựa vào đó để soạn các câu trả lời mẫu hoặc là trực tiếp nhắn tin sau khi đã nắm được yêu cầu 

# Cách tiếp cận ? 
- Tài khoản N8N có phí hosting khoảng 2-3 tr/năm.
- Tập xây dựng các workflow cơ bản như chatbot, liên kết telegram để nhắn tin,..... đến phức tạp hơn
- Ngoài ra, bạn có thể tự do "sáng tạo" ra các flow để hỗ trợ công việc (tuỳ vào nhu cầu)

 # Lời kết
 N8N chỉ là một trong các công cụ automate ngoài ra make, zipper, ... đã tích hợp AI cũng là lựa chọn để thử trải nghiệm
 Việc "ứng dụng" các giải pháp "automate" sẽ trở nên phổ biến hơn, vì thế nếu tận dụng và học cách sử dụng pro thì có thể
 giúp công việc trở nên mượt mà. 

 Sources : 
 https://substack.com/@nguynnguynngc
