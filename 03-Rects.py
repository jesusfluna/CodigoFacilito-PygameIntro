import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)

# Creación de un rectángulo en pygame
rect = pygame.Rect(100, 150, 120, 60)  # posX, posY, width, height
rect.center = (width//2, height//2)  # Centramos el rectángulo a mitad de la pantalla
print(rect.x)
print(rect.y)

# Creación de un rectángulo con arrays
rect2 = (100, 100, 80, 40) # posX, posY, width, height

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    # Pintamos el rectángulo
    pygame.draw.rect(surface, red, rect)  # surface, color, rectángulo
    pygame.draw.rect(surface, green, rect2)  # surface, color, rectángulo

    pygame.display.update()
