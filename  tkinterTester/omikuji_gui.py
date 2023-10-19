import tkinter as tk
import tkinter.messagebox as tmsg
import random

def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    tmsg.showinfo("title",random.choice(kuji))
root = tk.Tk()
root.geometry("300x250")
root.title("おみくじGUI")

btn = tk.Button(text="占う",command=omikuji)

btn.pack()

tk.mainloop()
