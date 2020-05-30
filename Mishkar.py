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
        # self.inventory = Item.Item("MishkarBests/unicorn.png", "unicorn")
        self.left = True
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.hitbox = (self.x, self.y - 2, 37, 55)

    def existance(self):
        print("I exist")

    def inventory(self):
        pass

    def draw(self):
        self.hitbox = (self.x, self.y - 2, 37, 55)
        pygame.draw.rect(self.win, (255, 0, 0), self.hitbox, 2)

    def movement(self):
        pass

    def interact(self):
        pass