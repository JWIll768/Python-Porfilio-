import turtle 
ari= turtle.Turtle()

def created_scene():
    ari.penup()
    ari.goto(-355,130) #This put the location of where you want to put your star in the coordinate plan (x,y)
    ari.pendown()
    ari.color("#ffcc00","yellow") #The first color is what is going to be the outline of the star and the second color is what is going to be the inside/fill color of the star
    ari.begin_fill()
    for i in range (5): #I repeated my triangle 5 times, because a star has 5 points to it
        for i in range(2):
            ari.forward(20)
            ari.left(120) #This got me a triangle but not closed off, so that it looks better
            #I turned it 120 degrees because 360 divided by 3 sides
        ari.left(192)
        #This positions the turtle so that it could do this again but at the right location
        #So that they don't overlap
    ari.end_fill()
#Main
created_scene()
