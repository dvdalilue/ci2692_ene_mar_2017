""" Examen I .algoritmos II .ene-mar 2017 
	fecha: 16/02/2017
	autores: Edymar Mijares 12-10882
	correo: - edys.beccaria@gmail.com

	Ejercicio 2:Hacer un programa que dado un archivo de texto con los ingredientes de una torta te diga si se puede hacer o no la torta segun la cantidad de ingredientes que hay
"""
from arrayT import ArrayT
from orden import mergesort

#abro el archivo e ingreso los datos de cada linea en un arreglo
def Abrir_archivo():
	f= open('entradaTorta.txt', 'r')
	C = []
	for line in f:
    		C.append(line)
	
	N=C[0]
	C.remove(C[0])
	"""D=[]
	for i in C:
		b=C[i]
		D=b.split('\t')
	for i in D:
		D[i]=D[i].replace("\n","")"""
	print(C)
	f.close()
	return C

def Crearsub_arrgleglos(A):
	Z=50
	arrIngrediente=ArrayT(Z)
	arrCantidad=ArrayT(Z)
	arrExistencia=ArrayT(Z)
	
	Separar= []
	for i in range (0,len(A)):
		b=A[i]
		Separar=b.split("\t")
		Ingrediente = Separar[0]                
		Cantidad = Separar[1]	                
		Existencia=Separar[2] 
		arrIngrediente.append(Ingrediente)          # Se agrega la tupla al arreglo de Ingredientes
		arrCantidad.append(Cantidad)         # Se agrega la tupla al arreglo de Cantidad de ingredientes
		arrExistencia.append(Existencia)
	for i in range (0,len(arrExistencia)):
		arrExistencia[i]=arrExistencia[i].replace("\n","")
	
	return arrIngrediente , arrCantidad, arrExistencia

def Ordenar(ArrIngredi,ArrCant,ArrExis):
	Aux1=[]
	Aux2=[]
	A1=[]
	A2=[]
	B1=[]
	B2=[]
	Sepuede= 0
	for i in range (0,len(ArrExis)):
		if (ArrExis[i]=="Si"):
			Aux1.append(ArrExis[i])
			A1.append(ArrIngredi[i])
			B1.append(ArrCant[i])
		else:
			Aux2.append(ArrExis[i])
			A2.append(ArrIngredi[i])
			B2.append(ArrCant[i])
	if len(Aux1) <= len(ArrExis) :
		Sepuede = 1
	else:
		pass 

	mergesort(B1,Aux1,A1)
	ArrIngredi1=A1
	ArrCant1=B1
	ArrExis1=Aux1
	mergesort(B2,Aux2,A2)
	ArrIngredi2=A
	ArrCant2=B2
	ArrExis2=Aux2
	return ArrIngredi1,ArrIngredi2,ArrCant1,ArrCant2,ArrExis1,ArrExis2, Sepuede

def imprimir( ArrIngredi1,ArrIngredi2,ArrCant1,ArrCant2,ArrExis1,ArrExis2, Sepuede):
	s=open('salidaTorta.txt','w')
	
	if Sepuede==1:
		for i in range (0,N):
			s.write(ArrIngredi1[i]+"\t"+ArrCant1[i]+"\t"+ArrExis1[i]+"\n")
			s.write(ArrIngredi2[i]+"\t"+ArrCant2[i]+"\t"+ArrExis2[i]+"\n")
		s.write("La torta se puede preparar")
	else:
		for i in range (0,N):
			s.write(ArrIngredi1[i]+"\t"+ArrCant1[i]+"\t"+ArrExis1[i]+"\n")
			s.write(ArrIngredi2[i]+"\t"+ArrCant2[i]+"\t"+ArrExis2[i]+"\n")
		s.write("La torta no  se puede preparar")

	s.close()
	
	

		
		
#############################################prueba ejecucion##################################

E=Abrir_archivo()
print(E)
imprimir(Ordenar(Crearsub_arrgleglos(E)))


