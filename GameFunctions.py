import pygame
import os


def loadImages(path):
    a = os.listdir(path + '/Down')
    if '.DS_Store' in a:
        a.pop(a.index('.DS_Store'))
    a.sort()
    down = [path + '/Down/' + img for img in a]

    b = os.listdir(path + '/Up')
    if '.DS_Store' in b:
        b.pop(b.index('.DS_Store'))
    b.sort()
    up = [path + '/Up/' + img for img in b]

    c = os.listdir(path + '/Left')
    if '.DS_Store' in c:
        c.pop(c.index('.DS_Store'))
    c.sort()
    left = [path + '/Left/' + img for img in c]

    d = os.listdir(path + '/Right')
    if '.DS_Store' in d:
        d.pop(d.index('.DS_Store'))
    d.sort()
    right = [path + '/Right/' + img for img in d]

    return [down, up, left, right]


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_points(self):
        point1 = (self.x, self.y)
        point2 = (self.x + self.width, self.y)
        point3 = (self.x, self.y + self.height)
        point4 = (self.x + self.width, self.y + self.height)

        return [point1, point2, point3, point4]


def isCollision(object1, object2):
    '''
    Check for collision (Positional overlap) between two objects
    :param object1: Any object with spacial data that corresponds to x,y,w,h
    :param object2: Any object with spacial data that corresponds to x,y,w,h
    :return: Boolean if collision
    '''

    collision = False
    rect1 = Rect(object1.x, object1.y, object1.width, object1.height)
    rect2 = Rect(object2.x, object2.y, object2.width, object2.height)
    rp1 = rect1.get_points()
    rp2 = rect2.get_points()

    for i, point in enumerate(rp1):
        x1 = point[0]
        y1 = point[1]
        x2 = rp2[i][0]
        y2 = rp2[i][1]
        between_rect2x = rect2.x <= x1 <= rect2.x + rect2.width
        between_rect1x = rect1.x <= x2 <= rect1.x + rect1.width
        between_rect2y = rect2.y <= y1 <= rect2.y + rect2.height
        between_rect1y = rect1.y <= y2 <= rect1.y + rect1.height

        collision = (between_rect2x and between_rect2y) or \
                    (between_rect1x and between_rect1y)

        if collision is True:
            return collision

    return collision


def collisionToBe(object1, object2):
    ob1_has_vel = False
    ob2_has_vel = False
    try:
        object1.vel
        ob1_has_vel = True
    except:
        ob1_has_vel = False
    try:
        object2.vel
        ob2_has_vel = True
    except:
        ob2_has_vel = False
    if ob1_has_vel:
        rect2b1 = Rect(object1.x + object1.vel, object1.y + object1.vel,
                       object1.width, object1.height)
    else:
        rect2b1 = Rect(object1.x, object1.y,
                       object1.width, object1.height)
    if ob2_has_vel:
        rect2b2 = Rect(object2.x + object2.vel, object2.y + object2.vel,
                       object2.width, object2.height)
    else:
        rect2b2 = Rect(object2.x, object2.y,
                       object2.width, object2.height)
    return isCollision(rect2b1, rect2b2)
