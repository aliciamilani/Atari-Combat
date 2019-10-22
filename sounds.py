# Som de vitória - https://freesound.org/people/rezyma/sounds/475148/

from os import system


def play_victory():
    system("aplay sounds/victory.wav")


def play_shot():
    system("aplay sounds/shot.wav")
