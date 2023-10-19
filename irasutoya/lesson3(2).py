import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
from tqdm import tqdm

# 検索結果画面のurlと空のsetを引数に入れ、詳細画面のurlが入ったsetを返す関数
def readResultHtml(targetUrl,urls):
    # レスポンスオブジェクトの作成
    html = requests.get(targetUrl)
    # BSオブジェクトの作成
    soup = BeautifulSoup(html.content, "html.parser")
    wb = soup.find(class_="widget Blog")
    for a in wb.find_all("a"):
        wb_a_href = a.get("href")
        if "/blog-post_" in wb_a_href:
            urls.add(wb_a_href)

# 詳細画面のURLを受け取って、画像のURLを返す
def getImageUrl(input_url):
    # レスポンスオブジェクトの作成(変更の必要性なし)
    html = requests.get(input_url)
    # BSオブジェクトの作成(レスポンスオブジェクトとパーサの指定)(取得したいモノの型によっては.contentの部分を変更)
    soup = BeautifulSoup(html.content, "html.parser")

    # 目的の場所の範囲指定(取得したいものによって任意に変更)
    entry = soup.find(class_="entry")
    entry_img = entry.find("img")
    entry_img_src = entry_img.get("src")

    # 特定したURLをreturnする(変更の必要性なし)
    return entry_img_src

# 画像のURLから、その画像をダウンロードする関数
def downloadImage(url):

    # 保存用フォルダの作成(保存先の変更をしたい場合に任意に変更)
    out_folder = Path("download11")
    out_folder.mkdir(exist_ok=True)

    # 保存用ファイル名の作成(変更の必要性なし)
    # スプリットしたurlのデータの右端を取る
    filename = url.split("/")[-1]
    # それを保存先のフォルダにくっつけてパスの名前にする
    out_path = out_folder.joinpath(filename)

    # https:でスタートしていなかったらhttps:を付ける
    if not url.startswith("https:"):
        url = 'https:' + url

    # 目的の画像のURLからレスポンスオブジェクトを作成(変更の必要性なし)
    target_url_resobj = requests.get(url)

    # 画像の保存(変更の必要性なし)
    f = open(out_path, mode="wb")
    f.write(target_url_resobj.content)
    f.close()

# ターゲットとなるURL
input_url = 'https://www.irasutoya.com/search?q=%E7%84%BC%E3%81%8D%E8%82%89'
# リンク入れる場所
set1 = set()
#　全ての詳細画面のURLを全てとってくる
readResultHtml(input_url,set1)
# 全ての詳細画面について、画像のURLを取って、画像の取得をする
with tqdm(total=len(set1)) as pbar:
    while set1:
        detail_url = set1.pop()
        img_url = getImageUrl(detail_url)
        downloadImage(img_url)
        time.sleep(1)
        pbar.update(1)