import pygame
import pytmx

pygame.init()
pygame.mixer.init()

class window:
    TITLE = "Py Cronicles"
    WIDTH = 600
    HEIGHT = 600
    ICON = pygame.image.load("imgs/apple.png")

class map:
    TILE_SIZE = 32
    NUMBER_TILES_x = 50
    NUMBER_TILES_Y = 50
    WIDTH = TILE_SIZE * NUMBER_TILES_x
    HEIGHT = TILE_SIZE * NUMBER_TILES_Y

class font:
    CARTER_ONE = pygame.font.Font("fonts/CarterOne-Regular.ttf", 25)

class skin:
    # BACKGROUND = pytmx.load_pygame("imgs/map_1.tmx")
    PLAYER = pygame.image.load("imgs/player.png")
    DRUID = pygame.image.load("imgs/druid.png")
    EXILED = pygame.image.load("imgs/exiled.png")
    CORRUPTED = pygame.image.load("imgs/orc.png")

class sound:
    BACKGROUND = pygame.mixer.Sound("sounds/background.mp3")
    BACKGROUND.set_volume(0.1)

    EATING = pygame.mixer.Sound("sounds/eating.wav")
    EATING.set_volume(0.3)

    OUCH = pygame.mixer.Sound("sounds/ouch.wav")
    OUCH.set_volume(0.3)

    GAME_OVER = pygame.mixer.Sound("sounds/game_over.wav")
    GAME_OVER.set_volume(0.2)

    COMPLETE = pygame.mixer.Sound("sounds/level_complete.wav")
    COMPLETE.set_volume(0.2)

class game:
    HUNGER_DECAY_TIME = 1
    ENERGY_RECOVERY_TIME = 1
    LIFE_RECOVERY_TIME = 5
    LIFE_RECOVERY_COST = 10
    MAX_LIFE = 10
    MUSHROOM_RESPAWN_TIME = 100
    POISON_DAMAGE = 1
