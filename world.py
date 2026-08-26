import pygame
import pytmx

from configs import *
from npc import Npc


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
        self.__entities = {
            "druid": Npc(1451.0, 1311.0, "druid"),
            "exiled": Npc(1387.0, 469.0, "exiled"),
            "corrupted": Npc(211.0, 135.0, "corrupted"),
        }

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

        self.__entities["druid"].draw(screen, camera)
        self.__entities["exiled"].draw(screen, camera)
        self.__entities["corrupted"].draw(screen, camera)

    def would_collide(self, rect):
        for col_rect in self.__collision_rects:
            if col_rect.colliderect(rect):
                return True

        return None

    def get_nearby_npc(self, player):
        for entity in self.__entities:
            if self.__entities[entity].collides(player.collision_rect.inflate(100, 100)):
                return self.__entities[entity]

        return None

    def update(self, player, dt):
        self.update_pickups(player, dt)
        self.__entities["druid"].update(self, dt)
        self.__entities["exiled"].update(self, dt)
        self.__entities["corrupted"].update(self, dt)

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