from turtle import *
shape("turtle")
speed(-1)
base = ["red", "blue", "brown", "yellow", "grey"]
for i in range(5):
    begin_fill()
    color(base[i])
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    penup()
    forward(50)
    pendown()
    end_fill()
mainloop()
