import requests
from bs4 import BeautifulSoup

# 伪装为浏览器，不伪装，会被识别为爬虫，返回418
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
}

for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers = headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)

# print(response)
# print(response.status_code)


