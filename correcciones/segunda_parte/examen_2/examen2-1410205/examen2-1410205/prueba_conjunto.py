#Aurivan Castro 14-10205

#Cliente para probar la clase Conjunto implementada en el archivo conjunto.py

from conjunto import Conjunto, Nodo
import sys

def Empezar_Cliente():
	print("Biinvenido al cliente de prueba de Conjunto. Elija la opcion de menu que corresponda.")
	menustring="1.- Crear un conjunto.\n2.- Agregar un elemento al conjunto.\n3.- Verificar que un elemento pertenezca al conjunto.\n4.- Unir con conjunto con el actual.\n5.-Intersectar un conjunto con el actual.\n6.- Mostrar el conjunto actual.\n7.- Mostrar el menu.\n8.-Salir."
	print(menustring)
	cjto=None
	while True:
		m=int(input("Opcion: "))
		while m not in range(1,8):
			print("Opcion invalida. Intente nuevamente.")
			m=int(input("Opcion: "))
		if m==1:
			#Crea un conjunto si no existe uno
			if cjto==None:
				cjto=Conjunto()
				print("El conjunto se ha creado. Agregue elementos con la opcion correspondiente")
			elif cjto!=None:
				print("Ya hay un conjunto creado.")
		elif m==2:
			#Agrega un elemento dado al conjunto
			inputlisto=False
			while not inputlisto:
				try:
					m=int(input("Introduzca el elemento que desea agregar: "))
					inputlisto=True
				except:
					print("Elemento invalido. Introduza un elemento valido.")
					m=int(input("Introduzca el elemento que desea agregar: "))
					inputlisto=True
			cjto.Agregar(m)
		elif m==3:
			#Dice si un elemento pertenece al conjunto
			inputlisto=False
			while not inputlisto:
				try:
					m=int(input("Introduzca el elemento que desea buscar: "))
					inputlisto=True
				except:
					print("Elemento invalido. Introduza un elemento valido.")
					m=int(input("Introduzca el elemento que desea buscar: "))
					inputlisto=True
			estar=cjto.Pertenece(m)
			if estar:
				print("El elemento esta en el conjunto.")
			else:
				print("El elemento no esta en el conjunto.")
		elif m==4:
			#Hace la union entre un conjunto dado y el actual
			inputlisto=False
			while not inputlisto:
				try:
					m=input("Introduzca el tamaño del conjunto que va a introducir: ")
					m=int(m)
					Arreglo=[None for i in range(m)]
					for i in range(m):
						Arreglo[i]=int(input("Introduzca el elemento "+ str(i)+" de la lista: "))
					inputlisto=True
				except:
					print("Alguno de los datos introducidos es invalido, intente de nuevo")
					m=int(input("Introduzca el tamaño del conjunto que va a introducir: "))
					Arreglo=[cjto.self.head.elemento() for i in range(m)]
					for i in range(m):
						A[i]=int(input("Introduzca el elemento "+ str(i)+" de la lista: "))
					inputlisto=True
			cjto=cjto.Union(Arreglo)
		elif m==5:
			#Hace la interseccion entre un conjunto dado y el actual
			inputlisto=False
			while not inputlisto:
				try:
					m=input("Introduzca el tamaño del conjunto que va a introducir: ")
					m=int(m)
					Arreglo=[None for i in range(m)]
					for i in range(m):
						Arreglo[i]=int(input("Introduzca el elemento "+ str(i)+" de la lista: "))
					inputlisto=True
				except:
					print("Alguno de los datos introducidos es invalido, intente de nuevo")
					m=int(input("Introduzca el tamaño del conjunto que va a introducir: "))
					Arreglo=[cjto.self.head.elemento() for i in range(m)]
					for i in range(m):
						A[i]=int(input("Introduzca el elemento "+ str(i)+" de la lista: "))
					inputlisto=True
			cjto=cjto.Interseccion(Arreglo)
		elif m==6:
			#Muestra el conjunto
			cjto.Mostrar()
		elif m==7:
			#Imprime el menu
			print(menustring)
		elif m==8:
			#Sale del cliente
			sys.exit()

#Iniciar el cliente
Empezar_Cliente()