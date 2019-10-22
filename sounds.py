# Som de vitória - https://freesound.org/people/rezyma/sounds/475148/
# Som de derrota - 
from os import system


def play_victory():
    system("aplay victory.wav")


def play_shot():
    system("aplay sounds/defeat.wav")