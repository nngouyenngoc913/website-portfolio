import requests
from bs4 import BeautifulSoup
import datetime
import os

def scrape_careerjet():
    # Lấy từ khóa từ ô nhập của GitHub Actions
    query = os.getenv('KEYWORD', 'Tuyển dụng mới nhất')
    search_url = f"https://www.careerjet.vn/tim-viec-lam?q={query.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Careerjet lưu tin tuyển dụng trong thẻ <article class="job">
        jobs = soup.find_all('article', class_='job')
        
        xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<job_results>\n'
        xml_output += f'    <keyword_used>{query}</keyword_used>\n'
        xml_output += f'    <last_updated>{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</last_updated>\n'

        if not jobs:
            xml_output += "    <status>No results found on Careerjet</status>\n"
        else:
            xml_output += "    <status>Success</status>\n"
            for i, job in enumerate(jobs[:15]): # Lấy tối đa 15 kết quả
                title_tag = job.find('h2').find('a') if job.find('h2') else None
                if title_tag:
                    title = title_tag.text.strip()
                    link = "https://www.careerjet.vn" + title_tag['href']
                    company = job.find('p', class_='company').text.strip() if job.find('p', class_='company') else "N/A"
                    location = job.find('ul', class_='location').text.strip() if job.find('ul', class_='location') else "N/A"
                    
                    xml_output += f'    <job id="{i+1}">\n'
                    xml_output += f'        <title>{title}</title>\n'
                    xml_output += f'        <company>{company}</company>\n'
                    xml_output += f'        <location>{location}</location>\n'
                    xml_output += f'        <link>{link}</link>\n'
                    xml_output += f'    </job>\n'
        
        xml_output += '</job_results>'

        with open("data.xml", "w", encoding="utf-8") as f:
            f.write(xml_output)

    except Exception as e:
        with open("data.xml", "w", encoding="utf-8") as f:
            f.write(f'<?xml version="1.0"?><job_results><status>Error: {str(e)}</status></job_results>')

if __name__ == "__main__":
    scrape_careerjet()
