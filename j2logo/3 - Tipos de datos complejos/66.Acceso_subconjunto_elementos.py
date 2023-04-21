# También es posible acceder a un subconjunto de elementos de una tupla utilizando el operador [:]:

>>> vocales = 'a', 'e', 'i', 'o', 'u'
>>> vocales[2:3]  # Elementos desde el índice 2 hasta el índice 3-1
('i',)
>>> vocales[2:4]  # Elementos desde el 2 hasta el índice 4-1
('i', 'o')
>>> vocales[:]  # Todos los elementos
('a', 'e', 'i', 'o', 'u')
>>> vocales[1:]  # Elementos desde el índice 1
('e', 'i', 'o', 'u')
>>> vocales[:3]  # Elementos hasta el índice 3-1
('a', 'e', 'i')


# O indicando un salto entre los elementos con el operador [::]:

>>> pares = 2, 4, 6, 8, 10, 12, 14
>>> pares[::2]  # Acceso a los elementos de 2 en 2
(2, 6, 10, 14)
>>> pares[1:5:2]  # Elementos del índice 1 al 4 de 2 en 2
(4, 8)
>>> pares[1:6:3]  # Elementos del índice 1 al 5 de 3 en 3
(4, 10)
