from turtle import *

def orinpic(col1,col2,col3,col4,col5,col6):
    col = [col1,col2,col3,col4,col5,col6]
    pensize(12)

    for i in col:
        if (i == ""):
            penup()
            home()
            right(90)
            forward(30)
            left(90)
            forward(30)
            pendown()
            continue
        color(i)
        circle(30)
        penup()
        forward(70)
        pendown()

