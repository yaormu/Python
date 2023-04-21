"""
Dado un conjunto A, subcolección del conjunto B o igual a este, sus elementos son un subconjunto de B. 
Es decir, A es un subconjunto de B y B es un superconjunto de A.

En Python se utiliza el operador <= para comprobar si un conjunto A es subconjunto de B y 
el operador >= para comprobar si un conjunto A es superconjunto de B.
"""

>>> a = {1, 2}
>>> b = {1, 2, 3, 4}
>>> a <= b
True
>>> a >= b
False
>>> b >= a
True

>>> a = {1, 2}
>>> b = {1, 2}
>>> a < b  # Ojo al operador < sin el =
False
>>> a <= b
True
