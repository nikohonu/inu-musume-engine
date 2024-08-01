import enum

import pygame.constants

QUIT = pygame.constants.QUIT


class Key(enum.Enum):
    A = pygame.constants.K_a
    D = pygame.constants.K_d
    S = pygame.constants.K_s
    W = pygame.constants.K_w
