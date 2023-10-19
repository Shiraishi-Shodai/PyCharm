import tkinter as tk
import tkinter.messagebox as tmsg

def clickevent():
    m = txt.get()#テキスト取得
    tmsg.showinfo("title",m)

root = tk.Tk()
root.geometry("230x150")
root.title("ウィンドウタイトル")

txt = tk.Entry(width=15)
btn = tk.Button(text="表示",command=clickevent)

txt.pack()
btn.pack()

tk.mainloop()