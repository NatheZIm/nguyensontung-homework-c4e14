from turtle import *
shape("turtle")
speed(-1)
for i in range(3,7):
    for j in range(1,i+1):
        if i%2==0:
            color("red")
        else:
            color("blue")
        left(360/i)
        forward(100)
mainloop()
