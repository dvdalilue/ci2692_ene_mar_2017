# Proyecto no. 3
# Autores: Jorge Sanchez 10-10673
#			Greanny Vivas 12-11167

from tablaRU import*
from listaContactos import*
from registro_usuarios import*

# TAD Usuario: 
class Usuario():
	# constructor de la 
	def __init__(self,nombre,password,telefono,contactos):
		assert(len(str(nombre))>1 and len(str(password))>1 and int(telefono))
		# assert para revisar que el nombre y password sean distintos de None y los numeros sean del 0 al 9
		self.nombre = str(nombre) # distinto de None
		self.password = str(password) # distinto de None
		self.telefono = str(telefono) # numeros del 0 al 9
		self.contactos = ListaContactos() # Lista enlazada de contactos en orden alfabetico
		self.next = None # apuntador al la lista de usuarios
		
	def AgregarContacto(self,usuario): # u de tipo usuario
		return self.contactos.Agregar_enlista(usuario)

	def EliminarContacto(self,nombre): # string n del nombre del usuario
		# buscar el elemento en la lista de contactos
		if self.contactos.Buscar_enlista(nombre) != None:
			# eliminar el usuario relacionado al nombre
			usuario = self.contactos.Buscar_enlista(nombre)
			return self.contactos.Eliminar_enlista(usuario.nombre)
		else:
			# si no encuentra el contacto, retornar False
			return False

	def BuscarContacto(self,nombre):
		if self.contactos.Buscar_enlista(nombre) != None:
			return True
		else:
			return False
	
	def MostrarContactos(self):
		# mostrar en forma de pares nombre-telefono en orden alfabetico
		self.contactos.Mostrar_enlista()
