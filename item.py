from pygame.examples.cursors import image
from unicodedata import name


class Item:
    def __init__(self, name, image):
        self.__name = name
        self.__image = image

    @property
    def image(self):
        return self.__image

class Food(Item):
    def __init__(self, name, image, hunger_restore, poisonous):
        super().__init__(name, image)
        self.__hunger_restore = hunger_restore
        self.__poisonous = poisonous