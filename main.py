import pygame
from pytmx import load_pygame
import random
import time

import GameFunctions
from Item import Item
from Mishkar import Mishkar
from Townie import Townie
from Beasts import Beasts

pygame.init()

screenWidth = 800
screenHeight = 800
win = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.display.set_caption("Mishkar The Germaphobe")

run = True
Mishkar = Mishkar(300, 300, 38, 60, GameFunctions.loadImages('MishkarBests/CharSprites/MishkarSprite'), win)
Fredrick = Townie(600, 400, 36, 58, GameFunctions.loadImages('MishkarBests/CharSprites/SheepMenSprites'), win)
Bucket = Item(500, 500, 32, 32, 'MishkarBests/GameSprites/bucket/WaterBucket.png', 'Bucket', win)
tmx_data = load_pygame("Maps/MishkarBG.tmx")

image = tmx_data.get_tile_image(0, 0, 0)


Mishkar.existance()


def redrawGameWindow():
    for layer in tmx_data.visible_layers:
        for x, y, gid, in layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
            if tile is not None:
                win.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
    Bucket.draw()
    Fredrick.draw()

    Mishkar.draw()
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

    Fredrick.movement()

    Mishkar.interact(Bucket, keys)
    if GameFunctions.isCollisionCollisionBox(Mishkar, Fredrick):
        Mishkar.voidDir = Mishkar.facing
    else:
        Mishkar.voidDir=''

    redrawGameWindow()

pygame.quit()
