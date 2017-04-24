f = open('entrada.txt', 'r+')

g = open('salida.txt', 'w')

ff = f.readlines()

print ff

for line in f.readlines():
	l = line.split('\t')
	
