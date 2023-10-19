from pathlib import Path
from urllib.parse import urljoin

from bs4 import  BeautifulSoup as bs4
import requests

url = "https://www.irasutoya.com/search?q=%E5%9C%B0%E7%90%83"

result = set()

def  readResultHtml(url, result):

    html = requests.get(url)
    soup = bs4(html.content, "html.parser")
    content = soup.find(class_="widget Blog")

    # すべてのaタグを検索して、リンクを表示する
    for element in content.find_all("a"):
        url = element.get("href")
        # 正規表現を使えばもっとシンプルに書ける
        if "/blog-post_" in url:
            # if "/blog-post_" in url and not "#comment" in url:

            result.add(url)  # リストを使う場合の追加
            # urls.add(url) # 重複を除外する セットを使う場合

        else:
            pass
            # print("NG-URL >> " + url)
    return result

def  getImageUrl(load_url):
    # HTMLの型はrequests.models.Response
    html = requests.get(load_url)
    soup = bs4(html.content, "html.parser")
    content = soup.find(class_="entry")

    return content.find("img").get("src")

def downloadImage(imageURL):

    out_folder = Path("download2")
    out_folder.mkdir(exist_ok=True)
    imageData = requests.get(imageURL)

    filename = imageURL.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    with open(out_path, mode="wb") as f:
        f.write(imageData.content)

readResultHtml(url, result)

for i in result:

    img_src = getImageUrl(i)

    if "https:" not in img_src :
        img_src = "https:" + img_src

    print(img_src)
    downloadImage(img_src)

print("ダウンロードが完了しました")


