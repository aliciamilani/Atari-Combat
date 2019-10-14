from support import draw
import sys
import tank
import turtle
from math import sin, cos, radians

direction = [270, 0, 270, 0, 90, 180, 270, 180, 90, 180,
                 270, 180, 90, 180, 270, 0, 90, 0, 90]

screen = turtle.Screen()
screen.title('ATARI: COMBAT TANK')
screen.bgcolor('#5e9e4a')
screen.setup(width=800, height=600)
screen.tracer(100000)

# lendo txt para gerar o labirinto
field = open(sys.argv[1], 'r')

# matriz dos blocos para verificar a colisão deles com os tanques
wall_list = []

y = 275
# percorrendo cada linha do txt
for line in field:
    x = -392
    # percorrendo cada item da linha
    for one in line:
        # verificando se é 1, ou seja, se é um bloco
        if (one == '1'):
            wall = draw('square', 1, '#ffc6a1', x, y)
            wall_list.append(wall)
        x += 8.3
    y -= 16.3

screen.listen()
screen.onkeypress(tank.rotate_left_1, 'a')
screen.onkeypress(tank.rotate_right_1, 'd')
screen.onkeypress(tank.go_ahead_1, 'w')
screen.onkeypress(tank.rotate_left_2, 'Left')
screen.onkeypress(tank.rotate_right_2, 'Right')
screen.onkeypress(tank.go_ahead_2, 'Up')

#criando tiro
shot = turtle.Turtle('square')
shot.penup()
shot.speed(0)

shot_one_list = []

shooter

#criando bala 1
def create_shooter_one():
    shot_one = shot.clone()
    shot_one.shapesize(0.16, 0.16)
    shot_one.color('#2441a1')
    shot_one.goto(tank.one.xcor(), tank.one.ycor())
    shot_one_list.append(shot_one)

def shooting_one():
    x = 0
    y = 0
    for angle in direction:
        y = sin(radians(angle)) * 15
        x = cos(radians(angle)) * 15
    shot_one_list[-1].dx = x
    shot_one_list[-1].dy = y
    
def shooter_one():
    create_shooter_one()
    shooting_one()

screen.onkeypress(shooter_one,'space')

playing = True


def close_screen():
    global playing
    playing = not playing

root = screen.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW', close_screen)

while playing:
    screen.update()
    # colisão dos tanques com as paredes
    for num in range(len(wall_list)):
        if tank.one.distance(wall_list[num]) <= 25:
            tank.one.forward(-20)
        if tank.two.distance(wall_list[num]) <= 25:
            tank.two.forward(-20)

    for angles in range(len(shot_one_list)):
        shot_one_list[angles].setx(shot_one_list[angles].xcor() + shot_one_list[angles].dx)
        shot_one_list[angles].sety(shot_one_list[angles].ycor() + shot_one_list[angles].dy)