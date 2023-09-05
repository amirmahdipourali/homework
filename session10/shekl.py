import turtle
import random
list=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", ]
turtle.bgcolor('black')
s=0
for i in range(800):
    cool_color=random.choice(list)
    turtle.pencolor(cool_color)
    turtle.forward(i)
    turtle.left(59)
    turtle.right(170)
    s+=10
    turtle.speed(0)
turtle.done()