#Jamari Williams
#January 15th, 2025
#Dream Dancer's Quest

#Functions
print("Welcome dancer to your Dream Dancer's Quest")
print("Are you ready to become the best dancer or remain as someone who can't dance")
confidence = 0
physical_training = 0
practice_xp= 0
quality_of_life = 0
while True:
    dance_style = int(input("""Choose your style of dancing:
    1. Hip/ Hop
    2. Country
    3. Classic
    4. Jazz
    5. Latin"""))
    print("""You have a dance competition soon. Make sure you Meditate, Practice, Work on your confidence and work on physical training.Note that having confidence is crucial to winning competitions""")
    activity = int(input("""Select an activity for the day:
    1. Meditate
    2. Practice
    3. Workout
    4. Spend time with family
    5. Compete
    6. Quit"""))

    if activity == 1:
        confidence = confidence + 2
        quality_of_life =  quality_of_life + 2
        physical_training = + 1
        print("You want to clear your mind off things so you choose to meditate")
        print("""Remember. You need to have at least 10 points in all stats to be ready for the boogie down""")
        if confidence < 20 and physical_training<20 and practice_xp<20 and quality_of_life<20:
            print("You're currently not ready for the boogie down")
    if activity == 2:
        confidence = confidence+3
        practice_xp =  practice_xp+ 3
        print("""We know some people can't dance but at least you're not afraid to say you can't. Keep up the good work""")
        if confidence < 20 and physical_training<20 and practice_xp<20 and quality_of_life<20:
            print("You're currently not ready for the boogie down")
         if confidnece == 20 and physical_training==20 and practice_xp==20 and quality_of_life==20:
            print("You're currently not ready for the boogie down")
    if activity == 3:
        physical_training = physical_training+ 2
        print("A weak dancer isn't only about their dancing moves")
        if confidence < 20 and physical_training<20 and practice_xp<20 and quality_of_life<20:
            print("You're currently not ready for the boogie down")
        if confidnece == 20 and physical_training==20 and practice_xp==20 and quality_of_life==20:
            print("You're currently not ready for the boogie down")
    if activity == 4:
         quality_of_life =  quality_of_life + 3
         print("You've been too busy dancing that you're family thinks you don't love them anymore so you spend time with them")
         if confidence < 20 and physical_training<20 and practice_xp<20 and quality_of_life<20:
            print("You're currently not ready for the boogie down")
         if confidnece == 20 and physical_training==20 and practice_xp==20 and quality_of_life==20:
            print("You're currently not ready for the boogie down")
    if activity == 5:
        print("Prepare for your boogie down")
    if activity == 6:
        break
