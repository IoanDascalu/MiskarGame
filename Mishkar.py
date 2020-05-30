import pygame
class Mishkar(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = True
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        self.hitbox = (self.x, self.y - 2, 37, 55)
        self.walkCount = 0

    def existance(self):
        print("I exist")

    def draw(self, win):
        self.hitbox = (self.x, self.y - 2, 37, 55)
        pygame.draw.rect(win,(255,0,0), self.hitbox, 2)