import pygame
WIDTH, HEIGHT = 1200, 600
class Moneta:
    
    def __init__(self, vel, rect):

        self.vel = vel
        self.rect = rect
        self.image = pygame.image.load("coins.png")
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    def move(self):
        
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

    def draw(self, screen):
        
        screen.blit(self.image, (self.rect.x, self.rect.y))