from conjunto import Conjunto
import sys

def test():
	#Cliente para probar las funciones de la clase Conjunto
	print("Cliente para probar Clase Conjunto.")
	menustr="1. Agregar elemento de tipo entero a un conjunto.\n2. Determinar si un elemento pertenece al conjunto.\n3. Unir dos conjuntos.\n4. Intersectar dos conjuntos.\n5. Mostrar los elementos del conjunto.\n6. Mostrar las opciones del menu.\n7. Salir del cliente."
	print(menustr)
	conjunto=Conjunto()
	while True:
		op=int(input("Introduzca la opcion de menu que desea: "))
		while op not in range(1,8):
			op=int(input("Introduzca la opcion de menu que desea: "))
		if op==1:
			#Agrega un elemento al conjunto
			elemento=int(input("Introduzca un elemento de tipo entero: "))
			#Si el elemento ya pertenece al conjunto, lo descarta
			if conjunto.pertenece(elemento)==True:
				print("El elemento ya pertenece al conjunto.")
			else:
				conjunto.agregar(elemento)
		if op==2:
			#Pertenece
			elemento=int(input("Introduzca el elemento que quiere determinar si pertenece o no al conjunto: "))
			if conjunto.pertenece(elemento)==True:
				print("El elemento pertenece al conjunto.")
			else:
				print("El elemento no pertenece al conjunto.")
		if op==3:
			#Unir
			tam=int(input("Introduzca el taman~o del conjunto que desea unir: "))
			nuevo=Conjunto()
			for i in range(tam):
				elemento=int(input("Introduzca el elemento "+ str(i) +" del conjunto: "))
				nuevo.agregar(elemento)
			conjunto.union(nuevo)
			conjunto.mostrar()
		if op==4:
			#Intersectar
			tam=int(input("Introduzca el taman~o del conjunto que desea intersectar: "))
			nuevo=Conjunto()
			for i in range(tam):
				elemento=int(input("Introduzca el elemento "+ str(i) +" del conjunto: "))
				nuevo.agregar(elemento)
			conjunto=conjunto.interseccion(nuevo)
			conjunto.mostrar()
		if op==5:
			#Mostrar elementos
			conjunto.mostrar()
		if op==6:
			print(menustr)
		if op==7:
			sys.exit()

test()