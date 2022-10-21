from collections import namedtuple
import csv
from datetime import datetime
import funciones_aux

seismo = namedtuple("seismo", "ID,TSUNAMI,FECHA,HORA,PAIS,LATITUD,LONGITUD,MUERTES,HERIDOS")
def lector_seismos(archivo):
    lista = []
    with open (archivo) as f:
        lector = csv.reader(f,delimiter = ";")
        next (lector)
        for i_d,tsun,fecha,hora,pais,lat,long,muert,her in lector:
            ident= int(i_d)
            tsunami = bool(tsun)
            fecha2 = datetime.strptime(fecha, "%d/%m/%Y").date()
            hora2 = datetime.strptime(hora, "%H:%M:%S").time()
            latitud = float(lat)
            longitud = float(long)
            muertes = funciones_aux.parse_muertes(muert)
            heridos = funciones_aux.parse_heridos(her)
            tupla = seismo(ident, tsunami, fecha2, hora2, pais, latitud, longitud, muertes, heridos)
            lista.append(tupla)
        return lista

