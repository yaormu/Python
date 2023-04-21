"""
Para acceder a un elemento de una lista se utilizan los índices. Un índice es un número entero que indica la posición de un elemento en una lista. El primer elemento de una lista siempre comienza en el índice 0.
"""

>>> lista = ['a', 'b', 'd', 'i', 'j']
>>> lista[0]  # Primer elemento de la lista. Índice 0
'a'
>>> lista[3]  # Cuarto elemento de la lista. Índice 3
'i'

"""
Si se intenta acceder a un índice que está fuera del rango de la lista, el intérprete lanzará la excepción IndexError. De igual modo, si se utiliza un índice que no es un número entero, se lanzará la excepción TypeError:
"""

>>> lista = [1, 2, 3]  # Los índices válidos son 0, 1 y 2
>>> lista[8]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range

>>> lista[1.0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: list indices must be integers or slices, not float


"""
Como hemos visto, las listas pueden contener otros elementos de tipo secuencia de forma anidada. Por ejemplo, una lista que uno de sus ítems es otra lista. Del mismo modo, se puede acceder a los elementos de estos tipos usando índices compuestos o anidados:
"""

>>> lista = ['a', ['d', 'b'], 'z']
>>> lista[1][1]  # lista[1] hace referencia a la lista anidada
'b'