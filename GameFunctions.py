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

    def get_rect(self):
        return [self.x, self.y, self.width, self.height]

class Triangle:
    def __init__(self, x, y, width, height, currDir):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.currDir = currDir

    def get_points(self):
        point1 = (self.x, self.y)
        if self.currDir is "Up":
            point2 = (self.x - self.width/2, self.y - self.height)
            point3 = (self.x + self.width/2, self.y - self.height)
        if self.currDir is "Down":
            point2 = (self.x + self.width/2, self.y + self.height)
            point3 = (self.x - self.width/2, self.y + self.height)
        if self.currDir is "Left":
            point2 = (self.x - self.height, self.y + self.width/2)
            point3 = (self.x - self.height, self.y - self.width/2)
        if self.currDir is "Right":
            point2 = (self.x + self.height, self.y - self.width/2)
            point3 = (self.x + self.height, self.y + self.width/2)

        return [point1, point2, point3]

    def get_triangle(self):
        return [self.x, self.y, self.width, self.height]


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
        if object2.currDir is "Up":
            rect2b1 = Rect(object1.x, object1.y - object1.vel,
                           object1.width, object1.height)
        if object2.currDir is "Down":
            rect2b1 = Rect(object1.x, object1.y + object1.vel,
                           object1.width, object1.height)
        if object2.currDir is "Left":
            rect2b1 = Rect(object1.x - object1.vel, object1.y,
                           object1.width, object1.height)
        if object2.currDir is "Right":
            rect2b1 = Rect(object1.x - object1.vel, object1.y,
                           object1.width, object1.height)

    else:
        rect2b1 = Rect(object1.x, object1.y,
                       object1.width, object1.height)
    if ob2_has_vel:
        if object2.currDir is "Up":
            rect2b1 = Rect(object1.x, object1.y - object1.vel,
                           object1.width, object1.height)
        if object2.currDir is "Down":
            rect2b1 = Rect(object1.x, object1.y + object1.vel,
                           object1.width, object1.height)
        if object2.currDir is "Left":
            rect2b1 = Rect(object1.x - object1.vel, object1.y,
                           object1.width, object1.height)
        if object2.currDir is "Right":
            rect2b1 = Rect(object1.x - object1.vel, object1.y,
                           object1.width, object1.height)
    else:
        rect2b2 = Rect(object2.x, object2.y,
                       object2.width, object2.height)
    return isCollision(rect2b1, rect2b2)

def isTriangleCollision(object1, object2):
    '''
    checks if Mishkar has made contact with any triangular objects
    :param object1: Mishkar
    :param object2: a triangle
    :return:
    '''

    hitbox = object1 #.collision_box
    hitbox_points = hitbox.get_points()
    tri_points = object2.get_points()
    for point in hitbox_points:
        x = point[0]
        y = point[1]
        line1_slope = (tri_points[1][1]-tri_points[0][1])/\
                      (tri_points[1][0]-tri_points[0][0])
        line2_slope = (tri_points[2][1]-tri_points[0][1])/\
                      (tri_points[2][0]-tri_points[0][0])

        if object2.currDir is "Up":
            if tri_points[1][1] <= y <= tri_points[0][1]:
                x_min = (y - tri_points[0][1])/line1_slope + tri_points[0][0]
                x_max = (y - tri_points[0][1])/line2_slope + tri_points[0][0]
                if x_min <= x <= x_max:
                    return True
            for tri_point in tri_points:
                if object1.x <= tri_point[0] <= object1.x + object1.width and \
                        object1.y <= tri_point[1] <= object1.y + object1.height:
                    return True

        if object2.currDir is "Down":
            if tri_points[0][1] <= y <= tri_points[1][1]:
                x_max = (y - tri_points[0][1]) / line1_slope + tri_points[0][0]
                x_min = (y - tri_points[0][1]) / line2_slope + tri_points[0][0]
                if x_min <= x <= x_max:
                    return True
            for tri_point in tri_points:
                if object1.x <= tri_point[0] <= object1.x + object1.width and \
                        object1.y <= tri_point[1] <= object1.y + object1.height:
                    return True

        if object2.currDir is "Left":
            if tri_points[1][0] <= x <= tri_points[0][0]:
                y_min = (x - tri_points[0][0]) * line1_slope + tri_points[0][1]
                y_max = (x - tri_points[0][0]) * line2_slope + tri_points[0][1]
                if y_min <= x <= y_max:
                    return True
            for tri_point in tri_points:
                if object1.x <= tri_point[0] <= object1.x + object1.width and \
                        object1.y <= tri_point[1] <= object1.y + object1.height:
                    return True

        if object2.currDir is "Right":
            if tri_points[0][0] <= x <= tri_points[1][0]:
                y_max = (x - tri_points[0][0]) * line1_slope + tri_points[0][1]
                y_min = (x - tri_points[0][0]) * line2_slope + tri_points[0][1]
                if y_min <= x <= y_max:
                    return True
            for tri_point in tri_points:
                if object1.x <= tri_point[0] <= object1.x + object1.width and \
                        object1.y <= tri_point[1] <= object1.y + object1.height:
                    return True

    return False
