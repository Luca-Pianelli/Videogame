import pygame 
import random

pygame.init()

LARGHEZZA, ALTEZZA = 800, 600
VELx = random.randint(-4, 4)
VELy = 4
VEL = 10

screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))

FPS = 60 

clock = pygame.time.Clock()

run = True

X = 120
Y = 20 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

rettangolo = pygame.Rect(LARGHEZZA / 2 - X / 2, ALTEZZA - Y - 20, X, Y)
rettangolino = pygame.Rect(LARGHEZZA / 2 - X / 4, 0, Y, Y)

while run:

    clock.tick(FPS)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

    key_pressed = pygame.key.get_pressed()

    rettangolino.y += VELy
    rettangolino.x += VELx

    if key_pressed[pygame.K_a] and rettangolo.x > 0:
        rettangolo.x -= VEL

    if key_pressed[pygame.K_d] and rettangolo.x < LARGHEZZA - X:
        rettangolo.x += VEL

    if rettangolino.x <= 0:
        VELx = VELx*-1

    if rettangolino.x > LARGHEZZA - Y:
        VELx = VELx*-1

    if rettangolino.y <= 0:
        VELy = VELy*-1

    if rettangolo.colliderect(rettangolino):
        VELy = VELy*-1

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, rettangolo)
    pygame.draw.rect(screen, WHITE, rettangolino)

    pygame.display.update()

pygame.quit()
