from collections import namedtuple
import csv
from datetime import datetime
import statistics
import funciones_aux
from statistics import *

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

def filtra_por_pais(archivo, pais):
    return [ t for t in archivo if t.PAIS==pais]

def promedio_muertes(archivo):
    lista =[]
    for t in archivo:
        lista.append(t.MUERTES)
        prom = mean(lista)
    return prom

def ordenar_por_fecha(archivo, n, tsunami = None):
    if tsunami != None:
        filtrado = [ t for t in archivo if t.TSUNAMI==tsunami]
        res = sorted(filtrado, key=lambda t:t.FECHA, reverse=False)[:n]
    else:
        res = sorted(archivo, key=lambda t:t.FECHA, reverse=False)[:n]
    return res

def maximos_heridos(archivo):
    maximo = max(archivo, key=lambda t:t.HERIDOS)
    res = [t for t in archivo if t.HERIDOS==maximo.HERIDOS]
    return res
    
def pais_mas_frecuente(archivo):
    freq = max(archivo, key = lambda t:t.PAIS)
    res = [ t.PAIS for t in archivo if t.PAIS==freq.PAIS]
    return set(res)
