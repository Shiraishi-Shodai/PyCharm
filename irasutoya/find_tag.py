import requests
from bs4 import  BeautifulSoup as bs4

load_url = "https://www.amazon.co.jp"
html = requests.get(load_url)
# html.text を渡してももちろん動作するのですが、 res.content を渡した方が「文字化け」する可能性を減らせますのでこちらで書く癖をつけましょう。
# ’lxml’というのはCで書かれたパース方式。標準の”html.parser”よりも早いです
soup = bs4(html.content, "html.parser")

# titile,h2,liタグを検索して表示
print(soup.find("title").text)
print(soup.find("h2").text)
print(soup.find("li").text)
