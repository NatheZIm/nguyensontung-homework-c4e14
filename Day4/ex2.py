# without count() function
base = [3,2,1,5,6,4,5,6,9,8,7,4,5,6,8,1,3,2,1,4,5,6,8,4,7,1,4,9,6,3]
dem = 0
n = int(input("Enter a number ? "))
for i in range(len(base)):
    if base[i] == n:
        dem +=1
print(n,"appears ",dem,"times in my list")


# with count() function
base = [3,2,1,5,6,4,5,6,9,8,7,4,5,6,8,1,3,2,1,4,5,6,8,4,7,1,4,9,6,3]
n = int(input("Enter a number ? "))
a = base.count(n)
print(n,"appears ",a,"times in my list")
