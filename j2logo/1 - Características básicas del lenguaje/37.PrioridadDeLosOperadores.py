"""
Este orden es el siguiente, de menos prioritario a más prioritario: asignación; operadores booleanos; operadores de comparación, identidad y pertenencia; a nivel de bits y finalmente los aritméticos (con el mismo orden de prioridad que en las matemáticas).

Este orden de prioridad se puede alterar con el uso de los paréntesis ():
"""

>>> x = 5
>>> y = 2
>>> z = x + 3 * y  # El producto tiene prioridad sobre la suma
>>> z
11
>>> z = (x + 3) * y  # Los paréntesis tienen prioridad
>>> z
16