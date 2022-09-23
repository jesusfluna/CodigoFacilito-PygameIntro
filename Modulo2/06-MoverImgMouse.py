import sys

import pygame

pygame.init()

width, height = 600, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Cargamos la imagen y la posicionamos en el centro de la ventana
image = pygame.image.load("../imagenes/medium_circle.png")
rect = image.get_rect()
rect.center = (width//2, height//2)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect.center = pygame.mouse.get_pos()  # con la posición del mouse modificamos el centro del rectángulo de la imagen

    surface.fill(white)
    surface.blit(image, rect)  # dibujamos la imagen

    pygame.display.update()
