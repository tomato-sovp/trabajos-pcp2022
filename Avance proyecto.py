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
surface=pygame.display.set_mode((500,300))
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
        self.pos=vec((10,280))
        self.acc=vec(0,0)
        self.vel=vec(0,0)
    #Definir la función para que se mueva
    def move(self):
        self.acc=vec(0,0.5)
        pressed=pygame.key.get_pressed()
        #Definir qué pasa según qué tecla se presione
        if pressed[K_LEFT]:
            self.acc.x=-acc
        if pressed[K_RIGHT]:
            self.acc.x=acc
        #Toda la parte vinculada a la física de la función (fricción, aceleración, velocidad)
        self.acc.x+=self.vel.x*fric
        self.vel+=self.acc
        self.pos+=self.vel+0.5*self.acc
        self.rect.midbottom=self.pos
        if self.pos.x > 500:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 500
        self.rect.midbottom = self.pos
    def colision(self, sprite2):
        col = pygame.sprite.collide_rect(self, sprite2)
        if col == True:
            self.vel.y = 0
            self.pos.y=sprite2.rect.top+1
class Suelo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((500, 20))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (250, 290))
#Crear al "jugador"
cubito1=Cubito()
suelo=Suelo()
platforms=pygame.sprite.Group()
platforms.add(suelo)
#Establecer el loop principal del juego
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    surface.fill((0,0,0))
    surface.blit(suelo.surf, suelo.rect)
    surface.blit(cubito1.surf, cubito1.rect)
    cubito1.move()
    cubito1.colision(suelo)
    pygame.display.update()
    fps.tick(60)