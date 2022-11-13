from funciones import *

def test_filtra_por_pais(archivo, pais):
    filtrado_pais= filtra_por_pais(archivo, pais)
    print(filtrado_pais)

def test_lector_seismos(archivo):
        for r in seismos:
            print(r)

def test_promedio_muertes(archivo):
    prom= promedio_muertes(archivo)
    print(prom)

def test_ordenar_por_fecha(archivo, n, tsunami):
    orden = ordenar_por_fecha(archivo, n, tsunami)
    print(orden)

def test_maximos_heridos(archivo):
    res = maximos_heridos(archivo)
    print(res)

def test_pais_mas_frecuente(archivo):
    res = pais_mas_frecuente(archivo)
    print (res) 

if __name__ == "__main__":
    seismos = lector_seismos("../P01-Proyecto-1C/data/seismo.csv")
    #test_lector_seismos(seismos)
    #test_filtra_por_pais(seismos, 'CHINA')
    #test_promedio_muertes(seismos)
    #test_ordenar_por_fecha(seismos, 4, True)
    #test_maximos_heridos(seismos)
    #test_pais_mas_frecuente(seismos)
