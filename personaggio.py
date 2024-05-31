import pygame
from funzioni import blocco_sotto

WIDTH, HEIGHT = 1200, 600

DISTANZA_DAL_BORDO = 100
GRAVITA = 0.5
FORZA_SALTO = -12
GROUND_Y = HEIGHT - 100

class Personaggio:
    def __init__(self, x, y):
        
        self.character = pygame.image.load("info_character.png").convert_alpha()
        self.character = pygame.transform.scale(self.character, (100, 100))
        self.rect = self.character.get_rect(topleft = (DISTANZA_DAL_BORDO, HEIGHT-100))
        self.rect.x = 100
        self.rect.y = y
        self.stop_y = HEIGHT
        self.jumping = False
        self.falling = False
        self.jump_speed = 0
        self.gravity = 0.5
        self.vel_y = 0
        self.terra = False
        self.doppio_salto = False

    def salta(self):
        if self.terra:
            self.vel_y = FORZA_SALTO
            self.terra = False
            self.doppio_salto = True
        elif self.doppio_salto:
            self.vel_y = FORZA_SALTO
            self.doppio_salto = False

    def aggiorna(self):
        self.vel_y += GRAVITA
        self.rect.y += self.vel_y

        # Simulazione della collisione con il terreno
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.terra = True
            self.doppio_salto = False

    def draw(self, screen):
        screen.blit(self.character, self.rect.topleft)