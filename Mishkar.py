import pygame
import Item


class Mishkar(object):

    def __init__(self, x, y, width, height, window):
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
        self.collisionbox = (self.x, self.y - 2, 37, 55)

    def existance(self):
        print("I exist")

    def inventory(self):
        pass

    def draw(self):
        self.collisionbox = (self.x, self.y - 2, 37, 55)
        pygame.draw.rect(self.win, (255, 0, 0), self.collisionbox, 2)

    def movement(self, keyPressed):

        if keyPressed[pygame.K_LEFT]:
            self.x -= self.vel
        elif keyPressed[pygame.K_RIGHT]:
            self.x += self.vel

        elif keyPressed[pygame.K_DOWN]:
            self.y += self.vel

        elif keyPressed[pygame.K_UP]:
            self.y -= self.vel

    def interact(self):
        pass
