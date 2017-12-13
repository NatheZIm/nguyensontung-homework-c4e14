b
n = int(input("Number of star : "))
for i in (range (n)):
    if i % 2 == 0:
        print("*",end="")
    else:
        print("x",end="")
print()
