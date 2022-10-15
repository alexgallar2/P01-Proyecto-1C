from datetime import *

def parse_muertes(cadena):
    if cadena:
        muertes_parseadas= int(cadena)
        return muertes_parseadas
    else:
        muertes_vacias = None
        return muertes_vacias
def parse_heridos(cadena2):
    if cadena2:
        heridos_parseados= int(cadena2)
        return heridos_parseados
    else:
        heridos_vacios = None
        return heridos_vacios

