import pygame.sprite
from .config import *
import os


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, dir_image):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(dir_image, 'coin.png'))  # pygame.Surface((20, 40))
        # self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.vel_x = SPEED

    def update(self):
        self.rect.left -= self.vel_x

    def stop(self):
        self.rect.left = 0
