from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
#
# def move():
#     t.forward(20)
#
# screen.listen()
# screen.onkey(key='space', fun=move)


def move_forwards():
    t.forward(20)


def turn_left():
    new_head = t.heading() + 10
    t.setheading(new_head)


def turn_right():
    new_head = t.heading() - 10
    t.setheading(new_head)


def move_backwards():
    t.backward(20)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def move_without_drawing():
    t.penup()
    t.forward(10)
    t.pendown()


screen.listen()
screen.onkey(key='l', fun=turn_right)
screen.onkey(key='i', fun=move_forwards)
screen.onkey(key='j', fun=turn_left)
screen.onkey(key='k', fun=move_backwards)
screen.onkey(key='c', fun=clear)
screen.onkey(key='m', fun=move_without_drawing)

screen.exitonclick()
