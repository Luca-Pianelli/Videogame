import pygame 

WIDTH, HEIGHT = 600, 600

class Cerchio:
    
    def __init__(self, colore, centro, raggio, velx, vely):
        
        self.colore = colore
        self.centro = centro
        self.raggio = raggio
        self.velx = velx
        self.vely = vely

    def velocità(self):

        self.centro[0] += self.velx
        self.centro[1] += self.vely

        if self.centro[0] - self.raggio < 0:
            self.velx = self.velx*(-1)

        if self.centro[0] - (WIDTH - self.raggio) > 0:
            self.velx = self.velx*(-1)

        if self.centro[1] - self.raggio < 0:
            self.vely = self.vely*(-1)

        if self.centro[1] - (HEIGHT - self.raggio) > 0:
            self.vely = self.vely*(-1)

    def draw(self, screen):

        pygame.draw.circle(screen, self.colore, self.centro, self.raggio)
