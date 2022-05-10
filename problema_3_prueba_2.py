##Problema de dibujo con PyGame
##Miranda Coloma 4° Medio B
import pygame as pg
pg.init()
#pantalla
surface=pg.display.set_mode((400,300))
#colores
c_pasto=(19,173,35)
c_caja=(163,128,67)
#sprite de gato (método simple)
gato=pg.image.load("cat.png")
#dibujos y personaje en pantalla (el personaje arriba de la caja porque se ve más bonito que dentro)
while True:
  pasto=pg.draw.rect(surface,c_pasto,(0,160,400,180))
  cuadro=pg.draw.rect(surface,c_caja,(160,85,75,75))
  surface.blit(gato,(170,30))
  pg.display.flip()