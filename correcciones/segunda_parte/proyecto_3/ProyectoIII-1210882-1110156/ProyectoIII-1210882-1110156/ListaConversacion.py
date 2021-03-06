""" Algoritmos II .ene-mar 2017 
	fecha: 1/04/2017
    Descripcion:  En este modulo esta implementada la lista doblemente enlazada con
la clase Dlist. La lista debe contiene elementos de tipo NodoConver
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/03/2017"""

from nodoConver import *
		
class Dlist(object):
	def __init__(self):
		self.primero = None
		self.size=0  #number of elements
		
                       
	def __len__ (self):
		return self.size
		
		
	def agregar_elem(self,e):#NodoConver e
		self.size = self.size + 1
		e.siguiente = self.primero
		self.primero = e
		if e.siguiente != None:
			e.siguiente.anterior = e
		
	def eliminar_elem(self,e):#NodoConver e
		if e.anterior != None:
			e.anterior.siguiente = e.siguiente
		else:
			self.primero = e.siguiente
		if e.siguiente != None:
			e.siguiente.anterior = e.anterior
			
	def buscar(self,clave):
		elemento = self.primero
		while elemento != None and elemento.Clave != clave:#.clave
			elemento = elemento.siguiente
		return elemento
		
	def imprimir(self):
		elemento = self.primero
		while elemento != None:
			print ((elemento.Nombre, elemento.Telefono))
			elemento = elemento.next
			
