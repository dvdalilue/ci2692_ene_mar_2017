


#algoritmo mergesort
def mergesort(A,B,C):
	k = 1
	N = len(A)
	A3 = []
	B3 = []
	C3= []
	while k < N:
		a = 0
		b = k
		c = min((2*k),N)
		while  b < N:
			for x in range(a,c):
				A3.append("")
				B3.append("")
				C3.append("")
			p,q,r = a,b,a
			while p!=b and q!=c:
				if A[p] <= A[q]:
					A3[r] = A[p]
					B3[r] = B[p]
					C3[r] = C[p]
					r += 1
					p += 1
				elif A[q] <= A[p]:
					A3[r] = A[q]
					B3[r] = B[q]
					C3[r] = C[q]
					r += 1
					q += 1
			while p!=b:
				A3[r] = A[p]
				B3[r] = B[p]
				C3[r] = C[p]
				r += 1
				p += 1
			while q!=c:
				A3[r] = A[q]
				B3[r] = B[q]
				C3[r] = C[q]
				r += 1
				q += 1
			r = a
			while r!=c:
				A[r] = A3[r]
				B[r] = B3[r]
				C[r] = C3[r]
				r += 1
			a,b,c = a+(2*k),b+(2*k),min((c+(2*k)),N)
		k = k*2
	return A,B,C
	


