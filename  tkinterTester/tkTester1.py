import tkinter as tk
import tkinter.messagebox as tmsg

def dispLabel():
    lbl.configure(text="こんにちは")#ラベルのテキストを書き換える
    tmsg.showinfo("title","こんにちは")
root = tk.Tk()
root.geometry("200x100")#画面サイズをしていする。小文字のエックスで指定する。

def hello():
    print("Hello")

lbl = tk.Label(text="LABEL")#ラベルを作成
btn = tk.Button(text="PUSH",command= dispLabel)#ボタンを作成,commandは押されたときの処理

lbl.pack()#画面上にラベルを配置
btn.pack()#画面上にボタンを配置
tk.mainloop()#ウィンドウの生成と破棄を繰り返す