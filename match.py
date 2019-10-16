import bullet
import support
import tank
import turtle


# fecha a tela
playing = True


def close_screen():
    global playing
    playing = not playing


# define as funções das teclas
def key_map(screen):

    # primeiro tanque
    screen.onkeypress(tank.rotate_left_1, 'a')
    screen.onkeypress(tank.rotate_right_1, 'd')
    screen.onkeypress(tank.go_ahead_1, 'w')
    screen.onkeypress(bullet.shooter_one, 'space')

    # segundo tanque
    screen.onkeypress(tank.rotate_left_2, 'Left')
    screen.onkeypress(tank.rotate_right_2, 'Right')
    screen.onkeypress(tank.go_ahead_2, 'Up')
    screen.onkeypress(bullet.shooter_two, 'o')

    # sair do jogo
    screen.onkeypress(close_screen, 'Escape')


# lê o txt pelo terminal e o percorre para criar o cenário
def create_zone(zone):
    field = open(zone, 'r')
    global wall_list
    wall_list = []
    y = 220
    for line in field:
        x = -392
        for block in line:
            if block == '1':
                wall = support.draw('square', 1, '#f7d4ab', x, y)
                wall_list.append(wall)
            x += 8.3
        y -= 16.3


# interação entre os elementos do jogo
def char_interplay():

    # colisão dos tanques com as paredes
    for block in range(len(wall_list)):
        if tank.one.distance(wall_list[block]) <= 25:
            tank.one.forward(-20)
        if tank.two.distance(wall_list[block]) <= 25:
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

    # colisão do projétil 1 com o labirinto
    for proj_1 in bullet.shot_one_list:
        for wall in wall_list:
            if (wall.distance(proj_1)) <= 25:
                proj_1.hideturtle()
                del(proj_1)
                break

    # colisão do projétil 2 com o labirinto
    for proj_2 in bullet.shot_two_list:
        for wall in wall_list:
            if (wall.distance(proj_2)) <= 25:
                proj_2.hideturtle()
                del(proj_2)
                break

    # movimentação do projétil 1
    for block in range(len(bullet.shot_one_list)):
        bullet.shot_one_list[block].setx(bullet.shot_one_list[block].xcor() +
                                         bullet.shot_one_list[block].dx)
        bullet.shot_one_list[block].sety(bullet.shot_one_list[block].ycor() +
                                         bullet.shot_one_list[block].dy)

    # movimentação do projétil 2
    for block in range(len(bullet.shot_two_list)):
        bullet.shot_two_list[block].setx(bullet.shot_two_list[block].xcor() +
                                         bullet.shot_two_list[block].dx)
        bullet.shot_two_list[block].sety(bullet.shot_two_list[block].ycor() +
                                         bullet.shot_two_list[block].dy)
