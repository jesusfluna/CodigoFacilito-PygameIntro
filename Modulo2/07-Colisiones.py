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

# creamos un primer rectángulo que dejaremos fijo en el centro de la ventana
rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width//2, height//2)

# un segundo rectángulo
rect2 = pygame.Rect(0, 0, 100, 80)

font = pygame.font.Font('freesansbold.ttf', 36)

while True:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    rect2.center = pygame.mouse.get_pos()  # El segundo rectángulo lo posicionamos en el puntero del mouse

    # pintamos los rectángulos
    pygame.draw.rect(surface, green, rect1)
    pygame.draw.rect(surface, red, rect2)

    # Creamos un mensaje arriba de la pantalla para escribir si hay colisión entre rectángulos
    message = ""
    if rect1.colliderect(rect2):  # Con la función de collision cambiamos el mensaje cuando haya.
        message = "Colisionando"

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)

    surface.blit(text, rect3)

    pygame.display.update()
