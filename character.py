import pygame

from configs import *
from direction import *
from fruit import Fruit


class Character:
    def __init__(self):
        self.__x = map.WIDTH / 2
        self.__y = map.HEIGHT / 2
        self.__skin = skin.CHARACTER
        self.__speed = 1
        self.__direction = None
        self.__lives = 10
        self.__fruits_eaten = 0
        self.__is_dead = False
        self.__is_flipped = False

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def fruits_eaten(self):
        return self.__fruits_eaten

    @property
    def lives(self):
        return self.__lives

    @property
    def is_dead(self):
        return self.__is_dead

    def draw(self, screen, camera):
        screen.blit(self.__skin, [self.__x - camera.x, self.__y - camera.y])

    def move(self, dir: direction):
        if self.__is_dead:
            return

        self.__direction = dir

        if dir == direction.LEFT:
            self.__x -= self.__speed
        elif dir == direction.RIGHT:
            self.__x += self.__speed
        elif dir == direction.UP:
            self.__y -= self.__speed
        else:
            self.__y += self.__speed

        print(f"{self.__x}, {self.__y}")
        # print(f"{window.WIDTH - 360 - self.__skin.get_width()}")

    def eat_fruit(self, fruit: Fruit):
        if self.__is_dead:
            return

        if fruit.is_eaten:
            return

        if fruit.is_poisoned:
            self.__lives -= fruit.poison_value
            if self.__lives <= 0:
                self.die()
                return
            self.__speed = 2
            sound.OUCH.play()
        else:
            self.__fruits_eaten += 1
            self.__speed += 2
            sound.EATING.play()

        fruit.get_eaten()

    def is_inside_map(self):
        if self.__x < 0:
            self.__x = 0
            return False
        elif self.__x > window.WIDTH - self.__skin.get_width():
            self.__x = window.WIDTH - self.__skin.get_width()
            return False

        if self.__y < 0:
            self.__y = 0
            return False
        elif self.__y > window.HEIGHT - self.__skin.get_width():
            self.__y = window.HEIGHT - self.__skin.get_width()
            return False

        return True

    def bounce_back(self):
        if self.__is_dead:
            return

        if self.__direction == direction.LEFT:
            self.__x += self.__speed * 2
        elif self.__direction == direction.RIGHT:
            self.__x -= self.__speed * 2
        elif self.__direction == direction.UP:
            self.__y += self.__speed * 2
        else:
            self.__y -= self.__speed * 2

    def die(self):
        self.__lives = 0
        self.__is_dead = True
        if not self.__is_flipped:
            self.__skin = pygame.transform.flip(self.__skin, 0, 1)
            self.__is_flipped = True

    def get_overlaping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        target_mask = pygame.mask.from_surface(skin)
        return target_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides(self, target):
        return target.get_overlaping_area(self.__skin, self.__x, self.__y) > 0