from dis import dis
from turtle import Turtle,Screen, setheading
import random
import turtle
colors=["red","blue","orange","indigo","violet","green"]
screen=Screen()
screen.setup(width=500,height=400)

def draw_rectangle():
    rect = Turtle()
    rect.penup()
    rect.goto(150,125)
    rect.pendown()
    rect.fillcolor("red")
    rect.begin_fill()
    for i in range(2):
        rect.forward(30)
        rect.right(90)
        rect.forward(300)
        rect.right(90)
    rect.end_fill()   
    rect.write("FINISH") 
    rect.hideturtle()    


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


draw_rectangle()
user_bet = screen.textinput("Make a bet", "Guess a 'Color Name' of turtle that gonna win the race")
is_race_on = False

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle_name in turtle_list:
        if turtle_name.xcor()>130:
            if user_bet == turtle_name.pencolor():
                print(f"Congratulations! your {turtle_name.pencolor().upper()} Color turtle  Wins the race")
            else: 
                print(f"Sorry {turtle_name.pencolor().upper()} Color turtle  Wins the race")   
            is_race_on=False
        turtle_name.forward(random.randint(2,10))    
    



screen.exitonclick()
