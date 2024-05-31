import pygame
import sys
from funzioni import get_collision_side
# Inizializza Pygame
pygame.init()

# Impostazioni dello schermo
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Salto del Rettangolo')

# Colori
black = (0, 0, 0)
gilberto = (255, 0, 0)
white = (255, 255, 255)

# Clock per controllare il frame rate
clock = pygame.time.Clock()

rect1 = pygame.Rect(0, screen_height - 100, 100, 100)
rect2 = pygame.Rect(90, screen_height - 100, 100, 100)

# Loop principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestione del salto
    
    print(get_collision_side(rect1, rect2))

    # Disegna tutto sullo schermo
    screen.fill(white)
    pygame.draw.rect(screen, black, rect1)
    pygame.draw.rect(screen, gilberto, rect2)
    pygame.display.flip()

    # Limita il frame rate
    clock.tick(30)
