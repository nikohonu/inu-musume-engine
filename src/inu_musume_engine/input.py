import pygame

from inu_musume_engine.key import Key


class Input:
    actions: dict[str, list[Key]] = {}
    pressed_keys: pygame.key.ScancodeWrapper | None = None

    @staticmethod
    def is_action_pressed(action: str) -> bool:
        for key in Input.actions[action]:
            if Input.pressed_keys and Input.pressed_keys[key.value]:
                return True
        return False
