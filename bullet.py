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
    shot_one_list.append(shot_one)


def shooting_one():
    x = 0
    y = 0
    for angle in tank.direction:
        y = sin(radians(angle)) * 15
        x = cos(radians(angle)) * 15
    shot_one_list[-1].dx = x
    shot_one_list[-1].dy = y


def shooter_one():
    create_shooter_one()
    shooting_one()


# criando projétil 2
def create_shooter_two():
    shot_two = draw('square', 0.16, '#a83232',
                    tank.two.xcor(), tank.two.ycor())
    shot_two_list.append(shot_two)


def shooting_two():
    x = 0
    y = 0
    for angle in tank.direction:
        y = sin(radians(angle)) * 15
        x = cos(radians(angle)) * 15
    shot_two_list[-1].dx = x
    shot_two_list[-1].dy = y


def shooter_two():
    create_shooter_two()
    shooting_two()
