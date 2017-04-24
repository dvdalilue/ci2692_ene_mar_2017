# Greanny Vivas Díaz 12-11167
from arrayT import ArrayT

#definimos Mergesort para ordenar:
def Mergesort (z):
	k = 1
	N = len(z)
	h = ArrayT(N)
	for i in range(N):
		h[i] = z[i]
	while k < N :
		a,b,c = 0,k,min((2*k),N)
		while b < N:
			p,q,r = a,b,a
			while p != b and q != c:
				if h[p]<=h[q]:
					z[r],r,p = h[p],r+1,p+1 
				elif h[q]<= h[p]:
					z[r],r,q = h[q],r+1,q+1  
			while p != b:
				z[r],r,p = h[p], r+1,p+1
			while q != c:
				z[r],r,q = h[q], r+1,q+1
			r = a
			while r!=c:
				h[r], r = z[r], r+1
			a,b,c = a+2*k,b+2*k,min(c+2*k,N)
		k = k*2

	return z

# abrir el archivo del mensaje:
fileM = open ('entrada1.txt', 'r')

# leemos el archivo
lineM = fileM.read()

# separamos la linea para hacer la lista de letras
# la linea es el arreglo 
linea = lineM.split("\t")

A = []
for i in linea:
	for letra in i:
		A.append(letra)
	print (A)


B = []
D = []
msj = []			
for i in range (0,len(A)):
	print (A[i])
	if A[i] == "*":
		for j in range(0,i):
			while A[j] != "*":
				B.append(A[j])
				break
			C = Mergesort(B)
			print("B")
			print(C)
			msj.append(C[0])
		print("msj")
		print(msj)
			

"""
# escribir el mensaje en el archivo de salida
fileS = open ('salida1.txt','w')
"""