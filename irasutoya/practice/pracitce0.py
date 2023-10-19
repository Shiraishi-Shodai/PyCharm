import requests
from bs4 import BeautifulSoup
from pathlib import  Path

url = "https://www.irasutoya.com"
html = requests.get(url)

soup = BeautifulSoup(html.content, "html.parser")

chap2 = soup.find(id="Label1")
# for element in chap2.find_all("li"):
#     print(element.text)

# 保存先フォルダを作る
out_folder = Path("download3")
out_folder.mkdir(exist_ok=True)


# タイトル画像の取得


