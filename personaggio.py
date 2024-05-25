import pygame

WIDTH, HEIGHT = 1200, 600

DISTANZA_DAL_BORDO = 100

GROUND = HEIGHT - 295

class Personaggio:
    def __init__(self, x, y):

        self.character = pygame.image.load("info_character.png").convert_alpha()
        self.character = pygame.transform.scale(self.character, (100, 100))
        self.rect = self.character.get_rect(topleft = (DISTANZA_DAL_BORDO, GROUND))
        self.rect.x = 100
        self.rect.y = GROUND
        self.velocita_y = 0
        self.gravita = 1
        self.h_salto = 18
        self.in_volo = False

    def jump(self):
        
        if not self.in_volo:
            self.in_volo = True
            self.velocita_y -= self.h_salto  

    def aggiorna_posizione_salto(self):
        
        if self.in_volo:
            self.velocita_y += self.gravita
            self.rect.y += self.velocita_y

            if self.rect.y >= GROUND:
                self.rect.y = GROUND
                self.in_volo = False
                self.velocita_y = 0

    def draw(self, screen):
        screen.blit(self.character, self.rect.topleft)