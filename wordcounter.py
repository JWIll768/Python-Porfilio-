#Jamari Williams
#feb 26th, 2025

#functions
def wordcounter(text):
    splitlist = text.split() #splits text given
    length = len(splitlist) #takes the count of the words in the text
    print(length) #prints the word count
    print(splitlist) #prints the split text 
#Main function
wordcounter("I am in computer science")
