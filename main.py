import pygame
from terreno import Terreno
from personaggio import Personaggio
from funzioni import blocco_sotto, sta_collidendo, get_collision_side
from pterodattilo import Pterodattilo
from coins import Moneta
import random
pygame.init()

WIDTH, HEIGHT = 1200, 600
VEL = 6   
GRAVITÀ = 1


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Videogame")
paesaggio = pygame.image.load("sfondo.jpg")
montagna = pygame.image.load("montagna.jpg")
vulcano = pygame.image.load("vulcano1.jpg")
erba = pygame.image.load("erba.jpg")
erbaS = pygame.image.load("erbaS.jpg")
lava = pygame.image.load("lava.jpg")
lavaS = pygame.image.load("lavaS.jpg")
roccia = pygame.image.load("roccia.jpg")
rocciaS = pygame.image.load("rocciaS.jpg")
character = pygame.image.load("info_character.png")


dim_blocco_x, dim_blocco_y, dim_blocco = 100, 100, 100
erba = pygame.transform.scale(erba, (dim_blocco_x, dim_blocco_y))
erbaS = pygame.transform.scale(erbaS, (dim_blocco_x, dim_blocco_y))
lava = pygame.transform.scale(lava, (dim_blocco_x, dim_blocco_y))
lavaS = pygame.transform.scale(lavaS, (dim_blocco_x, dim_blocco_y))
roccia = pygame.transform.scale(roccia, (dim_blocco_x, dim_blocco_y))
rocciaS = pygame.transform.scale(rocciaS, (dim_blocco_x, dim_blocco_y))
paesaggio = pygame.transform.scale(paesaggio, (WIDTH, HEIGHT))
montagna = pygame.transform.scale(montagna, (WIDTH, HEIGHT))
vulcano = pygame.transform.scale(vulcano, (WIDTH, HEIGHT))


texture = []
texture.append(erba)
texture.append(roccia)
texture.append(lava)
# texture.append(erbaS)
# texture.append(rocciaS) 
# texture.append(lavaS)

terreno = Terreno("mappa.txt", texture, dim_blocco)
# terreno.lista = ottieni_lista_blocchi("mappa.txt")
character = Personaggio(0, HEIGHT - 200)
FPS = 60
clock = pygame.time.Clock()
run = True
conta = 0

ticks = pygame.time.get_ticks()
conta_secondi = 0

WHITE = (200, 200, 200)
NERO = (0, 0, 0)
FORZA_SALTO = -10  

font = pygame.font.SysFont("Showcard Gothic", 48)
velocita_y = 0
a_terra = False
pos_corrente = 0
is_jumping = False
h_salto = 200

# character.falling = True
# character.jump_speed = 0

jump_speed = 0
lista_pt = []
lista_coins = []
tempo = 0
punteggio = 0
rubbish = []

while run:

    clock.tick(FPS)
    
    secondi = (pygame.time.get_ticks() - ticks) // 1000

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYUP:
            tasto_lasciato = pygame.key.name(event.key)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.salta()

    character.aggiorna()        
    key_pressed = pygame.key.get_pressed()
    tmp_lista = sta_collidendo(character.rect, terreno.lista)
    
    for i in range(len(terreno.lista)):
        for j in range(len(terreno.lista[i])):
            if terreno.lista[i][j][0] != None:
                collisione = get_collision_side(terreno.lista[i][j][0], character.rect)
                # if collisione == "top":
                #     print("su")

    for i in range(len(tmp_lista)):
        if tmp_lista[i][2] == texture[5]:
            run = False
    # if is_jumping == False:
    #     character.rect.y += GRAVITÀ

    # character.velocita_y += GRAVITÀ
    # character.rect.y += character.velocita_y

    # if character.rect.y >= HEIGHT - character.rect.y:
    #     character.rect.y = HEIGHT - character.rect.y
    #     character.velocita_y = 0
    #     a_terra = True

    if tempo != 0 and int(tempo) % 10 == 0 and int(tempo) == conta_secondi / 15:
        p = Pterodattilo([VEL*-2, 0], pygame.Rect(WIDTH, random.randint(380, 400), 80, 100))
        lista_pt.append(p)

    if tempo != 0 and int(tempo) % 25 == 0 and int(tempo) == conta_secondi / 15:
        coin = Moneta([VEL*-1, 0], pygame.Rect(WIDTH, HEIGHT - random.randint(175, 450), 80, 80))
        lista_coins.append(coin)


    for p in lista_pt:
        p.move()

    for coin in lista_coins:
        coin.move()
    
    # i quadrati si muovono verso sinistra

    for i in range(len(lista_pt)):
        if character.rect.colliderect(lista_pt[i].rect):
            run = False 

    for i in range(len(lista_coins)):
        if character.rect.colliderect(lista_coins[i].rect):
            punteggio += 30
            rubbish.append(lista_coins[i])

    for r in rubbish:
        lista_coins.remove(r)

    rubbish.clear()

    for i in range(len(terreno.lista)):
        for j in range(len(terreno.lista[i])):
            if terreno.lista[i][j][0] != None:
                terreno.lista[i][j][0].x -= VEL
                VEL += 0.00001  
                
    conta_secondi += 1
    tempo = conta_secondi // 15

    if WIDTH - conta < 0:
        conta = 0
    
    sfondo = paesaggio

    screen.blit(sfondo, (0 - conta, 0))
    screen.blit(sfondo, (WIDTH - conta, 0))

    # cambio sfondo
    if tempo > 75 and tempo < 160:
        sfondo = montagna
        screen.blit(sfondo, (0 - conta, 0))
        screen.blit(sfondo, (WIDTH - conta, 0))

    if tempo >= 160:
        sfondo = vulcano
        screen.blit(sfondo, (0 - conta, 0))
        screen.blit(sfondo, (WIDTH - conta, 0))
        
    # stampa oggetti
    scritta = font.render(f"Score: {tempo + punteggio}", True, NERO)
    rettangolo_scritta = scritta.get_rect()
    screen.blit(scritta, (WIDTH - rettangolo_scritta.width - 10, 10))

    ground = blocco_sotto(character.rect.x, terreno.lista, texture)
    character.stop_y = ground - character.rect.height
    
    # character.aggiorna_posizione_salto(ground)

    terreno.draw_terreno(screen)
    character.draw(screen)
    conta += VEL

    for p in lista_pt:
        p.draw(screen)

    for coin in lista_coins:
        coin.draw(screen)

    # # collisioni
    # for i in range(len(terreno.lista)):
    #     for j in range(len(terreno.lista[i])):
            
    #         if terreno.lista[i][j][0] != None:

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[0]:
    #                 character.rect.y = terreno.lista[i][j][0][1] - 100

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[2]:
    #                 character.rect.y = terreno.lista[i][j][0][1] - 100

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[4]:
    #                 character.rect.y = terreno.lista[i][j][0][1] - 100

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[1]:
    #                 run = False

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[3]:
    #                 run = False

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[5]:
    #                 run = False

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[6]:
    #                 run = False

    #             if terreno.lista[i][j][0].colliderect(character.rect) and terreno.lista[i][j][1] == texture[7]:
    #                 run = False

    #             if terreno.lista[i][j][0] == None:
    #                 character.rect.y = terreno.lista[i][j][-1][1]
                
    #                 if character.rect.y == HEIGHT:
    #                     run = False
    #             # pos_corrente += terreno.lista[i][j][0][0]

    #             # if int(terreno.lista[i+1][j][0]) > int(terreno.lista[i][j][0]):
    #             #     character.rect.y = terreno.lista[i][j][0].y - 100

    #             # if int(terreno.lista[i+1][j][0]) < int(terreno.lista[i][j][0]):
    #             #     character.rect.y = terreno.lista[i][j][0].y + 100

    
    if character.rect.y > HEIGHT - character.rect.height:
        run = False

    pygame.display.flip()
    pygame.display.update()

pygame.quit()