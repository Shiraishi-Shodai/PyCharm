import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# ターゲットのウェブサイトのURL
base_url = 'https://www.irasutoya.com'
search_url = base_url + '/search/label/%E5%A4%8F'

# リンクを保存するリスト
links = []

# ウェブページを取得
response = requests.get(search_url)
soup = BeautifulSoup(response.content, 'html.parser')

# 特定のクラス名を持つ要素を取得
boxim_elements = soup.find_all(class_='boxim')

# 各要素からリンクを取得
for boxim_element in boxim_elements:
    a_tags = boxim_element.find('a', href=True)
    for a_tag in a_tags:
        link_url = a_tag['href']
        if link_url:
            link_url = urljoin(base_url, link_url)
            links.append(link_url)

# 画像を保存するディレクトリ
download_dir = 'downloaded_images'
os.makedirs(download_dir, exist_ok=True)

# リンクから画像を取得してダウンロード
num_images_to_download = int(input("ダウンロードする画像の数を入力してください: "))  # ダウンロードする画像の数
downloaded_count = 0  # ダウンロードした画像のカウント

# リンクから画像を取得してダウンロード
for link in links:
    if downloaded_count >= num_images_to_download:
        break

    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 特定のクラス名を持つ要素を取得
    entry_elements = soup.find_all(class_='entry')

    # 各要素から画像を取得してダウンロード
    for entry_element in entry_elements:
        img_tags = entry_element.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(base_url, img_url)
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    img_name = img_url.split('/')[-1]
                    img_path = os.path.join(download_dir, img_name)
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f"Downloaded: {img_name}")
                    downloaded_count += 1