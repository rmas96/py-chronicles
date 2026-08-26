import pygame
from configs import *
from dialog_manager import DialogManager
from player import *
from direction import *
from hud import *
from world import *
from camera import *
from npc import *

pygame.init()
screen = pygame.display.set_mode([window.WIDTH, window.HEIGHT])
pygame.display.set_icon(window.ICON)
pygame.display.set_caption(window.TITLE)

clock = pygame.time.Clock()
world = World()
player = Player()
camera = Camera(window.WIDTH, window.HEIGHT, player)

hud = Hud(player)

# sound.BACKGROUND.play(loops=-1)

game_over = False
win = False
player_intent = playerintent.NONE
in_dialog = False
while True:
    dt = clock.tick(60)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit(0)

    key = pygame.key.get_pressed()

    if key[pygame.K_ESCAPE]:
        pygame.quit()
        quit(0)

    world.draw(screen, camera)
    if player_intent == playerintent.NONE:
        player_intent = player.handle_input(world, events)

        if player_intent == playerintent.INTERACT:
            npc = world.get_nearby_npc(player)
            # print(npc)
            if npc:
                dialog = DialogManager(npc)
                # print("sabe que é para entrar em dialogo")
            else:
                player_intent = playerintent.NONE
    elif player_intent == playerintent.INTERACT:
        player_intent = dialog.handle_input(events)

    world.update(player, dt)
    player.update_stats(dt)
    camera.update(player)
    hud.update(player)

    player.draw(screen, camera)
    hud.draw(screen)

    if player_intent == playerintent.INTERACT:
        print("pos em estado de dialogo")
        dialog.draw(screen, camera)

    pygame.display.update()