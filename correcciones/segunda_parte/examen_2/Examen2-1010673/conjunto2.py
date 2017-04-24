# Examen Nro. 2
# Autor: Jorge Sanchez
#		 10-10673
# Desarrollo del conjunto finito

""" Este es el intento para el conjunto usando una lista enlazada;
Note, por ejemplo, las lineas 74,33,23, donde hay error, pues no esta permitido;
Lea el encabezado del otro archivo.py: conjunto.py, que hace lo que se pide."""

class Conjunto():

	def __init__(self):
		self.entero = None
		self.next = None
		self.size_conj = 0

	def buscar_en_Conj(self,entero):
		i = self.entero
		while i != None:
			if i == entero:
				return i
			elif i != entero:
				i.next
		return None

	def Pertenece(self,entero):
		i = self.entero
		while i != None:
			if i == entero:
				
				return True
			else:
				i = i.next
	
		return False

	def Agregar(self,entero):
		if self.Pertenece(entero) == False:  
			if self.entero == None:
				self.next = self.entero
				self.entero = entero
				return True
			else:
				aux = self.entero
				aux2 = self.entero.next
				
				if entero < self.entero:
					entero.next = self.entero
					self.entero = entero
					return True
				else:
					while aux2 is not None:
						if entero < aux2:
							entero.next = aux2
							aux.next = entero
							return True
						else:
							aux = aux.next
							aux2 = aux2.next
					entero.next = aux2
					aux.next = entero
					return True
			self.size_conj += 1
					
		else:
			return False


	def Mostrar(self):
		Lista = []
		i = self.first
		while i != None:
			Lista.append(i)
			i = i.next
		return Lista








