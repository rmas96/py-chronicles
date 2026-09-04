import pygame

from camera import *
from configs import *
from direction import *


class Character:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__skin = self.get_skin()
        self.__attacking_skin = self.get_attack_skin()
        self.__speed = 1
        self.__direction = None
        self.__facing = direction.RIGHT
        self.__lives = 10
        self.__is_dead = False
        self.__is_flipped = False
        self.__is_attacking = False
        self.__attack_power = self.get_attack_power()
        self.__kill_count = 0

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def collision_rect(self):
        return pygame.Rect(
                            self.__x,
                            self.__y + self.__skin.get_height() / 2,
                            self.__skin.get_width(),
                            self.__skin.get_height() / 2
                        )

    @property
    def lives(self):
        return self.__lives

    @property
    def is_dead(self):
        return self.__is_dead

    @property
    def is_attacking(self):
        return self.__is_attacking

    @is_attacking.setter
    def is_attacking(self, value):
        self.__is_attacking = value

    @property
    def attack_power(self):
        return self.__attack_power

    @property
    def kill_count(self):
        return self.__kill_count

    def get_skin(self):
        return skin.PLAYER

    def get_attack_skin(self):
        return skin.PLAYER_ATTACKING

    def get_attack_power(self):
        return 1

    def increment_kill_count(self):
        self.__kill_count += 1

    def draw(self, screen, camera: Camera):
        if self.__direction == direction.LEFT and self.__facing != direction.LEFT:
            self.__skin = pygame.transform.flip(self.__skin, 1, 0)
            self.__attacking_skin = pygame.transform.flip(self.__attacking_skin, 1, 0)
            self.__facing = direction.LEFT
        elif self.__direction == direction.RIGHT and self.__facing != direction.RIGHT:
            self.__skin = pygame.transform.flip(self.__skin, 1, 0)
            self.__attacking_skin = pygame.transform.flip(self.__attacking_skin, 1, 0)
            self.__facing = direction.RIGHT

        if self.__is_attacking:
            screen.blit(self.__attacking_skin, [self.__x - camera.x, self.__y - camera.y])
        else:
            screen.blit(self.__skin, [self.__x - camera.x, self.__y - camera.y])

    def move(self, dir: direction, world):
        if self.__is_dead:
            return
        if not self.is_inside_map():
            return

        self.__direction = dir
        next_x = self.__x
        next_y = self.__y
        if dir == direction.LEFT:
            next_x -= self.__speed
        elif dir == direction.RIGHT:
            next_x += self.__speed
        elif dir == direction.UP:
            next_y -= self.__speed
        else:
            next_y += self.__speed

        if not world.would_collide(pygame.Rect(
                next_x,
                self.__y + self.__skin.get_height() / 2,
                self.__skin.get_width(),
                self.__skin.get_height() / 2
        )):
            self.__x = next_x

        if not world.would_collide(pygame.Rect(
                self.__x,
                next_y + self.__skin.get_height() / 2,
                self.__skin.get_width(),
                self.__skin.get_height() / 2
        )):
            self.__y = next_y


        # print(f"{self.__x}, {self.__y}")
        # print(f"{window.WIDTH - 360 - self.__skin.get_width()}")

    def change_speed(self, value):
        self.__speed = value

    def teleport(self, coord):
        self.__x = coord[0]
        self.__y = coord[1]

    def is_inside_map(self):
        if self.__x < 0:
            self.__x = 0
            return False
        elif self.__x > map.WIDTH - self.__skin.get_width():
            self.__x = map.WIDTH - self.__skin.get_width()
            return False

        if self.__y < 0:
            self.__y = 0
            return False
        elif self.__y > map.HEIGHT - self.__skin.get_height():
            self.__y = map.HEIGHT - self.__skin.get_height()
            return False

        return True

    def recover_life(self, value):
        self.__lives += value

        if self.__lives > game.MAX_LIFE:
            self.__lives = game.MAX_LIFE

    def lose_life(self, life_points):
        if self.__lives > 1:
            self.__lives -= life_points
            sound.OUCH.play()
        else:
            self.die()

    def die(self):
        self.__lives = 0
        self.__is_dead = True
        self.__is_attacking = False
        sound.GAME_OVER.play()

        if not self.__is_flipped:
            self.__skin = pygame.transform.flip(self.__skin, 0, 1)
            self.__is_flipped = True

    def get_overlapping_area(self, skin, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__skin)
        target_mask = pygame.mask.from_surface(skin)
        return target_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def collides(self, target):
        if isinstance(target, pygame.Rect):
            if target.colliderect(self.collision_rect):
                return True
        else:
            if target.get_overlapping_area(self.__skin, self.__x, self.__y) > 0:
                return True

        return False