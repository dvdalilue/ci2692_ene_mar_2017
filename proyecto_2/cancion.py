from pathlib import Path
from PyQt5.QtCore import QFile

class Cancion:
    def __init__(self, titulo, artista, filepath):
        assert titulo != "", "Titulo de canción no debe ser vacío"
        assert artista != "", "Artista de canción no debe ser vacío"

        my_file = Path(filepath)
        assert my_file.is_file(), "El  archivo '" + filepath[:-1] + "' debe existir"
        assert filepath.endswith('.wav'), "El archivo debe estar en formato wav"

        self.titulo = titulo
        self.artista = artista
        self.archivo = QFile(filepath)

    def es_igual(other):
        if self.titulo == other.titulo and self.artista == other.artista:
            return True
        return False

    def es_menor_artista(other):
        if self.artista < other.artista:
            return True
        elif self.artista == other.artista and self.titulo <= other.titulo:
            return True
        return False

    def es_menor_titulo(other):
        if self.titulo < other.titulo:
            return True
        elif self.titulo == other.titulo and self.artista <= other.artista:
            return True
        return False

    def mostrar_por_titulo(self):
        string = self.titulo + " - " + self.artista
        return string

    def mostrar_por_artista(self):
        string = self.artista + " - " + self.titulo
        return string