""" Tipo de Datos cuya funcionalidad consiste en almacenar los mensajes que se han enviado
	dos usuarios, en cualquier espacio de tiempo.
	
	Autores:

	- Orlando Chaparro
	- Angel Morante

	Ultima Modificacion:

		31 de marzo de 2017
"""

from usuario import * 
from registro_usuarios import *


#	Almacena los mensajes que se han enviado dos usuarios, en cualquier espacio de tiempo

#Vamos a trabajar con los mismos nodos de usuarios
#sin utilizar el atributo prev.

class NodoMensaje:

	def __init__(self,m):
		self.mensaje = m
		self.next = None


class chat:
	#	Se reciben como parametros dos usuarios y se crea el identificador Chat id.
	def __init__(self,u1,u2):
		if u1.nombre < u2.nombre:
			self.id = u1.nombre + "-" + u2.nombre
		else:
			self.id = u2.nombre + "-" + u1.nombre

		self.mensajes = []
		self.cantidad = 0 #cantidad de mensajes en la lista
		self.primero = None
		self.ultimo = None

	#	Recibe dos parametros. El usuario u y el mensaje m.
	#	Indica que el usuario u manda el mensaje m al chat 
	def AgregarMensajeAlChat(self,u,m):

		if self.cantidad == 0:

			mensaje = u.nombre + ": " + m
			NuevoNodo = NodoMensaje(mensaje)
			self.mensajes.append(NuevoNodo)
			self.primero = NuevoNodo
			self.ultimo = NuevoNodo
			NuevoNodo.next = None
			self.cantidad +=1

		elif self.cantidad > 0:

			mensaje = u.nombre + ": " + m
			NuevoNodo = NodoMensaje(mensaje)
			self.mensajes.append(NuevoNodo)
			self.ultimo.next = NuevoNodo
			self.ultimo = NuevoNodo
			NuevoNodo.next = None
			self.cantidad +=1 







