import pygame as pg
pg.init()
#pantalla
surface=pg.display.set_mode((400,300))
#colores
c_pasto=(19,173,35)
c_caja=(163,128,67)
#dibujos
while True:
  pasto=pg.draw.line(surface,c_pasto,(0,380),(400,380),3)
  #cajita=pg.draw.rect(surface,c_caja,pg.rect(30,30,60,60))
  pg.display.flip()