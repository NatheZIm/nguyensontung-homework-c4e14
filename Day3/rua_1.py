from turtle import *
shape("turtle")
speed(-1)
n = 7
base = ["red", "blue", "brown", "yellow", "grey"]
for i in range(3, n+1):
    color(base[i-3])
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()
