import sys
import pygame
from .config import *
from .platform import Platform


class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))  # Ventana principal del juego
        pygame.display.set_caption(TITLE)
        self.running = True

        self.platform = Platform()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.platform)

    def start(self):
        self.new()

    def new(self):
        self.run()

    def run(self):  # Bucle de ejecución de la aplicación
        while self.running:
            self.event()
            self.draw()
            self.update()

    def event(self):  # Método para las acciones de cada evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

    def draw(self):  # Dibujado de los elementos
        self.surface.fill(BLACK)  # Pintamos la ventana con un fondo, negro
        self.sprites.draw(self.surface)  # Pintamos todos los sprites contenidos en el grupo

    def update(self):  # Actualización del contenido de la ventana
        pygame.display.flip()  # Similar al update solo que lo realizara sobre toda la superficie

    def stop(self):  # Detención de las acciones de la aplicación
        pass

