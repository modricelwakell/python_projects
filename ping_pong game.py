from tkinter import font
import turtle

# Initialize screen
win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Madrab 1 (paddle 1)
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-350, 0)

# Madrab 2 (paddle 2)
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.11
ball.dy = 0.11
#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.goto(0,260)
score.hideturtle()
score.write("player 1: 0 player 2: 0",align="center",font=("Courier",24,"normal"))
# Functions for moving paddles
def madrab1_up():
    y = madrab1.ycor()
    if y < 250:  # Limit paddle movement within the screen
        y += 20
        madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    if y > -250:
        y -= 20
        madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    if y < 250:
        y += 20
        madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    if y > -250:
        y -= 20
        madrab2.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(madrab1_up, "")
win.onkeypress(madrab1_down, "s")
win.onkeypress(madrab2_up, "Up")
win.onkeypress(madrab2_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision check
    if ball.ycor() > 290:#if the ball at the top border
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:#if the ball at the bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:#if the ball at the right border
        ball.goto(0, 0)
        ball.dx *= -1
        score1+=1
        score.clear()
        score.write("player 1: {} player 2: {}.".format(score1,score2),align="center",font=("Courier",24,"normal"))
        


    if ball.xcor() < -390:#if the ball at the left border
        ball.goto(0, 0)
        ball.dx *= -1
        score2+=1
        score.clear()
        score.write("player 1: {} player 2: {}.".format(score1,score2),align="center",font=("Courier",24,"normal"))

    # Paddle collision check
    if (340 < ball.xcor() < 350) and (madrab2.ycor() - 50 < ball.ycor() < madrab2.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (madrab1.ycor() - 50 < ball.ycor() < madrab1.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
