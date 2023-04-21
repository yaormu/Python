# En Python dos conjuntos son iguales si y solo si todos los elementos de un conjunto 
# están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto del otro.

>>> a = {1, 2}
>>> b = {1, 2}
>>> id(a)
4475070656
>>> id(b)
4475072096
>>> a == b
True
