""" Algoritmos II .ene-mar 2017 
	fecha: 30/03/2017
    Descripcion:  Cliente que llama a la clase Conjunto 
	autores: Edymar Mijares 12-10882

	correo: - edys.beccaria@gmail.com
		   
Examen II"""
from conjunto import Conjunto

#clase que me permite enviar un mensaje de error cuando el test no pase
class NoPasaElTest(Exception):
	def __init__(self,mensaje):
		self.mensaje = mensaje
def PcrearConjunto(CC,n):
	try:
		CC.CrearConjunto(n)
		if CC.size != n:
			raise NoPasaElTest("usted intento agregar un elemento que ya esta en el conjunto")
		print("Se comprobo la creacion del Conjunto")
	except NoPasaElTest as e:
		print (e.mensaje)
def probarAgregar(CC,num):
	CC.Agregar(num)
	if CC.Pertenece(num) == False:
		raise NoPasaElTest("No se agrega un nuevo elemento")

def probarUnion(CC,NuevoC):
	Union = CC.Union(NuevoC)
	print(Union)
def probarInter(CC,NuevoC):
	Inter = CC.Intercepccion(NuevoC)
	print(Inter)
	
#######################################################################
####################         Pruebas           ########################
#######################################################################

Con = Conjunto()
NN = int(input("ingrese la cantidad de elementos del conjunto que desea crear:",))

PcrearConjunto(Con,NN)
Con.Mostrar()
a = 18
b = 12
c = 3
probarAgregar(Con,a)
probarAgregar(Con,b)
probarAgregar(Con,c)
Con.Mostrar()

B = [12,6,7,32,67,3,18,4]
probarUnion(Con,B)
probarInter(Con,B)






