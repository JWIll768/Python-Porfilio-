#simple claculator

#init
#Function
#Adds num1 and num2 and prints the result
def add(num1,num2):
    result= num1+num2
    print(result)
def sub(num1,num2):
    result= num1-num2
    print(result)
def div(num1,num2):
    result= num1/num2
    print(result)
def mul(num1,num2):
    result= num1*num2
    print(result)
#Main
print("Welcome Preschoolers to Simple Calculator" )
print ("Enter an Operation: ")


while True:
    operation = int(input("(1-5)Operation: "))
    print("""1.Addition 2.Substraction 3.Division 4.Multiplication 5.Quit""")
    if operation == 1:#True
        int1 = int(input("Enter your first number: "))
        int2 = int(input("Enter your second number: "))
        add(int1,int2)
    elif operation == 2: #True
        int1 = int(input("Enter your first number: "))
        int2 = int(input("Enter your second number: "))
        sub(int1,int2)
    elif operation == 3: #True
        int1 = int(input("Enter your first number: "))
        int2 = int(input("enter your second number: "))
        div(int1,int2)
    elif operation == 4:
        int1 = int(input("Enter your first number: "))
        int2 = int(input("enter your second number: "))
        mul(int1,int2)
    elif operation == 5:
        print("Quit")
        break

