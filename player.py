import pygame

from direction import *
from character import Character
from configs import *


class Player(Character):
    def __init__(self):
        super().__init__(
            map.WIDTH / 2 - skin.CHARACTER.get_width() / 2,
            map.HEIGHT / 2 - skin.CHARACTER.get_height() / 2
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


        print(f"{self.__hunger}, {self.__energy}")