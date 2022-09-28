import random
import sys
import pygame
from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
from .coin import Coin
import os


class Game:
    def __init__(self):
        """ Atributos """
        self.background = None
        self.player = None
        self.platform = None
        self.coins = None
        self.walls = None
        self.sprites = None
        self.level = 0

        pygame.init()

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))  # Ventana principal del juego
        pygame.display.set_caption(TITLE)
        self.running = True
        self.playing = True

        """ Reloj """
        self.clock = reloj = pygame.time.Clock()

        """ Puntuaciones """
        self.score = 0
        self.font = pygame.font.match_font(FONT, 30)

        """ ruta de assets"""
        self.dir = os.path.dirname(__file__).replace('\\Modulo3\\game', "")
        self.dir_sounds = os.path.join(self.dir, 'sounds')
        self.dir_imagenes = os.path.join(self.dir, 'imagenes')

    # Generación de elementos
    def generate_elements(self):
        """ Grupos de sprites """
        self.sprites = pygame.sprite.Group()  # Grupo de sprites para todos nuestros elementos gráficos
        self.walls = pygame.sprite.Group()  # Grupo de sprites para las 'paredes'
        self.coins = pygame.sprite.Group()  # Grupo de sprites para las 'monedas'

        """ Sprites """
        self.platform = Platform()
        self.sprites.add(self.platform)
        self.player = Player(100, self.platform.rect.top - 200, self.dir_imagenes)
        self.sprites.add(self.player)

        self.generate_walls()

    # Generación de monedas en posiciones aleatorias
    def generate_coins(self):
        last_position = WIDTH + 100

        for c in range(0, MAX_COINS):
            pos_x = random.randrange(last_position + 180, last_position + 300)
            coin = Coin(pos_x, 100, self.dir_imagenes)
            last_position = coin.rect.right
            self.sprites.add(coin)
            self.coins.add(coin)

    # Generación de walls en posiciones aleatorias
    def generate_walls(self):
        last_position = WIDTH + 100
        if not len(self.walls) > 0:
            for w in range(0, MAX_WALLS):
                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top, self.dir_imagenes)

                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)

            self.level += 1
            self.generate_coins()

    def start(self):
        self.menu()
        self.new()

    def new(self):
        self.playing = True
        self.score = 0
        self.level = 0
        self.background = pygame.image.load(os.path.join(self.dir_imagenes, 'background.png'))

        self.generate_elements()
        self.run()

    def run(self):  # Bucle de ejecución de la aplicación

        while self.running:
            self.clock.tick(FPS)  # frames
            self.event()
            self.update()
            self.draw()

    def event(self):  # Método para las acciones de cada evento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:  # Si presionamos space lanzamos la logica del salto del personaje
            self.player.jump()

        if key[pygame.K_r] and not self.playing:  # Si presionamos 'r' cuando hemos perdido se reinicia el juego
            self.new()

    def draw(self):  # Dibujado de los elementos
        self.surface.blit(self.background, (0, 0))  # self.surface.fill(BLACK) # Pintamos la ventana con un fondo, negro
        self.sprites.draw(self.surface)  # Pintamos todos los sprites contenidos en el grupo
        self.draw_text()  # Pintamos el texto con lo score
        pygame.display.flip()  # Similar al update solo que lo realizara sobre toda la superficie

    def update(self):  # Actualización del contenido de la ventana
        if self.playing:
            self.sprites.update()  # Todos los elementos de la lista ejecutan su método update
            self.player.validate_platform(self.platform)

            wall = self.player.collide_with(self.walls)  # Vemos si hay colisión y con quien se ha colisionado si se da

            # Si hay un elemento es que ha habido una colisión y detenemos el juego
            if wall:
                if self.player.collide_top(wall):
                    self.player.skid(wall)
                else:
                    sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "lose.wav"))
                    sound.play()
                    self.stop()

            # Si tocamos una moneda subimos los puntos
            coin = self.player.collide_with(self.coins)
            if coin:
                sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "coin.wav"))
                sound.play()
                self.score += 1
                coin.kill()

            self.update_elements(self.walls)
            self.update_elements(self.coins)
            self.generate_walls()

    def stop(self):  # Detención de las acciones de la aplicación
        self.player.stop()
        self.stop_elements(self.walls)
        self.playing = False

    def stop_elements(self, elements):  # Paramos los elementos de la lista
        for element in elements:
            element.stop()

    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()

    # Logica para definir un texto en la surface principal
    def display_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)
        self.surface.blit(text, rect)

    def draw_text(self):
        self.display_text('Score : {}'.format(self.score), 36, BLACK, WIDTH//2, TEXT_POSY)
        self.display_text('Leve : {}'.format(self.level), 36, BLACK, 60, TEXT_POSY)

        if not self.playing:
            self.display_text('Perdiste!!', 60, BLACK, WIDTH // 2, HEIGHT // 2)
            self.display_text('Presiona R para volver a intentar', 30, BLACK, WIDTH // 2, 100)

    def menu(self):
        self.surface.fill(GREEN_LIGHT)
        self.display_text("Presiona una tecla para comenzar", 36, BLACK, WIDTH//2, 10)

        pygame.display.flip()
        self.wait()

    def wait(self):
        wait = True

        while wait:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    wait = False

