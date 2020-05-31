import pygame
import Item


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
        self.left = True
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.walkCount = 0
        self.collisionbox = (self.x, self.y - 2, 37, 55)
        print(listOfFigures[1])
        self.downFig = [pygame.image.load(img) for img in listOfFigures[0]]
        self.upFig = [pygame.image.load(img) for img in listOfFigures[1]]
        self.leftFig = [pygame.image.load(img) for img in listOfFigures[2]]
        self.rightFig = [pygame.image.load(img) for img in listOfFigures[3]]

    def existance(self):
        print("I exist")


    def inventory(self):
        pass

    def draw(self):
        if self.walkCount + 1 >= 60:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                self.win.blit(self.leftFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                self.win.blit(self.rightFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                self.win.blit(self.upFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                self.win.blit(self.downFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
        # else:
        elif self.standing:
            if self.left:
                self.win.blit(self.leftFig[0], (self.x, self.y))
            if self.right:
                self.win.blit(self.rightFig[0], (self.x, self.y))
            if self.up:
                self.win.blit(self.upFig[0], (self.x, self.y))
            if self.down:
                self.win.blit(self.downFig[0], (self.x, self.y))

        else:
            if self.left:
                self.win.blit(self.leftFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                self.win.blit(self.rightFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                self.win.blit(self.upFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                self.win.blit(self.downFig[self.walkCount // len(self.leftFig)], (self.x, self.y))
                self.walkCount += 1
        self.collisionbox = (self.x, self.y - 2, 37, 55)
        pygame.draw.rect(self.win, (255, 0, 0), self.collisionbox, 2)

    def movement(self, keyPressed):

        if keyPressed[pygame.K_LEFT]:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.up = False
            self.down = False
            self.standing = False
        elif keyPressed[pygame.K_RIGHT]:
            self.x += self.vel
            self.left = False
            self.right = True
            self.up = False
            self.down = False
            self.standing = False
        elif keyPressed[pygame.K_DOWN]:
            self.y += self.vel
            self.left = False
            self.right = False
            self.up = False
            self.down = True
            self.standing = False
        elif keyPressed[pygame.K_UP]:
            self.y -= self.vel
            self.left = False
            self.right = False
            self.up = True
            self.down = False
            self.standing = False
        else:
            self.standing = True


    def interact(self):
        pass
