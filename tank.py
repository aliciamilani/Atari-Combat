import turtle

screen = turtle.Screen()
screen.tracer(100)


# criando e registrando o formato dos tanques
def tank_shape():
    direction = [270, 0, 270, 0, 90, 180, 270, 180, 90, 180,
                 270, 180, 90, 180, 270, 0, 90, 0, 90]
    steps = [3, 5, 6, 6, 20, 6, 4, 4, 12, 2, 12, 4, 4, 6, 20, 6, 6, 5, 3]
    drawing = turtle.Turtle()
    drawing.pencolor('black')
    drawing.hideturtle()
    drawing.begin_poly()
    for n in range(19):
        drawing.setheading(direction[n])
        drawing.forward(steps[n])
    drawing.end_poly()
    tank = drawing.get_poly()
    screen.clear()
    screen.tracer(100)
    return tank


screen.register_shape('tank', tank_shape())

# criação do primeiro tanque
one = turtle.Turtle()
one.penup()
one.goto(-350, 0)
one.shape('tank')
one.color('#2441a1')

# criação do segundo tanque
two = turtle.Turtle()
two.penup()
two.goto(350, 0)
two.setheading(180)
two.shape('tank')
two.color('#a83232')


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
