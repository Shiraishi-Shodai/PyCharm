import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urljoin
from pathlib import Path
import time


# 詳細画面から、最終目的である画像URLを取得する関数
# 引数
# url … 詳細画面のURL
# 戻り値
# 画像URL
def getImageUrl(url):
    # Webページを取得して解析する
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")


    entry = soup.find(class_="entry")
    # print(entry)

    img = entry.find("img")
    # print(img)

    src = img.get("src")
    # print(src)

    # URLにHTTPSがない場合は追加する
    if not "https:" in src:
        src = "https:" + src

    return src


# 入力された画像URLをローカルにダウンロードする
# 引数
# url 画像URL
# dir 保存先URL
# 戻り値 なし
# 画像ファイル名はWebのものを採用するバージョン
def downloadImage(url, dir):
    print("imaeg >> " + url)
    filename = url.split("/")[-1]
    fullpath = dir.joinpath(filename)


    imgdata = requests.get(url)
    with open(fullpath, mode="wb") as f:
        f.write(imgdata.content)

# 検索結果画面を読み込んで、詳細画面URLのリストを作成する
# targetUrl (入力) 検索結果画面のURL
# urls (出力) 詳細画面URLのリスト（またはセット）
def readResultHtml(targetUrl, urls):

    html = requests.get(targetUrl)
    soup = BeautifulSoup(html.content, "html.parser")

    result = soup.find(class_="widget Blog")

    # すべてのaタグを検索して、リンクを表示する
    for element in result.find_all("a"):
        # urljoinでtargetUrlとelement.get("her")のurlを組み合わせる
        url = urljoin(targetUrl, element.get("href"))

    # 正規表現を使えばもっとシンプルに書ける
    if "/blog-post_" in url:
        # if "/blog-post_" in url and not "#comment" in url:

        urls.append(url)  # リストを使う場合の追加
        # urls.add(url)	# 重複を除外する セットを使う場合

    else:
        pass
        # print("NG-URL >> " + url)

# ここから本題

# Webページを取得して解析する
resultUrl = "https://www.irasutoya.com/search?q=%E3%82%AB%E3%83%AC%E3%83%BC&updated-max=2019-10-31T13:00:00%2B09:00&max-results=20&start=0&by-date=false"

urls = []  # リスト
# urls = set() # セット

# 詳細画面一覧のURLリストが作成されます
readResultHtml(resultUrl, urls)

# ダウンロード先ディレクトリの作成
dldir = Path(f"download")
dldir.mkdir(exist_ok=True)

for url in urls:
    imageUrl = getImageUrl(url)
    print(url + "   image>> " + imageUrl)
    downloadImage(imageUrl, dldir)
    time.sleep(1)