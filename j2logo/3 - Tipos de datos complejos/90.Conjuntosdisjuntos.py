"""
Dos conjuntos A y B son disjuntos si no tienen elementos en común, es decir, 
la intersección de A y B es el conjunto vacío.

En Python se utiliza el método isdisjoint() de la clase set para comprobar 
si un conjunto es disjunto de otro.
"""

>>> a = {1, 2}
>>> b = {1, 2, 3, 4}
>>> a.isdisjoint(b)
False

>>> a = {1, 2}
>>> b = {3, 4}
>>> a.isdisjoint(b)
True
