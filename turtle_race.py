from turtle import Turtle,Screen
import random
our_turtles = []
my_screen = Screen()
my_screen.setup(width=800, height=400)


def paint_finishline():
    colors = ["black", "white"]
    referee = Turtle()
    referee.penup()
    referee.setposition(350,-180)
    referee.setheading(90)
    for i in range(0, 20):
        referee.dot(20,colors[i % 2])
        referee.forward(20)


paint_finishline()


thor=Turtle(shape="turtle")
thor.color('yellow')
our_turtles.append(thor)

cap=Turtle(shape="turtle")
cap.color('blue')
our_turtles.append(cap)

ironman=Turtle(shape="turtle")
ironman.color('red')
our_turtles.append(ironman)

hulk=Turtle(shape="turtle")
hulk.color('dark green')
our_turtles.append(hulk)

scarlet=Turtle(shape="turtle")
scarlet.color('pink')
our_turtles.append(scarlet)

black_widow = Turtle(shape="turtle")
black_widow.color('black')
our_turtles.append(black_widow)

print(our_turtles)
my_screen.bgcolor('grey')
# paint_finishline()
turt_place = 160
for turtle in our_turtles:
    turtle.penup()
    turtle.goto(-380, turt_place)
    turt_place -= 60

user_bet= my_screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

# while True:
is_race_over = True
while is_race_over:
    for turtle in our_turtles:
        if turtle.xcor() > 350-(40/2):
            is_race_over = False
            winner = turtle
            winner_color = turtle.pencolor()
            if winner_color == user_bet.lower() :
                print(f"You've won! The {winner_color} turtle is the Winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the Winner!")
            break
        else:
            pass
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


my_screen.exitonclick()