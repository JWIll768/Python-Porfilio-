#Init
import random

#Functions
def guess_the_number():
    print("Welcome to the guessing game")
    print("The rules to the game is guessing a number within a range")
    num= random.randint(0,10)
    for i in range (3):
        guess = int(input("Guess a number 1,10?"))
        if guess == num:
            print("You've guessed the number")
        else:
            print("You've guessed the wrong number")

#Main
guess_the_number()
