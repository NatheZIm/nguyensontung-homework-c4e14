#2.1
base = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Tung and these are my sheep sizes")
print(base)
#2.2
big = max(base)
print("Now my biggest sheep has size ",big," let's shear it ")
#2.3
for i in range(len(base)):
    if base[i] == big:
        base[i] = 8
        break
print("After shearing here is my flock")
print(base)
#2.4
print("One month has passed , now here is my flock")
for i in range(len(base)):
    base[i] += 50
print(base)
