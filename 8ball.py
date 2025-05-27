#Jamari Williams
#February 3, 2025
#Magic 8 ball
#Init

import random
import time

magic_8ball = [Yes, Yes likely, Maybe so, Probably, Definitely, No, Not Likely, Not very Likely, Possible, Not Possible,  ]

#Main
Print("Shake...")
time.sleep(2)
Print("Shake...")
time.sleep(2)
Print("Shake...")
time.sleep(2)
Print("Shake...")
time.sleep(2)

Print("If you believe in our ability to tell the future then use our Magic 8 ball")
while True:
    question = input("Please ask a use or no question)
    if question.endswith("?"):
        print(random.choice(magic_8ball))
    else:
        print("Please ask a yes or no question")
