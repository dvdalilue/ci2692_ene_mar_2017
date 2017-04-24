""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha:01/04/2017
    Descripcion:Nodo tipo USUARIO 
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/02/2017"""

class USUARIO:
	def __init__(self, n, p, t, s , a):
		self.Nombre = n #clave
		self.Password = p#dato
		self.Telefono = t#dato
		self.siguiente = s
		self.anterior = a
		
