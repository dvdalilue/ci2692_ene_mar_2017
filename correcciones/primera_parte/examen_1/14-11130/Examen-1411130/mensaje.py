#Sandra Vera
#14-11130

from arrayT import ArrayT
from heap_functions import heap_sort,dequeue

with open('pruebamensaje.txt','r') as f:
	list_entrada=f.readlines()
	list_letras=ArrayT(len(list_entrada))
	for i in range(len(list_letras)):
		list_letras[i]=list_entrada[i]
	mensj=str(list_letras)
	if mensj[len(mensj)-1]!='*':
		array_aux=ArrayT(len(list_letras))
		array_letras=ArrayT(len(list_letras))
		for i in range(len(array_letras)):
			array_letras[i]=mensj.split('*')
		for i in range(len(array_letras)):
			print(array_letras[i])
	#	array_letras=ArrayT(len(list_letras)-1)
	#	for i in range(len(array_letras)):
	#		array_letras[i]=list_letras[i].split('*')

	#for i in range(len(array_letras)):
	#	print(array_letras[i])

