# Examen 2
# Autor: Jorge Sanchez
#		 10-10673
#
""" Fracase implementando el conjunto como una lista enlazada.
No supe hacer que el programa aceptara el entero como un nodo,
o no se me ocurrio el procedimiento. Asi que lo hice sin utilizar 
una lista enlazada, hace todo lo que pide; exceptuando eso."""



class Conjunto():
	#Creo el conjunto
	def __init__(self):
		self.conj = []
		self.size = 0
	#Funcion que me determina si el entero esta o no en el conjunto
	def Pertenece(self,entero):
		n = self.size
		while n != 0:
			if entero == self.conj[n-1]:
				return True
			else:
				n -= 1
		return False
	# Funcion que me agrega un entero al conjunto
	def Agregar(self,entero):
		if self.Pertenece(entero) == False:  
			self.conj.append(entero)
			self.size += 1
			return print('True con '+str(entero))		
		else:
			return print('False con '+str(entero))
	# Funcion que me agrega un entero al conjunto, sin imprimir nada
	def Agregar2(self,entero):
		if self.Pertenece(entero) == False:  
			self.conj.append(entero)
			self.size += 1
			return True		
		else:
			return False

	#Funcion que me muestra en lista los elementos del conjunto
	def Mostrar(self):
		print(self.conj)

	#Funcion que muestra en lista los elementos del conjunto interseccion del 
	#conjunto self con el de entrada
	def Interseccion(self,C):
		aux = Conjunto()
		for i in range (self.size):
			for j in range(C.size):
				if self.conj[i] == C.conj[j]:
					aux.Agregar2(self.conj[i])
				else:
					pass
		return aux.Mostrar()

	# Funcion que retorna el conjunto interseccion del conjunto self
	# y el de entrada
	def Interseccion2(self,C):
		aux = Conjunto()
		for i in range (self.size):
			for j in range(C.size):
				if self.conj[i] == C.conj[j]:
					aux.Agregar2(self.conj[i])
				else:
					pass
		return aux

	#Funcion que retorna en lista el conjunto union del conjunto self
	# con el de entrada
	def Union(self,C):
		aux = Conjunto()
		Inter = self.Interseccion2(C)
		for i in range(self.size):
			aux.Agregar2(self.conj[i])
		for i in range(C.size):
			if Inter.Pertenece(C.conj[i]) == False:
				aux.Agregar2(C.conj[i])
			else:
				pass
		return aux.Mostrar()
