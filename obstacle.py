import pygame

class Obstacle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__skin = pygame.Surface((width,height))

    def get_overlaping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        target_mask = pygame.mask.from_surface(skin)
        return target_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides(self, target):
        return target.get_overlaping_area(self.__skin, self.__x, self.__y) > 0
