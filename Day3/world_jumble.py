from random import *
loop = True
base = ["alone","beautiful","look","ship","eyes","medicine","game","champion"]
pick = choice(base)
converse = list(pick)
shuffle(converse)
print(*converse)
while loop:
    guess = input("Now ! Guess the word : ")
    if guess == pick:
        print("You win ! ")
        loop=False
    else:
        print("Try again !")
