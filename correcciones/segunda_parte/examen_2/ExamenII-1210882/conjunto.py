""" Algoritmos II .ene-mar 2017 
	fecha: 30/03/2017
    Descripcion:  Conjunto es una lista enlazada simple que contiene elementos de tipo entero
	autores: Edymar Mijares 12-10882

	correo: - edys.beccaria@gmail.com
		   
Examen II"""

class NodoLista:
	def __init__(self, e, s):
		self.elemento = e
		self.siguiente = s

class Conjunto:
	def __init__(self):
		self.primero = None
		self.ultimo = None 
		self.size=0


	def Pertenece(self,e):
		x = self.primero
		Esta = False
		while x!= None:
			if x.elemento == e:
				Esta= True
			x = x.siguiente
		return Esta
		
	def Agregar(self,e):
		elemento = NodoLista(e,None)
		if self.size == 0:
			self.primero = elemento
			self.ultimo = self.primero
			self.size = self.size + 1
			
		else:
			if self.Pertenece(e):
				print("El Elemento que esta agregando ya esta en el conjunto:", e)
			else:
				self.ultimo.siguiente = elemento
				self.ultimo = self.ultimo.siguiente
				self.size = self.size + 1
	def Union(self,C):
		ConjuntoSelf = []
		x = self.primero
		for i in range (self.size):
			if self.Pertenece(C[i]):
				x = x.siguiente	
			else:
				ConjuntoSelf.append(x.elemento)
				x = x.siguiente
		ConjuntoUnion = ConjuntoSelf + C
		return ConjuntoUnion


			
	def Intercepccion(self,C):
		N= len(C)
		ConjuntoInter =[]
		for i in range (N):
			if self.Pertenece(C[i]):
				ConjuntoInter.append(C[i])
		return ConjuntoInter

	def Mostrar(self):
		print("Los elementos en el conjunto son:")
		x = self.primero
		while x != None:
			print(x.elemento)
			x = x.siguiente

	def CrearConjunto(self,n):
		for i in range (n):
			Num = int(input("ingrese un elemento en el conjunto:",))
			self.Agregar(Num)
		if self.size != 0:
			Conjunto = True
			print("El Conjunto fue creado exitosamente y contiene los siguientes elementos:")
			self.Mostrar()
		return Conjunto
	
		
	
				
		 
