"""DESCRIPCION: Los estudiantes del Laboratorio de Algoritmos II le quieren hacer una torta sor-
presa a la Prof. Catherine para celebrar su cumpleaños. Para ello deberán seguir una receta
en la cual se indican los ingredientes que se necesitan y su cantidad. Como no todos los ingre-
dientes son fáciles de conseguir, también se indicará si es posible conseguirlos o no.

Autor: David Segura 13-11341
Email: 13-11341@usb.ve"""

from arrayT import ArrayT

def merge_sort(arreglo):
	k = 1
	N=len(arreglo)
	NuevoArreglo=ArrayT(N)
	while k<N:
		a,b,c = 0, k, min(2*k,N)
		while b<N:
			p,q,r = a,b,a
			while p!=b and q !=c:
				if arreglo[p] <= arreglo[q]:
					NuevoArreglo[r] = arreglo[p]
					r,p = r+1, p+1
				elif arreglo[q] <= arreglo[p]:
					NuevoArreglo[r]=arreglo[q]
					r,q = r+1, q+1
			while p != b:
				NuevoArreglo[r] = arreglo[p]
				r,p = r+1, p+1
			while q != c:
				NuevoArreglo[r] = arreglo[q]
				r,q = r+1, q+1
			r = a
			while r!=c:
				arreglo[r]=NuevoArreglo[r]
				r = r+1
			a,b,c = a + 2*k, b + 2*k, min(c + 2*k,N)
		k = k*2
	return NuevoArreglo


archivo = input("Nombre del archivo(Debe terminar en .txt) = ")
lectura=open(archivo,"r")
numero = int(lectura.readline())

ingredientes=ArrayT(numero)
cantidad=ArrayT(numero)
existencia=ArrayT(numero)
original=ArrayT(numero)
resultado_cantidad=ArrayT(numero)
resultado_ingre=ArrayT(numero)

i = 0
for lineas in lectura.readlines():
	j = i+1
	while i < j and j<=numero:
		original[i]=lineas.strip("\n")
		tok = lineas.split("\t")
		ingredientes[i]=tok[0]
		cantidad[i]=tok[1].strip("\n")
		i = i + 1

ingredientes1= merge_sort(ingredientes)

j=0
for x in ingredientes1:
	for i in original:
		if x == i[0:len(x)]:
			resultado_ingre[j]=i
			j = j+1


escritura=open("salida.txt","w")
for x in resultado_ingre:
	escritura.write(x)
	escritura.write("\n")
escritura.close()
lectura.close()