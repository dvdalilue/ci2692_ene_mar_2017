""" Laboratorio Semana 10
# DESCRIPCIÓN: Elaboración del Hash Cuco
# Autor: Jesus Kauze y David Segura
# email: 12-10273@usb.ve y 13-11341@usb.ve
"""

class CucoEntry(object):
	# Clase que construye los elementos con sus llaves.
	def __init__(self,key,value):
		if type(key)!= str or type(value)!=str:
			print("La clave y el valor deben ser de tipo string.")
		else:
			self.clave = key
			self.valor = value