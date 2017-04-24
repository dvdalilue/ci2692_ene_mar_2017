class Gato:

    genero = 'felino'
    
    def __init__(self,nombre):
        self.nombre = nombre
        
    @classmethod
    def imprimir_genero(cls):
        s = 'Genero: ' + cls.genero # 
        print(s)