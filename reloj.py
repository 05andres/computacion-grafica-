import pygame
import math

ROJO=[250,0,0]
AZUL=[0,0,255]
VERDE=(0,255,0)
BLANCO=[255,255,255]
NEGRO=[0,0,0]


ANCHO=640
ALTO=480
D=(ANCHO/2,ALTO/2)




if __name__ == '__main__':
    pygame.init()
    print 'funciona'
    #us=input('Escriba valor del escalar :')
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pag=1
    Fuente=pygame.font.Font(None,32)


    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.K_SPACE:
                pag+=1

        if pag == 1:
            texto=Fuente.render("pagina 1",True,BLANCO)
            pantalla.fill(NEGRO)
            pantalla.blit(texto,[100,100])
            pygame.display.flip()
            reloj.tick(10)
        if pag == 2:
            fin=True
