import pygame
import random
import time

pygame.init()

screenWidth = 500
screenHeight = 500
win = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

pygame.display.set_caption("Miskar The Germaphobe")

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()