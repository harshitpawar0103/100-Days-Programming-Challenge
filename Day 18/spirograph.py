from turtle import Turtle, Screen

t = Turtle()
s = Screen()
r = 200
t.speed("fastest")
for _  in range(200):
    t.circle(r)
    t.right(5)



s.exitonclick()