##Laboratorio 6
##Miranda Coloma 4° Medio B
#Dibujar en PyGame
import pygame
#iniciar PyGame
pygame.init()
#hacer la pantalla donde se verá el "juego"
ventana=pygame.display.set_mode((400,300))
#declarar el loop principal
while True:
    #dibujar la figura
    pygame.draw.rect(ventana, (255,255,255), (40,80,60,60))
    pygame.display.flip()