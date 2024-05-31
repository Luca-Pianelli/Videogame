import pygame

def puntatore_dentro_cerchio(cerchio, pos):

    if ((pos[0] - cerchio.centro[0])**2 + (pos[1] - cerchio.centro[1])**2)**(0.5) <= cerchio.raggio:
        return True
    
    return False  