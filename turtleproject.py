import turtle


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
a=0
b=0
t.goto(0,200)
t.pendown()
t.speed(0)
t.penup()
while True:

    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==210:
        break
    t.hideturtle()