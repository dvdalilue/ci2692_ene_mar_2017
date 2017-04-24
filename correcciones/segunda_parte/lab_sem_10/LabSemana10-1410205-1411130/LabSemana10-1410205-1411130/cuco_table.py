from arrayT import ArrayT
import hashlib
from cuco_entry import CucoEntry
import math

class CucoTable:
	def __init__(self,n):
		#Inicializa la clase CucoTable
		self.crearCucoTabla(n)

	def crearCucoTabla(self,n):
		#Crea la tabla de tamaño n
		self.tabla=ArrayT(n)
		self.tamaño=n

	def h1(self,clave):
		#Funcion de hash 1
		h=hashlib.sha256(clave.encode())
		return int(h.hexdigest(),base=16)%self.tamaño

	def h2(self,clave):
		#Funcion de hash 2
		h=hashlib.md5(clave.encode())
		return (int(h.hexdigest(),base=16))%self.tamaño

	def rehash(self):
		#Funcion que crea una tabla de doble tamaño de la anterior
		aux=self.tabla
		n=len(aux)
		self.crearCucoTabla(2*n)
		for i in range(n):
			if aux[i]!=None:
				self.agregar(aux[i].clave,aux[i].valor)

	def agregar(self,clave,valor):
		#Agrega un elemento a la tabla
		ubicacion=self.h1(clave)
		elemento=CucoEntry(clave,valor)
		n=self.tamaño
		for i in range(n):
			if self.tabla[ubicacion]==None: #Si no hay ningun elemento en la posicion, agrega el elemento normalmente
				self.tabla[ubicacion]=elemento
				return 
			else:
				if elemento.clave==self.tabla[ubicacion].clave:
					#Si la clave dada es igual a la del elemento que ya se encuentra en la posicion encontrada,
					#sustituye el atributo valor de dicho elemento
					self.tabla[ubicacion].valor=elemento.valor
					return
				#Si no ocurre lo anterior, utiliza la funcion h2 para encontrar otra posicion
				elemento,self.tabla[ubicacion]=self.tabla[ubicacion],elemento
				if ubicacion== self.h1(elemento.clave):
					ubicacion=self.h2(elemento.clave)
				else:
					ubicacion=self.h1(elemento.clave)
		#Despues de n iteraciones no ha podido insertar el elemento, por lo cual hay que hacer rehash
		self.rehash()
		self.agregar(elemento.clave,elemento.valor)

	def buscar(self, stringClave):
		#Busca un elemento por medio de un string dado y retorna su valor en caso de haberlo encontrado
		ubicacion=self.h1(stringClave)
		if self.tabla[ubicacion]!=None and self.tabla[ubicacion].clave==stringClave:
			return self.tabla[ubicacion].valor
		else:
			return None

	def eliminar(self, stringClave):
		#Elimina un elemento por medio de un string dado y retorna su valor en caso de haberlo encontrado y eliminado
		ubicacion=self.h1(stringClave)
		if self.tabla[ubicacion]!=None and self.tabla[ubicacion].clave==stringClave:
			aux=self.tabla[ubicacion].valor
			self.tabla[ubicacion]=None
			return aux
		else:
			return None	

	def mostrar(self):
		#Muestra el contenido de la tabla
		print("La tabla de hash tiene los siguientes elementos.")
		for i in range(self.tamaño):
			if self.tabla[i]==None:
				print("/")
			else:
				print("["+ self.tabla[i].clave+" , "+self.tabla[i].valor+"]")

