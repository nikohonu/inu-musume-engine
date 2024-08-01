import pygame

from inu_musume_engine.game_object import GameObject
from inu_musume_engine.input import Input
from inu_musume_engine.key import Key

screen = pygame.display.set_mode((1280, 720))


class Game:
    def __init__(
        self,
        actions: dict[str, list[Key]] | None = None,
        game_objects: list[GameObject] | None = None,
    ) -> None:
        self.game_objects = game_objects if game_objects else []
        if actions:
            Input.actions = actions

    def add_object(self, game_object: GameObject):
        self.game_objects.append(game_object)

    def run(self) -> None:
        _ = pygame.init()
        clock = pygame.time.Clock()
        running = True
        dt = 0

        for game_object in self.game_objects:
            game_object.ready()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            Input.pressed_keys = pygame.key.get_pressed()

            _ = screen.fill("purple")

            for game_object in self.game_objects:
                game_object.process(dt)

            pygame.display.flip()

            dt = clock.tick(144) / 1000

        pygame.quit()
