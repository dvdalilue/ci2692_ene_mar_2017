""" Laboratorio Semana 10
# DESCRIPCIÓN: Elaboración de la Tabla de Hash Cuco
# Autor: Jesus Kauze y David Segura
# email: 12-10273@usb.ve y 13-11341@usb.ve
"""
from CucoEntry import CucoEntry
from arrayT import ArrayT
import hashlib


class CrearCucoTable(object):
	def __init__(self,n):
		self.tabla = None
		self.longitud = None
		self.tabla = ArrayT(n)
		self.longitud = n

	def h1(self,clave):
		h = hashlib.sha256(clave.encode())
		return int(h.hexdigest(),base=16)

	def h2(self,clave):
		h = hashlib.md5(clave.encode())
		return int(h.hexdigest(),base=16)

	def Rehash(self):
		NuevoArreglo = ArrayT(self.longitud)
		for x in range(self.longitud):
			NuevoArreglo[x] = self.tabla[x]
		self.tabla = ArrayT(self.longitud*2)
		self.longitud = self.longitud*2
		for i in NuevoArreglo:
			if i is not None:
				self.Agregar(i.clave,i.valor)

	def Agregar(self,key,value):
		# Agrega elementos a la tabla de Hash Cuco
		# try:
			x = CucoEntry(key,value)
			posicion = self.h1(x.clave) % len(self.tabla)
			for i in range(len(self.tabla)):
				if self.tabla[posicion] == None:
					self.tabla[posicion] = x
					return
				else:
					self.tabla[posicion],x = x,self.tabla[posicion]
					if posicion == (self.h1(x.clave) % len(self.tabla)):
						posicion = self.h2(x.clave) % len(self.tabla)
					else:
						posicion = self.h1(x.clave) % len(self.tabla)
			self.Rehash()
			print("Pase")
			self.Agregar(key,value)
		# except:
			# print("Hubo un error agregando")

	def Eliminar(self,key):
		# Elimina elementos buscando la llave en la tabla
		posicion = self.h1(key) % len(self.tabla)
		if self.tabla[posicion] != None:
			d = self.tabla[posicion].valor
			if self.tabla[posicion].clave == key:
				self.tabla[posicion] = None
				return d
			else:
				posicion = self.h2(key) % len(self.tabla)
				if self.tabla[posicion].clave == key:
					self.tabla[posicion] = None
					return d
				else:
					print("La llave no esta asignada")
		else:
			posicion = self.h2(key) % len(self.tabla)
			if self.tabla[posicion] != None:
				d = self.tabla[posicion].valor
				if self.tabla[posicion].clave == key:
					self.tabla[posicion] = None
					return d
				else:
					print("La llave no esta asignada")
			else:
				print("La llave no esta asignada")

	def Buscar(self,key):
		# Busca el elemento en la tabla a través de la llave
		posicion = self.h1(key) % len(self.tabla)
		if self.tabla[posicion] != None:
			if self.tabla[posicion].clave == key:
				return self.tabla[posicion].valor
			else:
				posicion = self.h2(key) % len(self.tabla)
				if self.tabla[posicion].clave == key:
					return self.tabla[posicion].valor
				else:
					print("La llave no esta asignada")
		else:
			posicion = self.h2(key) % len(self.tabla)
			if self.tabla[posicion] != None:
				if self.tabla[posicion].clave == key:
					return self.tabla[posicion].valor
				else:
					print("La llave no esta asignada")
			else:
				print("La llave no esta asignada")

	def mostrar(self):
		# Muestra los elementos que hay en la tabla
		for x in range(len(self.tabla)):
			if self.tabla[x] != None:
				print("("+str(self.tabla[x].clave)+","+str(self.tabla[x].valor)+")")
			else:
				pass