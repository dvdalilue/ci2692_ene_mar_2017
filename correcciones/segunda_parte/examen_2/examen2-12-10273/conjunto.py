"""
# Descripcion: Implementacion de un conjuto matematico finito
# Autor: Jesus Kauze 
# email: 12-10273@usb.ve 
"""
class Apuntador(object):
	def __init__(self, key, siguiente):
		self.next = siguiente
		self.key = key

class Conjunto(object):
	def __init__(self):
		self.nill = Apuntador(None, None) 
		self.conjunto = []
		self.nill.next = self.nill
		self.count = 0
		self.actual = self.nill
		self.intersectado = []

	def crearconjunto(self): #Crea el conjunto sobre el cual se guardan los valores (apuntadores) 
		self.conjunto.append(self.nill) #El self.nill queda guardado en la posicion 0 de la lista
		self.actual.next = self.nill

	def agregar(self, entero):
		self.count += 1 
		self.actual.next = Apuntador(entero, self.nill)
		self.actual = self.actual.next
		self.conjunto.append(Apuntador(entero, self.nill))
		#el head es el self.nill.next cuando se agrega el primer elemento

	def pertenece(self, entero):
		x = self.nill.next
		while x != self.nill:
			x = x.next
			if x.key == entero:
				print("\nencontro al entero\n")
				return True
		print("\nno lo encontro\n")
		return False

	def union(self,c):
		for i in self.conjunto:
			for j in c:
				if j == i.key:
					c.remove(j)
		c_apuntador = []
		for i in c:
			c_apuntador.append(Apuntador(i, self.nill))
		for i in range(len(c_apuntador)):
			try:
				c_apuntador[i].next = c_apuntador[i+1]
			except:
				c_apuntador[i].next = self.nill
		self.actual.next = c_apuntador[0]
		self.actual = c_apuntador[len(c_apuntador)-1]
		self.nill.next = self.conjunto[1]

	def interseccion(self,c):
		for i in self.conjunto:
			for j in c:
				if j == i.key:
					self.intersectado.append(i)
		for i in range(len(self.intersectado)):
			try:
				self.intersectado[i].next = self.intersectado[i+1]
			except:
				self.intersectado[i].next = self.nill
		self.nill.next = self.intersectado[0]
	
	def mostrar(self):
		x = self.nill.next
		while x != self.nill:
			print(x.key)
			x = x.next
		return 


