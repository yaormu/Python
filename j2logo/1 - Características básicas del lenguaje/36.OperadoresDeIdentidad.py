"""
Por último, los operadores de identidad se utilizan para comprobar si dos variables son, o no, el mismo objeto.

Operador	Descripción
is		Devuelve True si ambos operandos hacen referencia al mismo objeto; 		False en caso contrario.
is not		Devuelve True si ambos operandos no hacen referencia al mismo objeto; 		False en caso contrario.

?? Recuerda: Para conocer la identidad de un objeto se usa la función id().
"""

>>> x = 4
>>> y = 2
>>> lista = [1, 5]
>>> x is lista
False
>>> x is y
False
>>> x is 4
True