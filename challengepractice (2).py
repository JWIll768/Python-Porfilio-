#Jamari Williams
#february 27th, 2025

#functions
list = ["apple", "banana", "cherry", "apple", "apples", "pineapples", "cherry"]
def is_in_list(item, list):
    if item in list:
        print("Yes, 'apple' is in the fruits list")
    else:
        print("false")

def item_count(item, list):
    x = list.count(item)
    print(x)

def is_list_empty(list):
    if len(list) == 0:
        print("The list is empty")
    else:
        print("The list is not empty")

#Main function

