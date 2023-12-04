import turtle
import time
import random

postpone = 0.1

#Scoreboard
score = 0
high_score = 0

#Config Window
wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("Black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Body snake or segments
segments = []

#Text 
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0     High Score : 0", align = "center", font = ("Courier", 20, "normal"))

#Funtions

def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"
