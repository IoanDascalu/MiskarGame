import pygame


class GameFunctions(object):

    def __init__(self):
        pass

    def isCollision(self, object1, object2):
        # if object1.x +object1.vel < object2.x-object2.height:
        #     collideUp = False
        #     print("You will collide")
        collideUp = False
        collideDown = False
        collideLeft = False
        collideRight = False
        return collideUp, collideDown, collideLeft, collideRight
