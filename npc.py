from random import randint

from character import Character
from configs import skin
from direction import direction


class Npc(Character):
    def __init__(self, x, y, faction):
        self.__faction = faction
        super().__init__(x, y)
        self.__move_timer = 0
        self.__moving = False

    def get_skin(self):
        if self.__faction == "druid":
            self.__skin = skin.DRUID
        elif self.__faction == "exiled":
            self.__skin = skin.EXILED
        elif self.__faction == "corrupted":
            self.__skin = skin.CORRUPTED

        return self.__skin

    def update(self, world, dt):
        self.__move_timer += dt

        if self.__move_timer >= 1000:
            if self.__moving:
                self.__moving = False
            else:
                self.__moving = True
                direc = randint(0, 4)
                match direc:
                    case 0:
                        self.__direction = None
                    case 1:
                        self.__direction = direction.LEFT
                    case 2:
                        self.__direction = direction.RIGHT
                    case 3:
                        self.__direction = direction.DOWN
                    case 4:
                        self.__direction = direction.UP
            self.__move_timer -= 1000

        if self.__moving:
            self.move(self.__direction, world)