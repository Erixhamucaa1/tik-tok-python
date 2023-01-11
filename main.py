from turtle import *

width(20)
bgcolor('black')
colors=['#db0f3c','#50ebe7','white']
for col in  colors:
    up()
    goto(0,0)
    down()
    color(col)
    left(180)
    circle(50,270)
    forward(120)
    left(180)
    circle(50,90)
    