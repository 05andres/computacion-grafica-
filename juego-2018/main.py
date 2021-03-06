import pygame
from pygame.locals import *
import math
import random
from jugador import *
from enemigo import *
ROJO=[250,0,0]
AZUL=[0,0,255]
VERDE=(0,255,0)
BLANCO=[255,255,255]
NEGRO=[0,0,0]
ANCHO=900
ALTO=600
puntos=0
pantalla=pygame.display.set_mode([ANCHO,ALTO])

def Recortar(archivo_img,cr_an,cr_al):

    image= pygame.image.load(archivo_img)
    ancho_img, alto_img=image.get_size()
    lon_x=ancho_img/cr_an
    lon_y=alto_img/cr_al
    m=[]
    for j in range(lon_y):
        fila=[]
        for i in range(lon_x):
            plantilla=image.subsurface(0+(i*cr_an),0+(j*cr_al),cr_an,cr_al)
            fila.append(plantilla)
        m.append(fila)
    return m

def pausa():
    pausado=True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    pausado=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        pantalla.fill(BLANCO)




if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    reloj=pygame.time.Clock()
    fondo=pygame.image.load('imagenes/mapa.png')
    info= fondo.get_rect()
    fuente1=pygame.font.SysFont("Arial",20,True,False)
    textime=fuente1.render("TIME :",0,ROJO)
    fuente=pygame.font.SysFont("Arial",10,True,False)
    textime2=fuente.render("Andres:",0,ROJO)
    textime3=fuente1.render("rescatadas:",0,ROJO)


    fin=False
    pos_x=0
    pos_y=-50
    rango=30
    cont=0
    #imagenes de items
    imagen = "imagenes/jugador.png"
    #proyectil1 = "imagenes/PROYECTIL.png"
    barril = "imagenes/barel.png"
    #grupos de personajes y obstaculos e modificadores
    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    obstaculos = pygame.sprite.Group()
    balas=pygame.sprite.Group()
    enemigos1=pygame.sprite.Group()
    princes=pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()
    balas_ene=pygame.sprite.Group()
    posionvida=pygame.sprite.Group()
    posionvele=pygame.sprite.Group()
    posiondemage=pygame.sprite.Group()
    arboles=pygame.sprite.Group()
    arboles2=pygame.sprite.Group()
    arboles3=pygame.sprite.Group()
    movibles=pygame.sprite.Group()

    arbol1=arbol()
    arbol1.rect.x=400
    arbol1.rect.y=300
    arboles2.add(arbol1)
    todos.add(arbol1)
    movibles.add(arbol1)
    #imagenes barra vida
    '''v1="imagenes/vida1.png"
    v2="imagenes/vida2.png"'''
    vidas=Barravida()
    todos.add(vidas)



    arbol2=arbol()
    arbol2.rect.x=1000
    arbol2.rect.y=500
    arboles.add(arbol2)
    todos.add(arbol2)
    movibles.add(arbol2)

    arbol3=arbol()
    arbol3.rect.x=1300
    arbol3.rect.y=900
    arboles3.add(arbol3)
    todos.add(arbol3)
    movibles.add(arbol3)

    #musica
    sonido = pygame.mixer.Sound("musica/juego.wav")
    sonido.play()
    disparo = pygame.mixer.Sound("musica/disparo.wav")
    explosionN=pygame.mixer.Sound("musica/explosionN.wav")
    explosionar=pygame.mixer.Sound("musica/explosionar.wav")









    #recortes de los sprite
    m=Recortar(imagen,32,48)
    #b=Recortar(proyectil1,64,64)
    #personajes utlizados
    jugador = Jugador(m)
    #princesas a rescatar
    cantidad_princesas=10
    for i in range(cantidad_princesas):
        pri=princesas()

        pri.rect.x=random.randrange(0,1800)
        pri.rect.y=random.randrange(0,1000)
        pri.m=0
        princes.add(pri)
        todos.add(pri)
        movibles.add(pri)
    #crear mostruo enemigo estatico
    cantidad_mostruos=10
    for i in range (cantidad_mostruos):

        mos=mostruo(6)
        mos.rect.x=random.randrange(50,2000)
        mos.rect.y=1000
        mos.m=6
        todos.add(mos)
        enemigos2.add(mos)
        movibles.add(mos)

    #crear la estanpida enemigo dinamico
    cantidad_enemigos=50
    for i in range (cantidad_enemigos):
        e1= buffalo()
        e1.rect.x=1800
        e1.rect.y=random.randrange(100,1000)
        enemigos1.add(e1)
        todos.add(e1)
        movibles.add(e1)


    #obstaculos para el mapa
    cantidad_barriles=15
    for s in range(cantidad_barriles):
        obstaculo=Barril(barril)
        obstaculo.rect.x=random.randrange(0,1800)
        obstaculo.rect.y=random.randrange(0,1000)
        obstaculos.add(obstaculo)
        todos.add(obstaculo)
        movibles.add(obstaculo)
    #adicion a los grupos
    jugadores.add(jugador)
    todos.add(jugador)



    #variables auxiliares
    bandera=False
    bandera1=False
    bandera2=False
    bandera3=False
    parada=0
    varx=5
    vary=5
    velocidad=10
    var_x=10
    demage=0

    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    print 'letra a'
                if event.key==pygame.K_SPACE:
                    b=bala([jugador.rect.x-16,jugador.rect.y],parada)
                    disparo.play()
                    b.m=demage
                    todos.add(b)
                    balas.add(b)
                    movibles.add

                if event.key==pygame.K_UP:
                    jugador.vel_y=-velocidad
                    jugador.movimiento=1
                    jugador.m=3
                    parada=3
                    bandera3=True
                if event.key==pygame.K_DOWN:
                    jugador.vel_y=velocidad
                    jugador.movimiento=1
                    jugador.m=0
                    parada=0
                    bandera2=True
                if event.key==pygame.K_RIGHT:
                    jugador.vel_x=velocidad
                    jugador.movimiento=1
                    jugador.m=2
                    parada=2
                    bandera1=True
                if event.key==pygame.K_LEFT:
                    jugador.vel_x=-velocidad
                    jugador.movimiento=1
                    jugador.m=1
                    jugador.i+=1
                    parada=1
                    bandera=True
                if event.key == pygame.K_p:
                    pausa()
                if event.key==pygame.K_m:
                    for z in jugadores:
                        ls_jp=pygame.sprite.spritecollide(z,princes,True)
                    for salvada in ls_jp:
                        puntos+=1
                        print puntos
                        todos.remove(salvada)
                        princes.remove(salvada)
                    if puntos >= 10:
                        print 'salvaste a las princesas'
                        puntos=0

            if event.type==pygame.KEYUP:
                jugador.vel_y=0
                jugador.vel_x=0
                jugador.movimiento=0
                jugador.parada=parada
                bandera=False
                bandera1=False
                bandera2=False
                bandera3=False
        #tiempo del juego
        ticks = pygame.time.get_ticks()/1000
        if ticks == 60:
            print 'perdio'


        if jugador.salud <= 50 and jugador.salud>40:
            vidas.m=0
        if jugador.salud <= 40 and jugador.salud>30:
            vidas.m=1
        if jugador.salud <= 30 and jugador.salud>20:
            vidas.m=2
        if jugador.salud <= 20 and jugador.salud>10:
            vidas.m=3
        if jugador.salud <= 10 and jugador.salud>=0:
            vidas.m=4

        #variable eliminados enemigos para la regenerecion
        eliminados=0
        #parte que establece el limite y movimiento de la plataforma
        posi=[jugador.rect.x,jugador.rect.y]
        if jugador.movimiento == 1:
            if posi[0] <= ANCHO/2 and pos_x <= 0 and bandera==True:
                pos_x+=var_x
                for i in movibles:
                    i.rect.x+=var_x
            if posi[0] >= ANCHO/2  and pos_x >= (ANCHO-info[2]) and bandera1==True:
                pos_x-=var_x
                for i in movibles:
                    i.rect.x-=var_x
            if posi[1] <= ALTO/2 and pos_y <= 0 and bandera3==True:
                pos_y+=var_x
                for i in movibles:
                    i.rect.y+=var_x
            if posi[1] >= ALTO/2 and pos_y >= (ALTO-info[3]) and bandera2==True:
                pos_y-=var_x
                for i in movibles:
                    i.rect.y-=var_x







        #limistes bala jugador
        for i in balas:

            if i.rect.x>ANCHO:
                balas.remove(i)
                todos.remove(i)
            if i.rect.x<0:
                balas.remove(i)
                todos.remove(i)
            if i.rect.y>ALTO:
                balas.remove(i)
                todos.remove(i)
            if i.rect.y<0:
                balas.remove(i)
                todos.remove(i)
        #limistes bala enemigos
        for i in balas_ene:

            if i.rect.x>2016:
                balas_ene.remove(i)
                todos.remove(i)
                movibles.remove(i)
                i.kill()
            if i.rect.x<0:
                balas_ene.remove(i)
                todos.remove(i)
                movibles.remove(i)
                i.kill()
            if i.rect.y>1088:
                balas_ene.remove(i)
                todos.remove(i)
                movibles.remove(i)
                i.kill()
            if i.rect.y<0:
                balas_ene.remove(i)
                todos.remove(i)
                movibles.remove(i)
                i.kill()
        #limite del buffalo para limpiar memoria
        for e in enemigos1:
            if e.rect.x<0 :
                enemigos1.remove(e)
                todos.remove(e)
                movibles.remove(e)
                eliminados+=1




        for i in range (eliminados):
            e1= buffalo()
            e1.rect.x=1800
            e1.rect.y=random.randrange(20,1000)
            enemigos1.add(e1)
            todos.add(e1)
            movibles.add(e1)

        hits=pygame.sprite.groupcollide(enemigos1,balas,True,True)
        for hit in hits:
            explosionN.play()
            e=explosion([hit.rect.x,hit.rect.y])
            todos.add(e)
            todos.remove(hit)
            balas.remove(hit)
            movibles.remove(hit)
            hit.kill()

        hits2=pygame.sprite.groupcollide(obstaculos,balas,True,True)
        for hit in hits2:
            explosionN.play()
            e=explosion([hit.rect.x,hit.rect.y])
            todos.add(e)
            todos.remove(hit)
            movibles.remove(hit)
            hit.kill()
        #Generar las balas de enemigos
        for i in enemigos2:
            if  i.disparar == True:

                #crear bala
                p=bala_ene([i.rect.x-16,i.rect.y],3)
                p.var_y=10
                p.m=10
                todos.add(p)
                balas_ene.add(p)
                movibles.add(p)
                i.disparar=False
                i.temp=random.randrange(rango)
        hits3=pygame.sprite.groupcollide(arboles,balas,True,True)
        #crear la primera posimavida
        for hit in hits3:
            e=explosion([hit.rect.x,hit.rect.y])
            todos.add(e)
            explosionar.play()
            l=explosionArbol([hit.rect.x,hit.rect.y])
            todos.add(l)
            todos.remove(hit)
            balas.remove(hit)
            hit.kill()
            arboles.remove(hit)
            movibles.remove(hit)
            posion1=posimavida()
            posion1.rect.x=hit.rect.x+10
            posion1.rect.y=hit.rect.y+5
            posionvida.add(posion1)
            todos.add(posion1)
            movibles.add(posion1)
        #crea la segunda posionvele
        hits4=pygame.sprite.groupcollide(arboles2,balas,True,True)
        for hit in hits4:
            e=explosion([hit.rect.x,hit.rect.y])
            todos.add(e)
            explosionar.play()
            l=explosionArbol([hit.rect.x,hit.rect.y])
            todos.add(l)
            todos.remove(hit)
            balas.remove(hit)
            hit.kill()
            arboles.remove(hit)
            movibles.remove(hit)
            posion2=posimavele()
            posion2.rect.x=hit.rect.x+10
            posion2.rect.y=hit.rect.y+5
            posionvele.add(posion2)
            todos.add(posion2)
            movibles.add(posion2)
        hits5=pygame.sprite.groupcollide(arboles3,balas,True,True)
        for hit in hits5:
            e=explosion([hit.rect.x,hit.rect.y])
            todos.add(e)
            explosionar.play()
            l=explosionArbol([hit.rect.x,hit.rect.y])
            todos.add(l)
            todos.remove(hit)
            balas.remove(hit)
            hit.kill()
            arboles.remove(hit)
            movibles.remove(hit)
            posion3=posimademage()
            posion3.rect.x=hit.rect.x+10
            posion3.rect.y=hit.rect.y+5
            posiondemage.add(posion3)
            todos.add(posion3)
            movibles.add(posion3)


        '''hits2=pygame.sprite.groupcollide(jugadores,balas_ene,True,True)
        for hit in hits2:
            e=explosion([hit.rect.x,hit.rect.y])
            todos.add(e)
            todos.remove(hit)'''


        '''for c in balas:
            ls_bo=pygame.sprite.spritecollide(c,obstaculos,True)
        for d in obstaculos:
            ls_b2=pygame.sprite.spritecollide(d,balas,True)'''

        for b in jugadores:
            ls_je=pygame.sprite.spritecollide(b,balas_ene,True)

            for u in ls_je:
                e=explosion([b.rect.x,b.rect.y])
                todos.add(e)
                jugador.salud-=1

        for t in jugadores:
            ls_jpv=pygame.sprite.spritecollide(t,posionvida,True)
            for u in ls_jpv:
                u.kill()
                jugador.salud=50
                posionvida.remove(u)
                todos.remove(u)
                movibles.remove(u)
                print jugador.salud
        for t in jugadores:
            ls_jpv=pygame.sprite.spritecollide(t,posionvele,True)
            for u in ls_jpv:
                rango=100
                posionvele.remove(u)
                movibles.remove(u)
                todos.remove(u)
                print rango
        for t in jugadores:
            ls_jpd=pygame.sprite.spritecollide(t,posiondemage,True)
            for u in ls_jpd:
                demage
                print 'hola'

                posiondemage.remove(u)
                movibles.remove(u)
                todos.remove(u)

        for b in jugadores:
            ls_je=pygame.sprite.spritecollide(b,enemigos1,False)
            for u in ls_je:
                jugador.salud-=1

        if jugador.salud <= 0:
            print 'perdio'

        pantalla.fill(VERDE)
        pantalla.blit(fondo,[pos_x,pos_y])
        pantalla.blit(textime,(800,0))
        pantalla.blit(textime2,(0,0))
        pantalla.blit(textime3,(650,0))
        ticks=str(ticks)
        resca=str(puntos)
        contador=fuente1.render(ticks,0,ROJO)
        contador1=fuente1.render(resca,0,ROJO)
        pantalla.blit(contador,(860,0))
        pantalla.blit(contador1,(760,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
