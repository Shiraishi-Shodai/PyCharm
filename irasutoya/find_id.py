import requests
from bs4 import BeautifulSoup

load_url = "https://www.irasutoya.com"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# IDで検索し、その中のすべてのliタグを検索して表示する
lbl1 = soup.find(id="Label1")
for element in lbl1.find_all("li"):
    print(element.text)
