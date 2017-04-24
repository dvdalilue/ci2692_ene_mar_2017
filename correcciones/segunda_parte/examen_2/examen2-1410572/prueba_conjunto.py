from conjunto import Conjunto
from math import sqrt

"""
************************************
	Alumno: Yeferson Licet
	Carnet: 14-10572

	Parcial 2 - Cliente
	prueba_conjunto.py
************************************
"""


print("\n")
print("*****************************************")
print("Iniciando cliente")
print("\n")

print("*****************************************")
print("Creando conjunto de numeros primos < 50:")
print("*****************************************")
print("\n")
primos = Conjunto()

primos.Agregar(2)
for i in range(3,50, 2):
	
	prime = True
	for k in range(2, int(sqrt(i))+1):
		if i%k ==0:
			prime = False
			break

	if prime:
		primos.Agregar(i)

primos.Mostrar()
print("\n")
print("*****************************************")
print("Creando conjunto de numeros pares < 50:")
print("*****************************************")
print("\n")

pares = Conjunto()
for i in range(2,50, 2):
	pares.Agregar(i)
pares.Mostrar()

print("\n")
print("*****************************************")
print("Intersectando pares y primos < 50")
print("*****************************************")
print("\n")
paresprimos = primos.Interseccion(pares)
paresprimos.Mostrar()

print("\n")
print("*****************************************")
print("Pertenece el numero 2 al resultado?")
print("*****************************************")
print("\n")
print(paresprimos.Pertenece(2))

print("\n")
print("*****************************************")
print("Pertenece el numero 5 al resultado?")
print("*****************************************")
print("\n")
print(paresprimos.Pertenece(5))

print("\n")
print("*****************************************")
print("Uniendo el singleton {2} y el singleton {5}")
print("*****************************************")
print("\n")

singleton5 = Conjunto()
singleton5.Agregar(5)

resultadosingletones = singleton5.Union(paresprimos)
resultadosingletones.Mostrar()

print("\n")
print("*****************************************")
print("Pertenece el numero 2 al resultado?")
print("*****************************************")
print("\n")
print(resultadosingletones.Pertenece(2))

print("\n")
print("*****************************************")
print("Pertenece el numero 5 al resultado?")
print("*****************************************")
print("\n")
print(resultadosingletones.Pertenece(5))


print("\n")
print("*****************************************")
print("Intersectando el singleton {2} y el singleton {5}")
print("*****************************************")
print("\n")
interseccion52 = singleton5.Interseccion(paresprimos)
interseccion52.Mostrar()

print("\n")
print("Fin del cliente")
print("*****************************************")
print("\n")





