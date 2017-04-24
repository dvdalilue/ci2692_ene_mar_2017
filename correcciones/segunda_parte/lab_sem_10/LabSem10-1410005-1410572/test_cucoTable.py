from cuco_table import *
import random

table = CucoTable(15)

print("Agregando elementos repetidos usando AddEntry()")
for x in range(37):
	table.AddEntry(str(x), str(random.randint(0,1000)))

print("Estado de la tabla:")
table.Show()

print("Buscando elementos")
for x in range(13):
	print("Buscando el elemento de key="+str(x))
	print("Valor encontrado: ",table.Search(str(x)))

print("Borrando elementos")
for x in range(16):
	table.DeleteEntry(str(x))

print("Estado de la tabla:")
table.Show()

print("Han finalizado las pruebas")