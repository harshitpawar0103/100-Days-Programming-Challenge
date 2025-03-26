# import colorgram as c 
# colors = c.extract(r"D:/coding/Python/Udemy\Day 18/The Hirst/image.jpg",10)
# colors_rgb = []

# for i in range(10):
#     color = colors[i]
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     t = (r,g,b)
#     colors_rgb.append(t)
    
# print(colors_rgb)

# this color_list is extracted from above code 
color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49)]

from turtle import Turtle, Screen
from random import choice

t = Turtle()
s = Screen()
t.pensize(5)
s.colormode(255)
t.speed("fastest")

t.penup()
t.goto(-350,350)


for i in range(10):
    t.goto(-350,350-i*50)
    for j in range(10):
        t.color(choice(color_list))     
        t.dot()
        t.forward(50)



s.exitonclick()

