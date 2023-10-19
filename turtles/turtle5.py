from turtle import *
shape("turtle")

#col = ["orange","limegreen","gold","plum","tomato","orange","limegreen","gold","plum","tomato"]

colormode(255) # これ以降はRGBで指定できる

for i in range(10):
 #   color(col[i])
    color(0, 255, 0)
    forward((i+1) * 10)
    left(90)
done()