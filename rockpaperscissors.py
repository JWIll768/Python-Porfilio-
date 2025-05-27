#Jamari Williams

#January 6th 2025

#Rock Paper Scissors

#Functions
import random
print("Welcome to Rock, Paper, Scissors")
print("Choose an option between Rock,Paper,Scissors")
while True:
    selection = (input("Selection: "))

    #Computer's choice
    ai =(random.randint(1,3))
    if ai == 1:
        ai = "Rock"
        print("Ai has chosen Rock")
    elif ai == 2:
        ai = "Paper"
        print("Ai has chosen Paper")
    elif ai == 3:
        ai = "Scissors"
        print("Ai has chosen scissors")
    #RPS
    if selection == "Rock" and ai == "Rock":
        print("You've got a tie")
    if selection == "Rock" and ai == "Paper":
        print("Ai has won")
    if selection == "Rock" and ai == "Scissors":
        print("the player has won and the Ai lost")

    elif selection == "Paper" and ai == "Rock":
        print("The player has won and the Ai has lost")
    elif selection == "Paper" and ai =="Paper":
        print("Tie game")
    elif selection == "Paper" and ai =="Scissors":
        print("The player has lost and the Ai has won")

    elif selection == "Scissors" and ai == "Rock":
        print ("The player has lost and the Ai has won")
    elif selection =="Scissors" and ai == "Paper":
        print("The player has won and the Ai has lost")
    elif selection == "Scissors" and ai == "Scissors":
        print("There's a tie")


