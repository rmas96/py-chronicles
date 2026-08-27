import pygame

import configs
import dialogues
from configs import skin, window, font
from faction import Faction
from playerintent import playerintent


class DialogManager:
    def __init__(self, npc):
        match npc.faction.name:
            case "druid": self.__dialog_tree = dialogues.DRUID_DIALOGUE
            case "exiled": self.__dialog_tree = dialogues.EXILED_DIALOGUE
            case "corrupted": self.__dialog_tree = dialogues.CORRUPTED_DIALOGUE
        self.__faction_stage = npc.faction.stage
        match self.__faction_stage:
            case 0: self.__current_node = "start"
        self.__skin = skin.DIALOG_BACKGROUND

    def draw(self, screen, camera):
        screen.blit(self.__skin, [
            window.WIDTH / 2 - self.__skin.get_width() / 2,
            window.HEIGHT / 2 - self.__skin.get_height() / 2
        ])

        lines = font.split(self.__dialog_tree[self.__current_node]["text"])

        i = 1
        for line in lines:
            npc_text = font.LOBSTER_TWO.render(
                f"{line}", True, "black"
            )

            screen.blit(npc_text, [
                window.WIDTH / 2 - npc_text.get_width() / 2,
                window.HEIGHT / 2 - 125 + npc_text.get_height() / 1.5 * i
            ])

            i += 1

        i = 1
        for option in self.__dialog_tree[self.__current_node]["options"]:
            option_text = font.LOBSTER_TWO.render(
                f"{i}) {option["text"]}",
                True,
                "black"
            )
            screen.blit(
                option_text,
                [
                    window.WIDTH / 2 - option_text.get_width() / 2,
                    window.HEIGHT / 2 + 35 + option_text.get_height() / 1.5 * i
                ]
            )

            i += 1

    def handle_input(self, events):
        intent = playerintent.INTERACT
        options = self.__dialog_tree[self.__current_node]["options"]

        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        if len(options) > 0:
                            self.__current_node = options[0]["next"]
                        else:
                            intent = playerintent.NONE
                    case pygame.K_2:
                        if len(options) > 1:
                            self.__current_node = options[1]["next"]
                    case pygame.K_3:
                        if len(options) > 2:
                            self.__current_node = options[2]["next"]
                    case pygame.K_SPACE:
                        intent = playerintent.NONE

        return intent