import turtle

def createGameObject(x, y, shape, width, length):
    print("I am here")
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape(shape)
    paddle.color("white")
    paddle.shapesize(stretch_wid=width, stretch_len=length)
    paddle.penup()
    paddle.goto(x, y)
    return paddle

wn = turtle.Screen()
wn.title("PyPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Create Game Objects
paddle_a = createGameObject(-350, 0, "square", 5, 1)
paddle_b = createGameObject(350, 0, "square", 5, 1)
ball = createGameObject(0, 0, "circle", 1, 1)

# Main Loop
while True:
    wn.update()