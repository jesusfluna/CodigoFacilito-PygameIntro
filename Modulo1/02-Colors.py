import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

# Creación de color RGB con pygame
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)

# Creación de color RGB con un array timple
my_color = (200, 90, 130)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)  # Añadimos un color de fondo a la ventana
    pygame.display.update()  # Para que se actualicen los cambios necesitamos realizar el update
