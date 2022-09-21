import sys

import pygame

pygame.init()  # Iniciamos pygame

width, height = 400, 500
surface = pygame.display.set_mode((width, height))  # Generación de una ventana de 400x500
pygame.display.set_caption("Hola PyGame")  # establecemos un titulo para la ventana de la aplicación

while True:  # Bucle infinito

    for event in pygame.event.get():  # Recorremos los eventos de pygame para ver cuál se ha lanzado
        if event.type == pygame.QUIT:  # Si se ha lanzado un evento de cierre
            pygame.quit()  # Cerramos el programa pygame
            sys.exit()  # Detenemos la ejecución del programa completo
