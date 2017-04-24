""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha:01/04/2017
    Descripcion:Chat guarda los mensajes entre dos personas almacenadas en la pila MENSAJES 
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/02/2017"""
from pilaChat import Mensajes

class Chat:
	def __init__(self):
		self.id = None
		self.mensajes = None
		
	def CrearChat(self, u1, u2):
	
		if u1 < u2:
			self.id = u1 + "-"+ u2
		else:
			self.id = u2 +"-"+ u1
		self.mensajes = Mensajes()
	
	def AgregarMensaje(self, u, m):
		self.mensajes.push( u + ":" + m)
	


	
