import requests
import time

url = "https://www.irasutoya.com"
time.sleep(1)
response = requests.get(url)

# 文字化け対策
# response.apparent_encodingは呼び出す度に文字コード推定モジュールchardetを用いて、HTMLのバイト列から文字コードを推定している
response.encoding = response.apparent_encoding

print(response.text)

