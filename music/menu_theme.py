import pygame
import os

pygame.mixer.init()

def play_music(filename):
    filepath = os.path.join("music", filename)
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(-1)