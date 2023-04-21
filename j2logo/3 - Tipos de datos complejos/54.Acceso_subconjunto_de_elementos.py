"""
También es posible acceder a un subconjunto de elementos de una lista 
utilizando rangos en los índices. Esto es usando el operador [:]:
"""
>>> vocales = ['a', 'e', 'i', 'o', 'u']

>>> vocales[2:3]  # Elementos desde el índice 2 hasta el índice 3-1
['i']

>>> vocales[2:4]  # Elementos desde el 2 hasta el índice 4-1
['i', 'o']

>>> vocales[:]  # Todos los elementos
['a', 'e', 'i', 'o', 'u']

>>> vocales[1:]  # Elementos desde el índice 1
['e', 'i', 'o', 'u']

>>> vocales[:3]  # Elementos hasta el índice 3-1
['a', 'e', 'i']


"""
También es posible acceder a los elementos de una lista 
indicando un paso con el operador [::]:
"""
>>> letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

>>> letras[::2]  # Acceso a los elementos de 2 en 2
['a', 'c', 'e', 'g', 'i', 'k']

>>> letras[1:5:2]  # Elementos del índice 1 al 4 de 2 en 2
['b', 'd']

>>> letras[1:6:3]  # Elementos del índice 1 al 5 de 3 en 3
['b', 'e']









