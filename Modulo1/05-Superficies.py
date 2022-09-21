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

# Creamos una nueva surface con un ancho y alto
surface2 = pygame.Surface((200, 200))
# La pintamos de verde
surface2.fill(green)
# Las surface tienen un rectángulo por defecto que las perfila
rect = surface2.get_rect()
# usando el rectángulo de la surface podemos centrarla
rect.center = (width//2, height//2)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    # Colocamos la nueva surface en la principal y la posicionamos en las coordenadas del rectángulo de surface2
    surface.blit(surface2, rect)
    # pintamos un rectángulo en la segunda surface
    pygame.draw.rect(surface2, red, (100, 50, 80, 40))

    pygame.display.update()
