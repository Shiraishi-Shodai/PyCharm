import requests
from pathlib import Path
from bs4 import  BeautifulSoup as bs4

def  getImageUrl(load_url):
    # HTMLの型はrequests.models.Response
    html = requests.get(load_url)
    soup = bs4(html.content, "html.parser")
    content = soup.find(class_="separator")
    return content.find("img").get("src")

def downloadImage(imageURL):

    out_folder = Path("download2")
    out_folder.mkdir(exist_ok=True)
    imageData = requests.get(imageURL)

    filename = imageURL.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    with open(out_path, mode="wb") as f:
        f.write(imageData.content)
        print("ダウンロードが完了しました")

load_url = "https://www.irasutoya.com/2020/09/blog-post_386.html?m=1"
imageURL = getImageUrl(load_url)
downloadImage(imageURL)