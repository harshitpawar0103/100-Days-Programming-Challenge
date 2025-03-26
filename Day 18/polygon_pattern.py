from turtle import Turtle, Screen
from random import randint
t  = Turtle()
screen = Screen()
t.shape("turtle")
t.color("red")

colors_extended = [
    "gold", "silver", "navy", "maroon", "olive", "lime", "teal", "aqua", 
    "fuchsia", "indigo", "violet", "coral", "turquoise", "salmon", "beige",
    "lavender", "khaki", "chocolate", "crimson", "azure", "plum", "tan"
]

for i in range(3,10):
    angle = 360/i
    t.color(colors_extended[i])
    # t.color(randint(0,255),randint(0,255),randint(0,255))
    for f in range(i):
        t.forward(100)
        t.right(angle)

    









# screen.setup(width=.75, height=0.5, startx=-350, starty=350)
# t.hideturtle()
# # t.goto(-350,350)
# for i in range(100):
#     t.dot(10,"red")
#     t.penup()
#     t.forward(50)
#     t.pendown()
    


screen.exitonclick()




