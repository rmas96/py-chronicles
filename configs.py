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
    LOBSTER_TWO = pygame.font.Font("fonts/LobsterTwo-Regular.ttf", 22)

    @staticmethod
    def split(text):
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            if current_line == "":
                potential_line = word
            else:
                potential_line = current_line + " " + word

            if font.CARTER_ONE.render(f"{potential_line}", True, (0,0,0)).get_width() <= 300:
                current_line = potential_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines

class skin:
    # BACKGROUND = pytmx.load_pygame("imgs/map_1.tmx")
    PLAYER = pygame.image.load("imgs/player.png")
    PLAYER_ATTACKING = pygame.image.load("imgs/player attacking.png")
    DRUID = pygame.image.load("imgs/druid.png")
    EXILED = pygame.image.load("imgs/exiled.png")
    CORRUPTED = pygame.image.load("imgs/orc.png")
    # DIALOG_BACKGROUND = pygame.transform.scale(pygame.image.load("imgs/papyrus_quad.png"), (window.WIDTH - 400, window.HEIGHT - 400))
    DIALOG_BACKGROUND = pygame.image.load("imgs/papyrus_quad.png")


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
    HUNGER_DECAY_TIME = 2
    ENERGY_RECOVERY_TIME = 1
    LIFE_RECOVERY_TIME = 5
    LIFE_RECOVERY_COST = 10
    MAX_LIFE = 10
    SPRINT_ENERGY_COST = 2
    MUSHROOM_RESPAWN_TIME = 100
    POISON_DAMAGE = 1
    CORRUPTION_TIME = 3  # minutes
    CORRUPTED_KILL_TRIGGER = 1
    CORRUPTED_MAX_KILLS = 3
    EXILED_RESOURCE_OBJECTIVE = 5
    EXILED_BUILD_TIME = 4   # minutes
    DRUID_RESOURCE_LIMIT = 5
    DRUID_MAX_KILLS = 3
    ATTACK_COOLDOWN = 2
