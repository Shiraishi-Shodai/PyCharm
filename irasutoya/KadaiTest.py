#PyAudioとspeechrecognitionをインストール
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as tk
import countTime as ct


# 引数にしていされたキーワードをいらすとやで検索し、検索語のurlを返す
def search(keyword) :

    #クロームの立ち上げ
    driver=webdriver.Chrome()

    #ページ接続
    driver.get('https://www.irasutoya.com/')

    # 入力欄を取得
    input = driver.find_element(By.NAME, "q")
    input.send_keys(keyword)

    # 検索ボタンの取得
    searchButton = driver.find_element(By.ID, "searchBtn")
    searchButton.click()
    # 今いるページのurlを取得する
    searchUrl = driver.current_url

    #10秒終了を待つ
    time.sleep(1)

    #クロームの終了処理
    driver.close()

    #検索した先のurlを返す
    return searchUrl

def speechText():
    recognizer = sr.Recognizer()

    # countTimeファイルのTimerクラスをインスタンス化
    timer = ct.Timer()
    timer.main()

    # マイクから音声を連続録音
    with sr.Microphone() as source:

        audio_data = recognizer.listen(source, phrase_time_limit=5) #5秒で録音を停止する

    try:
        # 音声をテキストに変換
        text = recognizer.recognize_google(audio_data, language="ja-JP")#テキスト内容
        sv.set("テキスト化結果: " + text)

        print(search(text))

    except sr.UnknownValueError:
        sv.set("音声を理解できませんでした。")
    except sr.RequestError as e:
        sv.set("音声認識サービスにアクセスできませんでした。")

root = tk.Tk()
root.geometry('500x500')
root.title("GUI")

# 動的に文字列を扱えるようにする
sv = tk.StringVar()
sv.set("音声を録音してください...（5秒以内）")

# ボタンをクリックした時に、speechTextを実行
btn = tk.Button(textvariable=sv,width=25, height=5, bg="#FF6600")
btn.bind('<1>', speechText())
btn.place(x=200,y=230)

tk.mainloop()