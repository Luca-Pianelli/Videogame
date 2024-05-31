import pygame
from funzioni import blocco_sotto

WIDTH, HEIGHT = 1200, 600

DISTANZA_DAL_BORDO = 100

GROUND = HEIGHT 

class Personaggio:
    def __init__(self, x, y):
        
        self.character = pygame.image.load("info_character.png").convert_alpha()
        self.character = pygame.transform.scale(self.character, (100, 100))
        self.rect = self.character.get_rect(topleft = (DISTANZA_DAL_BORDO, GROUND))
        self.rect.x = 100
        self.rect.y = y
        self.stop_y = HEIGHT -100
        self.jumping = False
        self.falling = False
        self.jump_speed = 0
        self.gravity = 0.5

    def jump(self):
        if not self.jumping and not self.falling:
            self.jumping = True
            self.jump_speed = 15  # Velocità iniziale del salto

    def update(self):
        if self.jumping:
            self.rect.y -= self.jump_speed
            self.jump_speed -= self.gravity
            if self.jump_speed <= 0:
                self.jumping = False
                self.falling = True
                self.jump_speed = 0

        if self.falling:
            self.rect.y += self.jump_speed
            self.jump_speed += self.gravity
            if self.rect.y >= self.stop_y:
                self.rect.y = self.stop_y
                self.falling = False

    def draw(self, screen):
        screen.blit(self.character, self.rect.topleft)