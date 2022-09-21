import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Tiempo transcurrido desde que la función pygame.init() fue ejecutada en milisegundos
    time = pygame.time.get_ticks()
    time = time//1000  # Convertimos a segundos
    print(time)

    surface.fill(white)
    pygame.display.update()
