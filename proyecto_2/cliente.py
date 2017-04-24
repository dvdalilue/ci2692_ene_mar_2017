from pathlib import Path
from cancion import Cancion
from reproductor import Reproductor

from PyQt5.QtWidgets import *

import sys
import subprocess as sp

def processFile(filepath):
    songs = []

    with open(filepath) as f:
        for line in f:
            split = line.rstrip().split("-")
            songs.append(Cancion(split[1],split[0],split[2]))

    return songs

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Solo debe recibirse un argumento"
    assert Path(sys.argv[-1]).is_file(), "El archivo de entrada no existe"

    songs = processFile(sys.argv[-1])

    app = QApplication(sys.argv)
    rep = Reproductor()
    rep.show()
    sp.call('clear',shell=True)

    #############
    # Menu loop #
    #############
    print("\n1. List all songs\n2. Add song to play next\n3. Add song to play later\n4. Sort songs by artist\n5. Sort songs by title\n8. Show help\n9. Show GUI if is closed\n0. Quit")
    while True:
        option = int(input('Choose your option: '))
        if (option == 1):
            x = 0
            print("")
            for s in songs:
                print(x, s.mostrar_por_titulo())
                x += 1
            print("")
        elif (option == 2):
            item = int(input('Song number: '))
            rep.sonarDespues(songs[item])
        elif (option == 3):
            item = int(input('Song number: '))
            rep.sonarAntes(songs[item])
        elif (option == 4):
            # Sort songs by artist
            pass
        elif (option == 5):
            # Sort songs by title
            pass
        elif (option == 8):
            print("\n1. List all songs\n2. Add song to play next\n3. Add song to play later\n4. Sort song by artist\n5. Sort songs by title\n8. Show help\n9. Show GUI if is closed\n0. Quit")
        elif option == 9:
            rep.show()
            sp.call('clear',shell=True)
        elif option == 0:
            sys.exit(0)
        else:
            pass
    # Fin menu

    sys.exit(app.exec_())