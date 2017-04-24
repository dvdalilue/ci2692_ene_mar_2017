#TAD que guarda todos los chats entre los pares de usuarios

from chat import Chat
from arrayT import ArrayT

class HashEntry:
	def __init__ (self, chat):
		#Inicializa los elementos de tipo hashEntry para la tabla de hash
		self.clave=chat.id
		self.dato=chat
		self.next = None
		self.prev = None

class Dlist:
	def __init__(self, elemento):
		#Inicia un elemento de tipo lista doblemente enlazada
		self.head = elemento

	def search_clave(self,clave):
		#Busqueda por clave
		x=self.head
		while x!=None and x.clave!=clave:
			x=x.next
		if x!=None:
			return x.dato
		else:
			return x

	def addElement_hass(self,elemento): 
		#Agregar elemento de tipo HassEntry
		if self.head==None:
			self.head=elemento
		else:
			self.head.prev=elemento
			elemento.next=self.head
			self.head=elemento

	def Eliminar(self,x): 
		#Eliminar elemento
		if x.prev!=None:
			x.prev.next=x.next
		elif x.prev==None:
			self.head=x.next
		if x.next!=None:
			x.next.prev=x.prev

class Hash_table:
	def __init__ (self, entero): 
		#Inicializa una tabla de hash
		self.lista=ArrayT(entero)
		#self.lista=[None for i in range(entero)]
		self.long=entero

	def agregar_elem(self, chat): 
		#Agregar elemento de tipo HashEntry que contiene usuario a la tabla
		slot= len(chat.id)%self.long
		if self.lista[slot]==None:
			HashEntry_e=HashEntry(chat)
			self.lista[slot]=Dlist(HashEntry_e)
			return True
		else:
			m=self.lista[slot].search_clave(chat.id)
			if m==None:
				HashEntry_e=HashEntry(chat)
				self.lista[slot].addElement_hass(HashEntry_e)
				return True
			else:
				return False

	def eliminar(self,n): 
		#Eliminar elemento dada una clave
		ubicacion=n%self.long
		if self.lista[ubicacion]==None:
			return False
		else:
			elemento=self.lista[ubicacion].search_clave(n)
			if elemento==None:
				return False
			else:
				self.lista[ubicacion].Eliminar(elemento)
				return True

	def Mostrar(self):  
		#Mostrar la tabla
		print(str(self.long)+"\n")
		counter=0
		for i in self.lista:
			if i==None:
				print(str(counter)+ "	/ \n")
			else:
				string=str(counter)
				x=i.head
				while x!=None:
					string=string+" "+ str(x.clave) +" "
					x=x.next
				print(string+"\n")
			counter+=1


class Conversaciones:
	def crearTabla(self,n):
		self.int=0 #Este corresponde al numero de conversaciones dentro de la tabla.
		#Las instrucciones del proyecto indicaban que debia ser el numero de usuarios
		#registrados, pero esto parece ilogico considerando esta dentro de una clase diferente
		#que no toma en cuenta el registro sino las conversaciones entre usuarios. En
		#consecuencia, se eligio contar el numero de conversaciones dentro de la tabla.
		#Al inicializar, dicho numero es 0. Sin embargo, al agregar o eliminar elementos,
		#este atributo se va modificando.
		self.tablaC=Hash_table(n)

	def __init__(self,n):
		self.crearTabla(n)

	def agregarConversacion(self, chat):
		boolean=self.tablaC.agregar_elem(chat)
		if boolean:
			self.int=self.int+1
		return boolean

	def buscarConversacion(self,id_chat):
		#Convertimos el id a su clave de hash para buscar en el slot correspondiente
		slot=len(id_chat)%self.tablaC.long
		if self.tablaC.lista[slot]!=None:
			chat=self.tablaC.lista[slot].search_clave(id_chat)
			if chat!=None:
				return chat
		return None

	def mostrar(self):
		self.tablaC.Mostrar()