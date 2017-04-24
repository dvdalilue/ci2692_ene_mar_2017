# Parcial no.2
# Greanny Vivas 12-11167

from conjunto import*
# Tenemos un conjunto vacio A al que se le agregaran los enteros
A = Conjunto()

A.Agregar("7")
A.Agregar("6")
A.Agregar("5")
A.Agregar("4")
A.Agregar("3")
A.Agregar("2")
A.Agregar("1")
A.Agregar("1")
A.Agregar("2")
A.Agregar("3")
A.Agregar("4")
A.Agregar("5")
A.Agregar("6")
A.Agregar("7")

print("Sea A un conjunto")

print("A = ")
A.Mostrar()

# Tenemos un conjunto vacio B al que se le agregaran los enteros
B = Conjunto()

B.Agregar("15")
B.Agregar("14")
B.Agregar("13")
B.Agregar("12")
B.Agregar("11")
B.Agregar("10")
B.Agregar("9")
B.Agregar("8")
B.Agregar("7")
B.Agregar("6")

print("Sea B un conjunto")

print("B = ")
B.Mostrar()

# Unimos el conjunto A con el conjunto B
print("La union de A con B resulta en el conjunto")
print("A U B = ")

C = A.Union(B)
C.Mostrar()

# Intersectamos el conjunto A con el conjunto B
print("La interseccion de A con B resulta en el conjunto")
print("A ∩ B = ")

C = A.Interseccion(B)
C.Mostrar()
