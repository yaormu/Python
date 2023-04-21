"""
Un iterable es un objeto que se puede iterar sobre él, es decir, que permite recorrer sus elementos uno a uno. Para ser más técnico, un objeto iterable es aquél que puede pasarse como parámetro de la función iter().

Esta función devuelve un iterador basado en el objeto iterable que se pasa como parámetro.

Finalmente, un iterador es un objeto que define un mecanismo para recorrer los elementos del iterable asociado.
"""

>>> nums = [4, 78, 9, 84]
>>> it = iter(nums)
>>> next(it)
4
>>> next(it)
78
>>> next(it)
9
>>> next(it)
84
>>> next(it)
Traceback (most recent call last):
File "<input>", line 1, in <module>
StopIteration


"""
Como puedes observar, un iterador recorre los elementos de un iterable solo hacia delante. Cada vez que se llama a la función next() se recupera el siguiente valor del iterador.

En Python, los tipos principales list, tuple, dict, set o string entre otros, son iterables, por lo que podrán ser usados en el bucle for.
"""