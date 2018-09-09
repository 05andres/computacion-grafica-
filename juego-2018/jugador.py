import pygame

RES=[800,600]
CENTRO=[400,300]
BLACK=[0,0,0]
RED=[255,0,0]


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
class Jugador2(pygame.sprite.Sprite):
    def __init__(self, sabana):
		pygame.sprite.Sprite.__init__(self)
		self.i = 0
		self.m = 0
		self.s = sabana
		self.image = self.s[0][0]
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 250
		self.vel_x = 0
		self.vel_y = 0
		self.parada=0
		self.movimiento=0
		self.ANCHO=900
		self.ALTO=600
		self.salud=50
    def update(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y

		if self.movimiento == 1:
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
		else:
			if self.parada == 0:
				self.i=0
				self.m=0
		if self.rect.x >= (self.ANCHO-128):
			self.rect.x=self.ANCHO-128

		if self.rect.x <= 0:
			self.rect.x=0
		if self.rect.y >=(self.ALTO-64):
			self.rect.y=self.ALTO-68
		if self.rect.y <= 32:
			self.rect.y=32
		self.image = self.s[self.m][self.i]



class Jugador(pygame.sprite.Sprite):
	def __init__(self, sabana):
		pygame.sprite.Sprite.__init__(self)
		self.i = 0
		self.m = 0
		self.s = sabana
		self.image = self.s[0][0]
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 250
		self.vel_x = 0
		self.vel_y = 0
		self.parada=0
		self.movimiento=0
		self.ANCHO=900
		self.ALTO=600
		self.salud=50

	def update(self):
		self.rect.x += self.vel_x
		self.rect.y += self.vel_y

		if self.movimiento == 1:
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
		else:
			if self.parada == 0:
				self.i=0
				self.m=0
		if self.rect.x >= (self.ANCHO-128):
			self.rect.x=self.ANCHO-128

		if self.rect.x <= 0:
			self.rect.x=0
		if self.rect.y >=(self.ALTO-64):
			self.rect.y=self.ALTO-68
		if self.rect.y <= 32:
			self.rect.y=32
		self.image = self.s[self.m][self.i]

class bala(pygame.sprite.Sprite):
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
		self.image = self.s[self.m][self.i]

class explosion(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.explosion = "imagenes/explosion.png"
        self.e=Recortar(self.explosion,23,21)
        self.i = 0
        self.m = 0
        self.t=self.e
        self.image = self.e[0][0]
        self.rect= self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]



    def update(self):
        if self.m == 0:
            self.i += 1
            if self.i == 6:
                self.kill()

        self.image = self.e[self.m][self.i]
class explosionArbol(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.explosion = "imagenes/arbol.png"
        self.e=Recortar(self.explosion,64,64)
        self.i = 0
        self.m = 2
        self.t=self.e
        self.image = self.e[0][0]
        self.rect= self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]



    def update(self):
        if self.m == 2:
            self.i += 1
            if self.i == 3:
                self.kill()

        self.image = self.e[self.m][self.i]

class arbol(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.arbol = "imagenes/arbol.png"
        self.b=Recortar(self.arbol,64,64)
        self.s = self.b
        self.image = self.s[0][0]
        self.rect = self.image.get_rect()

class posimavida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    	self.moster = "imagenes/pociones.png"
        self.b=Recortar(self.moster,24,25)
        self.s = self.b
        self.image = self.s[3][0]
        self.rect = self.image.get_rect()

class posimavele(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    	self.moster = "imagenes/pociones.png"
        self.b=Recortar(self.moster,24,25)
        self.s = self.b
        self.image = self.s[0][3]
        self.rect = self.image.get_rect()
class posimademage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    	self.moster = "imagenes/pociones.png"
        self.b=Recortar(self.moster,24,25)
        self.s = self.b
        self.image = self.s[9][0]
        self.rect = self.image.get_rect()


class Barril(pygame.sprite.Sprite):
	def __init__(self,barril):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(barril)
		self.rect = self.image.get_rect()
		self.rect.x = 150
		self.rect.y = 200

class princesas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    	self.moster = "imagenes/princesa.png"
        self.b=Recortar(self.moster,32,49)
        self.i = 0
        self.m = 0
        self.s = self.b
        self.image = self.s[0][0]
        self.rect = self.image.get_rect()


    def update(self):

        if self.m == 0:
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
        self.image = self.s[self.m][self.i]
class Barril(pygame.sprite.Sprite):
	def __init__(self,barril):

		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(barril)
		self.rect = self.image.get_rect()
		self.rect.x = 150
		self.rect.y = 200
class Barravida(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.v1="imagenes/vida1.png"
        self.v2="imagenes/vida2.png"
        self.v3="imagenes/vida3.png"
        self.v4="imagenes/vida4.png"
        self.v5="imagenes/vida5.png"
        self.m=0
        self.vida=self.v1
        self.image=pygame.image.load(self.vida)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if self.m==0:
            self.vida=self.v1
        if self.m==1:
            self.vida=self.v2
        if self.m==2:
            self.vida=self.v3
        if self.m==3:
            self.vida=self.v4
        if self.m==4:
            self.vida=self.v5
        self.image=pygame.image.load(self.vida)
