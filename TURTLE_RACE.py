import random
from turtle import Turtle, Screen
# def go(turtle):
#     turtle.forward(random.randint(5, 60))
continue_race = True
rainbow = ["red", "blue", "green", "yellow", "purple", "orange"]
screen = Screen()
screen.setup(width=1000, height=800)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color:")
leo = Turtle()
mike = Turtle()
don = Turtle()
raph = Turtle()
splinter = Turtle()
april = Turtle()
k = -200
j = 0
turtle_list = [leo, mike, don, raph, splinter, april]
for i in turtle_list:
    k += 60
    i.speed(6)
    i.color(rainbow[j])
    i.penup()
    i.shape("turtle")
    i.setposition(-470, k)
    i.shape("turtle")
    i.speed(9)
    j += 1
while continue_race:
    for turtle in turtle_list:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 480:
            continue_race = False
            if user_bet == turtle.pencolor():
                print(f"You win! The winning color is {turtle.pencolor()}")
            else:
                print(f"You lose! The winning color is {turtle.pencolor()}")


screen.exitonclick()