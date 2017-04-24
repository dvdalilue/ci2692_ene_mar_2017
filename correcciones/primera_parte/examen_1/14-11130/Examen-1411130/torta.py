#Sandra Vera
#14-11130

from arrayT import ArrayT
from quicksort import quicksort_basico
from heap_functions import heap_sort

with open('pruebaingredientes.txt','r') as f:

	list_entrada=f.readlines()
	#print(list_i)
	total_ingredientes=list_entrada[0].strip('\n')
	list_ingr=ArrayT(int(total_ingredientes))
	for i in range(len(list_ingr)):
		list_ingr[i]=list_entrada[i+1].strip('\n')

	#Creo una lista para cada ingrediente
	ingrediente=ArrayT(len(list_ingr))
	for i in range(len(ingrediente)):
		ingrediente[i]=list_ingr[i].split('	')
f.close


#Cuento la cantidad de ingredientes que se pueden conseguir y los que no
cantidad_ingr_existen=0
cantidad_ingr_no_existen=0
for i in range(len(ingrediente)):
	if ingrediente[i][2]=='Si':
		cantidad_ingr_existen=cantidad_ingr_existen+1
	elif ingrediente[i][2]=='No':
		cantidad_ingr_no_existen=cantidad_ingr_no_existen+1

#Creo una lista con los ingredientes que existen
ingr_existen=ArrayT(cantidad_ingr_existen)
j=0
for i in range(len(ingrediente)):
	if ingrediente[i][2]=='Si':
		ingr_existen[j]=ingrediente[i]
		j=j+1
	else:
		pass

#for i in range(len(ingr_existen)):
#	print(ingr_existen[i])

#Creo una lista con los ingredientes que no existen
ingr_no_existen=ArrayT(cantidad_ingr_no_existen)
j=0
for i in range(len(ingrediente)):
	if ingrediente[i][2]=='No':
		ingr_no_existen[j]=ingrediente[i]
		j=j+1
	else:
		pass



#Ordeno los ingredientes que existen por cantidad
orden_ingr_existen=ArrayT(cantidad_ingr_existen)
for i in range(len(orden_ingr_existen)):
	orden_ingr_existen[i]=ingr_existen[i][1]

orden_ingr_existen=quicksort_basico(orden_ingr_existen)


#Indica si hay elementos que existen repetidos
repetidos_existen=0
j=0
for i in range(len(orden_ingr_existen)):
	for j in range(len(orden_ingr_existen)):
		if i!=j:
			if orden_ingr_existen[i]==orden_ingr_existen[j]:
				repetidos_existen=repetidos_existen+1

repetidos_existen=repetidos_existen//2
#Creo una lista con los indices de los elementos que tienen igual cantidad (si existen)
#if elementos_repetidos>0:
#	elementos_repetidos=ArrayT(repetidos_existen+1)
#for i in range(len(orden_ingr_existen)):
#	for j in range(len(orden_ingr_existen)):
#		if orden_ingr_existen[i]==orden_ingr_existen[j]:
#			elementos_repetidos[i]=i

#for i in range(len(elementos_repetidos)):
#	print(elementos_repetidos[i])

orden_ingr=quicksort_basico(orden_ingr_existen)

ingr_existen_ordenados=ArrayT(len(ingr_existen))

for i in range(len(ingr_existen_ordenados)):
	ingr_existen_ordenados[i]=ArrayT(3)
	ingr_existen_ordenados[i][1]=orden_ingr[i]
	ingr_existen_ordenados[i][2]='Si'


for i in range(len(ingr_existen_ordenados)):
	for j in range(len(orden_ingr)):
		if int(ingr_existen[i][1])==int(orden_ingr[j]):
			ingr_existen_ordenados[j][0]=ingr_existen[i][0]



#Ordeno los ingredientes que no existen por cantidad
orden_ingr_no_existen=ArrayT(cantidad_ingr_no_existen)
for i in range(len(orden_ingr_no_existen)):
	orden_ingr_no_existen[i]=ingr_no_existen[i][1]

orden_ingr_no=quicksort_basico(orden_ingr_no_existen)

ingr_no_existen_ordenados=ArrayT(len(ingr_no_existen))

for i in range(len(ingr_no_existen_ordenados)):
	ingr_no_existen_ordenados[i]=ArrayT(3)
	ingr_no_existen_ordenados[i][1]=orden_ingr[i]
	ingr_no_existen_ordenados[i][2]='No'

for i in range(len(ingr_no_existen_ordenados)):
	for j in range(len(orden_ingr_no)):
		if int(ingr_no_existen[i][1])==int(orden_ingr_no[j]):
			ingr_no_existen_ordenados[j][0]=ingr_no_existen[i][0]



with open('pruebaingredientes.txt','w') as f:
	#Escribo los ingredientes que existen en orden descendente
	f.write(total_ingredientes)
	f.write('\n')
	i=len(ingr_existen_ordenados)-1
	while i>=0:
		f.write(ingr_existen_ordenados[i][0])
		f.write('	')
		f.write(ingr_existen_ordenados[i][1])
		f.write('	')
		f.write(ingr_existen_ordenados[i][2])
		f.write('\n')
		i=i-1

	j=len(ingr_no_existen_ordenados)-1
	while j>=0:
		f.write(ingr_no_existen_ordenados[i][0])
		f.write('	')
		f.write(ingr_no_existen_ordenados[i][1])
		f.write('	')
		f.write(ingr_no_existen_ordenados[i][2])
		f.write('\n')
		j=j-1

	if cantidad_ingr_no_existen>(len(ingrediente)//2):
		f.write('La torta no se puede preparar.')
	elif cantidad_ingr_no_existen<(len(ingrediente)//2):
		f.write('La torta se puede preparar.')
f.close

