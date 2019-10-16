import bullet
import sys
from support import draw
import tank
import turtle

screen = turtle.Screen()
screen.title('ATARI: COMBAT TANK')
screen.bgcolor('#5e9e4a')
screen.setup(width=800, height=600)
screen.tracer(100000)

# lendo txt para gerar o labirinto
field = open(sys.argv[1], 'r')

# matriz dos blocos para verificar a colisão deles com os tanques
wall_list = []

y = 210
# percorrendo cada linha do txt
for line in field:
    x = -392
    # percorrendo cada item da linha
    for one in line:
        # verificando se é 1, ou seja, se é um bloco
        if one == '1':
            wall = draw('square', 1, '#ffc6a1', x, y)
            wall_list.append(wall)
        x += 8.3
    y -= 16.3

screen.listen()
screen.onkeypress(tank.rotate_left_1, 'a')
screen.onkeypress(tank.rotate_right_1, 'd')
screen.onkeypress(tank.go_ahead_1, 'w')
screen.onkeypress(bullet.shooter_one, 'space')

screen.onkeypress(tank.rotate_left_2, 'Left')
screen.onkeypress(tank.rotate_right_2, 'Right')
screen.onkeypress(tank.go_ahead_2, 'Up')
screen.onkeypress(bullet.shooter_two, 'o')

playing = True


def close_screen():
    global playing
    playing = not playing


root = screen.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW', close_screen)

while playing:
    screen.update()

    # colisão dos tanques com as paredes
    for ind in range(len(wall_list)):
        if tank.one.distance(wall_list[ind]) <= 25:
            tank.one.forward(-20)
        if tank.two.distance(wall_list[ind]) <= 25:
            tank.two.forward(-20)

    # colisão projétil 1 com o tanque 2
    for ind_1 in bullet.shot_one_list:
        if (tank.two.distance(ind_1)) <= 25:
            ind_1.hideturtle()
            del(ind_1)

    # colisão projétil 2 com o tanque 1
    for ind_2 in bullet.shot_two_list:
        if (tank.one.distance(ind_2)) <= 25:
            ind_2.hideturtle()
            del(ind_2)

    # movimentação do projétil 1
    for ind in range(len(bullet.shot_one_list)):
        bullet.shot_one_list[ind].setx(bullet.shot_one_list[ind].xcor() +
                                       bullet.shot_one_list[ind].dx)
        bullet.shot_one_list[ind].sety(bullet.shot_one_list[ind].ycor() +
                                       bullet.shot_one_list[ind].dy)

    # movimentação do projétil 2
    for ind in range(len(bullet.shot_two_list)):
        bullet.shot_two_list[ind].setx(bullet.shot_two_list[ind].xcor() +
                                       bullet.shot_two_list[ind].dx)
        bullet.shot_two_list[ind].sety(bullet.shot_two_list[ind].ycor() +
                                       bullet.shot_two_list[ind].dy)
