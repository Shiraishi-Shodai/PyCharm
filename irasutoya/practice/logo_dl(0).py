import requests
from bs4 import BeautifulSoup
from pathlib import Path

url = "https://www.irasutoya.com"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

#   画像のurlを取得
image_url = soup.find(id="homedesign").find("img").get("src")

def download_image(url):
    #フォルダを作る
    path = Path("download3")
    path.mkdir(exist_ok=True)

#     ファイル名の作成
    filename = image_url.split("/")[-1]
    path = path.joinpath(filename)

#     ダウンロード
    with open(path, mode="wb") as f:
        image_data = requests.get(url)
        f.write(image_data.content)
        print("ダウンロードが完了しました")

download_image(image_url)