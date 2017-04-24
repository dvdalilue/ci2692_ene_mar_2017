from CucoTable import *
from CucoEntry import *

#clase que me permite enviar un mensaje de error cuando el test no pase


class NoPasaElTest(Exception):
	def __init__(self,mensaje):
		self.mensaje = mensaje
		
def PruebaCrearTabla(TH,n):
	try:
		TH.Crearcucotabla(n)
		if len(TH.tabla) != n:
			raise NoPasaElTest("No se crea la tabla del tamano adecuado")
		print("Se comprobo la creacion de la tabla")
	except NoPasaElTest as e:
		print (e.mensaje)
def probarAgregar(TH,clave,valor):
	TH.Agregar(clave,valor)
	if TH.BuscarC(clave) == None:
		raise NoPasaElTest("No se agrega un nuevo elemento")
def probarEliminar(TH,clave):
	try:
		TH.EliminarClave(clave)
		if TH.BuscarC(clave) != None:
			raise NoPasaElTest("No se elimina correctamente")
		print ("Se comprobo la eliminacion")
	except NoPasaElTest as e:
		print (e.mensaje)
	pass

def probarBuscar(TH,clave):
	try:
		if TH.BuscarC(clave) == None:
			raise NoPasaElTest("No se elimina correctamente")
		else:
			print(TH.BuscarC(clave))
			print ("Se comprobo la busqueda")
	except NoPasaElTest as e:
		print (e.mensaje)
	pass

#####################################################################
##########################llamadas a pruebas#########################
#####################################################################
ht = CucoTable()

tamano = 5

PruebaCrearTabla(ht, tamano)

ht.Mostrar()
print(ht.size)


probarAgregar(ht,"R","Ana")
probarAgregar(ht, "O","Rhonald")
probarAgregar(ht,"M","Rogger")
probarAgregar(ht,"A","Edymar")
probarAgregar(ht,"O","Pedro")

ht.Mostrar()
probarEliminar(ht,"R")
ht.Mostrar()
probarBuscar(ht,"O")

