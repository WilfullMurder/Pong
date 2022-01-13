# WilfullMurder

import turtle

# window setup
wn = turtle.Screen()  # Initialise screen
wn.title("Pong by WilfullMurder")  # Give title
wn.bgcolor("black")  # Set Colour to black
wn.setup(width=400 * 2, height=300 * 2)  # Fix size (halfsize * 2)
wn.tracer(0)  # Stop automatic update

# Score
Score_A = 0
Score_B = 0

# Paddle A
Paddle_A = turtle.Turtle()
Paddle_A.speed(0)  # Animation speed inside turtle module (maxSpeed)
Paddle_A.shape("square")  # Default size = 20*20px
Paddle_A.shapesize(stretch_wid=5, stretch_len=1)  # Shape the paddle 100*20px
Paddle_A.color("white")
Paddle_A.penup()  # Removes the default line drawing
Paddle_A.goto(-350, 0)  # Sets the Paddle far left

# Paddle B
Paddle_B = turtle.Turtle()
Paddle_B.speed(0)  # Animation speed inside turtle module (maxSpeed)
Paddle_B.shape("square")  # Default size = 20*20px
Paddle_B.shapesize(stretch_wid=5, stretch_len=1)  # Shape the paddle 100*20px
Paddle_B.color("white")
Paddle_B.penup()  # Removes the default line drawing
Paddle_B.goto(350, 0)  # Sets the Paddle far right
# Ball
Ball = turtle.Turtle()
Ball.speed(0)  # Animation speed inside turtle module (maxSpeed)
Ball.shape("square")  # Default size = 20*20px
Ball.color("white")
Ball.penup()  # Removes the default line drawing
Ball.goto(0, 0)  # Sets the ball centre
Ball.dx = 0.1
Ball.dy = -0.1

# Turtle pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 260)
Pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))


# Function
def Paddle_A_Up():
    y = Paddle_A.ycor()
    y += 20
    Paddle_A.sety(y)


def Paddle_A_Down():
    y = Paddle_A.ycor()
    y -= 20
    Paddle_A.sety(y)


def Paddle_B_Up():
    y = Paddle_B.ycor()
    y += 20
    Paddle_B.sety(y)


def Paddle_B_Down():
    y = Paddle_B.ycor()
    y -= 20
    Paddle_B.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(Paddle_A_Up, "w")
wn.onkeypress(Paddle_A_Down, "s")
wn.onkeypress(Paddle_B_Up, "Up")
wn.onkeypress(Paddle_B_Down, "Down")

# Game Loop
while True:
    wn.update()

    # Move the ball

    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= - 1

    if Ball.ycor() < -288:  # Should be -290 but that pos has cutoff for some reason
        Ball.sety(-288)
        Ball.dy *= - 1

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_A += 1
        Pen.clear()
        Pen.write("Player 1: {}  Player 2: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "bold"))

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_B += 1
        Pen.clear()
        Pen.write("Player 1: {}  Player 2: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "bold"))

    # Collision check
    if (340 < Ball.xcor() < 350) and (Paddle_B.ycor() + 40 > Ball.ycor() > Paddle_B.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= -1

    if (-340 > Ball.xcor() > -350) and (Paddle_A.ycor() + 40 > Ball.ycor() > Paddle_A.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1
