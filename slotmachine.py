#Daniel Brookins and Jamari Williams
#Slot Machine
#Init
import random
slot = ["🌟", "🌕", "🚀","7"]
credits = 100
#Main
#1. Introduction
#2. Player decides to spin or quit
#3. If spin, randomly pull three symbols
#Tip: You must remeber these three
#symbols using varibales!!!
#4.Determine outcome using if, elif,else
#1. Start the player with 100(choice) credit
#2. Every spin cost 1(choice)
#4. 3 of a kind = x2 reward (choice)
#4b. 2 of a kind = x2 reward (choice)
#6. Display their credits consistently
#7. Do not let them play w/0 credits


print("Welcome to Slot Machine?")
while True:
    player =input("Choose Spin or Quit?")
    if player == "Quit":
        break
    if player == "Spin":
        slot1 = random.choice(slot)
        slot2 = random.choice(slot)
        slot3 = random.choice(slot)
        print(slot1 + slot2 + slot3)
    if slot1 == "🌟" and slot2 == "🌟" and slot3 == "🌟":
        print("Win!")
        credits = credits - 2
        credits = credits * 2
        print(credits)
    elif slot1 == "🌕" and slot2 == "🌕" and slot3 == "🌕":
        print("Win!")
        credits = credits - 2
        credits = credits * 2
        print(credits)
    elif slot1 == "🚀" and slot2 == "🚀" and slot3 == "🚀":
        print("Win!")
        credits = credits - 2
        credits = credits * 2
        print(credits)
    elif slot1 == "7" and slot2 == "7" and slot3 == "7":
        print("You've hit the JACKPOT!")
        credits = credits - 2
        credits = credits * 2
        print(credits)
    if slot1 == slot2 != slot3:
        print("Win!")
        credits = credits - 2
        credits = credits * 2
        print(credits)
    if slot2 == slot3 != slot3:
        print("Win!")
        credits = credits - 2
        credits = credits * 2
        print(credits)
    else:
        print("Take yo L!")
        credits = credits - 2
        print(credits)
