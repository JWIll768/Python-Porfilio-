def login():
    #Hardcoded valid username and password (Modify these)
    valid_username = "YourUsername"
    valid_password = "YourPassword"

    #Get user input for username and password
    NameofUser = str(input("What is your username?"))
    PasswordofUser = str(input("What is your Password?"))
    if valid_username.lower() == NameofUser.lower():
        if PasswordofUser == valid_password:
            print("You're are all logged in!")
        else:
            print("Password does not match username.")
    else:
        print("Invalid username.")
#Call the function to check Creditionals
login()
