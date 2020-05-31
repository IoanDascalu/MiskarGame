import pygame

from GameFunctions import Rect


class Item(object):

    def __init__(self,  x, y, width, height, imagepng, itemname, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = window
        self.imagepng = imagepng
        self.itemname = itemname
        self.collision_box = Rect(self.x + 12, self.y + 5, 38, 60)
        self.inInventory = False
        self.image = pygame.image.load(imagepng)

    def pickUpItem(self):
        self.inInventory = True

    def dropItem(self, MishkarX, MishkarY):
        self.x = MishkarX + 5
        self.y = MishkarY - 5
        self.inInventory = False

    def draw(self):
        if self.inInventory:
            self.x = 380
            self.y = 700
        self.win.blit(self.image, (self.x, self.y))
        self.collision_box = Rect(self.x, self.y, 32, 32)
        hit_box = self.collision_box.get_rect()
        # pygame.draw.rect(self.win, (255, 0, 0), hit_box, 2)


    def getCollisionBox(self):
        return self.collision_box

