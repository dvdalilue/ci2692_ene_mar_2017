# PROYECTO 3

# DESCRIPCIÓN: Cliente que probará el correcto funcionamiento de
# la implementación de la aplicación de mensajeria ALGOGRAM

# AUTORES: Jesus Kauze y David Segura
# EMAILS: 12-10273@usb.ve y 13-11341@usb.ve

from chat import Pila_Lista
from chat import TAD_chat
from registro_usuarios import RegistroUsuarios
import hashlib


def cargarCaritas(string):
	#debe ingresar el PATH del archivo
	try:
		caras = open(string, "r")
		contenido = caras.readlines()
		caras.close()
		otra= ""
		for x in contenido:
			otra = x
		otra = otra[0:len(otra)-1]
		caritas = otra.split("    ")
		lista_caritas = caritas
		return caritas
	except:
		print("No ingresaste un archivo valido de emoticones :(")

def mostrarCaritas(x):
	print("> Estos son tus emoticones disponibles: \n")
	for i in cargarCaritas(x):
		print(i[0:2])
	return