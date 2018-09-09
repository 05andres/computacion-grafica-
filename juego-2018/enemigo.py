import pygame
import math
import random
from jugador import Recortar

class buffalo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    	self.buffalo = "imagenes/redxiii.png"
        self.b=Recortar(self.buffalo,48,53)
        self.i = 0
        self.m = 1
        self.s = self.b
        self.image = self.s[0][0]
        self.rect = self.image.get_rect()
        self.vel=5
        self.vida=50


    def update(self):
        self.rect.x-=self.vel
        if self.m == 1:
            self.i += 1
            if self.i >= 2:
                self.i = 0
                self.m = 1


        self.image = self.s[self.m][self.i]
class mostruo(pygame.sprite.Sprite):
    def __init__(self,r):
        pygame.sprite.Sprite.__init__(self)
    	self.moster = "imagenes/enemigo2.png"
        self.b=Recortar(self.moster,32,32)
        self.i = 0
        self.m = 0
        self.s = self.b
        self.image = self.s[0][0]
        self.rect = self.image.get_rect()
        self.vel=5
        self.vida=50
        self.var_y=5
        self.disparar=False
        self.temp=random.randrange(100)
    def update(self):
        if self.temp < 0:
            self.disparar = True
        else:
            self.temp-=1

        if self.m == 1:
            self.i += 1
            if self.i >= 2:
                self.i = 0
                self.m = 1

        elif self.m == 0:
            self.i += 1
            if self.i > 2:
                self.i = 0
                self.m = 0
        elif self.m == 2:
            self.i += 1
            if self.i > 2:
                self.i = 0
                self.m = 2
        elif self.m == 3:
            self.i += 1
            if self.i > 2:
                self.i = 0
                self.m = 3
        elif self.m == 6:
            self.i += 1
            if self.i > 2:
                self.i = 0
                self.m = 6


        self.image = self.s[self.m][self.i]
class bala_ene(pygame.sprite.Sprite):
    def __init__(self,pos,s):
        pygame.sprite.Sprite.__init__(self)
        self.proyectil1 = "imagenes/PROYECTIL.png"
        self.b=Recortar(self.proyectil1,64,64)
        self.i = 0
        self.m = 0
        self.s = self.b
        self.image = self.s[0][0]
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.jugador=s
        self.vel=10
        self.dano=0

    def update(self):
        if self.jugador==0:
			self.rect.y+=self.vel
        elif self.jugador == 3:
			self.rect.y-=self.vel
        elif self.jugador == 1:
			self.rect.x-=self.vel
        elif self.jugador == 2:
			self.rect.x+=self.vel
        if self.m == 1:
			self.i += 1
			if self.i >= 2:
				self.i = 0
				self.m = 1
        elif self.m == 0:
            self.i += 1
            self.dano=15
            if self.i > 2:
                self.i = 0
                self.m = 0
        elif self.m == 2:
			self.i += 1
			if self.i > 2:
				self.i = 0
				self.m = 2
        elif self.m == 3:
			self.i += 1
			if self.i > 2:
				self.i = 0
				self.m = 3
        elif self.m == 10:
            self.i+=1
            if self.i>2:
                self.i=0
                self.m=10

		self.image = self.s[self.m][self.i]
