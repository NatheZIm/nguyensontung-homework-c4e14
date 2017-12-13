#2.5
base = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Tung and these are my sheep sizes")
print(base)
month = int(input("How many month have passed ? "))
loop = 1
while loop < month:
    print("MONTH ",loop,":")
    print("One month has passed , now here is my flock")
    for i in range(len(base)):
        base[i] += 50
    print(base)
    big = max(base)
    print("Now my biggest sheep has size ",big," let's shear it ")
    for i in range(len(base)):
        if base[i] == big:
            base[i] = 8
            print("After shearing here is my flock")
            print(base)
            break
    loop += 1
#2.6
total = sum(base)
money = total * 2
print("My flock has size in total : ",total)
print("I would get ",total," * 2$ = ",money,"$")
