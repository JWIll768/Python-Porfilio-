#name genrator
# Jamari Williams
#init

#Functions
def gamer_choice():
    print("Welcome to Gamer's Choice")
    print("Answer the questions to find out the game that fits you")
    ans = input("Story mode or Multiplayer?")
    if ans =="Multiplayer":
        ans = input("PVP or PVE")
        if ans == "PVP":
            input("Third person or First person?")
            if ans == "Third person":
                print("Grand Theft Auto")
            elif ans== "First person":
                print("Call of Duty")
        elif ans == "Pve":
            input("Base building or Boss fights?")
            if ans == "Base building":
                print ("Ark Survival")
            elif ans == "Boss fights":
                print("Elden Rings")
    elif ans == "Story mode":
        ans = input("Zombies or Superheros?")
        if ans == "Zombies":
            input("Do you value story or gameplay?")
            if ans == "story":
                print("Last of Us")
            elif ans == "gameplay":
                print("Dying Light")
        elif ans == "Superheros":
            input("Gotham or New York?")
            if ans == "Gotham":
                print("Batman Arkam Series")
            elif ans == "New York":
                print ("Spider-Man Games")
#Main
gamer_choice()

