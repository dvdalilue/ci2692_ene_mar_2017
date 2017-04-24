from conjunto import Apuntador
from conjunto import Conjunto


conjunto = Conjunto()

conjunto.crearconjunto()
conjunto.agregar(3)
conjunto.agregar(2)
conjunto.agregar(4)
conjunto.agregar(5)
conjunto.agregar(6)
conjunto.agregar(7)
conjunto.agregar(9)
print("~~~~~~~~estado inicial del conjunto~~~~~~")
conjunto.mostrar() #ESTADO 

print("~~~~~~~~Verificando si pertenece el valor 22~~~~~~")
conjunto.pertenece(22)

print("~~~~~~~~Verificando si pertenece el valor 9~~~~~~")
conjunto.pertenece(9)

conjunto.interseccion([1,2,3,4,5])
print("~~~~~~~~estado despues de intersectar del conjunto~~~~~~")
conjunto.mostrar() #ESTADO


conjunto.union([1,2,3,90])
print("~~~~~~~~estado despues de unir del conjunto~~~~~~")
conjunto.mostrar() #ESTADO

#conjunto.pertenece(40)