"""
Para acceder a un elemento de una tupla se utilizan los índices. Un índice es un número
entero que indica la posición de un elemento en una tupla. El primer elemento de una 
tupla siempre comienza en el índice 0.

Por ejemplo, en una tupla con 3 elementos, los índices de cada uno de los ítems serían 0, 1 y 2.
"""

>>> tupla = ('a', 'b', 'd')
>>> tupla[0]  # Primer elemento de la tupla. Índice 0
'a'
>>> tupla[1]  # Segundo elemento de la tupla. Índice 1
'b'

"""
Si se intenta acceder a un índice que está fuera del rango de la tupla, el intérprete
lanzará la excepción IndexError. De igual modo, si se utiliza un índice que no es un 
número entero, se lanzará la excepción TypeError:
"""
>>> tupla = 1, 2, 3  # Los índices válidos son 0, 1 y 2
>>> tupla[8]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: tuple index out of range
>>> tupla[1.0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: tuple indices must be integers or slices, not float
