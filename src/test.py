from funciones import *


if __name__ == "__main__":
    seismos = lector_seismos("C:/Users/ALEX/proy_entreg/P01-Proyecto-1C/data/seismo.csv")
    for r in seismos:
        print(r)