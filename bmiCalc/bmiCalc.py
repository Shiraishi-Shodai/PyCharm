weight = float(input("体重を入力してください(kg)"))
height = float(input("身長を入力してください(m)"))
bmi = weight / (height**2)
print('{:.2f}'.format(bmi)) #小数点以下2位
print(f'{bmi:.2f}') #小数点以下2位

if bmi < 18.5:
    print("低体重")
elif bmi < 25:
    print("普通体重")
elif bmi < 30:
    print("肥満(1)")
elif bmi < 35:
    print("肥満(2)")
elif bmi < 40:
    print("肥満(3)")
else:
    print("肥満(4)")

