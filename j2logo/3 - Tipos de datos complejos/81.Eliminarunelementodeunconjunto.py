"""
La clase set ofrece cuatro métodos para eliminar elementos de un conjunto. Son: 
discard(), remove(), pop() y clear(). A continuación te explico qué hace cada uno de ellos.

discard(elemento) y remove(elemento) eliminan elemento del conjunto. 
La única diferencia es que si elemento no existe, discard() no hace nada mientras 
que remove() lanza la excepción KeyError.

pop() es un tanto peculiar. Este método devuelve un elemento aleatorio del conjunto
y lo elimina del mismo. Si el conjunto está vacío, lanza la excepción KeyError.

Finalmente, clear() elimina todos los elementos contenidos en el conjunto.
"""

>>> mi_conjunto = {1, 3, 2, 9, 3, 1, 6, 4, 5}
>>> mi_conjunto
{1, 2, 3, 4, 5, 6, 9}

# Elimina el elemento 1 con remove()
>>> mi_conjunto.remove(1)
>>> mi_conjunto
{2, 3, 4, 5, 6, 9}

# Elimina el elemento 4 con discard()
>>> mi_conjunto.discard(4)
>>> mi_conjunto
{2, 3, 5, 6, 9}

# Trata de eliminar el elemento 7 (no existe) con remove()
# Lanza la excepción KeyError
>>> mi_conjunto.remove(7)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 7

# Trata de eliminar el elemento 7 (no existe) con discard()
# No hace nada
>>> mi_conjunto.discard(7)
>>> mi_conjunto
{2, 3, 5, 6, 9}

# Obtiene y elimina un elemento aleatorio con pop()
>>> mi_conjunto.pop()
2
>>> mi_conjunto
{3, 5, 6, 9}

# Elimina todos los elementos del conjunto
>>> mi_conjunto.clear()
>>> mi_conjunto
set()
