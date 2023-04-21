"""
Tal y como te he adelantado, las listas son secuencias mutables, es decir, sus elementos pueden ser modificados (se pueden añadir nuevos ítems, actualizar o eliminar).

Para añadir un nuevo elemento a una lista se utiliza el método append() y para añadir varios elementos, el método extend():
"""

>>> vocales = ['a']
>>> vocales.append('e')  # Añade un elemento
>>> vocales
['a', 'e']


>>> vocales.extend(['i', 'o', 'u'])  # Añade un grupo de elementos
>>> vocales
['a', 'e', 'i', 'o', 'u']


# También es posible utilizar el operador de concatenación + para unir dos listas
# en una sola. El resultado es una nueva lista con los elementos de ambas:

>>> lista_1 = [1, 2, 3]
>>> lista_2 = [4, 5, 6]
>>> nueva_lista = lista_1 + lista_2
>>> nueva_lista
[1, 2, 3, 4, 5, 6]

# Por otro lado, el operador * repite el contenido de una lista n veces:

>>> numeros = [1, 2, 3]
>>> numeros *= 3
>>> numeros
[1, 2, 3, 1, 2, 3, 1, 2, 3]


# También es posible añadir un elemento en una posición concreta de una lista 
# con el método insert(índice, elemento). Los elementos cuyo índice sea mayor 
# a índice se desplazan una posición a la derecha:

>>> vocales = ['a', 'e', 'u']
>>> vocales.insert(2, 'i')
>>> vocales
['a', 'e', 'i', 'u']












