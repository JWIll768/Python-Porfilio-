
#Initialize
#mySchedule stores a list of the classes you are currently taking at Jones  as strings
#Initialize the list with your first three periods ONLY
mySchedule = ["College Algebra" , "Spanish 4" , "AP COmputer Science"]

#Main

#Complete the following tasks using list/array methods. Print the result for each task.

#Task 1: Append periods 4 - 7 to the list
mySchedule.append("Team Sports")
mySchedule.append("Financial Alegebra")
mySchedule.append("Intermediate Film Study")
mySchedule.append("College Rhetoric and Composition")
mySchedule.append("College Rhetoric and Composition")

#Task 2: Insert your two lunch periods(A day and B Day) in their appropriate location
mySchedule.insert(3, "C Lunch")
mySchedule.insert(8, "B Lunch")

#Task 3: Remove your least favorite class
mySchedule.pop(7)
mySchedule.pop(8)
print(mySchedule)
#Task 4: Print just your 2nd period class by accessing the appropriate index in your array
print(mySchedule[1])
#Task 5: Print only your A day schedule and then only your B day schedule
print(mySchedule[:5])
print(mySchedule[5:8])
