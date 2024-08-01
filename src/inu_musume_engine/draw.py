import pygame

from inu_musume_engine import Vector2
from inu_musume_engine.game import screen


def draw_circle(position: Vector2, radius: float, color: str):
    _ = pygame.draw.circle(screen, color, position, radius)


def draw_sprite(position: Vector2, sprite: pygame.Surface):
    _ = screen.blit(sprite, (position.x, position.y))
