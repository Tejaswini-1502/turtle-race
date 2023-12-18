from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x_pos = -230
y_pos = -100
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x_pos, y=y_pos)
    y_pos = y_pos + 40
    all_turtles.append(new_turtle)

# checking if the user has provided input and setting 'is_race_on' true to start the race.
if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # checking if the turtle has reached the end of the screen (assuming turtle's w=40 and h=40)
        # 250- (40/2) = 230 (40/2 - considering the position from the turtle's center)
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            # checking if the winning turtle's color is same as the user's bet in the beginning
            if win_color == user_input:
                print(f"Yay! you won! The {win_color} turtle is the winner.")
            else:
                print(f"You lose. {win_color} turtle won the race.")
            break
        rand_distance = random.randint(0, 10) # Both 0 and 10 are inclusive
        turtle.forward(rand_distance) # moving the turtle by a random distance.

screen.exitonclick()