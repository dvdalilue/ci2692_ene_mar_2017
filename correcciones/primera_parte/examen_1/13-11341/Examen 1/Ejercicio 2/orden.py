"""
# Descripcion: EJERCICIO 3
# Autor: Jesus Kauze y David Segura
# email: 12-10273@usb.ve y 13-11341@usb.ve
"""
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
				if arreglo[p].lower() <= arreglo[q].lower():
					NuevoArreglo[r] = arreglo[p]
					r,p = r+1, p+1
				elif arreglo[q].lower() <= arreglo[p].lower():
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
