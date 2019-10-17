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


# criação do painel da pontuação
hud_score = support.draw('square', 1, 'white', 0, 250)
hud_score.hideturtle()
hud_score.penup()
hud_score.write('0 : 0', align='center', font=('Press Start 2P', 24, 'normal'))
score_1 = 0
score_2 = 0


# interação entre os elementos do jogo
def char_interplay():

    # colisão dos tanques com as paredes
    for block in range(len(wall_list)):
        if tank.one.distance(wall_list[block]) <= 25:
            tank.one.forward(-20)
        if tank.two.distance(wall_list[block]) <= 25:
            tank.two.forward(-20)

    global score_1
    global score_2
    # colisão do projétil 1 com o tanque 2
    for ind_1 in bullet.shot_one_list:
        if (tank.two.distance(ind_1)) <= 25:
            if ind_1.isvisible():
                score_1 += 1
            ind_1.hideturtle()
            ind_1.goto(500, 500)
            del(ind_1)
            hud_score.clear()
            hud_score.write('{} : {}'.format(score_1, score_2), align='center', font=(
                            'Press Start 2P', 24, 'normal'))

    # colisão do projétil 2 com o tanque 1
    for ind_2 in bullet.shot_two_list:
        if (tank.one.distance(ind_2)) <= 25:
            if ind_2.isvisible(): 
                score_2 += 1
            ind_2.hideturtle()
            ind_2.goto(-500, 500)
            del(ind_2)
            hud_score.clear()
            hud_score.write('{} : {}'.format(score_1, score_2), align='center', font=(
                            'Press Start 2P', 24, 'normal'))

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
    for shot in range(len(bullet.shot_one_list)):
        bullet.shot_one_list[shot].setx(bullet.shot_one_list[shot].xcor() +
                                         bullet.shot_one_list[shot].dx)
        bullet.shot_one_list[shot].sety(bullet.shot_one_list[shot].ycor() +
                                         bullet.shot_one_list[shot].dy)

    # movimentação do projétil 2
    for shot in range(len(bullet.shot_two_list)):
        bullet.shot_two_list[shot].setx(bullet.shot_two_list[shot].xcor() +
                                         bullet.shot_two_list[shot].dx)
        bullet.shot_two_list[shot].sety(bullet.shot_two_list[shot].ycor() +
                                         bullet.shot_two_list[shot].dy)
