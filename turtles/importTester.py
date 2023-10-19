# 毎回ライブラリ名.~と書く必要があるが、どのライブラリの関数やクラスを使っているのかがわかりやすい
# import turtle
# turtle.forward(100)

# ライブラリの特定の関数やクラスだけを使えるようにする(done()などは使えない)
# from turtle import forward
# forward(100)

# ライブラリ名を省略できるが、どのライブラリの関数やクラスを使っているのかがわかりずらくなる
# from turtle import *
# shape("turtle")  # shapeはturtle内の関数

# ライブラリに別名をつける -> どのライブラリの関数やクラスを使っているのかわかりやすく、コード量も削減できる
# import turtle as t
# t.forward(100)