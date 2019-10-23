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
        x = -398
        for block in line:
            if block == '1':
                wall_list.append(support.draw('square', 1, '#f7d4ab', x, y))
            elif block == '0':
                not_wall_list.append([x, y])
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


# colisão dos projéteis com o labirinto
def wall_collision(shot_list):
    for proj in shot_list:
        for wall in wall_list:
            if (wall.distance(proj)) <= 15:
                proj.hideturtle()
                del(proj)
                break


# colisão dos projéteis com os tanques
def tank_collision(shot_list, tank_hit, player_num):
    for proj in shot_list:
        if tank_hit.distance(proj) <= 25 and proj.isvisible():
            # som da colisão
            support.play_shot()
            # aumento da pontuação
            global score_1
            global score_2
            if player_num == 1:
                score_1 += 1
            elif player_num == 2:
                score_2 += 1
            hud_score.clear()
            support.write(hud_score, '{} : {}'.format(score_1, score_2))
            # mudança da posição do tanque atingido
            pos_random = random.choice(not_wall_list)
            tank_hit.goto(pos_random[0] - 50, pos_random[1] - 25)
            # deletando o projétil
            proj.hideturtle()
            del(proj)


# criação do painel da vitória
def victory(player_num):
    hud_victory = support.draw(None, None, 'white', 0, -15)
    hud_victory.hideturtle()
    support.write(hud_victory, 'PLAYER {} WINS!!!'.format(player_num))
    support.play_victory()
    close_screen()


# interação entre os elementos do jogo
def char_interplay():

    # colisão dos tanques com as paredes
    for block in wall_list:
        if tank.one.distance(block) <= 25:
            tank.one.forward(-20)
        if tank.two.distance(block) <= 25:
            tank.two.forward(-20)

    # movimentação do projétil 1
    bullet.shot_move(bullet.shot_one_list)

    # movimentação do projétil 2
    bullet.shot_move(bullet.shot_two_list)

    # colisão do projétil 1 com o labirinto
    wall_collision(bullet.shot_one_list)

    # colisão do projétil 2 com o labirinto
    wall_collision(bullet.shot_two_list)

    # colisão do projétil 1 com o tanque 2
    tank_collision(bullet.shot_one_list, tank.two, 1)

    # colisão do projétil 2 com o tanque 1
    tank_collision(bullet.shot_two_list, tank.one, 2)

    # verificando a condição de vitória
    if score_1 == 5:
        victory(1)
    elif score_2 == 5:
        victory(2)
