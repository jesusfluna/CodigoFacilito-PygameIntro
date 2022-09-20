import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)

#Creacion de un rectangulo en pygame
rect = pygame.Rect(100, 150, 120, 60) # posX, posY, width, height
rect.center = (width//2, height//2) #Centramos el rectangulo a mitad de la pantalla
print(rect.x)
print(rect.y)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    #Pintamos el rectangulo
    pygame.draw.rect(surface, red, rect)# surface, color, rectangulo

    pygame.display.update()
