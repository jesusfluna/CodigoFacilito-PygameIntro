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

    pressed = pygame.key.get_pressed()  # Contiene el estado de todas las teclas

    if pressed[pygame.K_w]:  # Preguntamos si "w" está presionada
        print("arriba")

    if pressed[pygame.K_s]:  # Preguntamos si "s" está presionada
        print("abajo")

    if pressed[pygame.K_a]:  # Preguntamos si "a" está presionada
        print("izquierda")

    if pressed[pygame.K_d]:  # Preguntamos si "d" está presionada
        print("derecha")

    surface.fill(white)
    pygame.display.update()
