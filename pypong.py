import turtle
import simpleaudio as sa
from functools import partial


ballFlag = [True, True]
scoreValue = [0, 0]

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

def scoreDraw(score, value, x, y, align):
    style = ('Courier', 40, 'bold')
    score.goto(x, y)
    score.write(str(value), font=style, align=align)

def paddleDirection(paddle, direction):
    y = paddle.ycor()
    if(y > 230):
        y = 230
    elif(y < -230):
        y = -230
    else:
        y = y + direction
    paddle.sety(y)

def countScore(score, paddleNumber):
    scoreValue[paddleNumber] = scoreValue[paddleNumber] + 1
    score.clear()
    scoreDraw(score, scoreValue[0], -200, 300, 'center')
    scoreDraw(score, scoreValue[1], 200, 300, 'center')

def ballColliderCheck(ball, paddle1, paddle2, score, flag):
    if (ball.ycor() > 290):
        wave_obj.play()
        ball.sety(290)
        ball.dy = -1 * ball.dy
    if (ball.ycor() < -290):
        wave_obj.play()
        ball.sety(-290)
        ball.dy = -1 * ball.dy
    if (ball.xcor() > 390 or ball.xcor() < -390):
        if(ball.xcor() > 390):
            countScore(score, 0)
        if(ball.xcor() < -390):
            countScore(score, 1)
        flag[1] = not flag[1]
        paddle1.goto(-350, 0)
        paddle2.goto(350, 0)
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0
    if ((ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40)):
        wave_obj.play()
        ball.setx(340)
        ball.dx = -1 * ball.dx
    if ((ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40)):
        wave_obj.play()
        ball.setx(-340)
        ball.dx = -1 * ball.dx

def ballDirection(ball, flag):
    if(flag[1]):
        if(flag[0]):
            ball.dx = 0.4
            ball.dy = -0.4
            flag[0] = False
        else:
            ball.dx = -0.4
            ball.dy = 0.4
            flag[0]  = True
        flag[1] = False

wave_obj = sa.WaveObject.from_wave_file('ball.wav')

wn = turtle.Screen()
wn.title("PyPong3")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# Create Game Objects
middleLine = createGameObject(0, 0, "square", 30, 0.05)
topLine = createGameObject(0, 300, "square", 0.05, 40)
bottomLine = createGameObject(0, -300, "square", 0.05, 40)

playerName = turtle.Turtle()
playerName.penup()
playerName.color('white')
playerName.goto(-200, -370)
playerName.write('PLAYER A', font=('Courier', 20, 'bold'), align='center')
playerName.goto(200, -370)
playerName.write('PLAYER B', font=('Courier', 20, 'bold'), align='center')
playerName.hideturtle()

score = turtle.Turtle()
score.penup()
score.color('white')
scoreDraw(score, 0, -200, 300, 'center')
scoreDraw(score, 0, 200, 300, 'center')
score.hideturtle()

leftPaddle = createGameObject(-350, 0, "square", 5, 1)
rightPaddle = createGameObject(350, 0, "square", 5, 1)
ball = createGameObject(0, 0, "circle", 1, 1)
ball.dx = 0
ball.dy = 0

# Key Listener
wn.listen()
wn.onkeypress(partial(paddleDirection, leftPaddle, 20), "w")
wn.onkeypress(partial(paddleDirection, leftPaddle, -20), "s")
wn.onkeypress(partial(paddleDirection, rightPaddle, 20), "Up")
wn.onkeypress(partial(paddleDirection, rightPaddle, -20), "Down")
wn.onkeypress(partial(ballDirection, ball, ballFlag), "space")

# Main Loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ballColliderCheck(ball, leftPaddle, rightPaddle, score, ballFlag)
