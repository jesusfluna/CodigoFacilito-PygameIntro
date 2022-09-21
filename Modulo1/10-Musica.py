import sys

import pygame

pygame.init()

width, height = 400, 500
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hola PyGame")

white = pygame.Color(255, 255, 255)

# Cargamos el audio
pygame.mixer.music.load("../sounds/Haggstrom.mp3")
# Valor Float 0.0 a 1.0 para el volumen
pygame.mixer.music.set_volume(1.0)
# Reproducimos el audio cargado
pygame.mixer.music.play(-1, 0.0)  # {numero de reproducciones (-1 infinito), momento a comenzar la reproducción}

"""
# Reiniciar la canción
pygame.mixer.music.rewind()
# Pausar la canción
pygame.mixer.music.pause()
# Detener la canción
pygame.mixer.music.stop()
# Detener la canción progresivamente
pygame.mixer.music.fadeout()  # {numero entero de milisegundos que tardara en detenerse la musica}
"""

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    pygame.display.update()
