import pygame

WIDTH, HEIGHT = 1200, 600

ALTEZZA_TESTO = 6
LUNGHEZZA_TESTO = 271

# def ottieni_lista_blocchi(s):   # [[rect, texture], [...], ...]
    
#     with open(s, "r", encoding="utf-8") as f:
#         righe = f.readlines()
    
#     righe = [riga.strip() for riga in righe]
#     mat = []

#     for riga in righe:
#         tmp1 = []
#         for num in riga:
#             tmp1.append(num)
#         mat.append(tmp1)

#     mat_giusta = []

#     for i in range(LUNGHEZZA_TESTO):
#         tmp2 = []
#         for j in range(ALTEZZA_TESTO):
#             tmp2.append(mat[j][i])
#         mat_giusta.append(tmp2)
    
#     f.close()
#     return mat_giusta


def blocco_sotto(x, lista = [], texture = []):
    ymin = HEIGHT
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j][0] != None:
                if x >= lista[i][j][0].x and x <= lista[i][j][0].x + lista[i][j][0].width:
                    if lista[i][j][0].y < ymin:
                        ymin = lista[i][j][0].y
                        
                    # if lista[i][j][1] == texture[0] or lista[i][j][1] == texture[2] or lista[i][j][1] == texture[4]:
                    #     return lista[i][j][0].y - 100

    return ymin


def sta_collidendo(rect, lista):
    lista = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(lista[i][j][0])
            if lista[i][j][0] != None:
                print(1)
                if rect.colliderect(lista[i][j][0]) or rect.bottom == lista[i][j][0].top:
                    lista.append([rect, lista[i][j][0], lista[i][j][1]])
                    print(2)
    return lista



def get_collision_side(rect1, rect2):
    """
    Determina quale lato di rect1 è in collisione o adiacente a rect2.

    Args:
    rect1 (pygame.Rect): Il primo rettangolo.
    rect2 (pygame.Rect): Il secondo rettangolo.

    Returns:
    str: Il lato di rect1 che è in collisione o adiacente a rect2 ('top', 'bottom', 'left', 'right') o None se non c'è collisione o adiacenza.
    """
    # Controllo collisione
    if rect1.colliderect(rect2):
        # Distanze tra i bordi dei rettangoli
        dx = (rect1.centerx - rect2.centerx) / rect2.width
        dy = (rect1.centery - rect2.centery) / rect2.height

        # Determina quale lato ha la collisione più significativa
        if abs(dx) > abs(dy):
            if dx > 0:
                return 'left'
            else:
                return 'right'
        else:
            if dy > 0:
                return 'top'
            else:
                return 'bottom'
    else:
        # Controllo adiacenza
        if rect1.right == rect2.left:
            return 'right'
        elif rect1.left == rect2.right:
            return 'left'
        elif rect1.bottom == rect2.top:
            return 'bottom'
        elif rect1.top == rect2.bottom:
            return 'top'
    
    return None

