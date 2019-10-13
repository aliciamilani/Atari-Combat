from support import draw
import turtle

screen = turtle.Screen()
screen.tracer(100)


# criando e registrando o formato dos tanques
def tank_shape():
    direction = [270, 0, 270, 0, 90, 180, 270, 180, 90, 180,
                 270, 180, 90, 180, 270, 0, 90, 0, 90]
    steps = [3, 5, 6, 6, 20, 6, 4, 4, 12, 2, 12, 4, 4, 6, 20, 6, 6, 5, 3]
    form = turtle.Turtle()
    form.pencolor('black')
    form.hideturtle()
    form.begin_poly()
    for n in range(19):
        form.setheading(direction[n])
        form.forward(steps[n])
    form.end_poly()
    tank = form.get_poly()
    screen.clear()
    screen.tracer(100)
    return tank


screen.register_shape('tank', tank_shape())

# criação do primeiro tanque
one = draw('tank', 1, '#2441a1', -350, 0)

# criação do segundo tanque
two = draw('tank', 1, '#a83232', 350, 0)
two.setheading(180)


# movimentação do primeiro tanque
def rotate_left_1():
    angle = one.heading()
    if angle == 360:
        angle = 0
    one.setheading(angle+18)


def rotate_right_1():
    angle = one.heading()
    if angle == 360:
        angle = 0
    one.setheading(angle-18)


def go_ahead_1():
    one.forward(5)


# movimentação do segundo tanque
def rotate_left_2():
    angle = two.heading()
    if angle == 360:
        angle = 0
    two.setheading(angle+18)


def rotate_right_2():
    angle = two.heading()
    if angle == 360:
        angle = 0
    two.setheading(angle-18)


def go_ahead_2():
    two.forward(5)
