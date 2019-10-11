import tank
import turtle

playing = True


def close_screen():
    global playing
    playing = not playing


def create_screen(title, width, height):
    screen = turtle.Screen()
    screen.title(title)
    screen.bgcolor('black')
    screen.setup(width=width, height=height)
    screen.tracer(100)
    return screen

screen = create_screen("ATARI COMBAT", 1000, 600)

screen.listen()
screen.onkeypress(tank.rotate_left_1, 'a')
screen.onkeypress(tank.rotate_right_1, 'd')
screen.onkeypress(tank.go_ahead_1, 'w')
screen.onkeypress(tank.rotate_left_2, 'Left')
screen.onkeypress(tank.rotate_right_2, 'Right')
screen.onkeypress(tank.go_ahead_2, 'Up')

root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

while playing:
    screen.update()
