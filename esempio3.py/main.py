import pygame
from rettangolo import Rettangolo
import random

pygame.init()

WITDH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WITDH, HEIGHT))

clock = pygame.time.Clock()

run = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

rettangoli = []

FPS = 60

clock = pygame.time.Clock()

while run:

    clock.tick(FPS)

    dim = random.randint(20,100)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT and len(rettangoli) < 10:
                rettangolo = Rettangolo(mouse_pos[0] - dim / 2, mouse_pos[1] - dim / 2, dim, dim, (dim, dim*2, dim*0,5), 5, 5)
                rettangoli.append(rettangolo)
    
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(BLACK)

    for rettangolo in rettangoli:
        rettangolo.draw(screen)

    pygame.display.update()

pygame.quit()