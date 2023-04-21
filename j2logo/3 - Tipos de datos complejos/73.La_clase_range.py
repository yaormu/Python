"""
Como te adelantaba en la introducción, range es un tipo de dato que representa una secuencia de números inmutable.

Para crear un objeto de tipo range, se pueden usar dos constructores :

range(fin): Crea una secuencia numérica que va desde 0 hasta fin - 1.

range(inicio, fin, [paso]): Crea una secuencia numérica que va desde inicio hasta fin - 1. 

Si además se indica el parámetro paso, la secuencia genera los números de paso en paso.
Veámoslo con un ejemplo:
"""

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(5, -5, -2))
[5, 3, 1, -1, -3]

"""
¿Por qué estoy utilizando en los ejemplos la clase range como argumento de list? range, además de un tipo secuencial 
es un tipo iterable con una particularidad: a diferencia de los tipos list o tuple, range calcula los ítems al vuelo, 
cuando los necesita. Como list acepta un objeto iterable como parámetro, por eso paso un objeto range al constructor de list, 
para que se muestre por pantalla la secuencia completa que se genera con range.

❗️NOTA: Si se llama al constructor range() con parámetros incorrectos, se obtendrá un objeto vacío.
"""

# Nunca se puede ir de 0 a 10 de -1 en -1

>>> list(range(0, 10, -1))
[]
