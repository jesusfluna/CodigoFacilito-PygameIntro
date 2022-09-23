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

rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width//2, height//2)

rect2 = pygame.Rect(0, 0, 100, 80)

font = pygame.font.Font('freesansbold.ttf', 36)

sound = pygame.mixer.Sound("../sounds/coin.wav")  # Cargamos nuestro fichero de audio

while True:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    rect2.center = pygame.mouse.get_pos()

    pygame.draw.rect(surface, green, rect1)
    pygame.draw.rect(surface, red, rect2)

    message = ""
    if rect1.colliderect(rect2):
        sound.play()  # Reproducimos el sonido cuando haya colisión
        message = "Colisionando"

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)

    surface.blit(text, rect3)

    pygame.display.update()
