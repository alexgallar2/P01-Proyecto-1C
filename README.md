# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<22\>/\<23\>)
Autor/a: \<Alejandro Gallardo González\>   uvus:\<alegalgon4\>

En este dataset se porporcionan los datos de distintos seismos o terremotos de distintos años


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<funciones.py\>**: Aqui se encuentra el codigo principal donde se ejecuta el proyecto .
  * **\<test.py\>**: Aqui se encuentra el modulo de pruebas donde se llaman a las distintas funciones del proyecto y se ejecutan por terminal.
  * **\<funciones_aux.py\>**: Aqui se encuentran las funciones auxiliares que ayudaran a las principales en procesos mas secundarios.
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<seismos.csv\>**: Contiene datos de distintos seismos a lo largo de varios años y en distintas partes del mundo.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<N\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<entero\>, representa un numero de identificacion para cada seismo
* **\<columna 2>**: de tipo \<booleano\>, representa si el seismo acarrea consigo un tsunami
* **\<columna 3>**: de tipo \<fecha\>, representa el dia en el que se produjo el seismo
* **\<columna 4>**: de tipo \<hora\>, representa la hora en la que se produjo el seismo
* **\<columna 5>**: de tipo \<cadena\>, representa el pais donde se produjo el seismo
* **\<columna 6>**: de tipo \<real\>, representa la latitud del seismo en coordenadas del globo
* **\<columna 7>**: de tipo \<real\>, representa la longitud del seismo en coordenadas del globo
* **\<columna 8>**: de tipo \<entero\>, representa el numero de muertes causadas
* **\<columna 9>**: de tipo \<entero\>, representa el numero de heridos causados

## Tipos implementados

la namedtuple implementada en la funcion de lectura contiene los indicativos de los datos de cada columna

## Funciones implementadas

la funcion lector_seismos como su nombre indica crea una lista de tuplas donde se recogen los datos del dataset ordenados por tipos

### \<funciones\>

* **<lector_seismos>**: Su funcion es una lectura completa del dataset proporcionado.


### \<test \>

* **<test funcion 1>**: Llama a la funcion de lector_seismos para ejecutarla
* **<test funcion 2>**: Descripción de las pruebas realizadas a la función 2.
* ...
* 
### \<funciones_aux\>

* **<parse_muertes>**: comprueba que no este vacia la cadena y de no estarlo la transforma en entero
* **<parse_heridos>**: comprueba que no este vacia la cadena y de no estarlo la transforma en entero
* ...
