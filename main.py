import pygame
from configs import *
from character import *
from direction import *
from ui import *
from world import World
from camera import Camera

pygame.init()
screen = pygame.display.set_mode([window.WIDTH, window.HEIGHT])
pygame.display.set_icon(window.ICON)
pygame.display.set_caption(window.TITLE)

clock = pygame.time.Clock()
world = World()
character = Character()
camera = Camera(window.WIDTH, window.HEIGHT, character)

sound.BACKGROUND.play(loops=-1)

game_over = False
win = False
while True:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    world.draw(screen, camera)

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        character.move(direction.LEFT)
        camera.update(character)

    if key[pygame.K_RIGHT]:
        character.move(direction.RIGHT)
        camera.update(character)

    if key[pygame.K_UP]:
        character.move(direction.UP)
        camera.update(character)

    if key[pygame.K_DOWN]:
        character.move(direction.DOWN)
        camera.update(character)

    if key[pygame.K_SPACE]:
        if win or game_over:
            break

    character.draw(screen, camera)

    pygame.display.update()