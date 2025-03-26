from turtle import Turtle,Screen
from random import choice,randint

t = Turtle()
screen = Screen()
screen.colormode(255)
t.pensize(0.1)
t.speed("fastest")

def random_color():
    color = (randint(0,255),randint(0,255),randint(0,255))
    return color
# colors = [
#     "gold", "silver", "navy", "maroon", "olive", "lime", "teal", "aqua", 
#     "fuchsia", "indigo", "violet", "coral", "turquoise", "salmon", "beige",
#     "lavender", "khaki", "chocolate", "crimson", "azure", "plum", "tan"
# ]

angles = [0,90,180,270]
for i in range(500):
    # t.color(random_color())
    t.color(random_color())
    t.forward(30)
    t.setheading(choice(angles))