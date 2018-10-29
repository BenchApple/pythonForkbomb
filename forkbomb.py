import os
import pygame

def main():
    pygame.mixer.init()
    song = Sound("Curb_Your_Enthusiasm_theme_song.mp3")
    song.play()
    executeFork()
    song.fadeout(15000)


def executeFork():
    while True:
        os.fork

if __name__ == "__main__":
    main()