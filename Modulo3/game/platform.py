import pygame
from .config import *


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.height = 40

        self.image = pygame.Surface((WIDTH, self.height))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - self.height
