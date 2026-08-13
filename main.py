import pygame
from configs import *
from player import *
from direction import *
from hud import *
from world import World
from camera import Camera

pygame.init()
screen = pygame.display.set_mode([window.WIDTH, window.HEIGHT])
pygame.display.set_icon(window.ICON)
pygame.display.set_caption(window.TITLE)

clock = pygame.time.Clock()
world = World()
player = Player()
camera = Camera(window.WIDTH, window.HEIGHT, player)

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

    player.update_stats(dt)
    camera.update(player)

    player.draw(screen, camera)

    pygame.display.update()