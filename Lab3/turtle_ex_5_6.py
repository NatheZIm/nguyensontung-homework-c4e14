from turtle import *
speed(-1)
color("blue")
def draw_star(x,y,z):
    count = 0
    penup()
    setx(x)
    sety(y)
    pendown()
    while count <= 5:
        forward(z)
        right(144)
        count += 1
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3,10)
    draw_star(x, y, length)
mainloop()
