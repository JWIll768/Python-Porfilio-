numberlist = [1,101,54,23,47,85,77,12,11,68,]
fruitlist = ["Pineapple","Kiwi","Strawberry","Mangoes","Peaches","grape"]

#Simple for loop
#for i in range(10):
    #print(numberlist[i])

#For loop w/ len()
#for i in range(len(numberlist)):
    #print(numberlist[i])

#For loops using list elements
#  For fruit in fruitlist:
    #print(fruit)

#Challenge 1
#print the sum of all numbers in number list (variable)
sum = 0
#for number in numberlist:
    #sum = sum + number
#print(sum)
#for i in range(len(numberlist)):
    #sum = sum + numberlist[i]
#print(sum)
#Challenge 2
#print the largest numbers
largestnum = 0
for number in numberlist:
    if number > largestnum:
        largestnum = number
print(largestnum)
