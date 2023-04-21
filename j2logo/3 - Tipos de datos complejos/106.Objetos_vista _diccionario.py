"""
La clase dict implementa tres métodos muy particulares, dado que devuelven un tipo de dato, iterable, conocido como objetos vista. Estos objetos ofrecen una vista de las claves y valores contenidos en el diccionario y si el diccionario se modifica, dichos objetos se actualizan al instante.

Los métodos son los siguientes:

keys(): Devuelve una vista de las claves del diccionario.
values(): Devuelve una vista de los valores del diccionario.
items(): Devuelve una vista de pares (clave, valor) del diccionario.
"""

>>> d = {'uno': 1, 'dos': 2, 'tres': 3}

# d.keys() es diferente a list(d), aunque ambos
# contengan las claves del diccionario
# d.keys() es de tipo dict_keys y list(d) es de tipo list
>>> v = d.keys()
>>> type(v)
<class 'dict_keys'>
>>> v
dict_keys(['uno', 'dos', 'tres'])

>>> l = list(d)
>>> type(l)
<class 'list'>
>>> l
['uno', 'dos', 'tres']

>>> v = d.values()
>>> type(v)
<class 'dict_values'>
>>> v
dict_values([1, 2, 3])

>>> v = d.items()
>>> type(v)
<class 'dict_items'>
>>> v
dict_items([('uno', 1), ('dos', 2), ('tres', 3)])