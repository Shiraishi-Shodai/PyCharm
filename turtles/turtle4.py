from turtle import *
shape("turtle")

col = ["orange","limegreen","gold","plum","tomato","orange","limegreen","gold","plum","tomato"]

for i in range(10):
    color(col[i])
    forward((i+1) * 10)
    left(90)
done()