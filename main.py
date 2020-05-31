import pygame
from pytmx import load_pygame
import random
import time

import GameFunctions
from Item import Item
from Mishkar import Mishkar
from Beasts import Beasts

pygame.init()

screenWidth = 800
screenHeight = 800
win = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.display.set_caption("Mishkar The Germaphobe")

run = True
Mishkar = Mishkar(100, 100, 50, 50, GameFunctions.loadImages('MishkarBests/CharSprites/MishkarSprite'), win)
# Apple = Item(100, 300, 512, 256, "MishkarBests/unicorn.png", "apple", win)
tmx_data = load_pygame("Maps/MishkarBG.tmx")

image = tmx_data.get_tile_image(0, 0, 0)


Mishkar.existance()


def redrawGameWindow():
    for layer in tmx_data.visible_layers:
        for x, y, gid, in layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
            if tile is not None:
                win.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
    Mishkar.draw()
    # Apple.draw()
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
