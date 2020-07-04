import pygame
import Item
import GameFunctions
from GameFunctions import Rect


class Mishkar(object):

    def __init__(self, x, y, width, height, listOfFigures, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = window
        self.health = 100
        self.vel = 5
        # self.inventory = Item.Item("MishkarBests/unicorn.png", "unicorn")
        self.collision_box = Rect(self.x+12, self.y+5, 38, 60)
        self.walkCount = 0
        self.facing = 'Down'
        self.currDir = 'Stand'
        self.downFig = [pygame.image.load(img) for img in listOfFigures[0]]
        self.upFig = [pygame.image.load(img) for img in listOfFigures[1]]
        self.leftFig = [pygame.image.load(img) for img in listOfFigures[2]]
        self.rightFig = [pygame.image.load(img) for img in listOfFigures[3]]
        self.health = 100

    def existance(self):
        print("I exist")

    def inventory(self):
        pass

    def draw(self):
        if self.walkCount + 1 >= 18:
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


        self.collision_box = Rect(self.x+12, self.y+5, 38, 60)
        hit_box = self.collision_box.get_rect()
        # pygame.draw.rect(self.win, (255, 0, 0), hit_box, 2)

    def movement(self, keyPressed, voidDirections):

        if keyPressed[pygame.K_LEFT] and 'Left' not in voidDirections:
            self.currDir = 'Left'
            self.facing = 'Left'
            self.x -= self.vel

        elif keyPressed[pygame.K_RIGHT] and 'Right' not in voidDirections:
            self.currDir = 'Right'
            self.facing = 'Right'
            self.x += self.vel

        elif keyPressed[pygame.K_UP] and 'Up' not in voidDirections:
            self.currDir = 'Up'
            self.facing = 'Up'
            self.y -= self.vel

        elif keyPressed[pygame.K_DOWN] and "Down" not in voidDirections:
            self.currDir = 'Down'
            self.facing = 'Down'
            self.y += self.vel

        else:
            self.currDir = 'Stand'

    def interact(self, object, keyPressed):
        if GameFunctions.isCollisionCollisionBox(self, object):
            if keyPressed[pygame.K_x]:
                object.pickUpItem()

        else:
            if keyPressed[pygame.K_z] and object.inInventory:
                object.dropItem(self.getCollisionBox().x, self.collision_box.y)

    def getCollisionBox(self):
        return self.collision_box

    def updateDir(self, keyPressed):
        if keyPressed[pygame.K_LEFT]:
            self.currDir = 'Left'
        elif keyPressed[pygame.K_RIGHT]:
            self.currDir = 'Right'
        elif keyPressed[pygame.K_UP]:
            self.currDir = 'Up'
        elif keyPressed[pygame.K_DOWN]:
            self.currDir = 'Down'
