import pygame
from configs import *
from player import *
from direction import *
from hud import *
from world import World
from camera import Camera
from npc import *

pygame.init()
screen = pygame.display.set_mode([window.WIDTH, window.HEIGHT])
pygame.display.set_icon(window.ICON)
pygame.display.set_caption(window.TITLE)

clock = pygame.time.Clock()
world = World()
player = Player()
camera = Camera(window.WIDTH, window.HEIGHT, player)
druid = Npc(1451.0, 1311.0, "druid")
exiled = Npc(1387.0, 469.0, "exiled")
corrupted = Npc(211.0, 135.0, "corrupted")

hud = Hud(player)

# sound.BACKGROUND.play(loops=-1)

game_over = False
win = False
while True:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
        pygame.quit()
        quit(0)

    world.draw(screen, camera)

    player.handle_input(world)
    world.update_pickups(player, dt)
    player.update_stats(dt)
    druid.update(world, dt)
    exiled.update(world, dt)
    corrupted.update(world, dt)
    camera.update(player)
    hud.update(player)

    druid.draw(screen, camera)
    exiled.draw(screen, camera)
    corrupted.draw(screen, camera)
    player.draw(screen, camera)
    hud.draw(screen)

    pygame.display.update()