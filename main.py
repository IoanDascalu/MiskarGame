import pygame
from pytmx import load_pygame
import random
import time

import GameFunctions
from Item import Item
from Mishkar import Mishkar
from Townie import Townie
from Beasts import Beasts
import pygame.freetype

pygame.init()
pygame.freetype.init()
GAME_FONT = pygame.freetype.SysFont(pygame.font.get_default_font(), 30)

screenWidth = 800
screenHeight = 800
win = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.display.set_caption("Mishkar The Germaphobe")

run = True
youLost = False
Mishkar = Mishkar(300, 300, 38, 60, GameFunctions.loadImages('MishkarBests/CharSprites/MishkarSprite'), win)
Fredrick = Townie(400, 400, 36, 58, GameFunctions.loadImages('MishkarBests/CharSprites/SheepMenSprites'), win)
Bucket = Item(500, 500, 32, 32, 'MishkarBests/GameSprites/bucket/WaterBucket.png', 'Bucket', win)
tmx_data = load_pygame("Maps/MishkarBG.tmx")


# def loadLevel(levelInt):
#     if levelInt is 1:
#         mishkar = Mishkar(300, 300, 38, 60, GameFunctions.loadImages('MishkarBests/CharSprites/MishkarSprite'), win)
#         Fredrick = Townie(400, 400, 36, 58, GameFunctions.loadImages('MishkarBests/CharSprites/SheepMenSprites'), win)
#         Bucket = Item(500, 500, 32, 32, 'MishkarBests/GameSprites/bucket/WaterBucket.png', 'Bucket', win)
#         tmx_data = load_pygame("Maps/MishkarBG.tmx")
#     elif levelInt is 2:
#         mishkar = Mishkar(600, 600, 38, 60, GameFunctions.loadImages('MishkarBests/CharSprites/MishkarSprite'), win)
#         Fredrick = Townie(400, 400, 36, 58, GameFunctions.loadImages('MishkarBests/CharSprites/SheepMenSprites'), win)
#         Bucket = Item(500, 500, 32, 32, 'MishkarBests/GameSprites/bucket/WaterBucket.png', 'Bucket', win)
#         tmx_data = load_pygame("Maps/MishkarBG.tmx")
#     else:
#         mishkar = Mishkar(300, 300, 38, 60, GameFunctions.loadImages('MishkarBests/CharSprites/MishkarSprite'), win)
#         Fredrick = Townie(400, 400, 36, 58, GameFunctions.loadImages('MishkarBests/CharSprites/SheepMenSprites'), win)
#         Bucket = Item(500, 500, 32, 32, 'MishkarBests/GameSprites/bucket/WaterBucket.png', 'Bucket', win)
#         tmx_data = load_pygame("Maps/MishkarBG.tmx")
#     return mishkar, Fredrick, Bucket, tmx_data
#
#
# Mishkar, Fredrick, Bucket, tmx_data = loadLevel(1)

retryButton = GameFunctions.button((255, 0, 0), 350, 600, 200, 50, "Retry")


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
    retryButton.draw(win, (0, 0, 0))
    if youLost:
        GAME_FONT.render_to(win, (40, 350), 'YOU LOST', (255, 0, 0))

    pygame.display.update()


while run:
    clock.tick(60)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if retryButton.isOver(pos) and retryButton.visible:
                retryButton.visible = False

        if event.type == pygame.MOUSEMOTION:
            if retryButton.isOver(pos) and retryButton.visible:
                retryButton.color = (230, 25, 0)
            else:
                retryButton.color = (255, 0, 0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    if youLost:
        pass
        #pygame.time.wait(1000)

    Mishkar.interact(Bucket, keys)
    Mishkar.updateDir(keys)
    collision = GameFunctions.collisionToBeCollisionBox(Mishkar, Fredrick)
    spotted = GameFunctions.isTriangleCollision(Mishkar.getCollisionBox(), Fredrick)

    if collision:
        Mishkar.voidDir = Mishkar.facing
        Fredrick.voidDir = Fredrick.facing
    else:
        Mishkar.voidDir = ''
        Fredrick.voidDir = ''
    if spotted:
        retryButton.visible = True
        youLost = True
        print("hit...")
    Mishkar.movement(keys)
    Fredrick.movement()

    redrawGameWindow()

pygame.quit()
