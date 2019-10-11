import turtle

wn = turtle.Screen()
wn.tracer(100)


# criando e registrando o formato dos tanques
def tank_shape():
    drawing = turtle.Turtle()
    drawing.pencolor('black')
    drawing.hideturtle()
    drawing.begin_poly()
    drawing.setheading(270)
    drawing.forward(3)
    drawing.setheading(0)
    drawing.forward(5)
    drawing.setheading(270)
    drawing.forward(6)
    drawing.setheading(0)
    drawing.forward(6)
    drawing.setheading(90)
    drawing.forward(20)
    drawing.setheading(180)
    drawing.forward(6)
    drawing.setheading(270)
    drawing.forward(4)
    drawing.setheading(180)
    drawing.forward(4)
    drawing.setheading(90)
    drawing.forward(12)
    drawing.setheading(180)
    drawing.forward(2)
    drawing.setheading(270)
    drawing.forward(12)
    drawing.setheading(180)
    drawing.forward(4)
    drawing.setheading(90)
    drawing.forward(4)
    drawing.setheading(180)
    drawing.forward(6)
    drawing.setheading(270)
    drawing.forward(20)
    drawing.setheading(0)
    drawing.forward(6)
    drawing.setheading(90)
    drawing.forward(6)
    drawing.setheading(0)
    drawing.forward(5)
    drawing.setheading(90)
    drawing.forward(3)
    drawing.end_poly()
    tank = drawing.get_poly()
    wn.clear()
    wn.tracer(100)
    return tank


wn.register_shape('tank', tank_shape())

# criação do primeiro tanque
one = turtle.Turtle()
one.penup()
one.goto(-300, 0)
one.shape('tank')
one.color('green')

# criação do segundo tanque
two = turtle.Turtle()
two.penup()
two.goto(300, 0)
two.setheading(180)
two.shape('tank')
two.color('red')


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
