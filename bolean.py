#Name
#Date
#Part 1: Boolean

#(Replace the comparison operator with another that makes the statement True.)
print(10 > 5)
print(3 > 2)
print("dog" != "cat")
print(8 == 8)
print(15 < 20)
print(4 > 3)
print(2 + 2 == 4)
print(True != False)
print(not (4 < 6) != True)
print(len("python") < 7)

#Part 2: Logic
#Complete each function one at a time and test them using the examples provided.


#Logic 1 (AND Operator)
#num = integer
def is_in_range(num):
    # Check if the number is between 10 and 20 (inclusive)
    if 10 < num and num < 20:
        print(True)
    else:
        print(False)
# Example: is_in_range(15) should print True, is_in_range(25) should print False

#Logic 2 (OR Operator)
#day = string
def is_weekend(day):
    # Check if the day is either Saturday or Sunday
    if day == "Saturday" or "Sunday":
        print(True)
    else:
        print(False)
# Example: is_weekend("Saturday") should print True, is_weekend("Monday") should print False
is_weekend("Saturday")

#Logic 3 (NOT Operator)
# num = integer
def is_not_negative(num):
    # Check if a number is not negative
    if num > 0:
        print(True)
    else:
        print(False)
# Example: is_not_negative(5) should print True, is_not_negative(-3) should print False

