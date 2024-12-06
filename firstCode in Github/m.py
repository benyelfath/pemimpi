from turtle import *
speed(0)
bgcolor('black')
color('aqua')
for i in range(250):
    rt(i)
    circle(240, i)
    fd(i)
    rt(90)
hideturtle()
done()