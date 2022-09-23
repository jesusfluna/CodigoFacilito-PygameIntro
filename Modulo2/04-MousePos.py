import sys

import pygame

pygame.init()

width, height = 600, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

font = pygame.font.Font('freesansbold.ttf',48)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pos_x, pos_y = pygame.mouse.get_pos()  # coordenadas de la posición de nuestro mouse
    message = 'pos x : {} pos y : {}'.format(pos_x, pos_y)  # mensaje con la posición recogida

    text = font.render(message, True, red)
    rect = text.get_rect()
    rect.center = (width//2, height//2)

    surface.fill(white)
    surface.blit(text, rect)
    pygame.display.update()
