import pygame


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def isCollision(object1, object2):
    '''
    Check for collision (Positional overlap) between two objects
    :param object1: Any object with spacial data that corresponds to x,y,w,h
    :param object2: Any object with spacial data that corresponds to x,y,w,h
    :return: Boolean if collision
    '''

    collision = False
    rect1 = []
    rect2 = []
    rect1.append((object1.x, object1.y))
    rect1.append((object1.x + object1.width, object1.y))
    rect1.append((object1.x, object1.y + object1.height))
    rect1.append((object1.x + object1.width, object1.y + object1.height))

    rect2.append((object2.x, object2.y))
    rect2.append((object2.x + object2.width, object2.y))
    rect2.append((object2.x, object2.y + object2.height))
    rect2.append((object2.x + object2.width, object2.y + object2.height))

    for point in rect1:
        x = point[0]
        y = point[1]
        between_rect2x = object2.x <= x <= object2.x + object2.width
        between_rect2y = object2.y <= y <= object2.y + object2.height

        collision = between_rect2x and between_rect2y
        if collision is True:
            return collision
    for point in rect2:
        x = point[0]
        y = point[1]
        between_rect1x = object1.x <= x <= object1.x + object1.width
        between_rect1y = object1.y <= y <= object1.y + object1.height

        collision = between_rect1x and between_rect1y
        if collision is True:
            return collision

    return collision

def collisionToBe(object1, object2):
    return
