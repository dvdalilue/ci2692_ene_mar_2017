# Examen 2
# Autor: Jorge Sanchez
#
# Examen2
# Autor: Jorge Sanchez
# 		 10-10673

from conjunto import*

A = Conjunto()
B = Conjunto()

print('')
print('Agregamos elementos a A, conjunto vacio:')

A.Agregar(0)
A.Agregar(4)
A.Agregar(6)
A.Agregar(0)
A.Agregar(3)
A.Agregar(8)
print('')
print('Agregamos elementos a B, conjunto vacio:')
B.Agregar(3)
B.Agregar(5)
B.Agregar(1)
B.Agregar(7)
B.Agregar(8)
B.Agregar(4)
B.Agregar(6)
B.Agregar(1)
print('')
print('Conjunto A')
A.Mostrar()
print('')
print('Conjunto B')
B.Mostrar()
print('')
print('Interseccion de A y B')
B.Interseccion(A)
print('')
print('Union de A y B')
A.Union(B)