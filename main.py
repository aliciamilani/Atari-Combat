from support import draw
import tank
import turtle

playing = True


def close_screen():
    global playing
    playing = not playing


def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor('#5e9e4a')
    screen.setup(width=width, height=height)
    screen.tracer(100000)
    return screen


screen = create_screen('ATARI COMBAT', 1000, 600)

screen.listen()
screen.onkeypress(tank.rotate_left_1, 'a')
screen.onkeypress(tank.rotate_right_1, 'd')
screen.onkeypress(tank.go_ahead_1, 'w')
screen.onkeypress(tank.rotate_left_2, 'Left')
screen.onkeypress(tank.rotate_right_2, 'Right')
screen.onkeypress(tank.go_ahead_2, 'Up')

root = screen.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW', close_screen)


# lendo txt para gerar o labirinto
field = open('field.txt', 'r')

# matriz dos blocos para verificar a colisão deles com os tanques
wall_list = []

y = 275
# percorrendo cada linha do txt
for line in field:
    x = -390
    # percorrendo cada item da linha
    for one in line:
        # verificando se é 1, ou seja, se é um bloco
        if (one == '1'):
            wall = draw('square', 1, '#ffe2b0', x, y)
            wall_list.append(wall)
        x += 8.3
    y -= 16.3


while playing:
    screen.update()
    # colisão dos tanques com as paredes
    for num in range(len(wall_list)):
        if tank.one.distance(wall_list[num]) <= 25:
            tank.one.forward(-7)
        if tank.two.distance(wall_list[num]) <= 25:
            tank.two.forward(-7)
