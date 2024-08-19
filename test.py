from turtle import Turtle,Screen
import random
our_turtles=[]
my_screen=Screen()
my_screen.setup(width=800 , height= 400)

# def paint_finishline():
#     colors=["black","white"]
#     refree=Turtle()
#     refree.penup()
#     refree.setposition(350,-200)
#     while refree.position==(350,200):
#         for i in range (0,10):
#             refree.dot(size=30,color=colors[i%2])
# paint_finishline()
colors=["black","white"]
refree=Turtle()
refree.penup()
refree.setposition(350,-180)
refree.setheading(90)
for i in range (0,20):
    refree.dot(20,colors[i%2])
    refree.forward(20)
my_screen.exitonclick()