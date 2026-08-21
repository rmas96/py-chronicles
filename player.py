import pygame

from direction import *
from character import Character
from configs import *
from item import *
from world import Pickup


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
        self.__inventory = []

    @property
    def hunger(self):
        return self.__hunger

    @property
    def energy(self):
        return self.__energy

    @property
    def inventory(self):
        return self.__inventory

    def handle_input(self, world):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.move(direction.LEFT, world)

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move(direction.RIGHT, world)

        if key[pygame.K_UP] or key[pygame.K_w]:
            self.move(direction.UP, world)

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.move(direction.DOWN, world)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if len(self.inventory) > 0:
                        self.__inventory[0].item.use(self)

                        if self.__inventory[0].item.consumable:
                            self.__inventory[0].decrease_quant()

                            if self.__inventory[0].quantity == 0:
                                self.__inventory.remove(self.__inventory[0])

                elif event.key == pygame.K_2:
                    if len(self.__inventory) > 1:
                        self.__inventory[1].item.use(self)

                        if self.__inventory[1].item.consumable:
                            self.__inventory[1].decrease_quant()

                            if self.__inventory[1].quantity == 0:
                                self.__inventory.remove(self.__inventory[1])

    def update_stats(self, dt):
        self.__hunger_timer += dt
        self.__energy_timer += dt

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


        # print(f"{self.__hunger}, {self.__energy}")

    def take_damage(self, dmg):
        self.__lives -= dmg

        if self.__lives <= 0:
            self.die()

        sound.OUCH.play()

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
            # elif obj.tile.type == "mushroom_p":
            #     item = InventoryItem(Food("mushroom_p", image, obj.tile.hunger_restore, obj.tile.poisonous))
            #     if item in self.__inventory:
            #         for inv_item in self.__inventory:
            #             if inv_item.item == item:
            #                 inv_item.increment_quant()
            #     else:
            #         self.__inventory.append(item)
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
