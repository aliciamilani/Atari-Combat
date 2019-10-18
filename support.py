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
