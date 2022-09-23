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

        if event.type == pygame.MOUSEBUTTONDOWN:   # Si el evento lanzado es de tipo botón de ratón presionado
            print(event)  # Imprimimos el contenido del evento MOUSEBUTTONDOWN

            # Preguntamos por cada button e imprimimos el mensaje correspondiente
            if event.button == 1:
                print("Click botón izquierdo")
            if event.button == 2:
                print("Click botón central")
            if event.button == 3:
                print("Click botón derecho")
            if event.button == 4:
                print("Scroll arriba")
            if event.button == 5:
                print("Scroll abajo")

    surface.fill(white)
    pygame.display.update()
