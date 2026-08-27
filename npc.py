from random import randint

from character import Character
from configs import *
from direction import *
from faction import Faction


class Npc(Character):
    def __init__(self, faction):
        self.__faction = faction
        super().__init__(faction.get_region()[0], faction.get_region()[1])
        self.__move_timer = 0
        self.__moving = False
        self.__hostile = False
        self.__target = None
        self.__attack_timer = 0
        self.__in_cooldown = False

    @property
    def faction(self):
        return self.__faction

    def get_skin(self):
        if self.__faction.name == "druid":
            self.__skin = skin.DRUID
        elif self.__faction.name == "exiled":
            self.__skin = skin.EXILED
        elif self.__faction.name == "corrupted":
            self.__skin = skin.CORRUPTED

        return self.__skin

    def update(self, world, dt, player):
        if self.is_dead:
            return

        self.update_cooldown_timer(dt)

        if self.__hostile:
            if self.__target.get_skin() == player.get_skin():
                self.attack(player, world)
        else:
            self.move_randomly(dt, world)

    def move_randomly(self, dt, world):
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

    def become_hostile(self, player):
        if not self.is_dead:
            self.__hostile = True
            self.__target = player

    def attack(self, target, world):
        if self.collides(target):
            if not self.__in_cooldown:
                target.lose_life(self.attack_power)
                self.__in_cooldown = True
        else:
            x_diff = target.x - self.x
            y_diff = target.y - self.y

            if x_diff < 0 and abs(x_diff) >= abs(y_diff):
                self.__direction = direction.LEFT

            if x_diff > 0 and abs(x_diff) >= abs(y_diff):
                self.__direction = direction.RIGHT

            if y_diff < 0 and abs(y_diff) >= abs(x_diff):
                self.__direction = direction.UP

            if y_diff > 0 and abs(y_diff) >= abs(x_diff):
                self.__direction = direction.DOWN

            self.move(self.__direction, world)

        if target.is_dead:
            self.__hostile = False

    def update_cooldown_timer(self, dt):
        if self.__in_cooldown:
            self.__attack_timer += dt

            if self.__attack_timer >= game.ATTACK_COOLDOWN * 1000:
                self.__in_cooldown = False
                self.__attack_timer = 0