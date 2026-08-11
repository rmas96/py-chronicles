from configs import *
from direction import *
from random import randint

class Fruit:
    def __init__(self, x, y, is_poisoned):
        self.__x = x
        self.__y = y
        self.__is_poisoned = is_poisoned
        self.__is_eaten = False

        if is_poisoned:
            self.__skin = skin.APPLE_BAD
            self.__poison_value = randint(1, 5)
        else:
            self.__skin = skin.APPLE_GOOD
            self.__poison_value = 0

    @property
    def is_poisoned(self):
        return self.__is_poisoned

    @property
    def poison_value(self):
        return self.__poison_value

    @property
    def is_eaten(self):
        return self.__is_eaten

    def draw(self, screen: pygame.Surface):
        screen.blit(self.__skin, [self.__x, self.__y])

    def relocate(self):
        self.__x = randint(0, window.WIDTH)
        self.__y = randint(0, window.HEIGHT)

    def get_eaten(self):
        self.__is_eaten = True
        self.__skin = skin.APPLE_EATEN

    def get_overlaping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        target_mask = pygame.mask.from_surface(skin)
        return target_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides(self, target):
        if self.__is_eaten:
            return False

        return target.get_overlaping_area(self.__skin, self.__x, self.__y) > 0#------- Com transparência ---------
