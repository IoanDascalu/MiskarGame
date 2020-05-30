import pygame


class Beasts(object):

    def __init__(self,  x, y, width, height, beastspnglist, beastsname, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.win = window
        self.beastspnglist = beastspnglist
        self.beastsname = beastsname
        self.inInventory = False
        for i in range(len(self.beastspnglist)):
            pygame.image.load(self.beastspnglist(i))

    def draw(self):
        pass