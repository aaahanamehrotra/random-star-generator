import turtle
from random import randint

turtle.speed(0)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.colormode(255)

colors = []
sides = randint(3,51)
print(sides)
x = 1

for _ in range(sides):
	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)
	colors.append((255-r,255-g,255-b))

while True:
	turtle.pencolor(colors[x%sides])
	turtle.fd(50 + x)
	turtle.rt(((sides-2)*180)/sides)
	x = x + 1