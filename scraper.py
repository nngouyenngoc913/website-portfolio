import requests
from bs4 import BeautifulSoup
import datetime

def scrape_jobs():
    # Truy vấn trực tiếp đến trang tìm kiếm của Joblum
      search_url = "https://vn.joblum.com/jobs?q=operations+coordinator+staff"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Joblum thường để thông tin trong các thẻ div có class 'item-details' hoặc 'job-item'
        job_items = soup.find_all('div', class_='item-details')
        
        xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<job_results>\n'
        xml_output += f'    <last_updated>{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</last_updated>\n'

        if not job_items:
            xml_output += "    <status>No jobs found on Joblum. Class might have changed.</status>\n"
        else:
            xml_output += "    <status>Success</status>\n"
            for i, item in enumerate(job_items[:10]): # Lấy 10 tin tuyển dụng mới nhất
                # Tìm tiêu đề và link
                title_tag = item.find('h3').find('a')
                title = title_tag.text.strip()
                link = "https://vn.joblum.com" + title_tag['href']
                
                # Tìm công ty (nếu có)
                company_tag = item.find('span', class_='company-name')
                company = company_tag.text.strip() if company_tag else "N/A"
                
                xml_output += f'    <job id="{i+1}">\n'
                xml_output += f'        <title>{title}</title>\n'
                xml_output += f'        <company>{company}</company>\n'
                xml_output += f'        <link>{link}</link>\n'
                xml_output += f'    </job>\n'
        
        xml_output += '</job_results>'

        with open("data.xml", "w", encoding="utf-8") as f:
            f.write(xml_output)
        print("Scraping successful!")

    except Exception as e:
        print(f"Error: {e}")
        # Ghi lỗi vào XML để Dashboard hiển thị được
        with open("data.xml", "w", encoding="utf-8") as f:
            f.write(f'<?xml version="1.0"?><job_results><status>Error: {str(e)}</status></job_results>')

if __name__ == "__main__":
    scrape_jobs()
