import pygame.sprite
from .config import *
import os


class Wall(pygame.sprite.Sprite):
    def __init__(self, left, bottom, dir_image):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(dir_image, 'wall.png'))  # pygame.Surface((40, 80))
        # self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.vel_x = SPEED

        # Rectángulo de un pixel en la parte superior del muro para no matar al jugador al subir
        self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 1)

    def update(self):
        self.rect.left -= self.vel_x
        self.rect_top.x = self.rect.x

    def stop(self):
        self.vel_x = 0
