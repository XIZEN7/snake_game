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

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")       

while True:
    wn.update()
    #Edge collisions
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #Hide segments
        for segment in segments:
            segment.goto(1000, 1000)
        #Clear Segments
        segments.clear()        
        #Reset scoreboard
        score = 0
        text.clear()
        text.write("Score: {}     High Score : {}".format(score, high_score), align = "center", font = ("Courier", 20, "normal"))
