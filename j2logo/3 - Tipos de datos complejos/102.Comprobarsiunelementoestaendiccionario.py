"""
Al operar con diccionarios, se puede usar el operador de pertenencia in para comprobar si una clave está contenida, o no, en un diccionario. Esto resulta útil, por ejemplo, para asegurarnos de que una clave existe antes de intentar eliminarla.
"""

>>> print('uno' in d)
True
>>> print(1 in d)
False
>>> print(1 not in d)
True

# Intenta eliminar la clave 1 si existe
>>> if 1 in d:
...     del d[1]
...     
>>> d
{'uno': 1, 'dos': 2, 'tres': 3}