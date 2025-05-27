#Jamari Williams
#January 28,2024
listofitems = []

#Functions
while True:
    checklist = input("""Choose how you want to update your checklist:
                        1. View the current checklist
                        2. Add an item to your checklist
                        3. Remove an item from your checklist
                        4. exit""")
    checklist = int(checklist)

    if checklist == 1:
        print("You would like to review your checklist")
        print(listofitems)
    elif checklist == 2:
        additem = input("What would you like to add to your checklist")
        listofitems.append(additem)
    elif checklist == 3:
        remitem = input("What would you like to remove from youur checklist?")
        listofitems.remove(remitem)
    elif checklist == 4:
        print("You're done updating items on your checklist at the moment")
        print("Have a good day")
        break
