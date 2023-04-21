# Para añadir un elemento a un conjunto se utiliza el método add(). 
# También existe el método update(), que puede tomar como argumento
# una lista, tupla, string, conjunto o cualquier objeto de tipo iterable.

>>> mi_conjunto = {1, 3, 2, 9, 3, 1}
>>> mi_conjunto
{1, 2, 3, 9}

# Añade el elemento 7 al conjunto
>>> mi_conjunto.add(7)
>>> mi_conjunto
{1, 2, 3, 7, 9}

# Añade los elementos 5, 3, 4 y 6 al conjunto
# Los elementos repetidos no se añaden al conjunto
>>> mi_conjunto.update([5, 3, 4, 6])
>>> mi_conjunto
{1, 2, 3, 4, 5, 6, 7, 9}

# 🎯 NOTA: add() y update() no añaden elementos que ya existen al conjunto.
