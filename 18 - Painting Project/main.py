import turtle as t
import colorgram
import random

t.colormode(255)
turtle = t.Turtle()
turtle.hideturtle()
turtle.speed(0)

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

turtle.penup()

xpos = -420
ypos = -350

turtle.setpos(xpos, ypos)
number_of_dots = 270

for dot_count in range(1, number_of_dots + 1):   
    turtle.dot(30, random.choice(color_list))
    turtle.forward(50)

    if dot_count % 18 == 0:
        ypos += 50
        turtle.setpos(xpos, ypos)



screen = t.Screen()
screen.exitonclick()