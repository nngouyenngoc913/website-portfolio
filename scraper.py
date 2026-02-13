import requests
from bs4 import BeautifulSoup
import datetime

def scrape_jobs():
    # Câu lệnh Boolean Search của bạn
    query = 'site:vn.joblum.com "hiring" "operations" ("coordinator" OR "staff") "full-time" -freelance'
    
    # URL tìm kiếm (Sử dụng Google để quét index của Joblum)
    search_url = f"https://www.google.com/search?q={query}"
    
    # Header để giả lập trình duyệt người dùng thật, tránh bị chặn
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Tìm các kết quả tìm kiếm (Google thường dùng các thẻ div có class 'g')
        search_results = soup.find_all('div', class_='g')
        
        # Khởi tạo nội dung XML
        xml_output = f'<?xml version="1.0" encoding="UTF-8"?>\n<job_results>\n'
        xml_output += f'    <last_updated>{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</last_updated>\n'

        if not search_results:
            xml_output += "    <status>No results found or IP blocked by Google</status>\n"
        else:
            for i, result in enumerate(search_results[:5]): # Lấy 5 kết quả đầu tiên
                title_tag = result.find('h3')
                link_tag = result.find('a')
                
                title = title_tag.text if title_tag else "No Title"
                link = link_tag['href'] if link_tag else "#"
                
                xml_output += f'    <job id="{i+1}">\n'
                xml_output += f'        <title>{title}</title>\n'
                xml_output += f'        <link>{link}</link>\n'
                xml_output += f'    </job>\n'
        
        xml_output += '</job_results>'

        # Ghi ra file data.xml
        with open("data.xml", "w", encoding="utf-8") as f:
            f.write(xml_output)
        print("Scraping thành công! Đã cập nhật data.xml")

    except Exception as e:
        print(f"Lỗi khi scraping: {e}")

if __name__ == "__main__":
    scrape_jobs()
