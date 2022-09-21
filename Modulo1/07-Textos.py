import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)

# 1º Obtener una fuente
font = pygame.font.Font('freesansbold.ttf', 48)  # {rutaFuente/nombre, tamaño}
font2 = pygame.font.Font('../roboto/Roboto-Thin.ttf', 28)  # Load de un fichero de fuente
# 2º Crear texto. Devuelve una superficie
text = font.render("Hola mundo!", True, red)  # {texto, antialiasing, color}
text2 = font2.render("Bienvenido", True, green)
# posicionamos en el centro
rect = text.get_rect()
rect.center = (width//2, height//2)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    surface.fill(white)
    surface.blit(text, rect)  # Pintamos nuestro texto en una superficie
    surface.blit(text2, (10, 10))

    pygame.display.update()
