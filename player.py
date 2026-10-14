import pygame

from direction import *
from character import Character
from configs import *
from item import *
from playerintent import playerintent
from world import World, Pickup


class Player(Character):
    def __init__(self, reputation=None, discovered=None):
        super().__init__(
            map.WIDTH / 2 - skin.PLAYER.get_width() / 2,
            map.HEIGHT / 2 - skin.PLAYER.get_height() / 2
        )
        self.__target = None
        self.__energy = 100
        self.__energy_timer = 0
        self.__hunger = 0
        self.__hunger_timer = 0
        self.__life_timer = 0
        self.__attack_timer = 0
        self.__is_sprinting = False
        self.__sprint_timer = 0
        self.__inventory = []
        if reputation is None:
            self.__reputation = {
                "druid": 0,
                "exiled": 0,
                "corrupted": 0
            }
            self.__discovered = {
                "druid": False,
                "exiled": False,
                "corrupted": False
            }
        else:
            self.__reputation = reputation
            self.__discovered = discovered
        self.__in_dialog = False


    @property
    def hunger(self):
        return self.__hunger

    @property
    def energy(self):
        return self.__energy

    @property
    def inventory(self):
        return self.__inventory

    @property
    def discovered(self):
        return self.__discovered

    @property
    def in_dialog(self):
        return self.__in_dialog
    @in_dialog.setter
    def in_dialog(self, value):
        self.__in_dialog = value

    @property
    def reputation(self):
        return self.__reputation

    def discover(self, faction):
        self.__discovered[faction] = True
        # print(f"{self.__discovered}")

    def get_skin(self):
        return skin.PLAYER

    def get_attack_skin(self):
        return skin.PLAYER_ATTACKING

    def increase_reputation(self, faction, value):
        if self.__discovered[faction]:
            self.__reputation[faction] += value

    def decrease_reputation(self, faction, value):
        if self.__discovered[faction]:
            self.__reputation[faction] -= value

    def lose_energy(self, value):
        if self.__energy - value < 0:
            self.__energy = 0
            return

        self.__energy -= value

    def handle_input(self, world, events):
        self.handle_movement_input(world)

        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        self.use_inventory_item(0)
                    case pygame.K_2:
                        self.use_inventory_item(1)
                    case pygame.K_3:
                        self.use_inventory_item(2)
                    case pygame.K_c:
                        self.__in_dialog = True
                    case pygame.K_e:
                        self.attack(world)

    def attack(self, world):
        if self.__energy <= 5:
            return

        if not self.is_attacking:
            self.is_attacking = True
            self.lose_energy(5)

            npc = world.get_nearby_npc(self)
            if npc:
                if not npc.is_dead:
                    self.__target = npc

                    if self.collides(npc):
                        npc.lose_life(self.attack_power)
                        npc.become_hostile(self)

                    if self.__target.is_dead:
                        if self.__target.faction.name == "corrupted":
                            if self.__discovered["druid"]:
                                self.increase_reputation("druid", 50)
                                if self.__reputation["druid"] > 0:
                                    world.factions["druid"].increment_kill_count()
                            # print("Aumentou reputação com os druidas")
                            self.decrease_reputation("corrupted", 10)
                        elif self.__target.faction.name == "druid":
                            self.decrease_reputation("druid", 60)
                            if self.__discovered["corrupted"]:
                                self.increase_reputation("corrupted", 100)
                                if self.__reputation["corrupted"] > 0:
                                    world.factions["corrupted"].increment_kill_count()
                        elif self.__target.faction.name == "exiled":
                            self.decrease_reputation("exiled", 30)
                            if self.__discovered["corrupted"]:
                                self.increase_reputation("corrupted", 100)
                                if self.__reputation["corrupted"] > 0:
                                    world.factions["corrupted"].increment_kill_count()

                        self.increment_kill_count()
                        self.__target = None

    def use_inventory_item(self, i):
        if len(self.inventory) > i:
            self.__inventory[i].item.use(self)

            if self.__inventory[i].item.consumable:
                self.__inventory[i].decrease_quant()

                if self.__inventory[i].quantity == 0:
                    self.__inventory.remove(self.__inventory[i])

        # print(self.__inventory)

    def handle_movement_input(self, world):
        key = pygame.key.get_pressed()

        if key[pygame.K_LSHIFT]:
            self.change_speed(1.5)
            self.__is_sprinting = True

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.move(direction.LEFT, world)

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move(direction.RIGHT, world)

        if key[pygame.K_UP] or key[pygame.K_w]:
            self.move(direction.UP, world)

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.move(direction.DOWN, world)

        self.change_speed(1)

    def update_stats(self, dt):
        self.__hunger_timer += dt
        self.__energy_timer += dt
        self.__attack_timer += dt

        if self.lives < 10:
            self.__life_timer += dt

        if self.__is_sprinting:
            self.__sprint_timer += dt
            self.__is_sprinting = False

        if self.__attack_timer >= 1000:
            self.is_attacking = False
            self.__attack_timer = 0

        if self.__sprint_timer >= 1000:
            self.lose_energy(game.SPRINT_ENERGY_COST)
            self.__sprint_timer = 0

        while self.__hunger_timer >= game.HUNGER_DECAY_TIME * 1000:
            if self.__hunger < 100:
                self.__hunger += 1

            self.__hunger_timer -= game.HUNGER_DECAY_TIME * 1000

        while self.__energy_timer >= game.ENERGY_RECOVERY_TIME * 1000:
            if self.__hunger >= 100:
                if self.__energy <= 0:
                    self.lose_life(1)
                else:
                    self.lose_energy(1)
            else:
                if self.__energy < 100:
                    self.__energy += 1

            self.__energy_timer -= game.ENERGY_RECOVERY_TIME * 1000

        while self.__life_timer >= game.LIFE_RECOVERY_TIME * 1000:
            if self.__energy - game.LIFE_RECOVERY_COST > 0:
                self.recover_life(0.5)
                self.lose_energy(game.LIFE_RECOVERY_COST)

            self.__life_timer -= game.LIFE_RECOVERY_TIME * 1000

        # print(f"{self.__hunger}, {self.__energy}")

    def replenish_hunger(self, val):
        self.__hunger -= val
        self.recover_life(0.25)

        if self.__hunger < 0:
            self.__hunger = 0

    def add_to_inventory(self, obj, image):
        repeated_item = False

        if isinstance(obj, Pickup):
            if obj.tile.type == "mushroom":
                item = InventoryItem(Food(obj.tile.name, image, obj.tile.hunger_restore, obj.tile.poisonous))
                # print(item.item.name)
                # print(item.quantity)
            elif obj.tile.type == "resource":
                item = InventoryItem(Resource(obj.tile.name, image))

            if self.__inventory:
                for inv_item in self.__inventory:
                    if item.item.name == inv_item.item.name:
                        # print("sabe que já tinha mushrooms")
                        inv_item.increment_quant()
                        repeated_item = True
            if not repeated_item:
                self.__inventory.append(item)
                # print("adicionou o item")
        # print(self.__inventory)

class InventoryItem:
    def __init__(self, item):
        self.__item = item
        self.__quantity = 1

    @property
    def item(self):
        return self.__item

    @property
    def quantity(self):
        return self.__quantity

    def increment_quant(self):
        self.__quantity += 1

    def decrease_quant(self):
        if self.__quantity > 0:
            self.__quantity -= 1
