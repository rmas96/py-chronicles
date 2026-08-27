import pygame

import configs
from character import Character
from configs import font
from player import *


class Hud:

    def __init__(self, player):
        self.__lives = player.lives
        self.__hunger = player.hunger
        self.__energy = player.energy
        self.__inventory = player.inventory

    def update(self, player):
        self.__lives = player.lives
        self.__hunger = player.hunger
        self.__energy = player.energy
        self.__inventory = player.inventory

    def draw(self, screen):
        # pygame.draw.rect(screen, "#212531", [648, 60, 115, 45])
        # pygame.draw.rect(screen, "#212531", [565, 60, 70, 40])
        # pygame.draw.rect(screen, "#212531", [773, 60, 70, 40])

        label_txt = font.CARTER_ONE.render(f"Life   Hunger  Energy", True, "white")
        lives_txt = font.CARTER_ONE.render(f"{self.__lives:.0f}", True, "red")
        hunger_txt = font.CARTER_ONE.render(f"{self.__hunger:.0f}", True, "yellow")
        energy_txt = font.CARTER_ONE.render(f"{self.__energy:.0f}", True, "blue")



        screen.blit(label_txt, [130 - label_txt.get_width() / 2, 10])
        screen.blit(lives_txt, [70 - lives_txt.get_width() / 2, 50])
        screen.blit(hunger_txt, [140 - hunger_txt.get_width() / 2, 50])
        screen.blit(energy_txt, [210 - energy_txt.get_width() / 2, 50])

        i = 1
        for item in self.__inventory:
            item_txt = font.CARTER_ONE.render(f"{item.quantity}", True, "white")
            screen.blit(item.item.image, [window.WIDTH - (window.WIDTH - 40 * i), window.HEIGHT - 40])
            screen.blit(item_txt, [window.WIDTH - (window.WIDTH - 35 * i), window.HEIGHT - 35])
            i += 1

