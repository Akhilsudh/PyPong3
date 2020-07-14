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

def paddle_direction(paddle, direction):
    y = paddle.ycor()
    y = y + direction
    paddle.sety(y)


wn = turtle.Screen()
wn.title("PyPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Create Game Objects
paddle_a = createGameObject(-350, 0, "square", 5, 1)
paddle_b = createGameObject(350, 0, "square", 5, 1)
ball = createGameObject(0, 0, "circle", 1, 1)

# Key Listener
wn.listen()
wn.onkeypress(partial(paddle_direction, paddle_a, 10), "w")
wn.onkeypress(partial(paddle_direction, paddle_a, -10), "s")
wn.onkeypress(partial(paddle_direction, paddle_b, 10), "Up")
wn.onkeypress(partial(paddle_direction, paddle_b, -10), "Down")

# Main Loop
while True:
    wn.update()