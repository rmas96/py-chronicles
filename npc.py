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

    def update(self, world, dt, player, faction):
        if self.is_dead:
            return

        self.update_cooldown_timer(dt)

        if self.__hostile:
            self.attack(self.__target, world)
        else:
            self.move_randomly(dt, world)

        match self.__faction.name:
            case "druid":
                if faction.stage == 1:
                    npc = world.get_nearby_npc(self)
                    if npc:
                        if npc.faction.name == "corrupted" and not npc.is_dead:
                            self.__hostile = True
                            self.__target = npc
                elif faction.stage == 2:
                    self.be_hostile_to_all(player, world)

            case "corrupted":
                if faction.stage == 1:
                    self.be_hostile_to_all(player, world)
                elif faction.stage == 2:
                    self.kill_all(player, world)

            case "exiled":
                if faction.stage == 2:
                    self.travel_to([60, 333.0], world)

                    if self.x == 60 and self.y == 333:
                        self.teleport([30, 333])
                        self.faction.wall_exploded()

    def be_hostile_to_all(self, player, world):
        npc = world.get_nearby_npc(self)
        player_target = world.get_nearby_npc(player)

        if npc:
            self.__hostile = True
            self.__target = npc

        if player_target:
            if player_target.x == self.x and player_target.y == self.y:
                self.__hostile = True
                self.__target = player

        if self.__target:
            if self.__target.is_dead:
                self.__hostile = False
                self.faction.increment_kill_count()
                self.__target = None

    def kill_all(self, player, world):
        if not self.__target:
            self_count = 0
            while not self.__target:
                target = world.get_random_npc()
                if target == self:
                    self_count += 1

                if self_count >= 3:
                    target = player

                if target != self:
                    self.__target = target

        self.__hostile = True

        if self.__target:
            if self.__target.is_dead:
                self.faction.increment_kill_count()
                self.__target = None

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

    def become_hostile(self, target):
        if not self.is_dead:
            self.__hostile = True
            self.__target = target

    def attack(self, target, world):
        if target.is_dead:
            self.__hostile = False
            return

        if self.collides(target):
            if not self.__in_cooldown:
                target.lose_life(self.attack_power)
                if target.get_skin() != skin.PLAYER:
                    target.become_hostile(self)
                self.__in_cooldown = True
                self.is_attacking = True
        else:
            self.travel_to([target.x, target.y], world)


    def travel_to(self, coord, world):
        x_diff = coord[0] - self.x
        y_diff = coord[1] - self.y

        if x_diff < 0 and abs(x_diff) >= abs(y_diff):
            self.__direction = direction.LEFT

        if x_diff > 0 and abs(x_diff) >= abs(y_diff):
            self.__direction = direction.RIGHT

        if y_diff < 0 and abs(y_diff) >= abs(x_diff):
            self.__direction = direction.UP

        if y_diff > 0 and abs(y_diff) >= abs(x_diff):
            self.__direction = direction.DOWN

        self.move(self.__direction, world)

    def update_cooldown_timer(self, dt):
        if self.__in_cooldown:
            self.__attack_timer += dt

            if self.__attack_timer >= 1000:
                self.is_attacking = False

            if self.__attack_timer >= game.ATTACK_COOLDOWN * 1000:
                self.__in_cooldown = False
                self.__attack_timer = 0