import match
import sys
import turtle
import random

warzones = ['warzone1.txt', 'warzone2.txt',
            'warzone3.txt', 'warzone4.txt', 'warzone5.txt']

# criação da tela
screen = turtle.Screen()
screen.title('ATARI: COMBAT TANK')
screen.bgcolor('#5e9e4a')
screen.setup(width=800, height=600)
screen.tracer(100000)

# criação do cenário
match.create_zone(random.choice(warzones))

# mapeamento das teclas
screen.listen()
match.key_map(screen)

# fechamento da tela do jogo
root = screen.getcanvas().winfo_toplevel()
root.protocol('WM_DELETE_WINDOW', match.close_screen)

# início do jogo
while match.playing:
    screen.update()
    match.char_interplay()
