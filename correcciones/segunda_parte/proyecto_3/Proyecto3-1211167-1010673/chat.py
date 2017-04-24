# Proyecto no. 3
# Autores: Jorge Sanchez 10-10673
#		   Greanny Vivas 12-11167

from listaMensajes import*
from usuario import*

# TAD Chat que almacena los mensajes que se han enviado dos usuarios
class Chat():

	def __init__(self,u1,u2):
		n1 = u1.nombre
		n2 = u2.nombre
		if n1.lower() < n2.lower():
			self.ID = str(n1)+"-"+str(n2)
		else:
			self.ID = str(n2)+"-"+str(n1)
		self.mensajes = ListaMensajes()
		self.next = None

	def AgregarMensaje(self,u,m):
		msj = str(u.nombre)+": "+m
		self.mensajes.Agregar_enmsjs(Mensaje(msj))

	def MostrarChat(self):
		self.mensajes.Mostrar_enmsjs()
