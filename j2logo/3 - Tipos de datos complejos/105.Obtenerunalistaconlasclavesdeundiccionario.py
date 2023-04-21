"""
En ocasiones, es necesario tener almacenado en una lista las claves de un diccionario. Para ello, simplemente pasa el diccionario como argumento del constructor list(). Esto devolverá las claves del diccionario en una lista.
"""

>>> d = {'uno': 1, 'dos': 2, 'tres': 3}
>>> list(d)
['uno', 'dos', 'tres']