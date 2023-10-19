# GUI
import tkinter as tk
import tkinter.ttk as ttk
# 画像処理
import PIL.Image
import PIL.ImageTk

import random

# 画像とその画像の動物名を対応させた辞書を作成
animal = [
    {"Q": "rabbit.jfif", "A": "ウサギ"},
    {"Q": "elephant.jfif", "A": "ゾウ"},
    {"Q": "owl.jfif", "A": "フクロウ"},
    {"Q": "monkey.jfif", "A": "サル"},
    {"Q": "rion.jfif", "A": "ライオン"},
    {"Q": "madagascar.jfif", "A": "マダガスカル"},
    {"Q": "kaba.jfif", "A": "カバ"},
    {"Q": "eagle.jfif", "A": "ワシ"},
    {"Q": "penguin.jfif", "A": "ペンギン"},
    {"Q": "crocodile.jfif", "A": "ワニ"},
]

# 回答結果を表示する関数
def judge():
    # 質問回数をカウント
    global QUESTION_COUNT
    QUESTION_COUNT = QUESTION_COUNT + 1
    seikai = animal[ANSWER]["A"]
    if entry.get() == seikai:
        # 正解回数をカウント
        global CORRECT_COUNT
        CORRECT_COUNT = CORRECT_COUNT + 1
        result["text"] = "正解"
    else:
        text = "不正解。正解は{}でした"
        result["text"] = text.format(seikai)
    path = animal[ANSWER]["Q"]
    # 画像を読み込む
    newImage = PIL.Image.open(path).resize((700, 400), resample=0)
    # 読み込んだ画像をimageLabelに表示
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData
    imageLabel.update()
    result.update()

# 正解インデックス保存するグローバル変数ANSWER
ANSWER = 0
# 正解した回数
CORRECT_COUNT = 0
# 解いた問題数
QUESTION_COUNT = 0

# 画像のパスを読み込みimageLabelに画像を表示する関数
def input_image():
    # ランダムでインデックスを生成
    index = random.randint(0,len(animal) - 1)
    global ANSWER

    # ANSWERにランダムに抽出したインデックスを代入
    ANSWER = index
    # pathに画像のパスを代入
    path = animal[index]["Q"]
    # 画像を読み込む
    newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((700,400),resample=0)
    #読み込んだ画像をimageLabelに表示
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

    result.configure(text="結果表示")
    result.update()


# スタート画面を準備
root = tk.Tk()
root.title("kadai application")
root.geometry("1000x1000")

# rootメインウィンドウのグリッドを 1x1にしておくと、Frameの配置がズレなくなります。
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# スタートフレームの作成と設置
start_frame = ttk.Frame(root)
# 重ねる各Frameはgrid()メソッドで座標（0, 0）に設置します。
# また引数にsticky="nsew"を入れて、メインウィンドウと同じサイズにしておくことも必要です。
start_frame.grid(row=0, column=0, sticky="nsew", pady=20)

# クイズフレームの作成と設置
quize_frame = ttk.Frame(root)
quize_frame.grid(row=0, column=0, sticky="nsew", pady=20)

# 結果レームの作成と設置
result_frame = ttk.Frame(root)
result_frame.grid(row=0, column=0, sticky="nsew", pady=20)

# ---スタートフレームの編集----

# ラベルのスタイルを作成
label_style = ttk.Style()
label_style.configure("TLabel", font=("Helvetica", 16))
# ラベルを作成
lbl = ttk.Label(start_frame,text="画像に映っている動物を当てよう！",style="TLabel")

# ボタンのスタイルを作成
label_style = ttk.Style()
label_style.configure("TButton", width=20, height=200)
# スタートボタンを作成
btn = ttk.Button(start_frame,text="スタート!",style="TButton",command=lambda: quize_frame.tkraise())
# ラベルとボタンを配置
lbl.place(x= 500,y=350)
btn.place(x= 600,y=400)


# ---クイズフレームの編集----

# 画像を表示するラベルを準備
imageLabel = tk.Label(quize_frame)
imageLabel.pack()

# 結果表示
result = tk.Label(quize_frame)
input_image()
#  解答欄ラベルを準備
explanationLabel = ttk.Label(quize_frame,text="解答欄:")
# 入力欄のスタイルを作成
style = ttk.Style()
style.configure("TEntry", fieldbackground="yellow", width=30)
# 入力欄を準備
entry = ttk.Entry(quize_frame,style="TEntry")

# ボタンのスタイルを作成
label_style = ttk.Style()
label_style.configure("TButton", width=30, height=30)

# 解答するボタンを作成
answer_btn = ttk.Button(quize_frame,text="解答する",style="TButton",command=judge)

# 解答するボタンを作成
next_btn = ttk.Button(quize_frame,text="次の問題へ",style="TButton",command=input_image)

# 終了するボタンを作成
end_btn = ttk.Button(quize_frame,text="終わる",style="TButton",command=lambda: result_frame.tkraise())

result.pack()
explanationLabel.place(x=550,y=500)
entry.place(x=630,y=500)
answer_btn.place(x=600,y=550)
next_btn.place(x=600,y=600)
end_btn.place(x=600,y=630)

# ---結果レームの編集----
text = "お疲れさまでした。あなたは{}問中{}問正解しました"

lbl = tk.Label(result_frame)
def end():
    global QUESTION_COUNT
    global  CORRECT_COUNT
    lbl.configure(text=text.format(QUESTION_COUNT, CORRECT_COUNT))

end()
lbl.pack()

# frameを前面にする
# 表示したいFrameはtkraise()メソッドを使用して、最前面に移動させます。
# tkraise()メソッドは対象のFrameを最前面に移動させます。
start_frame.tkraise()

root.mainloop()

