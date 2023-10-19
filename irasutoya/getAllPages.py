import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import urljoin
from pathlib import Path
import time
from tqdm import tqdm

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
        url = urljoin(targetUrl, element.get("href"))

        # 正規表現を使えばもっとシンプルに書ける
        if "/blog-post_" in url:
            # if "/blog-post_" in url and not "#comment" in url:

            urls.add(url)  # リストを使う場合の追加
            # urls.add(url)	# 重複を除外する セットを使う場合

        else:
            pass
            # print("NG-URL >> " + url)

# 次のページが存在するか判断する関数
def hasNextButton(url):

    # 判断用変数
    flag = "True"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    result = soup.find(id="blog-pager-older-link")

    if result is None :
        flag = False

    return flag



# ここから本題

keyword = urllib.parse.quote("地球")
step = 20
start = step * 0

# Webページを取得して解析する
resultUrl = f"https://www.irasutoya.com/search?q={keyword}&max-results={step}&start={start}&by-date=false"

# urls = [] # リスト
urls = set() # セット

# 詳細画面一覧のURLリストが作成されます
#readResultHtml(resultUrl,urls)

# ダウンロード先ディレクトリの作成
dldir = Path(f"download")
dldir.mkdir(exist_ok=True)

# カウント変数i
i = 0

isNext = True

while isNext:

    # Webページを取得して解析する
    # by-date=falseは投稿日順に検索結果をな並べ変えないという意味
    resultUrl = f"https://www.irasutoya.com/search?q={keyword}&max-results={step}&start={step * i}&by-date=false"
    print(resultUrl)
    readResultHtml(resultUrl,urls)

    i = i + 1
    isNext = hasNextButton(resultUrl)

for url in urls:
    imageUrl = getImageUrl(url)
    print (url + "   image>> " + imageUrl)
    downloadImage(imageUrl,dldir)
    time.sleep(0.1)