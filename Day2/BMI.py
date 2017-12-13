#1 BMI
cm = int(input("chiều cao của bạn : "))
nang = int(input("Cân nặng của bạn : "))

m = cm * 0.01

bmi = nang / (m * m)
if bmi < 16:
    print("You're severely underweight")
else:
    if bmi <= 18.5:
        print("You're underweight")
    else:
        if bmi <= 25:
            print("You're Normal")
        else:
            if bmi <= 30:
                print("You're overweigh")
            else:
                print(" Congratulation !!! You have diabetes")
