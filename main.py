import pygame
from terreno import Terreno
from funzioni import ottieni_lista_blocchi
from personaggio import Personaggio


pygame.init()
WIDTH, HEIGHT = 1200, 600
GROUND = HEIGHT - 195
VEL = 5


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Videogame")
paesaggio = pygame.image.load("sfondo.jpg")
montagna = pygame.image.load("montagna.jpg")
vulcano = pygame.image.load("vulcano.jpg")
erba = pygame.image.load("erba.jpg")
erbaS = pygame.image.load("erbaS.jpg")
lava = pygame.image.load("lava.jpg")
lavaS = pygame.image.load("lavaS.jpg")
lavaR = pygame.image.load("lavaR.jpg")
roccia = pygame.image.load("roccia.jpg")
rocciaS = pygame.image.load("rocciaS.jpg")
rocciaR = pygame.image.load("rocciaR.jpg")
character = pygame.image.load("info_character.png")


dim_blocco_x, dim_blocco_y, dim_blocco = 100, 100, 100
erba = pygame.transform.scale(erba, (dim_blocco_x, dim_blocco_y))
erbaS = pygame.transform.scale(erbaS, (dim_blocco_x, dim_blocco_y))
lava = pygame.transform.scale(lava, (dim_blocco_x, dim_blocco_y))
lavaS = pygame.transform.scale(lavaS, (dim_blocco_x, dim_blocco_y))
lavaR = pygame.transform.scale(lavaR, (dim_blocco_x, dim_blocco_y))
roccia = pygame.transform.scale(roccia, (dim_blocco_x, dim_blocco_y))
rocciaS = pygame.transform.scale(rocciaS, (dim_blocco_x, dim_blocco_y))
rocciaR = pygame.transform.scale(rocciaR, (dim_blocco_x, dim_blocco_y))
paesaggio = pygame.transform.scale(paesaggio, (WIDTH, HEIGHT))
montagna = pygame.transform.scale(montagna, (WIDTH, HEIGHT))
vulcano = pygame.transform.scale(vulcano, (WIDTH, HEIGHT))


texture = []
texture.append(erba)
texture.append(erbaS)
texture.append(roccia)
texture.append(rocciaS)
texture.append(lava)
texture.append(lavaS)
texture.append(rocciaR)
texture.append(lavaR)


terreno = Terreno("mappa.txt", texture, dim_blocco)
mat = ottieni_lista_blocchi("mappa.txt")
character = Personaggio(100, GROUND)
FPS = 60
clock = pygame.time.Clock()
run = True
conta = 0
font = pygame.font.SysFont(None, 36)


while run:

    clock.tick(FPS)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYUP:
            tasto_lasciato = pygame.key.name(event.key)
            print(f"tasto lasciato: {tasto_lasciato}")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.jump() 

    key_pressed = pygame.key.get_pressed()

    if WIDTH - conta < 0:
        conta = 0
    
    screen.blit(paesaggio, (0 - conta, 0))
    screen.blit(paesaggio, (WIDTH - conta, 0))

    screen.blit(montagna, (6200 - conta + 1, 0))
    screen.blit(montagna, (6200 + WIDTH - conta + 1, 0))
    
    screen.blit(vulcano, (15700 - conta + 1, 0))
    screen.blit(vulcano, (15700 + WIDTH - conta + 1, 0))
    
    # for i in range(len(mat)):
    #     for j in range(len(mat[i])):
    #         print(mat[i], end = "")
    #     print()
    
    character.aggiorna_posizione_salto()
    terreno.draw_terreno(screen)
    character.draw(screen)
    conta += VEL
    
    for i in range(len(terreno.lista1)):
        for j in range(len(terreno.lista1[i])):
            if terreno.lista1[i][j][0] != None:
                terreno.lista1[i][j][0].x -= VEL

    for i in range(len(terreno.lista1)):
        for j in range(len(terreno.lista1[i])):
            
    #terreno.lista1[i][0].collide_rect()

    pygame.display.flip()
    pygame.display.update()

pygame.quit()
