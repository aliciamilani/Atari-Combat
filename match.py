import bullet
import random
import support
import tank
import turtle

# fecha a tela
playing = True


def close_screen():
    global playing
    playing = not playing


# lê o txt pelo terminal e o percorre para criar o cenário
def create_zone(zone):
    field = open(zone, 'r')
    global wall_list
    global not_wall_list
    wall_list = []
    not_wall_list = []
    y = 220
    for line in field:
        x = -392
        for block in line:
            if block == '1':
                wall_list.append(support.draw('square', 1, '#f7d4ab', x, y))
            elif block == '0':
                not_wall_list.append([x-8.3, y+16.3])
            x += 8.3
        y -= 16.3


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


# criação do painel da pontuação
hud_score = support.draw('square', 1, 'white', 0, 250)
hud_score.hideturtle()
support.write(hud_score, '0 : 0')
score_1 = score_2 = 0


# interação entre os elementos do jogo
def char_interplay():

    # colisão dos tanques com as paredes
    for block in wall_list:
        if tank.one.distance(block) <= 25:
            tank.one.forward(-20)
        if tank.two.distance(block) <= 25:
            tank.two.forward(-20)

    # movimentação do projétil 1
    for proj_1 in bullet.shot_one_list:
        proj_1.setx(proj_1.xcor() + proj_1.dx)
        proj_1.sety(proj_1.ycor() + proj_1.dy)

    # movimentação do projétil 2
    for proj_2 in bullet.shot_two_list:
        proj_2.setx(proj_2.xcor() + proj_2.dx)
        proj_2.sety(proj_2.ycor() + proj_2.dy)

    # colisão do projétil 1 com o labirinto
    for proj_1 in bullet.shot_one_list:
        for wall in wall_list:
            if (wall.distance(proj_1)) <= 15:
                proj_1.hideturtle()
                del(proj_1)
                break

    # colisão do projétil 2 com o labirinto
    for proj_2 in bullet.shot_two_list:
        for wall in wall_list:
            if (wall.distance(proj_2)) <= 15:
                proj_2.hideturtle()
                del(proj_2)
                break

    global score_1
    global score_2

    # colisão do projétil 1 com o tanque 2
    for proj_1 in bullet.shot_one_list:
        if tank.two.distance(proj_1) <= 25 and proj_1.isvisible():
            # aumento da pontuação
            score_1 += 1
            hud_score.clear()
            support.write(hud_score, '{} : {}'.format(score_1, score_2))
            # mudança da posição do tanque atingido
            pos_random_2 = random.choice(not_wall_list)
            tank.two.goto(pos_random_2[0], pos_random_2[1])
            # deletando o projétil
            proj_1.hideturtle()
            proj_1.goto(500, 500)
            del(proj_1)

    # colisão do projétil 2 com o tanque 1
    for proj_2 in bullet.shot_two_list:
        if tank.one.distance(proj_2) <= 25 and proj_2.isvisible():
            # aumento da pontuação
            score_2 += 1
            hud_score.clear()
            support.write(hud_score, '{} : {}'.format(score_1, score_2))
            # mudança da posição do tanque atingido
            pos_random_1 = random.choice(not_wall_list)
            tank.one.goto(pos_random_1[0], pos_random_1[1])
            # deletando o projétil
            proj_2.hideturtle()
            proj_2.goto(-500, 500)
            del(proj_2)
