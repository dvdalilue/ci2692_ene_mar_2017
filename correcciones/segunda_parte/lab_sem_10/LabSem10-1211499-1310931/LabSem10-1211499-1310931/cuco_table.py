from arrayT import ArrayT

from CucoEntry import *
import hashlib

# Descripcion: Implementa la clase CucoTable, la cual crea la tabla de Hash de Tipo Cuco
#
# Autor: 	ORLANDO CHAPARRO 12-11499
#		    ANGEL MORANTE 13-10931
#
#Atributos: self.Tabla: crea un arreglo de tipo ArrayT


# Funciones de Hash a utilizar en la implementacion
def h1(clave):
	h = hashlib.sha256(clave.encode())
	return int(h.hexdigest(),base=16)

def h2(clave):
	h = hashlib.md5(clave.encode())
	return int(h.hexdigest(),base=16)




class CrearCucoTable: 


	def __init__(self,n):
		self.Tabla = ArrayT(n)


	def Agregar(self,clave,valor):
		x = crearCucoEntry(clave,valor)
		pos = h1(x.clave) % len(self.Tabla)


		#Las siguientes lineas de codigo evitan que entre en un ciclo infinito
		# haciendo Rehash, dado que se presenta el caso en el que si se quiere agregar un elemento
		# donde su clave ya aparece 2 veces en la Tabla, entonces el algoritmo comienza a hacer Rehash
		# de forma infinita.

		if self.Buscar(clave) != None:
			pos = h1(clave) % len(self.Tabla)
			pos2 = h2(clave) % len(self.Tabla)

			if self.Tabla[pos] != None and self.Tabla[pos].clave == clave:
				self.Tabla[pos].valor = valor
			if self.Tabla[pos2] != None and self.Tabla[pos2].clave == clave:
				self.Tabla[pos2].valor = valor 

			return

		#Funcion AGregar tomada de las laminas del Profesro Blai Bonet
		for i in range(0,len(self.Tabla)):
			if self.Tabla[pos] == None:
				self.Tabla[pos] = x
				return
			else:
				x,self.Tabla[pos] = self.Tabla[pos],x
				if pos == h1(x.clave)% len(self.Tabla):
					pos = h2(x.clave)% len(self.Tabla)
				else:
					pos = h1(x.clave)% len(self.Tabla)

		self.Rehash()
		self.Agregar(x.clave,x.valor)


	#Funcion que crea un arregla del doble del tamano del anterior
	def Rehash(self):
		Tabla = self.Tabla
		self.Tabla = ArrayT(len(Tabla)*2)

		for i in range(0,len(Tabla)):
			if Tabla[i] != None:
				self.Agregar(Tabla[i].clave,Tabla[i].valor)



	def Buscar(self,clave):
		"""Definicion: Dada un clave
			c
			, se busca el elemento en la tabla de hash que posea la
			clave igual a
			c
			. Si el elemento se encuentra en la tabla, entonces se retorna el
			String
			asociado a esa clave. En caso de que no haya ninguna clave
			c
			en la tabla de hash, se
			retorna
			None
		"""


		pos = h1(clave) % len(self.Tabla)
		pos2 = h2(clave) % len(self.Tabla)

		if self.Tabla[pos] != None and self.Tabla[pos].clave == clave:
			return self.Tabla[pos].valor
		if self.Tabla[pos2] != None and self.Tabla[pos2].clave == clave:
			return self.Tabla[pos2].valor


	def Eliminar(self,clave):
		"""Definicion: Dada un clave
			c
			, si alg ́un elemento en la tabla de hash tiene una
			clave igual a
			c
			, entonces el elemento se elimina de la tabla y retorna el
			String
			asociado
			a esa clave. En caso de que no haya ninguna clave
			c
			en la tabla de hash, se retorna
			None

		"""

		pos = h1(clave) % len(self.Tabla)
		pos2 = h2(clave) % len(self.Tabla)

		if self.Tabla[pos] != None and self.Tabla[pos].clave == clave:
			Aux = self.Tabla[pos].valor
			self.Tabla[pos] = None 

			return Aux

		if self.Tabla[pos2] != None and self.Tabla[pos2].clave == clave:
			Aux2 = self.Tabla[pos2].valor
			self.Tabla[pos] = None

			return Aux2 

	def mostrar(self):
		"""Definicion: 
		Se muestra por la salida est ́andar todos los elementos de la tabla
		de hash, en forma de pares clave y valor asociado.

		"""
		print('-------------------------------------------------')
		print('Los elementos contenidos en la tabla de Hash de tipo Cuco son:')
		for i in range(len(self.Tabla)-1):
			if  self.Tabla[i] != None :
				print(self.Tabla[i].clave,self.Tabla[i].valor)
		print('-------------------------------------------------')