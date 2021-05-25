import requests
import re
import json
from bs4 import BeautifulSoup

TARGET_URL = 'https://www.bosch-home.com.tr/urun-listesi/buzdolaplari-derin-dondurucular/buzdolaplari/alttan-donduruculu-buzdolaplari'

# HEADER is not spesific any HEADER file can work
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

result_data = list()

r = requests.get(url=TARGET_URL, headers=HEADER)
soup = BeautifulSoup(r.content, 'html.parser')
product_data = soup.find_all('script', {'data-init-data':'ajax-productlist'})

cleanr = re.compile('<.*?>')
cleantext = re.sub(cleanr, '', str(product_data[0]))

parsed = json.loads(cleantext.strip())

for item in parsed['response']['items']:
    score = item.get('review').get('rating')
    headers = item.get('headers')
    product_name = ' '.join(headers[:-1])
    # for clean output
    code = headers[-1]      
    print(f"Product Name :{product_name}, Code: {code}, Score: {score}")
    result_data.append({"name": product_name, "code": code, "score": score})


max_page_number = int(parsed['response']['maxPageNumber'])

for i in range(2, max_page_number+1):
    next_page_url = f"{TARGET_URL}?pageNumber={i}"
    r = requests.get(url=next_page_url, headers=HEADER)
    soup = BeautifulSoup(r.content, 'html.parser')
    product_data = soup.find_all('script', {'data-init-data':'ajax-productlist'})

    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(product_data[0]))

    parsed = json.loads(cleantext.strip())
    for item in parsed['response']['items']:
        score = item.get('review').get('rating')
        headers = item.get('headers')
        product_name = ' '.join(headers[:-1])
        code = headers[-1]
        print(f"Product Name :{product_name}, Code: {code}, Score: {score}")
        result_data.append({"name": product_name, "code": code, "score": score})


with open("outputfile.json", "w", encoding='utf-8') as jsonfile:
    json.dump(result_data, jsonfile, ensure_ascii=False, indent=4)
