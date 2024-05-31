# abbiamo un cerchio: se premiamo tasto sinistro si muove con la freccia del mouse, se scrolliamo la rotella in alto si ingrandisce
# e se la scrolliamo in basso diminuisce (la grandezza) e se posizioniamo sopra il cursore cambia leggermente di colore

import pygame
from classecerchio1 import Cerchio
from mouse1 import puntatore_dentro_cerchio

pygame.init()

WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("matthew è bello")

run = True

FPS = 60

clock = pygame.time.Clock()

ROSSO = (255, 0, 0)
ARANCIONE = (180, 0, 0)
GRIGIO = (30, 30, 30)


cerchio = Cerchio(100, (WIDTH / 2, HEIGHT / 2), ROSSO)

while run:
    
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                cerchio.raggio += 5 
            else:
                cerchio.raggio -= 5 

    mouse_pos = pygame.mouse.get_pos()

    if puntatore_dentro_cerchio(cerchio, mouse_pos):
        cerchio.colore = ARANCIONE
    else:
        cerchio.colre = ROSSO

    if not puntatore_dentro_cerchio(cerchio, mouse_pos):
        cerchio.colore = ROSSO
    else:
        cerchio.colore = ARANCIONE

    muose_pressed = pygame.mouse.get_pressed() #(true, false, false)

    if muose_pressed[0] == True and puntatore_dentro_cerchio(cerchio, mouse_pos):
        cerchio.centro = mouse_pos

    if cerchio.centro[0] - cerchio.raggio < 0:
        cerchio.centro = cerchio.raggio

    if cerchio.centro[0] + cerchio.raggio > WIDTH:
        cerchio.centro = WIDTH - cerchio.raggio

    if cerchio.centro[1] - cerchio.raggio < 0:
        cerchio.centro = cerchio.raggio

    if cerchio.centro[1] + cerchio.raggio > HEIGHT:
        cerchio.centro = HEIGHT - cerchio.raggio

    screen.fill(GRIGIO)
    
    cerchio.draw(screen)

    pygame.display.update()

pygame.quit() 