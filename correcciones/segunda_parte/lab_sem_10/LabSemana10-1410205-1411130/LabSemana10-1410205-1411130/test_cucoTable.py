from cuco_table import *
import random

table = CucoTable(15)

print("Agregando elementos repetidos usando AddEntry()")
for x in range(37):
	table.agregar(str(x), str(random.randint(0,1000)))

print("Estado de la tabla:")
table.mostrar()

print("Buscando elementos")
for x in range(13):
	print("Buscando el elemento de key="+str(x))
	print("Valor encontrado: ",table.buscar(str(x)))

print("Borrando elementos")
for x in range(16):
	table.eliminar(str(x))

print("Estado de la tabla:")
table.mostrar()

print("Han finalizado las pruebas")