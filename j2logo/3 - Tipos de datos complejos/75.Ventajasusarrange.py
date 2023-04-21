"""
La principal ventaja de usar range sobre list o tuple es que es un iterable que genera los elementos 
solo en el momento en que realmente los necesita. Esto implica que usa una cantidad de memoria mínima, 
por muy grande que sea el rango de números que represente.

Veamos una comparación de una lista que almacena los números del 0 al 100.000 y un rango del 0 al 100.000:
"""

>>> import sys
>>> lista = list(range(0, 100000))
>>> rango = range(0, 100000)
>>> sys.getsizeof(lista)
900120
>>> sys.getsizeof(rango)
48

# Como puedes apreciar, la lista ocupa casi 1 MB en memoria frente a los 48 bytes que ocupa el rango.
