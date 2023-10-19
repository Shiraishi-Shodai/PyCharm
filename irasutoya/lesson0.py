import requests
from bs4 import  BeautifulSoup as bs4
from  pathlib import  Path
import urllib
import  time

load_url = "https://www.irasutoya.com/2021/01/onepiece.html"

html = requests.get(load_url)
soup = bs4(html.content, "html.parser")

out_folder = Path("download2")
out_folder.mkdir(exist_ok=True)

entry = soup.find(class_="entry")

for element in entry.find_all("img"):

    src = element.get("src")

    # srcを相対パスから絶対パスに変換
    image_url = urllib.parse.urljoin(load_url, src)
    imagedata = requests.get(image_url)

    filename = image_url.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    with open(out_path, mode="wb") as f:
        f.write(imagedata.content)

    time.sleep(1)

