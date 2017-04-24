""" Laboratorio 1 .algoritmos II .ene-mar 2017 
	fecha:01/04/2017
    Descripcion:Nodo tipo Contacto 
	autores: Edymar Mijares 12-10882
	         Jose Carmona 11-10156

	correo: - edys.beccaria@gmail.com
		   - carmona621@hotmail.com
ultima edicion :30/02/2017"""

class NodoContacto:
	def __init__(self, n, t, s , a):
		self.nombre = n #clave
		self.telefono = t
		self.siguiente = s
		self.anterior = a
