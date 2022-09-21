import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

white = pygame.Color(255, 255, 255)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Preguntamos por el evento de teclado KEYDOWN, tecla presionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:  # Si la tecla presionada es <= o 'a' es izquierda
                print('Izquierda')

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:  # Si la tecla presionada es => o 'a' es derecha
                print('Derecha')

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:  # Si la tecla presionada es ^ o 'a' es abajo
                print('Abajo')

            if event.key == pygame.K_UP or event.key == pygame.K_w:  # Si la tecla presionada es v o 'a' es arriba
                print('Arriba')

    surface.fill(white)
    pygame.display.update()
