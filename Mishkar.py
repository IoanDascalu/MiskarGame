import pygame
import Item
from GameFunctions import Rect


class Mishkar(object):

    def __init__(self, x, y, width, height, listOfFigures, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = window
        self.health = 100
        self.vel=5
        # self.inventory = Item.Item("MishkarBests/unicorn.png", "unicorn")
        self.facing = 'Down'
        self.currDir = 'Stand'
        self.walkCount = 0
        self.collision_box = (self.x, self.y - 2, 37, 55)
        self.downFig = [pygame.image.load(img) for img in listOfFigures[0]]
        self.upFig = [pygame.image.load(img) for img in listOfFigures[1]]
        self.leftFig = [pygame.image.load(img) for img in listOfFigures[2]]
        self.rightFig = [pygame.image.load(img) for img in listOfFigures[3]]

    def existance(self):
        print("I exist")

    def inventory(self):
        pass

    def draw(self):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.currDir is not 'Stand':
            if self.currDir is 'Left':
                self.win.blit(self.leftFig[self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Right':
                self.win.blit(self.rightFig[self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Up':
                self.win.blit(self.upFig[self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Down':
                self.win.blit(self.downFig[self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1
        # else:
        elif self.currDir is 'Stand':
            if self.facing is 'Left':
                self.win.blit(self.leftFig[0], (self.x, self.y))
            if self.facing is 'Right':
                self.win.blit(self.rightFig[0], (self.x, self.y))
            if self.facing is 'Up':
                self.win.blit(self.upFig[0], (self.x, self.y))
            if self.facing is 'Down':
                self.win.blit(self.downFig[0], (self.x, self.y))

        else:
            if self.currDir is 'Left':
                self.win.blit(self.leftFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Right':
                self.win.blit(self.rightFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Up':
                self.win.blit(self.upFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Down':
                self.win.blit(self.downFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
        self.collision_box = (self.x, self.y - 2, 37, 55)
        pygame.draw.rect(self.win, (255, 0, 0), self.collision_box, 2)

    def movement(self, keyPressed):

        if keyPressed[pygame.K_LEFT]:
            self.x -= self.vel
            self.currDir = 'Left'
            self.facing = 'Left'

        elif keyPressed[pygame.K_RIGHT]:
            self.x += self.vel
            self.currDir = 'Right'
            self.facing = 'Right'

        elif keyPressed[pygame.K_UP]:
            self.y -= self.vel
            self.currDir = 'Up'
            self.facing = 'Up'

        elif keyPressed[pygame.K_DOWN]:
            self.y += self.vel
            self.currDir = 'Down'
            self.facing = 'Down'

        else:
            self.currDir = 'Stand'

    def interact(self):
        pass
