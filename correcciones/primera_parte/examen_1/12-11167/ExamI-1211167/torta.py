#Greanny Vivas Díaz 12-11167

from arrayT import ArrayT


def Mergesort (z,L,D):
	k = 1
	N = len(z)
	h = ArrayT(N)
	l = ArrayT(N)
	m = ArrayT(N)
	for i in range(N):
		h[i],l[i], m[i] = z[i],L[i],D[i]
	while k < N :
		a,b,c = 0,k,min((2*k),N)
		while b < N:
			p,q,r = a,b,a
			while p != b and q != c:
				if h[p]<=h[q]:
					z[r],L[r],D[r],r,p = h[p],l[p],m[p],r+1,p+1 
				elif h[q]<= h[p]:
					z[r],L[r],D[r],r,q = h[q],l[q],m[q],r+1,q+1  
			while p != b:
				z[r],L[r],D[r],r,p = h[p],l[p],m[p],r+1,p+1
			while q != c:
				z[r],L[r],D[r],r,q = h[q],l[q],m[q],r+1,q+1
			r = a
			while r!=c:
				h[r],l[r],m[r],r = z[r],L[r],D[r], r+1
			a,b,c = a+2*k,b+2*k,min(c+2*k,N)
		k = k*2
	return (z,L,D)

fileE = open ('entrada2.txt', 'r')

i = []
c = []
d = []

lineE = fileE.readline()
for lineE in fileE:
	tok = lineE.split("\t")
	# ingredientes:
	i.append(tok[0])
	# cantidad: 	
	c.append(tok[1])
	# disponibilidad
	d.append(tok[2].strip("\n"))

# Ordenamiento por disponibilidad:
M = Mergesort(d,i,c)
print(M)

fileS = open ('salida2.txt','w')
