# Proyecto no. 3
# Autores: Jorge Sanchez 10-10673
#			Greanny Vivas 12-11167

# TAD Registro de usuarios: Tabla de hash estática que contiene elementos de tipo usuario

from tablaRU import*
from usuario import*
from arrayT import ArrayT

# Creacion de tablaRU con 10 usuarios
TablaRU = tablaRU(10)

class RegistroUsuarios():

	def __init__(self,n,tablaRU):
		# assert del numero de usuarios con el numero de elementos de la tabla
		assert(n == TablaRU.size)
		self.num_usuarios = n
		self.usuarios = tablaRU.arregloHash # tabla de hash con el registro de los usuarios
		self.contador = 0

	# funcion para buscar si el password del usuario es correcto
	def BuscarPassword(self,nombre,password):
		return TablaRU.SearchPassword(nombre,password)

	# funcion BuscarUsuario para buscar el nombre del usuario que se quiere agregar a la lista de contactos
	def BuscarUsuario(self,nombre):
		if TablaRU.Buscar(nombre) != None:
			return True
		else:
			return False

	# funcion DarUsuario que da la informacion del usuario registrado para agregarlo a la lista de contactos
	def DarUsuario(self,nombre):
		return TablaRU.SearchUser(nombre)

	# funcion AgregarUsuario que agrega el usuario a la tablaRU si el nombre dado no coincide con otro nombre de la tabla
	def AgregarUsuario(self,u):
		self.contador += 1
		if self.contador <= self.num_usuarios:
			if TablaRU.Buscar(u.nombre) != None:
				return False  
			else:
				TablaRU.Agregar(u)
				return True
		else:
			self.contador -= 1
			return False

	# funcion ELiminarUsuario que elimina el usuario a la tablaRU si el nombre dado coincide con otro nombre de la tabla
	def EliminarUsuario(self,nombre):
		if TablaRU.Buscar(nombre) != None:
   			TablaRU.Eliminar(nombre)
   			# restamos un elemento al contador
   			self.contador -= 1
   			return True
		else:
   			return False

	def CargarUsuario(self,archivo):
		txt = archivo+".txt"
		f = open(txt,'r')
		lineas = []
		for line in f:
			line = line.split('	')
			lineas.append(line)
		a = ArrayT(len(lineas))
		for i in range(0,len(lineas)):
			a[i] = lineas[i]
		# estado inicial de agregar para que retorne False en caso de que algun usuario no se agregue correctamente
		for i in range(0,len(a)): 
			nombre = str(a[i][0])
			password = str(a[i][1])
			telefono = str(a[i][2])[:-1]
			contactos = []
			u = Usuario(nombre,password,telefono,contactos)
			estado = self.AgregarUsuario(u)
		return estado


	def MostrarRegistro(self):
		TablaRU.Mostrar()

