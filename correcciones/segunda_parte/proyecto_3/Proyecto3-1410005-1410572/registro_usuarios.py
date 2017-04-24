from hash_table import hashTable
from usuario import Usuario

class Registro_Usuarios():
	def __init__(self,n):
		self.n = n
		self.tablaRU = hashTable(self.n)

	def AgregarUsuario(self,u):
		return self.tablaRU.addValue(u.nombre,u)
	
	def EliminarUsuario(self,n):
		return self.tablaRU.deleteKey(n)

	def CargarUsuarios(self,archivo):
		retornar = True
		f = open(archivo,'r')
		for line in f:
			usuario = line.split('\t')[0]
			password = line.split('\t')[1]
			telefono = line.split('\t')[2].strip('\n')
			u = Usuario(usuario,password,telefono)
			if u == None:
				retornar = False
			elif u != None:
				agregado = AgregarUsuario(u.nombre,u)
				if not agregado:
					retornar = False
		return retornar

	def MostrarRegistro(self):
		self.tablaRU.show()
	
	def Search(self,nombre):
		return self.tablaRU.search(nombre) 