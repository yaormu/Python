"""
Además de los tipos básicos, otros tipos fundamentales de Python son las secuencias (list y tuple), los conjuntos (set) y los mapas (dict).

Todos ellos son tipos compuestos y se utilizan para agrupar juntos varios valores.

Las listas son secuencias mutables de valores.
Las tuplas son secuencias inmutables de valores.
Los conjuntos se utilizan para representar conjuntos únicos de elementos, es decir, en un conjunto no pueden existir dos objetos iguales.
Los diccionarios son tipos especiales de contenedores en los que se puede acceder a sus elementos a partir de una clave única.
"""

>>> lista = [1, 2, 3, 8, 9]
>>> tupla = (1, 4, 8, 0, 5)
>>> conjunto = set([1, 3, 1, 4])
>>> diccionario = {'a': 1, 'b': 3, 'z': 8}

>>> print(lista)
[1, 2, 3, 8, 9]

>>> print(tupla)
(1, 4, 8, 0, 5)

>>> print(conjunto)
{1, 3, 4}

>>> print(diccionario)
{'a': 1, 'b': 3, 'z': 8}