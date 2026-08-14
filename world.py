import pygame
import pytmx

from configs import *
from character import *


class World:
    COLLISION_GID = 267
    PRICKLY_GID = 458

    def __init__(self):
        self.__map = pytmx.load_pygame("tiled/map_1.tmx")
        self.__collision_rects = [pygame.Rect(
            x * self.__map.tilewidth,
            y * self.__map.tileheight,
            self.__map.tilewidth,
            self.__map.tileheight)
            for x, y, gid in self.__map.layernames["Colision"] if gid != 0
        ]
        self.__pickups = [Pickup(pickup) for pickup in self.__map.layernames["Pickups2"]]

    def draw(self, screen, camera):
        for layer in self.__map.visible_tile_layers:
            for x, y, gid in self.__map.layers[layer]:
                tile = self.__map.get_tile_image_by_gid(gid)
                x = x * self.__map.tilewidth - camera.x
                y = y * self.__map.tileheight - camera.y

                if tile:
                    screen.blit(tile, (x, y))

        for pickup in self.__pickups:
            if pickup.visible:
                tile = self.__map.get_tile_image_by_gid(pickup.tile.gid)
                x = pickup.tile.x - camera.x
                y = pickup.tile.y - camera.y

                if tile:
                    screen.blit(tile, (x, y))

    def would_collide(self, rect):
        for col_rect in self.__collision_rects:
            if col_rect.colliderect(rect):
                return True

        return None

    def update_pickups(self, player, dt):
        for pickup in self.__pickups:
            if not pickup.visible:
                pickup.respawn(dt)
            else:
                if player.collides(pygame.Rect(
                        pickup.tile.x,
                        pickup.tile.y,
                        self.__map.tilewidth,
                        self.__map.tileheight
                )):
                    player.add_to_inventory(
                        pickup,
                        self.__map.get_tile_image_by_gid(pickup.tile.gid)
                    )
                    pickup.disappear()

class Pickup:
    def __init__(self, pickup):
        self.__tile = pickup
        self.__visible = True
        self.__respawn_timer = 0

    @property
    def tile(self):
        return self.__tile

    @property
    def visible(self):
        return self.__visible

    def disappear(self):
        self.__visible = False

    def respawn(self, dt):
        self.__respawn_timer += dt

        if self.__respawn_timer >= game.MUSHROOM_RESPAWN_TIME * 1000:
            self.__visible = True
            self.__respawn_timer = 0