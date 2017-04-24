from pathlib import Path
from PyQt5.QtCore import QFile

class Cancion:
    def __init__(self, titulo, artista, filepath):
        
        if len(titulo) < 1:
            print("El Titulo de la cancion es muy corto")
            return
        elif len(artista) < 1:
            print("El Artista de la cancion es muy corto")
            return
        elif filepath == None:
            print("La ruta del archivo es invalida")
            return
        
        self.titulo     = titulo
        self.artista    = artista
        self.archivo    = QFile(filepath)
        
    def es_igual(self, other):
        return self.titulo == other.titulo and self.artista == other.artista

    def es_menor_artista(self, other):
        if self.artista == other.artista:
            return self.titulo <= other.titulo
        
        return self.artista <= other.artista

    def es_menor_titulo(self, other):
        if self.titulo == other.titulo:
            return self.artista <= other.artista
        
        return self.titulo <= other.titulo