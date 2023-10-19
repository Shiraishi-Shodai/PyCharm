import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    # 画像を読み込む
    # resample=0でアンチエイリアスを無効にする
    # resize((32,32))で圧縮したものをresize((300,300)で引き延ばすことでモザイクを表現
    # メソッドチェーン
    # open(path)で返ったImageがconvert("L")を呼び出し,convert("L")で返ったImageがresize((32,32))を呼び出すといった動きをしている
    newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300), resample=0)
    # そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    # ガベージコレクションのバグ発生を避けるために記述
    imageLabel.image = imageData
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
root = tk.Tk()
root.geometry("400x350")
btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
