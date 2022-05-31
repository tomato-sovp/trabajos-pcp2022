##Ejercicio PyGame
##Miranda Coloma 4° Medio B
##En su mayoría, el código es sacado de la wiki de PyGame, con algunas modificaciones y la adición de comentarios
#Importar la librería
import pygame
from pygame.locals import *
import sys
#Iniciar PyGame
pygame.init()
#Iniciar la pantalla
surface=pygame.display.set_mode((250,300))
fps=pygame.time.Clock()
#Hacer vector para después mover la sprite y definir constantes
vec=pygame.math.Vector2
acc=0.3
fric=-0.10
#Construir clase de la sprite
class Cubito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf=pygame.Surface((30, 30))
        self.surf.fill((26,255,0))
        self.rect=self.surf.get_rect(center = (10, 300))
        self.pos=vec((10,300))
        self.acc=vec(0,0)
        self.vel=vec(0,0)
    #Definir la función para que se mueva
    def move(self):
        self.acc=vec(0,0)
        pressed=pygame.key.get_pressed()
        #Definir qué pasa según qué tecla se presione
        if pressed[K_LEFT]:
            self.acc.x=-acc
        if pressed[K_RIGHT]:
            self.acc.x=acc
        if pressed[K_UP]:
            self.acc.y=-acc
        if pressed[K_DOWN]:
            self.acc.y=acc
        #Toda la parte vinculada a la física de la función (fricción, aceleración, velocidad)
        self.acc.x+=self.vel.x*fric
        self.acc.y+=self.vel.y*fric
        self.vel+=self.acc
        self.pos+=self.vel+0.5*self.acc
        self.rect.midbottom=self.pos
#Crear al "jugador"
cubito1=Cubito()
#Establecer el loop principal del juego
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((0,0,0))
    surface.blit(cubito1.surf, cubito1.rect)
    cubito1.move()
    pygame.display.update()
    fps.tick(60)