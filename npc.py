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
        self.__is_stuck = False
        self.__stuck_timer = 0
        self.__stuck_coords = [0, 0]
        self.__escape_direction = None

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
                                self.become_hostile(npc)

                        if player.reputation["corrupted"] > 0:
                            player_target = world.get_nearby_npc(player)
                            if player_target:
                                if player_target.x == self.x and player_target.y == self.y:
                                    self.become_hostile(player)
                    elif faction.stage == 2:
                        self.be_hostile_to_all(player, world)

                case "corrupted":
                    if faction.stage == 1:
                        self.be_hostile_to_all(player, world)
                    elif faction.stage == 2:
                        self.kill_all(player, world)

                case "exiled":
                    if faction.stage == 2:
                        self.travel_to([504, 1395], world)

                        if self.x == 504 and self.y == 1395:
                            self.teleport([200, 1395])
                            self.faction.wall_exploded()

    def be_hostile_to_all(self, player, world):
        npc = world.get_nearby_npc(self)
        player_target = world.get_nearby_npc(player)

        if npc:
            if npc.faction.name != self.__faction.name:
                self.become_hostile(npc)

        if player_target:
            if player_target.x == self.x and player_target.y == self.y:
                self.become_hostile(player)

    def kill_all(self, player, world):
        if not self.__target:
            self_count = 0
            while not self.__target:
                target = world.get_random_npc()
                while target.faction.name == self.__faction.name and self_count <= 7:
                    target = world.get_random_npc()
                    self_count += 1

                if self_count > 7:
                    target = player

                self.__target = target
                self.become_hostile(target)

    def move_randomly(self, dt, world):
        self.__move_timer += dt

        if self.__move_timer >= 1000:
            if self.__moving:
                self.__moving = False
            else:
                self.__moving = True
                self.__direction = self.get_random_direction()
            self.__move_timer -= 1000

        if self.__moving:
            self.move(self.__direction, world)

    def get_random_direction(self):
        direc = randint(0, 4)
        match direc:
            case 0:
                return None
            case 1:
                return direction.LEFT
            case 2:
                return direction.RIGHT
            case 3:
                return direction.DOWN
            case 4:
                return direction.UP

        return None

    def become_hostile(self, target):
        if not self.is_dead:
            self.__hostile = True
            self.__target = target

    def attack(self, target, world):
        if target.is_dead:
            self.__hostile = False

            self.__faction.increment_kill_count()

            self.__target = None
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

        previous_pos = [self.x, self.y]

        if not self.__is_stuck:
            if x_diff < 0 and abs(x_diff) >= abs(y_diff):
                self.__direction = direction.LEFT

            if x_diff > 0 and abs(x_diff) >= abs(y_diff):
                self.__direction = direction.RIGHT

            if y_diff < 0 and abs(y_diff) >= abs(x_diff):
                self.__direction = direction.UP

            if y_diff > 0 and abs(y_diff) >= abs(x_diff):
                self.__direction = direction.DOWN

            self.move(self.__direction, world)

            if previous_pos == [self.x, self.y]:

                if self.__direction == direction.RIGHT or self.__direction == direction.LEFT:
                    if y_diff < 0:
                        self.__direction = direction.UP
                    else:
                        self.__direction = direction.DOWN
                elif self.__direction == direction.UP or self.__direction == direction.DOWN:
                    if x_diff < 0:
                        self.__direction = direction.LEFT
                    else:
                        self.__direction = direction.RIGHT

                self.move(self.__direction, world)

                if [self.x, self.y] == self.__stuck_coords:
                    self.__is_stuck = True
                    print(f"{self.faction.name} is stuck")
                    self.__escape_direction = self.get_random_direction()
                else:
                    self.__stuck_coords = previous_pos
        else:
            self.__stuck_timer += 1

            if self.__stuck_timer <= 60 * 4:
                self.move(self.__escape_direction, world)
            else:
                self.__stuck_timer = 0
                self.__is_stuck = False


    def update_cooldown_timer(self, dt):
        if self.__in_cooldown:
            self.__attack_timer += dt

            if self.__attack_timer >= 1000:
                self.is_attacking = False

            if self.__attack_timer >= game.ATTACK_COOLDOWN * 1000:
                self.__in_cooldown = False
                self.__attack_timer = 0