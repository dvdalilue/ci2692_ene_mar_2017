from arrayT import ArrayT

#Nombre de los archivos
file_input = input('Introduzca el nombre del archivo de entrada (Ej: entrada.txt):')
file_output = "salida.txt"

#Funcion para determinar la existencia

def orden(a,b):
	if a.lower() == 'si' and (b.lower() == 'no' or b.lower() == 'si'):
		return True
	elif a.lower() == 'no' and b.lower() == 'no':
		return True
	elif a.lower() == 'no' and b.lower() == 'si':
		return False

def merge_sort_existence(E, C, N, tipo):
	n = len(E)
	k = 1

	while k < n:
		a,b,c = 0, k, min((2*k),n)

		while b < n:
			p,q,r = a,b,a
			z  = ArrayT(c)
			z2 = ArrayT(c)
			z3 = ArrayT(c)
			while p!= b and q != c:
				if tipo == 1:
					if orden(E[p], E[q]): 
						z[r] = E[p]
						z2[r] = C[p]
						z3[r] = N[p]
						r,p  = r+1, p+1
					else:
						z[r] = E[q]
						z2[r] = C[q]
						z3[r] = N[q]
						r,q  = r+1, q+1
				elif tipo == 2:
					if int(C[p]) >= int(C[q]): 
						z[r] = E[p]
						z2[r] = C[p]
						z3[r] = N[p]
						r,p  = r+1, p+1
					else:
						
						z[r] = E[q]
						z2[r] = C[q]
						z3[r] = N[q]
						r,q  = r+1, q+1
				elif tipo == 3:
					if N[p] <= N[q]: 
						z[r] = E[p]
						z2[r] = C[p]
						z3[r] = N[p]
						r,p  = r+1, p+1
					else:
						
						z[r] = E[q]
						z2[r] = C[q]
						z3[r] = N[q]
						r,q  = r+1, q+1

			while p != b:
				z[r] = E[p]
				z2[r] = C[p]
				z3[r] = N[p]
				r,p = r+1, p+1

			while q != c:
				z[r] = E[q]
				z2[r] = C[q]
				z3[r] = N[q]
				r,q = r+1, q+1
			r = a

			while r != c:
				E[r] = z[r]
				C[r] = z2[r]
				N[r] = z3[r]
				r = r+1

			a,b,c = a+2*k,b+2*k, min((c+2*k), n)
		k = k*2


def torta(E, C, N):

	merge_sort_existence(E, C, N, 1)

	i = 0
	while i < len(E)-1:
		if E[i] == E[i+1] and E[i].lower() == 'si':
			j = i + 1
			while j < len(E)-1 and E[i] == E[j+1]:
				j = j + 1
		
			auxE = ArrayT(j-i+1)
			auxC = ArrayT(j-i+1)
			auxN = ArrayT(j-i+1)
			for k in range(j-i+1):
				auxN[k] = N[i+k]
				auxC[k] = C[i+k]
				auxE[k] = E[i+k]
			merge_sort_existence(auxE,auxC,auxN,2)
			for k in range(j-i+1):
				N[i+k] = auxN[k]
				C[i+k] = auxC[k]
				E[i+k] = auxE[k]
			i = j + 1
		else:
			i = i + 1

	si = j
	i = 0
	while i < si:
		if int(C[i]) == int(C[i+1]):
			j = i + 1
			while j < si and int(C[i]) == int(C[j+1]):
				j = j + 1
		
			auxE = ArrayT(j-i+1)
			auxC = ArrayT(j-i+1)
			auxN = ArrayT(j-i+1)
			for k in range(j-i+1):
				auxN[k] = N[i+k]
				auxC[k] = C[i+k]
				auxE[k] = E[i+k]
			merge_sort_existence(auxE,auxC,auxN,3)
			for k in range(j-i+1):
				N[i+k] = auxN[k]
				C[i+k] = auxC[k]
				E[i+k] = auxE[k]
			i = j + 1
		else:
			i = i + 1

	i = si + 1
	while i < len(C)-1:
		if int(C[i]) == int(C[i+1]):
			j = i + 1
			while j < len(C)-1 and int(C[i]) == int(C[j+1]):
				j = j + 1
		
			auxE = ArrayT(j-i+1)
			auxC = ArrayT(j-i+1)
			auxN = ArrayT(j-i+1)
			for k in range(j-i+1):
				auxN[k] = N[i+k]
				auxC[k] = C[i+k]
				auxE[k] = E[i+k]
			merge_sort_existence(auxE,auxC,auxN,3)
			for k in range(j-i+1):
				N[i+k] = auxN[k]
				C[i+k] = auxC[k]
				E[i+k] = auxE[k]
			i = j + 1
		else:
			i = i + 1

## Almacenamos los datos en arreglos
with open(file_input, 'r') as f:
	lineas = int(f.readline())
	ingredientes = ArrayT(lineas)
	cantidad  = ArrayT(lineas)
	existen = ArrayT(lineas)
	for i in range(lineas):
		datos = f.readline().split("\t")
		ingredientes[i] = datos[0]
		cantidad[i] = datos[1]
		existen[i] = datos[2].strip("\n")
f.close()

# Ordenamos
torta(existen, cantidad, ingredientes)
file = open(file_output, "w")

for i in range(lineas):
	file.write(ingredientes[i] + "\t" + cantidad[i] + "\t" + existen[i] + "\n")

i = 0
posible = 0
while i<lineas:
	if existen[i].lower() == 'si':
		posible = posible + 1
	i = i+1

if posible >= (lineas/2):
	file.write("La torta se puede preparar" + "\n")
else:
	file.write("La torta no se puede preparar" + "\n")

file.close()