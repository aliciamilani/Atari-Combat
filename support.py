# Som de vitória - https://freesound.org/people/rezyma/sounds/475148/

from os import system
from time import sleep
import turtle


def draw(shape, size, color, x, y):
    element = turtle.Turtle()
    element.speed(0)
    element.shape(shape)
    element.shapesize(stretch_wid=size, stretch_len=size)
    element.color(color)
    element.penup()
    element.goto(x, y)
    return element


def write(element, exp):
    element.write(exp, align='center', font=('Press Start 2P', 24, 'normal'))


def play_victory():
    system("aplay sounds/victory.wav")
    sleep(2)


def play_shot():
    system("aplay sounds/shot.wav")
