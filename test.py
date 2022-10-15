from funciones import lector_seismos
import funciones_aux
from datetime import datetime


if __name__ == "__main__":
    seismos = lector_seismos("C:/Users/ALEX/proy_entreg/P01-Proyecto-1C/data/seismo.csv")
    print(seismos)