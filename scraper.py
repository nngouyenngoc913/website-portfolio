import requests
from bs4 import BeautifulSoup
import datetime

def scrape_jobs():
    # Cấu hình tìm kiếm: Role + Seniority + Contract Type
    # Ví dụ: Operations + Senior + Full-time
    query = "operations senior full-time"
    search_url = f"https://www.careerjet.vn/tim-viec-lam?q={query.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Careerjet thường dùng class 'job' hoặc cấu trúc thẻ article cho mỗi tin tuyển dụng
        jobs = soup.find_all('article', class_='job')
        
        xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<job_results>\n'
        xml_output += f'    <last_updated>{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</last_updated>\n'
        xml_output += f'    <source>Careerjet</source>\n'

        if not jobs:
            xml_output += "    <status>No jobs found on Careerjet</status>\n"
        else:
            xml_output += "    <status>Success</status>\n"
            for i, job in enumerate(jobs[:10]):
                # Trích xuất tiêu đề và link
                title_tag = job.find('header').find('h2').find('a')
                title = title_tag.text.strip()
                link = "https://www.careerjet.vn" + title_tag['href']
                
                # Trích xuất công ty
                company_tag = job.find('p', class_='company')
                company = company_tag.text.strip() if company_tag else "N/A"
                
                # Trích xuất mô tả ngắn hoặc địa điểm
                location_tag = job.find('ul', class_='location')
                location = location_tag.text.strip() if location_tag else "N/A"
                
                xml_output += f'    <job id="{i+1}">\n'
                xml_output += f'        <title>{title}</title>\n'
                xml_output += f'        <company>{company}</company>\n'
                xml_output += f'        <location>{location}</location>\n'
                xml_output += f'        <link>{link}</link>\n'
                xml_output += f'    </job>\n'
        
        xml_output += '</job_results>'

        with open("data.xml", "w", encoding="utf-8") as f:
            f.write(xml_output)
        print("Scraping Careerjet thành công!")

    except Exception as e:
        with open("data.xml", "w", encoding="utf-8") as f:
            f.write(f'<?xml version="1.0"?><job_results><status>Error: {str(e)}</status></job_results>')

if __name__ == "__main__":
    scrape_jobs()
