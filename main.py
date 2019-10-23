import match
import sys
import turtle
import bullet

# criação da tela
screen = turtle.Screen()
screen.title('ATARI: COMBAT TANK')
screen.bgcolor('#5e9e4a')
screen.setup(width=900, height=600)
screen.tracer(100000)

# criação do cenário
match.create_zone('zones/'+sys.argv[1])

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
