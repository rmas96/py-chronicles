import pygame
import pytmx

class World:
    COLLISION_GID = 268

    def __init__(self):
        self.__map = pytmx.load_pygame("tiled/map_1.tmx")
        self.__collision_rects = [pygame.Rect(
            x * self.__map.tilewidth,
            y * self.__map.tileheight,
            self.__map.tilewidth,
            self.__map.tileheight)
            for x, y, gid in self.__map.layernames["Colision"] if gid != 0
        ]

    def draw(self, screen, camera):
        for layer in self.__map.visible_tile_layers:
            for x, y, gid in self.__map.layers[layer]:
                tile = self.__map.get_tile_image_by_gid(gid)
                x = x * self.__map.tilewidth - camera.x
                y = y * self.__map.tileheight - camera.y

                if tile:
                    screen.blit(tile, (x, y))

    def would_collide(self, rect):
        for col_rect in self.__collision_rects:
            if col_rect.colliderect(rect):
                return True

        return None