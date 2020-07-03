
import turtle

wn = turtle.Screen()
wn.title("a good game if ALLAH makes me make it")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle a
padle_a = turtle.Turtle()
padle_a.speed(0)
padle_a.shape("square")
padle_a.color("white")
padle_a.shapesize(stretch_len=1, stretch_wid=10)
padle_a.penup()
padle_a.goto(-350, 0)
#paddle b
padle_b = turtle.Turtle()
padle_b.speed(0)
padle_b.shape("square")
padle_b.color("white")
padle_b.shapesize(stretch_len=1, stretch_wid=10)
padle_b.penup()
padle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(-350, 0)
ball.dx = 2
ball.dy = -2

#functions
def padle_a_up():
    y = padle_a.ycor()
    y += 20
    padle_a.sety(y)

def padle_a_down():
    y = padle_a.ycor()
    y -= 20
    padle_a.sety(y)

def padle_b_up():
    y = padle_b.ycor()
    y += 20
    padle_b.sety(y)

def padle_b_down():
    y = padle_b.ycor()
    y -= 20
    padle_b.sety(y)
#keyboard bindings
wn.listen()
wn.onkeypress(padle_a_up, "w")
wn.onkeypress(padle_a_down, "s")
wn.onkeypress(padle_b_up, "i")
wn.onkeypress(padle_b_down, "k")




#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1


        #padle and ball collusions
        if ball.xcor() > 340 and (ball.ycor() < padle_b.ycor() + 50 and ball.ycor() > padle_b.ycor() - 50):






    





















