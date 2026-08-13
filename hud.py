import pygame

import configs
from character import Character
from configs import font
from player import *


class Hud:

    def __init__(self, player: Player):
        self.__lives = player.lives
        self.__hunger = player.hunger
        self.__energy = player.energy

    def update(self, player: Player):
        self.__lives = player.lives
        self.__hunger = player.hunger
        self.__energy = player.energy

    def draw(self, screen):
        # pygame.draw.rect(screen, "#212531", [648, 60, 115, 45])
        # pygame.draw.rect(screen, "#212531", [565, 60, 70, 40])
        # pygame.draw.rect(screen, "#212531", [773, 60, 70, 40])

        label_txt = font.CARTER_ONE.render(f"Life   Fruits", True, "white")
        lives_txt = font.CARTER_ONE.render(f"{self.__lives}", True, "white")
        fruits_eaten_txt = font.CARTER_ONE.render(f"{self.__fruits_eaten}/{self.__n_fruits_to_eat}", True, "white")

        screen.blit(label_txt, [100 - label_txt.get_width() / 2, 20])
        screen.blit(lives_txt, [70 - lives_txt.get_width() / 2, 50])
        screen.blit(fruits_eaten_txt, [140 - fruits_eaten_txt.get_width() / 2, 50])

