##Dibujo casa
##Miranda Coloma 4° Medio B
import pygame as pg
pg.init()
#pantalla
surface=pg.display.set_mode((400,300))
#colores
c_pasto=(19,173,35)
c_casa=(237,208,144)
c_cielo=(66,135,245)
c_techo=(232,39,39)
c_puerta=(92,53,28)
#cambiar color pantalla
surface.fill(c_cielo)
#invocar una sprite
arbol=pg.image.load("arbol.png")
#dibujo
while True:
  pasto=pg.draw.rect(surface,c_pasto,(0,160,400,180))
  casa=pg.draw.rect(surface,c_casa,(160,85,100,75))
  puerta=pg.draw.rect(surface,c_puerta,(195,115,25,45))
  techo=pg.draw.polygon(surface,c_techo,points=[(130,85),(205,40),(280,85)])
  ventana=pg.draw.rect(surface,c_cielo,(170,110,20,20))
  surface.blit(arbol,(30,35))
  pg.display.flip()