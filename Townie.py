import pygame
import Item
import random
from GameFunctions import Triangle
import pygame
import Item
from GameFunctions import Rect


class Townie(object):

    def __init__(self, x, y, width, height, listOfFigures, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = window
        self.vel = 3
        self.collision_box = Rect(self.x+30, self.y+5, 38, 60)
        self.walkCount = 0
        self.facing = 'Down'
        self.currDir = 'Stand'
        self.voidDir = ''
        self.downFig = [pygame.image.load(img) for img in listOfFigures[0]]
        self.upFig = [pygame.image.load(img) for img in listOfFigures[1]]
        self.leftFig = [pygame.image.load(img) for img in listOfFigures[2]]
        self.rightFig = [pygame.image.load(img) for img in listOfFigures[3]]
        self.stepCount = 0
        self.triangle_offset = (23,18)
        self.triangle = Triangle(self.x + self.triangle_offset[0], self.y + self.triangle_offset[0], 30, 200, self.facing)

    def draw(self):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        if self.currDir is not 'Stand':
            if self.currDir is 'Left':
                self.win.blit(self.leftFig[self.walkCount // 10], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Right':
                self.win.blit(self.rightFig[self.walkCount // 10], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Up':
                self.win.blit(self.upFig[self.walkCount // 10], (self.x, self.y))
                self.walkCount += 1
            elif self.currDir is 'Down':
                self.win.blit(self.downFig[self.walkCount // 10], (self.x, self.y))
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

        self.collision_box = Rect(self.x+5, self.y+10, 36, 58)
        hit_box = self.collision_box.get_rect()
        pygame.draw.polygon(self.win, (255, 255, 255), self.triangle.get_points(), 0)
        # pygame.draw.rect(self.win, (255, 0, 0), hit_box, 2)

    def movement(self):

        if self.stepCount != 0:
            # if not GameFunctions.collisionToBe(self, Mishkar)
            pass
        else:
            self.stepCount = random.randrange(30, 50)
            ranDir = random.randrange(0,5)
            possibleDir = ['Left', 'Right', 'Up', 'Down', 'Stand']
            self.currDir = possibleDir[ranDir]

        if self.currDir is 'Left' and self.voidDir is not 'Left':
            self.stepCount -= 1
            self.x -= self.vel
            self.facing = 'Left'
            self.triangle.movement_update(self.x + self.triangle_offset[0], self.y + self.triangle_offset[1],
                                          self.facing)

        elif self.currDir is 'Right' and self.voidDir is not 'Right':
            self.stepCount -= 1
            self.x += self.vel
            self.facing = 'Right'
            self.triangle.movement_update(self.x + self.triangle_offset[0], self.y + self.triangle_offset[1],
                                          self.facing)
        elif self.currDir is 'Up' and self.voidDir is not 'Up':
            self.stepCount -= 1
            self.y -= self.vel
            self.facing = 'Up'
            self.triangle.movement_update(self.x + self.triangle_offset[0], self.y + self.triangle_offset[1],
                                          self.facing)
        elif self.currDir is 'Down' and self.voidDir is not 'Down':
            self.stepCount -= 1
            self.y += self.vel
            self.facing = 'Down'
            self.triangle.movement_update(self.x + self.triangle_offset[0], self.y + self.triangle_offset[1],
                                          self.facing)
        else:
            self.stepCount -= 1
            self.currDir = 'Stand'
            self.triangle.movement_update(self.x + self.triangle_offset[0], self.y + self.triangle_offset[1],
                                          self.facing)
    def getCollisionBox(self):
        return self.collision_box
