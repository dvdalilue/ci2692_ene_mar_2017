""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha:01/04/2017
    Descripcion:Conversaciones guarda los mensajes entre dos personas almacenadas en el Chat, es una tabla de hash 
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/02/2017"""
from nodoConver import *
from ListaConversacion import Dlist

#mis elementos a agregar seran chat
#mi tabla guarda los chat en una lista detro de cada slot

class CONVERSACIONES:
	def __init__(self):
		self.tabla = []
		self.size = 0
		
	def Crear_Tabla(self,n):
		self.size = n
		N= self.size
		self.tabla=[Dlist() for x in range(N)]
		
	def buscarConversacion(self,Nombre1, Nombre2):
		if Nombre1 < Nombre2:
			chatid = Nombre1 + "-"+ Nombre2
		else:
			chatid = Nombre2+ "-" + Nombre1
			
		H=hash(chatid)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar(chatid)
		if elemento != None:
			return elemento.elemento #es un elemento tipo chat
		else:
			return None
			
	def Agregar_Mensaje(self, Nombre1, Nombre2,m):
		if Nombre1 < Nombre2:
			chatid = Nombre1 + "-"+ Nombre2
		else:
			chatid = Nombre2+ "-" + Nombre1
			
		H=hash(chatid)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar(chatid)
		if elemento != None:
			elemento.elemento.push( Nombre2 + ":" + m) 
		else:
			print("No hay una conversacion de estos usuarios")
		
	def MostrarConversacion(self,Nombre1, Nombre2):
		if Nombre1 < Nombre2:
			chatid = Nombre1 +"-"+ Nombre2
		else:
			chatid = Nombre2+ "-" + Nombre1
		H=hash(chatid)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar(chatid)
		if elemento != None:
			return elemento.elemento.Mostrar() #es la pila de mensajes
		else:
			return None
			
	def agregar_Conversacion(self,chat):
	
		H=hash(chat.id)
		bucket= H%(self.size)
		elemento = self.tabla[bucket].buscar(chat.id)
		if elemento == None:
			elemento = NodoConver( chat.id, chat.mensajes, None, None)
			self.tabla[bucket].agregar_elem(elemento)
			return True
		else:
			elemento.elemento = chat.mensajes
			return False
			
	def MostrarRegistro(self):
		for i in range(0,len(self.tabla)):
			print ("Lista",i)
			self.tabla[i].imprimir()
