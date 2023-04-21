# Con los conjuntos también se puede usar el operador de pertenencia in para comprobar 
# si un elemento está contenido, o no, en un conjunto:

>>> mi_conjunto = set([1, 2, 5, 3, 1, 5])
>>> print(1 in mi_conjunto)
True
>>> print(6 in mi_conjunto)
False
>>> print(2 not in mi_conjunto)
False
