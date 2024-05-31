import pygame

class Cerchio:
    def __init__(self, raggio, centro, colore):
        
        self.raggio = raggio
        self.centro = centro
        self.colore = colore

    def draw(self, screen):

        pygame.draw.circle(screen, self.colore, self.centro, self.raggio)



