from typing import NamedTuple

import pygame
import pygame.base

init = pygame.base.init
quit = pygame.quit


class Size2i(NamedTuple):
    w: int
    h: int


class Size2f(NamedTuple):
    w: float
    h: float
