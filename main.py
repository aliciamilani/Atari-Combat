import tank
import turtle

playing = True


def close_screen():
    global playing
    playing = not playing


def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor('black')
    screen.setup(width=width, height=height)
    screen.tracer(100)
    return screen


def create_wall(x, y, width, length, color):
    wall = turtle.Turtle()
    wall.speed(0)
    wall.shape("square")
    wall.color(color)
    wall.shapesize(stretch_wid=width, stretch_len=length)
    wall.penup()
    wall.goto(x, y)
    return wall


screen = create_screen("ATARI COMBAT", 1000, 600)

screen.listen()
screen.onkeypress(tank.rotate_left_1, 'a')
screen.onkeypress(tank.rotate_right_1, 'd')
screen.onkeypress(tank.go_ahead_1, 'w')
screen.onkeypress(tank.rotate_left_2, 'Left')
screen.onkeypress(tank.rotate_right_2, 'Right')
screen.onkeypress(tank.go_ahead_2, 'Up')

root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)


# lendo txt para gerar o labirinto
field = open('field.txt', 'r')

y = 250
# percorrendo cada linha do txt
for line in field:
    x = -390
    # percorrendo cada item da linha
    for one in line:
        # verificando se é 1, ou seja, se é um bloco
        if(one == '1'):
            create_wall(x, y, 1, 1, "yellow")
        x += 8.3
    y -= 16.3


while playing:
    screen.update()
