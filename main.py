import pygame
import random
import time
from Mishkar import Mishkar

pygame.init()

screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.display.set_caption("Miskar The Germaphobe")


def movement(keyPressed):
    if keyPressed[pygame.K_LEFT]:
        pass
    elif keyPressed[pygame.K_RIGHT]:
        pass

    elif keyPressed[pygame.K_DOWN]:
        pass

    elif keyPressed[pygame.K_UP]:
        print("up")
    pass


run = True
Mishkar=Mishkar(100, 100, 50, 50)

Mishkar.existance()


def redrawGameWindow():
    Mishkar.draw()

while run:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    movement(keys)

    

pygame.quit()
