import pygame

ALTEZZA_TESTO = 6
LUNGHEZZA_TESTO = 271

def ottieni_lista_blocchi(s):
    
    with open(s, "r", encoding="utf-8") as f:
        righe = f.readlines()
    
    righe = [riga.strip() for riga in righe]
    mat = []

    for riga in righe:
        tmp1 = []
        for num in riga:
            tmp1.append(num)
        mat.append(tmp1)

    mat_giusta = []

    for i in range(LUNGHEZZA_TESTO):
        tmp2 = []
        for j in range(ALTEZZA_TESTO):
            tmp2.append(mat[j][i])
        mat_giusta.append(tmp2)
        
    f.close()
    return mat_giusta

# 1 8 2
# 4 4 2 
# 5 7 2
        # tmp = []
        # for riga in f:
        #     riga = riga.strip()
        #     for num in riga:
        #         tmp.append(num)
        #     mat.append(tmp)