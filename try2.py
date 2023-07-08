import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://18av.mm-cg.com/zh/chinese_list/all/{}.html"
total_pages = 5

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37"
}

all_data = []  # 存储链接和日期的对应数据

for page in range(1, total_pages + 1):
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    all_titles = soup.select("h3[itemprop='name headline'] a")
    all_links = [title.string for title in all_titles]
    
    all_dates = soup.select("div.meta")
    all_dates = [date.text.strip() for date in all_dates]
    
    # 将链接和日期的对应数据合并
    combined_data = list(zip(all_links, all_dates))
    all_data.extend(combined_data)
    
    time.sleep(1)  # 添加1秒的延迟

# 写入CSV文件
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link', 'Date'])  # 写入表头
    writer.writerows(all_data)  # 写入数据
    
