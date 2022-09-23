import sys
import math
import pygame

pygame.init()

width, height = 600, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

image1 = pygame.image.load("../imagenes/medium_circle.png")
rect1 = image1.get_rect()
rect1.center = (width//2, height//2)

image2 = pygame.image.load("../imagenes/medium_circle.png")
rectCirc = image2.get_rect()

surface2 = pygame.Surface((rect1.width, rect1.height), pygame.SRCALPHA)
surface2.fill((0, 0, 0, 50))
rect2 = surface2.get_rect()
rect2.center = rect1.center

font = pygame.font.Font('freesansbold.ttf', 36)

while True:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    rectCirc.center = pygame.mouse.get_pos()

    surface.blit(image1, rect1)
    surface.blit(image2, rectCirc)
    surface.blit(surface2, rect2)

    # dist = Raíz cuadrada de = x * x + y * y, x = x1-x2, y = y1 - y2
    dist = math.hypot(rect1.x - rectCirc.x, rect1.y - rectCirc.y)
    message = "Pixels {}".format(str(int(dist)))  # mostramos la longitud de la línea
    # Pintamos una línea del centro de uno de los círculos al otro
    pygame.draw.line(surface, red, rect1.center, rectCirc.center, 2)

    if dist < (64 + 64):  # Existe colisión, 64 = radio del círculo
        message = "Colisión"

    text = font.render(message, True, blue)
    rectTxt = text.get_rect()
    rectTxt.midtop = (width//2, 50)

    surface.blit(text, rectTxt)
    pygame.display.update()
