from cancion import Cancion

test_counter = 0
test_passed = 0

# Prueba unitarias para canciones

c1 = Cancion("High", "Rawayana","samples/audio1.wav")
c2 = Cancion("Blue Boy","Mac Demarco", "samples/audio2.wav")
c3 = Cancion("Dopamime", "DIIV","samples/audio3.wav")
c4 = Cancion("Under Cover","Ducktails", "samples/audio4.wav")
c5 = Cancion("15 Step","Radiohead", "samples/audio5.wav")

test_counter += 1

if c1.titulo == "High":
        test_passed += 1
test_counter += 1

if c2.titulo == "Blue Boy":
        test_passed += 1
test_counter += 1

if c3.titulo == "Dopamime":
        test_passed += 1
test_counter += 1

if c4.titulo == "Under Cover":
        test_passed += 1
test_counter += 1

if c5.titulo == "15 Step":
        test_passed += 1

test_counter += 1

if c1.artista == "Rawayana":
        test_passed += 1
test_counter += 1

if c2.artista == "Mac Demarco":
        test_passed += 1
test_counter += 1

if c3.artista == "DIIV":
        test_passed += 1
test_counter += 1

if c4.artista == "Ducktails":
        test_passed += 1
test_counter += 1

if c5.artista == "Radiohead":
        test_passed += 1

test_counter += 1

if c2.es_menor_titulo(c1):
        test_passed += 1
test_counter += 1

if c5.es_menor_titulo(c2):
        test_passed += 1
test_counter += 1

if c4.es_menor_titulo(c4):
        test_passed += 1
test_counter += 1

if c1.es_menor_titulo(c4):
        test_passed += 1
test_counter += 1

if c3.es_menor_titulo(c1):
        test_passed += 1

test_counter += 1

if c1.es_menor_artista(c1):
        test_passed += 1
test_counter += 1

if c2.es_menor_artista(c5):
        test_passed += 1
test_counter += 1

if c3.es_menor_artista(c2):
        test_passed += 1
test_counter += 1

if c4.es_menor_artista(c2):
        test_passed += 1
test_counter += 1

if c5.es_menor_artista(c1):
        test_passed += 1

test_counter += 1

if c1.es_igual(c1):
        test_passed += 1
test_counter += 1

if c2.es_igual(c2):
        test_passed += 1
test_counter += 1

if c3.es_igual(c3):
        test_passed += 1
test_counter += 1

if c4.es_igual(c4):
        test_passed += 1
test_counter += 1

if c5.es_igual(c5):
        test_passed += 1
print("Grade: " + str(float(test_passed)/float(56)))

lista = ListaReproduccion()


lista.agregar_final(c1)

lista.agregar_final(c2)
test_counter += 1

if lista.proximo.elemento.es_igual(c1):
        test_passed += 1
test_counter += 1

if lista.proximo.anterior.elemento.es_igual(c2):
        test_passed += 1


lista.agregar(c3)
test_counter += 1

if lista.proximo.elemento.es_igual(c3):
        test_passed += 1
test_counter += 1

if lista.proximo.siguiente.elemento.es_igual(c1):
        test_passed += 1


lista.agregar_final(c4)
test_counter += 1

if lista.proximo.elemento.es_igual(c3):
        test_passed += 1
test_counter += 1

if lista.proximo.anterior.elemento.es_igual(c4):
        test_passed += 1


lista.agregar(c5)

test_counter += 1

if lista.proximo.elemento.es_igual(c5):
        test_passed += 1
test_counter += 1

if lista.proximo.anterior.elemento.es_igual(c4):
        test_passed += 1


lista.ordenar_titulo(lista)

tmp = lista.proximo

for i in range(lista.count-1):
    test_counter += 1

    if tmp.elemento.es_menor_titulo(tmp.siguiente.elemento):
        test_passed += 1
    tmp = tmp.siguiente

lista.ordenar_artista(lista)

tmp = lista.proximo

for i in range(lista.count-1):
    test_counter += 1

    if tmp.elemento.es_menor_artista(tmp.siguiente.elemento):
        test_passed += 1
    tmp = tmp.siguiente

# 31 ifs

def member(lista, titulo):
    tmp = lista.proximo

    for i in range(lista.count-1):
        if tmp.elemento.titulo == titulo:
            return True
        tmp = tmp.siguiente
    

    return False


lista.eleminar("High")

tmp = lista.proximo

for i in range(lista.count-1):
    test_counter += 1

    if not member(lista,"High"):
        test_passed += 1
    tmp = tmp.siguiente


tmp = lista.proximo

for i in range(lista.count-1):
    test_counter += 1

    if tmp.elemento.es_menor_artista(tmp.siguiente.elemento):
        test_passed += 1
    tmp = tmp.siguiente

lista.ordenar_titulo(lista)

tmp = lista.proximo

for i in range(lista.count-1):
    test_counter += 1

    if tmp.elemento.es_menor_titulo(tmp.siguiente.elemento):
        test_passed += 1
    tmp = tmp.siguiente

lista.eleminar("Dopamine")

tmp = lista.proximo

for i in range(lista.count-1):
    test_counter += 1

    if not member(lista,"Dopamine"):
        test_passed += 1
    tmp = tmp.siguiente


tmp = lista.proximo

for i in range(lista.count-1):
    test_counter += 1

    if tmp.elemento.es_menor_titulo(tmp.siguiente.elemento):
        test_passed += 1
    tmp = tmp.siguiente

print("Grade: " + str(float(test_passed)/float(test_counter)))