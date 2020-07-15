import turtle
from functools import partial

# Functions
def createGameObject(x, y, shape, width, length):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape(shape)
    paddle.color("white")
    paddle.shapesize(stretch_wid=width, stretch_len=length)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

def paddleDirection(paddle, direction):
    y = paddle.ycor()
    if(y > 250):
        y = 250
    elif(y < -250):
        y = -250
    else:
        y = y + direction
    paddle.sety(y)

def ballColliderCheck(ball, paddle1, paddle2):
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy = -1 * ball.dy
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy = -1 * ball.dy
    if (ball.xcor() > 390 or ball.xcor() < -390):
        ball.goto(0, 0)
        ball.dx = -1 * ball.dx
    if ((ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40)):
        ball.setx(340)
        ball.dx = -1 * ball.dx
    if ((ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40)):
        ball.setx(-340)
        ball.dx = -1 * ball.dx

wn = turtle.Screen()
wn.title("PyPong")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# Create Game Objects
paddle_a = createGameObject(-350, 0, "square", 5, 1)
paddle_b = createGameObject(350, 0, "square", 5, 1)
ball = createGameObject(0, 0, "circle", 1, 1)
ball.dx = 0.1
ball.dy = -0.1

# Key Listener
wn.listen()
wn.onkeypress(partial(paddleDirection, paddle_a, 10), "w")
wn.onkeypress(partial(paddleDirection, paddle_a, -10), "s")
wn.onkeypress(partial(paddleDirection, paddle_b, 10), "Up")
wn.onkeypress(partial(paddleDirection, paddle_b, -10), "Down")

# Main Loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ballColliderCheck(ball, paddle_a, paddle_b)
