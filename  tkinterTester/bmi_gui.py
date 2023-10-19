import tkinter as tk
import tkinter.messagebox as tmsg

def bmi():

    bmi = float(weight.get()) / (float(height.get()) ** 2)
    if bmi < 18.5:
        tmsg.showinfo("低体重")
    elif bmi < 25:
        tmsg.showinfo("普通体重")
    elif bmi < 30:
        tmsg.showinfo("肥満(1)")
    elif bmi < 35:
        tmsg.showinfo("肥満(2)")
    elif bmi < 40:
        tmsg.showinfo("肥満(3)")
    else:
        tmsg.showinfo("肥満(4)")

root = tk.Tk()
root.geometry("300x250")
root.title("BMI_GUI")

heightLbl = tk.Label(text="身長を入力してください(m)")
height = tk.Entry(width=15)
weightLbl = tk.Label(text="体重を入力してください(kg)")
weight = tk.Entry(width=15)

heightLbl.pack()
height.pack()
weightLbl.pack()
weight.pack()

btn = tk.Button(text="結果を見る",command=bmi)

btn.pack()

tk.mainloop()
