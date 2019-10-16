import match
import sys
import turtle

# criação da tela
screen = turtle.Screen()
screen.title('ATARI: COMBAT TANK')
screen.bgcolor('#5e9e4a')
screen.setup(width=800, height=600)
screen.tracer(100000)

# criação do cenário
match.create_zone(sys.argv[1])

<<<<<<< HEAD
hud_score = draw("square", 1, 'white', 0, 250)
hud_score.hideturtle()
hud_score.penup()
hud_score.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))
score_1 = 0
score_2 = 0

=======
# mapeamento das teclas
>>>>>>> a528d2ee912b2a06fc42cfe5c51b3ea8325fad72
screen.listen()
match.key_map(screen)

# fechamento da tela do jogo
root = screen.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW', match.close_screen)

# início do jogo
while match.playing:
    screen.update()
<<<<<<< HEAD

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
            ind_1.setx(500)
            ind_1.sety(500)
            del(ind_1)
            score_1 += 1
            hud_score.clear()
            hud_score.write("{} : {}".format(score_1, score_2), align="center", font=(
                            "Press Start 2P", 24, "normal"))


    # colisão projétil 2 com o tanque 1
    for ind_2 in bullet.shot_two_list:
        if (tank.one.distance(ind_2)) <= 25:
            ind_2.hideturtle()
            ind_2.setx(-500)
            ind_2.sety(500)
            del(ind_2)
            score_2 += 1
            hud_score.clear()
            hud_score.write("{} : {}".format(score_1, score_2), align="center", font=(
                            "Press Start 2P", 24, "normal"))


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
=======
    match.char_interplay()
>>>>>>> a528d2ee912b2a06fc42cfe5c51b3ea8325fad72
