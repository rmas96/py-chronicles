import pygame
import pytmx

class World:
    def __init__(self):
        self.__map = pytmx.load_pygame("tiled/map_1.tmx")

    def draw(self, screen, camera):
        for layer in self.__map.visible_tile_layers:
            for x, y, gid in self.__map.layers[layer]:
                tile = self.__map.get_tile_image_by_gid(gid)
                x = x * self.__map.tilewidth - camera.x
                y = y * self.__map.tileheight - camera.y

                if tile:
                    screen.blit(tile, (x, y))