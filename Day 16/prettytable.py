# import turtle as t

# timmy = t.Turtle()
# my_screen = t.Screen()

# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color('red','green')
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name","Skills"]
table.add_rows(
    [
        ["Pikachu","Electric"],
        ["Turtle","water"],
        ["Pipocu","hammerThrow"]
    ]
)
table.align = 'l'
print(table)