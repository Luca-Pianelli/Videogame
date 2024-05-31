import pygame
from cerchio import Cerchio
import random

pygame.init()

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True 

FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

palle = [Cerchio(WHITE, [WIDTH / 2, HEIGHT / 2], 10, random.choice([7, -7]), random.choice([5, -5]))]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    nuove_palle = []
    
    for palla in palle:
        if palla.velocità():
            nuove_palle.append(Cerchio(WHITE, [WIDTH / 2, HEIGHT / 2], 10, random.choice([7, -7]), random.choice([5, -5])))
    
    palle.extend(nuove_palle)

    screen.fill(BLACK)
    
    for palla in palle:
        palla.draw(screen)

    pygame.display.update()

pygame.quit()