from turtle import *
speed(-1)
def draw_square(dai,mau):
    for i in range(4):
        color(mau)
        forward(dai)
        left(90)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
