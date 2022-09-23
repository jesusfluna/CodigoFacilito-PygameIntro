import sys

import pygame

pygame.init()

width, height = 600, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

imagen = pygame.image.load("../imagenes/medium_circle.png")
rect1 = imagen.get_rect()
rect1.center = (width//2, height//2)

mask_circle = pygame.mask.from_surface(imagen)  # Creamos una máscara de nuestra imagen círculo

imagen2 = pygame.image.load("../imagenes/small_rectangle.png")
rect2 = imagen2.get_rect()
mask_rect = pygame.mask.from_surface(imagen2)  # Creamos una máscara de nuestro rectángulo

font = pygame.font.Font('freesansbold.ttf', 36)

while True:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    rect2.center = pygame.mouse.get_pos()

    surface.blit(imagen, rect1)
    surface.blit(imagen2, rect2)

    message = ""

    offset = (rect2.x-rect1.x, rect2.y-rect1.y)  # Coordenada de intersección (orden importante)
    # en vez de detectar colisión detectamos overlaping de las imágenes a través de las máscaras (orden importante)
    if mask_circle.overlap(mask_rect, offset):
        message = "Colisionando"

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)

    surface.blit(text, rect3)

    pygame.display.update()
