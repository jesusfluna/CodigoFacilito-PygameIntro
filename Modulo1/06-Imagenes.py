import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)

# Cargamos la imagen de una dirección. Esto devuelve una surface con la imagen
image = pygame.image.load('../imagenes/small_rectangle.png')
# Vamos a pintar la imagen en el centro usando su rectángulo default
rect = image.get_rect()
rect.center = (width//2, height//2)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    # Cargamos la imagen en la superficie en unas coordenadas
    surface.blit(image, rect)

    pygame.display.update()
