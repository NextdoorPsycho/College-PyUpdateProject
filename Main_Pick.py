import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
from Game import *

WINDOW_WIDTH = 470
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30
BACKGROUND_COLOR = (174, 198, 207)

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Some Very Generic Matching Game  --  Brian Fopiano')
pygame_icon = pygame.image.load('assets/Java.png')
bg_img = pygame.image.load('assets/bg.png')
bg_img = pygame.transform.scale(bg_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
audio = pygame.mixer.Sound('assets/music.mp3')
pygame.mixer.music.load('assets/music.mp3')

win = pygame.mixer.Sound('assets/win.mp3')
wrong = pygame.mixer.Sound('assets/wrong.mp3')
click = pygame.mixer.Sound('assets/click.mp3')
audio.play()
pygame.display.set_icon(pygame_icon)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

oGame = Game(window)

# Main code
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Let the game handle all events
        oGame.handleEvent(event)

    # Music

    # Draw background
    window.blit(bg_img, (0, 0))

    # Draw the game
    oGame.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)