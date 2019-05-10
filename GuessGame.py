## Game to guess dice number ##


import random

diceNumber = int(random.randint(1,6))
print("Value appearing on dice = " ,diceNumber)
winVariable = False

# 3 tries for a user
for i in range(3):
    try:
        userInput = int(input("Guess a number : "))
    except ValueError:
        print("EXCEPTION -- Not a valid integer value")
        continue
    if userInput < diceNumber:
        print("Guessed number is less than actual number")
    elif userInput > diceNumber :
        print("Guessed number is greater than actual number")
    elif  userInput == diceNumber:
        winVariable = True
        print("Guessed number is correct, You Won")
        break


if winVariable is True:
    print("User has won the game")
else:
    print("User has lost the game, thanks for trying")



