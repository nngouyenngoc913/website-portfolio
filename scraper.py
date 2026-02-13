import requests
from bs4 import BeautifulSoup
import datetime
import os

def scrape_to_xml():
    # Lấy từ khóa từ Action Input
    query = os.getenv('KEYWORD', 'Accountant Junior Part-time')
    
    # Truy vấn Boolean qua DuckDuckGo Lite (site:careerjet.vn để lọc nguồn)
    search_query = f"{query} site:careerjet.vn"
    url = f"https://html.duckduckgo.com/html/?q={search_query.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='result')

        xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n<job_results>\n'
        xml_output += f'    <last_updated>{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</last_updated>\n'
        
        if not results:
            xml_output += "    <status>No results found</status>\n"
        else:
            xml_output += "    <status>Success</status>\n"
            for i, res in enumerate(results[:15]):
                # Trích xuất Tiêu đề và Link
                title_tag = res.find('a', class_='result__a')
                if not title_tag: continue
                
                title = title_tag.get_text().strip().replace('&', '&amp;')
                link = title_tag['href']
                
                # Trích xuất Snippet (chứa thông tin công ty/địa điểm trên Careerjet)
                snippet_tag = res.find('a', class_='result__snippet')
                snippet = snippet_tag.get_text().strip() if snippet_tag else ""
                
                # Giả lập phân tách Company/Location từ snippet của Careerjet
                # Thông thường snippet Careerjet có dạng: "Tên Công Ty - Địa Điểm - Mô tả..."
                parts = snippet.split(' - ')
                company = parts[0].replace('&', '&amp;') if len(parts) > 0 else "N/A"
                location = parts[1].replace('&', '&amp;') if len(parts) > 1 else "N/A"

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
    scrape_to_xml()
