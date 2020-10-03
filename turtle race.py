from turtle import *
from random import randint

# drawing track

penup()
goto(-140, 140)
speed(10)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(180)
    penup()
    backward(190)
    left(90)
    forward(20)

# drawing turtles
red = Turtle()
red.color("red")
red.shape("turtle")
red.penup()
red.goto(-160, 100)
red.pendown()

blue = Turtle()
blue.color("blue")
blue.shape("turtle")
blue.penup()
blue.goto(-160, 70)
blue.pendown()

yellow = Turtle()
yellow.color("yellow")
yellow.shape("turtle")
yellow.penup()
yellow.goto(-160, 40)
yellow.pendown()

green = Turtle()
green.color("green")
green.shape("turtle")
green.penup()
green.goto(-160, 10)
green.pendown()

black = Turtle()
black.color("black")
black.shape("turtle")
black.penup()
black.goto(-160, -20)
black.pendown()

for turn in range(1):
    red.right(360)
    blue.right(360)
    yellow.right(360)
    green.right(360)
    black.right(360)

for turn in range(100):
    red.forward(randint(1, 5))
    blue.forward(randint(1, 5))
    yellow.forward(randint(1, 5))
    green.forward(randint(1, 5))
    black.forward(randint(1, 5))
