from math import sin, cos, radians
from support import draw
import tank
import turtle

# listas com os projéteis
shot_one_list = []
shot_two_list = []


# criando projétil 1
def create_shooter_one():
    shot_one = draw('square', 0.16, '#2441a1',
                    tank.one.xcor(), tank.one.ycor())
    shot_one.setheading(tank.one.heading())
    shot_one.forward(20)
    shot_one_list.append(shot_one)


def shooting_one():
    x = cos(radians(tank.one.heading()))
    y = sin(radians(tank.one.heading()))
    shot_one_list[-1].dx = x
    shot_one_list[-1].dy = y


def shooter_one():
    create_shooter_one()
    shooting_one()


# criando projétil 2
def create_shooter_two():
    shot_two = draw('square', 0.16, '#a83232',
                    tank.two.xcor(), tank.two.ycor())
    shot_two.setheading(tank.two.heading())
    shot_two.forward(20)
    shot_two_list.append(shot_two)


def shooting_two():
    x = cos(radians(tank.two.heading()))
    y = sin(radians(tank.two.heading()))
    shot_two_list[-1].dx = x
    shot_two_list[-1].dy = y


def shooter_two():
    create_shooter_two()
    shooting_two()