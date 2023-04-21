# Al tratarse de un tipo secuencial, range implementa las operaciones básicas de ese tipo 
# a excepción de la concatenación y la repetición:

>>> r = range(0,30, 3)
>>> r[2]
6
>>> r[-1]
27
>>> 13 in r
False
>>> 12 in r
True
>>> r.index(18)
6
