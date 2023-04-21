# En Python se puede eliminar un elemento de una lista de varias formas.

# Con la sentencia del se puede eliminar un elemento a partir de su índice:

# Elimina el elemento del índice 1
>>> vocales = ['a', 'e', 'i', 'o', 'u']
>>> del vocales[1]
>>> vocales
['a', 'i', 'o', 'u']

# Elimina los elementos con índices 2 y 3
>>> vocales = ['a', 'e', 'i', 'o', 'u']
>>> del vocales[2:4]
>>> vocales
['a', 'e', 'u']

# Elimina todos los elementos
>>> del vocales[:]
>>> vocales
[]


"""
Además de la sentencia del, podemos usar los métodos remove() y pop([i]). remove() elimina la primera ocurrencia que se encuentre del elemento en una lista. Por su parte, pop([i]) obtiene el elemento cuyo índice sea igual a i y lo elimina de la lista. Si no se especifica ningún índice, recupera y elimina el último elemento.
"""

>>> letras = ['a', 'b', 'k', 'a', 'v']

# Elimina la primera ocurrencia del carácter a
>>> letras.remove('a')
>>> letras
['b', 'k', 'a', 'v']

# Obtiene y elimina el último elemento
>>> letras.pop()
'v'
>>> letras
['b', 'k', 'a']

# Finalmente, es posible eliminar todos los elementos de una 
# lista a través del método clear():

>>> letras = ['a', 'b', 'c']
>>> letras.clear()
>>> letras
[]

# El código anterior sería equivalente a del letras[:].