import pygame

ALTEZZA_TESTO = 6
LUNGHEZZA_TESTO = 271

class Terreno:
    def __init__(self, testo, texture, dim):
        
        self.testo = testo
        self.texture = texture
        self.dim = dim
        self.lista1 = []
        
        for _ in range(ALTEZZA_TESTO):
            self.lista1.append([])
        
        with open(self.testo, "r", encoding = "utf-8") as f:
            i = 0
            for riga in f:
                riga = riga.strip()
                j = 0
                for num in riga:
                    num = int(num)
                    if num != 0:
                        self.lista1[i].append([pygame.Rect(j * self.dim, i * self.dim, self.dim, self.dim), self.texture[num - 1]])
                    else:
                        self.lista1[i].append([None, None])
                    j += 1
                i += 1
        f.close()

    def draw_terreno(self, screen):
        for i in range(ALTEZZA_TESTO):
            for j in range(LUNGHEZZA_TESTO):
                if self.lista1[i][j][0] != None:
                    # print(self.lista[i][j][0].x, self.lista[i][j][0].y, self.lista[i][j][-1])
                    screen.blit(self.lista1[i][j][-1], (self.lista1[i][j][0].x, self.lista1[i][j][0].y))
