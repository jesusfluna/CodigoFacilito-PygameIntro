import pygame.sprite
from .config import *
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom, dir_image):
        pygame.sprite.Sprite.__init__(self)

        self.images = (
            pygame.image.load(os.path.join(dir_image, 'player1.png')),
            pygame.image.load(os.path.join(dir_image, 'jump.png'))
        )

        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.vel_y = 0

        self.can_jump = False
        self.playing = True

    # Logica de caída
    def update_pos(self):
        self.vel_y += PLAYER_GRAV  # Gravedad
        self.pos_y += self.vel_y * 0.5 * PLAYER_GRAV

    def update(self):

        if self.playing:
            self.update_pos()
            self.rect.bottom = self.pos_y

    # Logica para detener la caída del jugador en la plataforma
    def validate_platform(self, platform):
        result = pygame.sprite.collide_rect(self, platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True
            self.image = self.images[0]

    # Logica para el salto del personaje
    def jump(self):
        if self.can_jump:
            self.vel_y = - JUMP_HEIGHT
            self.can_jump = False
            self.image = self.images[1]

    # Logica para la colisión del jugador con algún objeto
    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def stop(self):
        self.playing = False

    def collide_top(self, wall):
        return self.rect.colliderect(wall.rect_top)

    def skid(self, wall):
        self.pos_y = wall.rect.top
        self.vel_y = 0
        self.can_jump = True
        self.image = self.images[0]
