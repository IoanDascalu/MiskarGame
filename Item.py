import pygame


class Item(object):

    def __init__(self,  x, y, width, height, imagepng, itemname, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = window
        self.imagepng = imagepng
        self.itemname = itemname
        self.inInventory = False
        self.image = pygame.image.load(imagepng)

    def pickUpItem(self):
        self.inInventory = True

    def dropItem(self):
        self.inInventory = False

    def draw(self):
        self.win.blit(self.image, (self.x, self.y))

