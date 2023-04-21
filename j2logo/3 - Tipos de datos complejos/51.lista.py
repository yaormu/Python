Las listas en Python son un tipo contenedor, compuesto, que se usan para almacenar conjuntos de elementos relacionados del mismo tipo o de tipos distintos.

Junto a las clases tuple, range y str, son uno de los tipos de secuencia en Python, con la particularidad de que son mutables. Esto último quiere decir que su contenido se puede modificar después de haber sido creada.

Para crear una lista en Python, simplemente hay que encerrar una secuencia de elementos separados por comas entre paréntesis cuadrados [].

Por ejemplo, para crear una lista con los números del 1 al 10 se haría del siguiente modo:

>>> numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Como te decía, las listas pueden almacenar elementos de distinto tipo. La siguiente lista también es válida:

>>> elementos = [3, 'a', 8, 7.2, 'hola']
Incluso pueden contener otros elementos compuestos, como objetos u otras listas:

>>> lista = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']
Las listas también se pueden crear usando el constructor de la clase, list(iterable). En este caso, el constructor crea una lista cuyos elementos son los mismos y están en el mismo orden que los ítems del iterable. El objeto iterable puede ser o una secuencia, un contenedor que soporte la iteración o un objeto iterador.

Por ejemplo, el tipo str también es un tipo secuencia. Si pasamos un string al constructor list() creará una lista cuyos elementos son cada uno de los caracteres de la cadena:

>>> vocales = list('aeiou')
>>> vocales
['a', 'e', 'i', 'o', 'u']
Termino esta sección mostrando dos alternativas de crear una lista vacía:

>>> lista_1 = []  # Opción 1
>>> lista_2 = list()  # Opción 2