from dis import dis
from turtle import Turtle,Screen
import random
colors=["red","blue","orange","indigo","violet","green"]
screen=Screen()
screen.setup(width=500,height=400)
turtle_list = []
counter = 0
y_pos = -150

for turtle_name in colors:
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(colors[counter])
    turtle_name.penup()
    turtle_name.goto(-240,y_pos)
    turtle_name.pendown()
    turtle_list.append(turtle_name)
    counter +=1
    y_pos +=50

# red = Turtle(shape="turtle")
# blue = Turtle(shape="turtle")
# orange = Turtle(shape="turtle")
# indigo = Turtle(shape="turtle")
# violet = Turtle(shape="turtle")
# green = Turtle(shape="turtle")

# print(turtle_list)


# red.color(colors[0])
# red.penup()
# red.goto(-240,0)
# red.pendown()

# blue.color(colors[1])
# blue.penup()
# blue.goto(-240,50)
# blue.pendown()

# orange.color(colors[2])
# orange.penup()
# orange.goto(-240,-50)
# orange.pendown()


# indigo.color(colors[3])
# indigo.penup()
# indigo.goto(-240,100)
# indigo.pendown()

# violet.color(colors[4])
# violet.penup()
# violet.goto(-240,-100)
# violet.pendown()

# green.color(colors[5])
# green.penup()
# green.goto(-240,150)
# green.pendown()

user_bet = screen.textinput("Make a bet", "Guess a 'Color Name' of turtle that gonna win the race")
is_race_on = False

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle_name in turtle_list:
        if turtle_name.xcor()>230:
            if user_bet == turtle_name.pencolor():
                print(f"Congratulations! your {turtle_name.pencolor().upper()} Color turtle  Wins the race")
            else: 
                print(f"Sorry {turtle_name.pencolor().upper()} Color turtle  Wins the race")   
            is_race_on=False
        turtle_name.forward(random.randint(2,10))    
    



screen.exitonclick()
