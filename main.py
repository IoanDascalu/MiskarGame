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
Reiny = Beasts(600, 500, 50, 50, GameFunctions.loadImages('MishkarBests/CharSprites/GoldenReindeerSprites'), win)
Bucket = Item(500, 500, 32, 32, 'MishkarBests/GameSprites/bucket/WaterBucket.png', 'Bucket', win)
tmx_data = load_pygame("Maps/MishkarBG.tmx")

retryButton = GameFunctions.Button((255, 0, 0), 350, 600, 200, 50, "Retry")


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
    Reiny.draw()

    Mishkar.draw()

    #pygame.draw.rect(win, (255, 0, 0), (260, 150, 500, 430), 4)
    pygame.draw.rect(win, (255, 0, 0), (600, 700, 160, 30), 2)
    GAME_FONT.render_to(win, (640, 705), 'Health', (0, 0, 0))
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
                youLost = False

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

    boundary = GameFunctions.Rect(260, 150, 500, 430)

    Mishkar.interact(Bucket, keys)
    Mishkar.updateDir(keys)
    voidDirs1, voidDirs2 = GameFunctions.collisionToBeCollisionBox(Mishkar, Fredrick)
    voidDirs3 = GameFunctions.inBoundary(boundary, Mishkar)
    voidDirs4 = GameFunctions.inBoundary(boundary, Fredrick)
    voidDirs5 = GameFunctions.inBoundary(boundary, Reiny)
    for item in voidDirs3:
        voidDirs1.append(item)
    for item in voidDirs4:
        voidDirs2.append(item)
    spotted = GameFunctions.isTriangleCollision(Mishkar, Fredrick)

    if spotted:
        retryButton.visible = True
        youLost = True
    Mishkar.movement(keys, voidDirs1)
    Fredrick.movement(voidDirs2)
    Reiny.movement(voidDirs5)

    redrawGameWindow()

pygame.quit()
