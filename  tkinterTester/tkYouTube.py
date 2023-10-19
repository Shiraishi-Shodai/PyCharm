import tkinter as tk
# import tkinter.messagebox as tmsg
import YoutubeDL

def download():

    download_url = "https://youtu.be/BO5_hWTtFzk"
    ydl_opts = {
        'format': '22',
        # 保存先を指定
        'outtmpl': "C:\Python_Work\Pycharm\ tkinterTester" + '/%(title)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([download_url])
root = tk.Tk()
root.title("YouTube")
root.geometry("250x250")


btn = tk.Button(text="Download",command=download)
tk.mainloop()