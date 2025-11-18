import pygame
from pygame import mixer

def music():
    """This function runs the mechanics of the background music
    of the game. Uses pygame to do so. """
    pygame.init()
    mixer.init()
    mixer.music.load("music/music.mp3")
    mixer.music.play(-1)

