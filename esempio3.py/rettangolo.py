import pygame

WITDH, HEIGHT = 600, 600

class Rettangolo:
    def __init__(self, x, y, height, width, colore, velx, vely):
        
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.colore = colore
        self.velx = velx
        self.vely = vely

    def velocità(self):
        
        self.x += self.velx
        self.y += self.vely

        if self.x <= 0:
            self.velx = self.velx*-1

        if self.x + self.width >= WITDH:
            self.velx = self.velx*-1

        if self.y <= 0:
            self.vely = self.vely-1

        if self.y + self.height >= HEIGHT:
             self.vely = self.vely*-1

    def draw(self, screen):
        pygame.draw.rect(screen, self.colore, pygame.Rect(self.x, self.y, self.width, self.height))
