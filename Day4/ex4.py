bacteria = int(input("How many bacteria are there ? "))
minutes = int(input("How many minutes have passes ? "))
count =0
remain = 0
rep = minutes // 2
while count < rep:
    remain = remain + (bacteria *2)
    count = count + 1
print("After",minutes,"minutes,we would have",remain,"bacteria")
