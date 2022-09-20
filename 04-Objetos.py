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

color = pygame.Color(180, 255, 50)
color2 = pygame.Color(100, 100, 255)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    # Draw
    # 1º Donde se pintará
    # 2º De que color
    # 3º Array de coordenadas y tamaño
    pygame.draw.rect(surface, red, (100, 100, 80, 40))  # Rectángulo
    pygame.draw.circle(surface, green, (200, 300), 100)  # Circulo
    pygame.draw.line(surface, blue, (100, 100), (200, 300), 2)  # Linea

    pygame.draw.polygon(surface, color, ((0, 400), (100, 300), (200, 400)))  # Triangulo
    pygame.draw.polygon(surface, color2, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))  # Pentágono

    pygame.display.update()
