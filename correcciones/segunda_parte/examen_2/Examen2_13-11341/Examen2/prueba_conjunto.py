# EXAMEN 2

# DESCRIPCIÓN: Cliente que muestra el correcto funcionamiento
# de la implementación del conjunto de números enteros

# AUTOR: DAVID SEGURA 13-11341
# CORREO: 13-11341@usb.ve

from conjunto import Conjunto
from random import randint

# CREACIÓN DEL CONJUNTO 1
conjunto1 = Conjunto()
conjunto1.crearConjunto()

conjunto1.agregar(1)
conjunto1.agregar(2)
conjunto1.agregar(3)
conjunto1.agregar(4)
conjunto1.agregar(5)
conjunto1.agregar(6)
conjunto1.agregar(7)
conjunto1.agregar(8)
conjunto1.agregar(9)

# CREACIÓN DEL CONJUNTO 2
conjunto2 = Conjunto()
conjunto2.crearConjunto()
conjunto2.agregar(1)
conjunto2.agregar(2)
conjunto2.agregar(3)
conjunto2.agregar(10)
conjunto2.agregar(11)
conjunto2.agregar(12)

# CREACIÓN DEL CONJUNTO 3
conjunto3 = Conjunto()
conjunto3.crearConjunto()
conjunto3.agregar(1)
conjunto3.agregar(2)
conjunto3.agregar(3)

# UNION DE LOS ELEMENTOS
print("--------Union--------")
conjunto1.union(conjunto2)
conjunto1.mostrar()

# INTERSECCIÓN
print("--------Interseccion--------")
nuevo = conjunto1.interseccion(conjunto3)
nuevo.mostrar()

# PERTENECE
print("--------Pertenece-------")
for x in range(5):
	if conjunto1.pertenece(x) == True:
		print("El elemento "+str(x)+" pertenece al conjunto1 unido con el conjunto2")
	else:
		print("El elemento "+str(x)+" no pertenece al conjunto1 unido con el conjunto2")