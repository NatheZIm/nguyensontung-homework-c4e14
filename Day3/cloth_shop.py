ds = ["T-shirt","Sweater"]
loop = True
while loop:
    print("Welcome to our shop! Press E to exit shop ! ")
    letter = input("what do you want (C, R, U, D) ? ")
    if letter.islower():
        print("Try again with uppercase letter ! ")
    else:
        if letter == "R":
            print("Our item:",*ds)
        elif letter == "C":
            item = input("Enter new item: ")
            ds.append(item)
            print("Our item:",*ds)
        elif letter == "U":
            pos = int(input("Update position ? "))
            if pos < 0 or pos > len(ds):
                print("Invalid position , try again")
            else:
                itemrep = input(" New item ? ")
                ds[pos -1] = itemrep
                print("Our item:",*ds)
        elif letter == "D":
                pos2 = int(input("Delete position ? "))
                if pos2 < 0 or pos2 > len(ds):
                    print("Invalid position , try again")
                else:
                    ds.pop(pos2-1)
                    print("Our item:",*ds)
        if letter == "E":
            loop = False
