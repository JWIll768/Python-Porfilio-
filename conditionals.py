#driver license check
#Init

#functions

#16 yrs+
#passed drivers ed exam

def driver_check():
    age=int(input("Please enter your age"))
    exam= input("Have you passed your Drivers Education exam?")
    #process w conditional statements
    if age > 15 and exam== "yes": #Evaluate as True or False
        print("You are old enough to drive!")
    else:
        print ("You are NOT old enough to drive!")
def vote_check():
    age=int(input("Please enter your age"))
    citizenship=input("Are you a U.S citizen?")
    if age > 18 and citizenship== "yes":
        print("you are elgible to vote!")
    else:
        print("You are not allowed to vote :(" )
#Print the largest of the three numbers
def max_num(a,b,c):
    #No input needed
    #Process the date with conditional statements
    if a > b and a > c:
        print(str(a) + "is the largest number, a is greatest.")
    elif b > a and b > c:
        print(str(b) + " is the largest number, b is greatest.")
    elif c > a and c > b:
        print(str(c) + " is the largest number, c is the greatest")
    else:
        print(" Error, there is no largest number")
def score_to_grade(score):
    if score > 89.5:
        print("You got an A")
    elif score > 79.5:
        print("You got a B")
    elif score > 69.5:
        print("You got a C")
    elif score > 59.5:
        print("You got a F")
#Main
score_to_grade(79)
