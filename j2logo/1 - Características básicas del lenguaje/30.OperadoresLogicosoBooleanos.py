"""
A la hora de operar con valores booleanos, tenemos a nuestra disposición los operadores and, or y not.

?? IMPORTANTE: Las operaciones and, or y not realmente no devuelven True o False, sino que devuelven uno de los operandos como veremos en el cuadro de abajo.
"""

>>> x = True
>>> y = False
>>> x or y
True

>>> x and y
False

>>> not x
False

>>> x = 0
>>> y = 10
>>> x or y
10

>>> x and y
0

>>> not x
True