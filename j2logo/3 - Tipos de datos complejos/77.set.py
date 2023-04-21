Qué es el tipo set en Python
Al comienzo del tutorial adelantaba que el tipo set en Python es utilizado para trabajar con conjuntos de elementos. La principal característica de este tipo de datos es que es una colección cuyos elementos no guardan ningún orden y que además son únicos.

Estas características hacen que los principales usos de esta clase sean conocer si un elemento pertenece o no a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

Además, esta clase también implementa las típicas operaciones matemáticas sobre conjuntos: unión, intersección, diferencia, …

Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {}, o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable (como una lista, una tupla, una cadena …).

# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
>>> c = {1, 3, 2, 9, 3, 1}
>>> c
{1, 2, 3, 9}
# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan

>>> a = set('Hola Pythonista')
>>> a
{'a', 'H', 'h', 'y', 'n', 's', 'P', 't', ' ', 'i', 'l', 'o'}

# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan

>>> unicos = set([3, 5, 6, 1, 5])
>>> unicos
{1, 3, 5, 6}
Para crear un conjunto vacío, simplemente llama al constructor set() sin parámetros.

❗️ IMPORTANTE: {} NO crea un conjunto vacío, sino un diccionario vacío. Usa set() si quieres crear un conjunto sin elementos.

🎯 NOTA: Los elementos que se pueden añadir a un conjunto deben ser de tipo hashable. Un objeto es hashable si tiene un valor de hash que no cambia durante todo su ciclo de vida. En principio, los objetos que son instancias de clases definidas por el usuario son hashables. También lo son la mayoría de tipos inmutables definidos por Python.
