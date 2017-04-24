"""
# Descripcion: Examen 1 Torta
# Autor: 10-10673 Jorge Sanchez

# email: jorges1002@gmail.com

"""
from arrayT import ArrayT
# Nota: Fracase implementando el mergesort para utilizar el ArrayT.
# La siguiente entrega funciona sin utilizar el ArrayT, mas insertion sort.

def swap(array, i, j):
    array [i],array[j] = array[j] , array[i]
    return


#File de Entrada:
fileE = open ('ing2.txt', 'r')

I = []
C = []
E = []

lineE = fileE.readline()
for lineE in fileE:
	tok = lineE.split("\t")
	I.append(tok[0])
	C.append(tok[1]) 	
	E.append(tok[2].strip("\n"))

#Insertion para ordenar por existencia de ingredientes
def insertion_sortE(a,b,c):
	n = len(a)
	for i in range (1,n):
		key = a[i]
		j = i-1
		while j >= 0 and a[j] < key:
			swap(a,j+1,j)
			swap(b,j+1,j)
			swap(c,j+1,j)
			j -= 1
		a[j+1] = key	
	return (b,c,a)

#Numero de inexistencias de ingredientes
NumNo = 0
for i in range(0,len(I)):
	if E[i] == 'No':
		NumNo += 1

# Insertion para ordenar por cantidad de ingredientes
def insertion_sortC(a,b,c):
	n = len(a)-NumNo
	for i in range (1,n):
		key = a[i]
		j = i-1
		while j >= 0 and a[j] < key:
			swap(a,j+1,j)
			swap(b,j+1,j)
			swap(c,j+1,j)
			j -= 1
		a[j+1] = key	
	return (b,a,c)

# Ordenamiento por existencia:

A = insertion_sortE(E,I,C)

print(A)
print('')
I,C,E = A[0],A[1],A[2]

#Ordenamiento por Cantidad
B = insertion_sortC(C,I,E)
print(B)
print('')
I,C,E = B[0],B[1],B[2]
#Ordenamiento por Ingredientes (de ser necesario)
def Ord_Ingrediente(I,C,E):
	for i in range(0,len(E)-NumNo):
		if C[i] == C[i+1] and I[i] > I[i+1] and E[i] == E[i+1]:
			swap(I,i+1,i)
			swap(C,i+1,i)
			swap(E,i+1,i)
		else:
			pass
	return(I,C,E)

D = Ord_Ingrediente(I,C,E)
print(D)

fileS = open ('salida2.txt','w')
for i in range(0,len(I)):
	fileS.write(D[0][i])
	fileS.write("	")
	fileS.write(D[1][i])
	fileS.write("	")
	fileS.write(D[2][i])
	fileS.write("\n")

fileS.write("\n")

no_se_puede = 0
for i in range (0,len(E)):
	if E[i] == 'No':
		no_se_puede += 1

if no_se_puede > len(E)//2:
	fileS.write("La torta no se puede preparar")
else:
	fileS.write("La torta se puede preparar")
