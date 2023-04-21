# Como te he indicado, las tuplas son objetos inmutables. No obstante, las tuplas pueden contener objetos
# u otros elementos de tipo secuencia, por ejemplo, una lista. 
# Estos objetos, si son mutables, sí se pueden modificar:

>>> tupla = (1, ['a', 'b'], 'hola', 8.2)
>>> tupla[1].append('c')  # tupla[1] hace referencia a la lista
>>> tupla
(1, ['a', 'b', 'c'], 'hola', 8.2)
