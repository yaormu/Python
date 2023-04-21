"""
Los operadores de pertenencia se utilizan para comprobar si un valor o variable se encuentran en una secuencia (list, tuple, dict, set o str).

Todavía no hemos visto estos tipos, pero son operadores muy utilizados.

Operador	Descripción
in		Devuelve True si el valor se encuentra en una secuencia; False en caso 		contrario.
not in		Devuelve True si el valor no se encuentra en una secuencia; False en 		caso
"""

>>> lista = [1, 3, 2, 7, 9, 8, 6]
>>> 4 in lista
False
>>> 3 in lista
True
>>> 4 not in lista
True