from conjunto import Conjunto
import random

print('Creamos un primer conjunto con elementos al alzar del 0 al 30')
conjunto1 = Conjunto()

for i in range(15):
	conjunto1.Agregar(random.randint(0,30))

print('Este es el conjunto resultante')
conjunto1.Mostrar()

print('\n')
print('Creamos un segundo conjuntos con elementos al alzar del 10 al 40')
conjunto2 = Conjunto()

for i in range(15):
	conjunto2.Agregar(random.randint(10,40))

print('Este es el conjunto resultante')
conjunto2.Mostrar()


print('\n')
print('Creamos un tercer conjunto con elementos al alzar del 20 al 50')
conjunto3 = Conjunto()

for i in range(15):
	conjunto3.Agregar(random.randint(20,50))

print('Este es el conjunto resultante')
conjunto3.Mostrar()

print('\n')
print('Ahora intersectamos el conjunto 1 y 2')
intersectados1 = conjunto1.Interseccion(conjunto2)
intersectados1.Mostrar()

print('\n')
print('Ahora intersectamos el conjunto 2 y 3')
intersectados2 = conjunto2.Interseccion(conjunto3)
intersectados2.Mostrar()

print('\n')
print('Ahora intersectamos el conjunto 1 y 3')
intersectados3 = conjunto1.Interseccion(conjunto3)
intersectados3.Mostrar()

print('\n')
print('Ahora unimos el conjunto 1 y 2')
unidos1 = conjunto1.Union(conjunto2)
unidos1.Mostrar()

print('\n')
print('Ahora unimos el conjunto 2 y 3')
unidos2 = conjunto2.Union(conjunto3)
unidos2.Mostrar()

print('\n')
print('Ahora unimos el conjunto 1 y 3')
unidos3 = conjunto1.Union(conjunto3)
unidos3.Mostrar()

print('\n')
print('Finalmente vemos si elementos al azar entre 0 y 50 pertenecen a los conjuntos')
for i in range(20):
	n = random.randint(0,50)
	if i in [0,3,6,9,12,15,18]:
		print('El elemento '+str(n)+' pertenece al primer conjunto:', conjunto1.Pertenece(n))
	elif i in [1,4,7,10,13,16,19]:
		print('El elemento '+str(n)+' pertenece al segundo conjunto:', conjunto2.Pertenece(n))
	else:
		print('El elemento '+str(n)+' pertenece al tercer conjunto:', conjunto3.Pertenece(n))

print('\n')
print('Han terminado las pruebas')