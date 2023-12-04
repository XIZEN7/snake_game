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
 #Food collisions
    if head.distance(food) < 20:
       x = random.randint(-280, 280)
       y = random.randint(-280, 280)
       food.goto(x,y)

       new_segment = turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("square")
       new_segment.color("green")
       new_segment.penup()
       segments.append(new_segment)
       #Increase score
       score += 10
       if score > high_score:
           high_score = score
       text.clear()
       text.write("Score: {}     High Score : {}".format(score, high_score), align = "center", font = ("Courier", 20, "normal"))
#Move the snake's body 
    totalseg = len(segments)
    for index in range(totalseg -1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    if totalseg > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)    
    mov()

  #Collisions with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            #Hide segments
            for segment in segments:
                segment.goto(1100, 1100)
            #Clear segments
            segments.clear() 
            #Reset scoreboard
            score = 0
            text.clear()
            text.write("Score: {}     High Score : {}".format(score, high_score), align = "center", font = ("Courier", 20, "normal"))               
    time.sleep(postpone)
