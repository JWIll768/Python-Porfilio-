import random
states=["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida",
        "Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine",
        "Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska",
        "Nevada","New,Hampshire","New,Jersey","New,Mexico","New,York","North,Carolina","North,Dakota",
        "Ohio","Oklahoma","Oregon","Pennsylvania","Rhode,Island","South,Carolina","South,Dakota",
        "Tennessee","Texas","Utah","Vermont","Virginia","Washington","West,Virginia","Wisconsin","Wyoming"]

state_sizes= [52420,665384,113990,53179,163695,104094,5543,2489,65758,59425,10932,83569,57914,36420,56273,82278,40408,52378,35380,12406,10554,96714,86936,48432,69707,147040,77348,110572,9349,8723,121590,54555,53819,70698,44826,69899,98379,46054,1545,32020,77116,42144,268596,84897,9616,42775,71298,24230,65496,97813]

print("When we talk about the biggest states, we usually refer to those who are biggest by population like California")
print("But have you ever wondered what states are considered small, medium, or big in relation to area?")
print("Whatever the case will be, you will see the size of states... in relation to area of course")

filtered_list =[]

size = input("What size of states are you looking for? Small, Medium or Big")
def state_recommendation(size):
    if size == "Small":
        for i in range(len(state_sizes)):
            if state_sizes[i] >= 0 and state_sizes[i] <= 50000:
                filtered_list.append(states[i])
        print("Out of the list of small sized states, " + random.choice(filtered_list) + " has been chosen for you")


    if size == "Medium":
        for i in range(len(state_sizes)):
            if state_sizes[i] >= 50000 and state_sizes[i] <= 100000:
                filtered_list.append(states[i])
        print("Out of the list of medium sized states, " + random.choice(filtered_list) + " has been chosen for you")


    if size == "Big":
        for i in range(len(state_sizes)):
             if state_sizes[i] >=100000:
                filtered_list.append(states[i])
                random.choice(filtered_list)
        print("Out of the list of big sized states, " + random.choice(filtered_list) + " has been chosen for you")


state_recommendation(size)
#data source: https://docs.google.com/spreadsheets/d/1y-7zguIiZ98CQ3Lh3U0b0QSRbd_fA9I4oea2Qtsyw9w/edit?usp=sharing





