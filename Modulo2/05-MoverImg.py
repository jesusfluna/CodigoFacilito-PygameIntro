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

    pressed = pygame.key.get_pressed()  # recogemos los eventos de presión de tecla para preguntar por ellos

    if pressed[pygame.K_w]:  # Movemos la imagen arriba 5px
        rect.y -= 5

    if pressed[pygame.K_s]:  # Movemos la imagen abajo 5px
        rect.y += 5

    if pressed[pygame.K_a]:  # Movemos la imagen a la izquierda 5px
        rect.x -= 5

    if pressed[pygame.K_d]:  # Movemos la imagen a la derecha 5px
        rect.x += 5

    # validaciones para que la imagen no salga de la ventana
    if rect.left < 0:
        rect.left = 0
    if rect.right > width:
        rect.right = width
    if rect.top < 0:
        rect.top = 0
    if rect.bottom > height:
        rect.bottom = height



    surface.fill(white)
    surface.blit(image, rect)  # dibujamos la imagen

    pygame.display.update()
