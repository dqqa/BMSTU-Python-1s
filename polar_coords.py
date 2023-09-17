import turtle
import math


func = lambda x: 2*(1-math.cos(x))
# func = lambda x: math.e**math.sin(x)-2*math.cos(4*x)+math.sin((2*x-math.pi)/24)**5
# func = lambda x: (2*(1-math.cos(x)))**2

scale = 75
prec = 20

tu = turtle.Turtle()
tu.speed(0)
tu.hideturtle()

phi = 0
while phi <= math.pi * 4:
    try:
        r = func(phi)
        x, y = r * math.cos(phi), r * math.sin(phi)
        tu.goto(x*scale, y*scale)
        tu.dot(3)
    except:
        pass
    phi += math.pi / prec

turtle.done()