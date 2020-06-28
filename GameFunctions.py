import pygame
from pygame import Rect
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


class Triangle:
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing

    def get_points(self):
        point1 = (self.x, self.y)
        if self.facing is "Up":
            point2 = (self.x - self.width / 2, self.y - self.height)
            point3 = (self.x + self.width / 2, self.y - self.height)
        if self.facing is "Down":
            point2 = (self.x + self.width / 2, self.y + self.height)
            point3 = (self.x - self.width / 2, self.y + self.height)
        if self.facing is "Left":
            point2 = (self.x - self.height, self.y + self.width / 2)
            point3 = (self.x - self.height, self.y - self.width / 2)
        if self.facing is "Right":
            point2 = (self.x + self.height, self.y - self.width / 2)
            point3 = (self.x + self.height, self.y + self.width / 2)

        return [point1, point2, point3]

    def get_triangle(self):
        return [self.x, self.y, self.width, self.height]

    def movement_update(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing


def isCollision(object1, object2):
    '''
    Check for collision (Positional overlap) between two objects
    :param object1: Any object with spacial data that corresponds to x,y,w,h
    :param object2: Any object with spacial data that corresponds to x,y,w,h
    :return: Boolean if collision
    '''
    rect1 = Rect(object1.x, object1.y, object1.width, object1.height)
    rect2 = Rect(object2.x, object2.y, object2.width, object2.height)

    collision = rect1.colliderect(rect2)

    return collision


def isCollisionCollisionBox(object1, object2):
    '''
    Check for collision (Positional overlap) between two objects
    :param object1: Any object with spacial data that corresponds to x,y,w,h
    :param object2: Any object with spacial data that corresponds to x,y,w,h
    :return: Boolean if collision
    '''

    rect1 = Rect(object1.getCollisionBox().x, object1.getCollisionBox().y, object1.getCollisionBox().width,
                 object1.getCollisionBox().height)
    rect2 = Rect(object2.getCollisionBox().x, object2.getCollisionBox().y, object2.getCollisionBox().width,
                 object2.getCollisionBox().height)

    collision = rect1.colliderect(rect2)


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
            rect2b1 = Rect(object1.x, object1.y,
                           object1.width, object1.height + object1.vel)
        if object2.currDir is "Left":
            rect2b1 = Rect(object1.x - object1.vel, object1.y,
                           object1.width, object1.height)
        if object2.currDir is "Right":
            rect2b1 = Rect(object1.x, object1.y,
                           object1.width + object1.vel, object1.height)

    else:
        rect2b1 = Rect(object1.x, object1.y,
                       object1.width, object1.height)
    if ob2_has_vel:
        if object2.currDir is "Up":
            rect2b2 = Rect(object2.x, object2.y - object2.vel,
                           object2.width, object2.height)
        if object2.currDir is "Down":
            rect2b2 = Rect(object2.x, object2.y,
                           object2.width, object2.height + object2.vel)
        if object2.currDir is "Left":
            rect2b2 = Rect(object2.x - object2.vel, object2.y,
                           object2.width, object2.height)
        if object2.currDir is "Right":
            rect2b2 = Rect(object2.x, object2.y,
                           object2.width + object2.vel, object2.height)
    else:
        rect2b2 = Rect(object2.x, object2.y,
                       object2.width, object2.height)
    return isCollision(rect2b1, rect2b2)


def collisionToBeCollisionBox(object1, object2):
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
    if ob1_has_vel and object1.currDir is not "Stand":
        if object1.currDir is "Up":
            rect2b1 = Rect(object1.getCollisionBox().x, object1.getCollisionBox().y - object1.vel,
                           object1.getCollisionBox().width, object1.getCollisionBox().height)
        if object1.currDir is "Down":
            rect2b1 = Rect(object1.getCollisionBox().x, object1.getCollisionBox().y,
                           object1.getCollisionBox().width, object1.getCollisionBox().height + object1.vel)
        if object1.currDir is "Left":
            rect2b1 = Rect(object1.getCollisionBox().x - object1.vel, object1.getCollisionBox().y,
                           object1.getCollisionBox().width, object1.getCollisionBox().height)
        if object1.currDir is "Right":
            rect2b1 = Rect(object1.getCollisionBox().x, object1.getCollisionBox().y,
                           object1.getCollisionBox().width + object1.vel, object1.getCollisionBox().height)

    else:
        rect2b1 = Rect(object1.getCollisionBox().x, object1.getCollisionBox().y,
                       object1.getCollisionBox().width, object1.getCollisionBox().height)
    if ob2_has_vel and object2.currDir is not "Stand":
        if object2.currDir is "Up":
            rect2b2 = Rect(object2.getCollisionBox().x, object2.getCollisionBox().y - object2.vel,
                           object2.getCollisionBox().width, object2.getCollisionBox().height)
        if object2.currDir is "Down":
            rect2b2 = Rect(object2.getCollisionBox().x, object2.getCollisionBox().y,
                           object2.getCollisionBox().width, object2.getCollisionBox().height + object2.vel)
        if object2.currDir is "Left":
            rect2b2 = Rect(object2.getCollisionBox().x - object2.vel, object2.getCollisionBox().y,
                           object2.getCollisionBox().width, object2.getCollisionBox().height)
        if object2.currDir is "Right":
            rect2b2 = Rect(object2.getCollisionBox().x, object2.getCollisionBox().y,
                           object2.getCollisionBox().width + object2.vel, object2.getCollisionBox().height)

    else:
        rect2b2 = Rect(object2.getCollisionBox().x, object2.getCollisionBox().y,
                       object2.getCollisionBox().width, object2.getCollisionBox().height)
    # pygame.draw.rect(object1.win, (255, 0, 0), rect2b1.get_rect(), 0)
    # pygame.draw.rect(object2.win, (255, 0, 0), rect2b2.get_rect(), 0)
    # pygame.display.update()

    # object1.collision_box = rect2b1
    return isCollision(rect2b1, rect2b2)


def isTriangleCollision(object1, object2):
    '''
    checks if Mishkar has made contact with any triangular objects
    :param object1: Mishkar
    :param object2: a triangle
    :return:
    '''

    hitbox = object1  # .collision_box
    hitbox_points = hitbox.get_points()
    tri_points = object2.get_points()
    for point in hitbox_points:
        x = point[0]
        y = point[1]
        line1_slope = (tri_points[1][1] - tri_points[0][1]) / \
                      (tri_points[1][0] - tri_points[0][0])
        line2_slope = (tri_points[2][1] - tri_points[0][1]) / \
                      (tri_points[2][0] - tri_points[0][0])

        if object2.currDir is "Up":
            if tri_points[1][1] <= y <= tri_points[0][1]:
                x_min = (y - tri_points[0][1]) / line1_slope + tri_points[0][0]
                x_max = (y - tri_points[0][1]) / line2_slope + tri_points[0][0]
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


def isTriangleCollision(object1, object2):
    '''
    checks if Mishkar has made contact with any triangular objects
    :param object1: Mishkar
    :param object2: a triangle
    :return:
    '''
    # hitbox = object1  # .collision_box
    # hitbox_points = hitbox.get_points()
    # tri_points = object2.triangle.get_points()
    # for point in hitbox_points:
    #     x = point[0]
    #     y = point[1]
    #     line1_slope = (tri_points[1][1] - tri_points[0][1]) / \
    #                   (tri_points[1][0] - tri_points[0][0])
    #     line2_slope = (tri_points[2][1] - tri_points[0][1]) / \
    #                   (tri_points[2][0] - tri_points[0][0])
    #
    #     if object2.currDir is "Up":
    #         if tri_points[1][1] <= y <= tri_points[0][1]:
    #             x_min = (y - tri_points[0][1]) / line1_slope + tri_points[0][0]
    #             x_max = (y - tri_points[0][1]) / line2_slope + tri_points[0][0]
    #             if x_min <= x <= x_max:
    #                 return True
    #         for tri_point in tri_points:
    #             if object1.x <= tri_point[0] <= object1.x + object1.width and \
    #                     object1.y <= tri_point[1] <= object1.y + object1.height:
    #                 return True
    #
    #     if object2.currDir is "Down":
    #         if tri_points[0][1] <= y <= tri_points[1][1]:
    #             x_max = (y - tri_points[0][1]) / line1_slope + tri_points[0][0]
    #             x_min = (y - tri_points[0][1]) / line2_slope + tri_points[0][0]
    #             if x_min <= x <= x_max:
    #                 return True
    #         for tri_point in tri_points:
    #             if object1.x <= tri_point[0] <= object1.x + object1.width and \
    #                     object1.y <= tri_point[1] <= object1.y + object1.height:
    #                 return True
    #
    #     if object2.currDir is "Left":
    #         if tri_points[1][0] <= x <= tri_points[0][0]:
    #             y_min = (x - tri_points[0][0]) * line1_slope + tri_points[0][1]
    #             y_max = (x - tri_points[0][0]) * line2_slope + tri_points[0][1]
    #             if y_min <= x <= y_max:
    #                 return True
    #         for tri_point in tri_points:
    #             if object1.x <= tri_point[0] <= object1.x + object1.width and \
    #                     object1.y <= tri_point[1] <= object1.y + object1.height:
    #                 return True
    #
    #     if object2.currDir is "Right":
    #         if tri_points[0][0] <= x <= tri_points[1][0]:
    #             y_max = (x - tri_points[0][0]) * line1_slope + tri_points[0][1]
    #             y_min = (x - tri_points[0][0]) * line2_slope + tri_points[0][1]
    #             if y_min <= x <= y_max:
    #                 return True
    #         for tri_point in tri_points:
    #             if object1.x <= tri_point[0] <= object1.x + object1.width and \
    #                     object1.y <= tri_point[1] <= object1.y + object1.height:
    #                 return True
    #
    return False


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.visible = False

    def draw(self, win, outline=None):
        if self.visible:
            # Call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('comicsans', 60)
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False
