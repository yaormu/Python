"""
Dado que los conjuntos son colecciones desordenadas, en ellos no se guarda la posición en la que son 
insertados los elementos como ocurre en los tipos list o tuple. Es por ello que no se puede acceder 
a los elementos a través de un índice.

Sin embargo, sí se puede acceder y/o recorrer todos los elementos de un conjunto usando un bucle for:
"""

>>> mi_conjunto = {1, 3, 2, 9, 3, 1}
>>> for e in mi_conjunto:
...     print(e)
...     
1
2
3
9
