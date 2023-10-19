import tkinter as tk

class Timer:

    # __init__はコンストラクタのようなもの。selfは自分自身のインスタンスを指す
    def __init__(self):
        self.root = tk.Tk()
        # 文字列を扱えるようにする。StringVar()は直前の文字を引き継がない。
        self.message = tk.StringVar()
        # textvariableでラベルの文字列を動的に挿入している。引数にはStringVar()インスタンスが入る
        label = tk.Label(textvariable=self.message, font=('Helvetica', 48))
        label.pack()

    def update(self):
        # countプロパティが-1より大きいとき
        if self.count > -1:
            # messageプロパティにcountプロパティを文字列化して代入
            self.message.set(str(self.count))
            self.count -= 1
            # 一秒経過したら再帰する
            self.root.after(1000, self.update)

    def main(self):
        # カウントダウン開始時の数字を指定
        self.count = 5
        self.update()
        # self.root.mainloop() # 描画処理が始まる


# app = Timer()  # インスタンス生成：速やかに終わらせる
# app.main()     # メインループ処理：描画やイベント処理を行う
# # mainloopから下の行はウィンドウを閉じたときに実行される
# app.root.mainloop()
#
# print("end")
