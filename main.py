import pygame
import random
import time

from Item import Item
from Mishkar import Mishkar
from Beasts import Beasts

pygame.init()

screenWidth = 700
screenHeight = 700
win = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.display.set_caption("Mishkar The Germaphobe")

run = True
Mishkar = Mishkar(100, 100, 50, 50, win)
Apple = Item(100, 300, 512, 256, "MishkarBests/unicorn.png", "apple", win)


Mishkar.existance()


def redrawGameWindow():
    Mishkar.draw()
    Apple.draw()
    pygame.display.update()

while run:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    Mishkar.movement(keys)

    redrawGameWindow()



pygame.quit()
