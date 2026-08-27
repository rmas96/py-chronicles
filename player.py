import pygame

from direction import *
from character import Character
from configs import *
from item import *
from playerintent import playerintent
from world import World, Pickup


class Player(Character):
    def __init__(self):
        super().__init__(
            map.WIDTH / 2 - skin.PLAYER.get_width() / 2,
            map.HEIGHT / 2 - skin.PLAYER.get_height() / 2
        )
        self.__energy = 100
        self.__energy_timer = 0
        self.__hunger = 0
        self.__hunger_timer = 0
        self.__life_timer = 0
        self.__attack_timer = 0
        self.__inventory = []
        self.__reputation = {
            "Druids": 0,
            "Exiled": 0,
            "Corrupted": 0
        }

    @property
    def hunger(self):
        return self.__hunger

    @property
    def energy(self):
        return self.__energy

    @property
    def inventory(self):
        return self.__inventory

    def get_skin(self):
        return skin.PLAYER

    def handle_input(self, world, events):
        self.handle_movement_input(world)
        intent = playerintent.NONE

        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        self.use_inventory_item(0)
                    case pygame.K_2:
                        self.use_inventory_item(1)
                    case pygame.K_c:
                        intent = playerintent.INTERACT
                    case pygame.K_e:
                        intent = playerintent.ATTACK
                        self.is_attacking = True
                        self.__energy -= 1

        return intent

    def use_inventory_item(self, i):
        if len(self.inventory) > i:
            self.__inventory[i].item.use(self)

            if self.__inventory[i].item.consumable:
                self.__inventory[i].decrease_quant()

                if self.__inventory[i].quantity == 0:
                    self.__inventory.remove(self.__inventory[i])

    def handle_movement_input(self, world):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.move(direction.LEFT, world)

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move(direction.RIGHT, world)

        if key[pygame.K_UP] or key[pygame.K_w]:
            self.move(direction.UP, world)

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.move(direction.DOWN, world)

    def update_stats(self, dt):
        self.__hunger_timer += dt
        self.__energy_timer += dt
        self.__attack_timer += dt

        if self.lives < 10:
            self.__life_timer += dt

        if self.__attack_timer >= 1000:
            self.is_attacking = False
            self.__attack_timer = 0

        while self.__hunger_timer >= game.HUNGER_DECAY_TIME * 1000:
            if self.__hunger < 100:
                self.__hunger += 1

            self.__hunger_timer -= game.HUNGER_DECAY_TIME * 1000

        while self.__energy_timer >= game.ENERGY_RECOVERY_TIME * 1000:
            if self.__hunger >= 100:
                if self.__energy <= 0:
                    self.lose_life(1)
                else:
                    self.__energy -= 1
            else:
                if self.__energy < 100:
                    self.__energy += 1

            self.__energy_timer -= game.ENERGY_RECOVERY_TIME * 1000

        while self.__life_timer >= game.LIFE_RECOVERY_TIME * 1000:
            if self.__energy - game.LIFE_RECOVERY_COST > 0:
                self.recover_life()
                self.__energy -= game.LIFE_RECOVERY_COST

            self.__life_timer -= game.LIFE_RECOVERY_TIME * 1000

        # print(f"{self.__hunger}, {self.__energy}")

    def replenish_hunger(self, val):
        self.__hunger -= val

        if self.__hunger < 0:
            self.__hunger = 0

    def add_to_inventory(self, obj, image):
        repeated_item = False

        if isinstance(obj, Pickup):
            if obj.tile.type == "mushroom" or obj.tile.type == "mushroom_p":
                item = InventoryItem(Food(obj.tile.type, image, obj.tile.hunger_restore, obj.tile.poisonous))
                print(item.item.name)
                print(item.quantity)
                if self.__inventory:
                    for inv_item in self.__inventory:
                        if item.item.name == inv_item.item.name:
                            print("sabe que já tinha mushrooms")
                            inv_item.increment_quant()
                            repeated_item = True
                if not repeated_item:
                    self.__inventory.append(item)
                    print("adicionou o item")
        print(self.__inventory)

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
