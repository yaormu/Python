"""
Un diccionario puede contener un valor de cualquier tipo, entre ellos, otro diccionario. Este hecho se conoce como diccionarios anidados.

Para acceder al valor de una de las claves de un diccionario interno, se usa el operador de indexación anidada [clave1][clave2]...

"""
>>> d = {'d1': {'k1': 1, 'k2': 2}, 'd2': {'k1': 3, 'k4': 4}}
>>> d['d1']['k1']
1
>>> d['d2']['k1']
3
>>> d['d2']['k4']
4
>>> d['d3']['k4']
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'd3'