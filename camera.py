import pygame
from configs import *


class Camera:
    def __init__(self, size_x, size_y, target):
        self.__width = size_x
        self.__height = size_y
        self.__x = target.x - size_x / 2
        self.__y = target.y - size_y / 2

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def update(self, target):
        if not self.at_border_x(target):
            self.__x = target.x - self.__width / 2

        if not self.at_border_y(target):
            self.__y = target.y - self.__height / 2

    def at_border_x(self, target):
        if target.x - self.__width / 2 <= 0:
            return True
        elif target.x + self.__width / 2 >= map.WIDTH:
            return True

        return False

    def at_border_y(self, target):
        if target.y - self.__height / 2 <= 0:
            return True
        elif target.y + self.__height / 2 >= map.HEIGHT:
            return True

        return False