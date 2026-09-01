from pygame.examples.cursors import image
from unicodedata import name

from configs import *


class Item:
    def __init__(self, name, image):
        self.__name = name
        self.__image = image
        self.__consumable = False

    @property
    def image(self):
        return self.__image

    @property
    def name(self):
        return self.__name

    @property
    def consumable(self):
        return self.__consumable

    def use(self, player):
        pass

class Food(Item):
    def __init__(self, name, image, hunger_restore, poisonous):
        super().__init__(name, image)
        self.__hunger_restore = hunger_restore
        self.__poisonous = poisonous
        self.__consumable = True

    @property
    def consumable(self):
        return self.__consumable

    def use(self, player):
        if self.__poisonous:
            player.lose_life(game.POISON_DAMAGE)

        player.replenish_hunger(self.__hunger_restore)
        sound.EATING.play()

class Resource(Item):
    def __init__(self, name, image):
        super().__init__(name, image)
        self.__consumable = True

    @property
    def consumable(self):
        return self.__consumable
