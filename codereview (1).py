#Jamari Williams
#Feb 11th

#Challenge 1
#def double_num(num):
    #return (num*2)
#Challenge 2 (Print true if number is even)
def is_even(num):
    if num % 2 == 0:
        return(True) #Boolean A state of on and off.
    else:
        return(False)
#Final challenge
numlist = [1,2,3,4,5,6,7]
def last_number(list):
    return (numlist[len(list)-1])

#Main
#print(is_even(4))
#x = double_num(137)
#print(x/2)
#main
last_number(numlist)
