"""
Python define tres tipos de datos numéricos básicos: enteros, números de punto flotante (simularía el conjunto de los números reales, pero ya veremos que no es así del todo) y los números complejos.
"""

"""
Números enteros
El tipo de los números enteros es int. 
"""

>>> a = -1  # a es de tipo int y su valor es -1
>>> b = a + 2  # b es de tipo int y su valor es 1
>>> print(b)
1

"""
Los números octales se crean anteponiendo 0o a una secuencia de dígitos octales (del 0 al 7).

Para crear un número entero en hexadecimal, hay que anteponer 0x a una secuencia de dígitos en hexadecimal (del 0 al 9 y de la A la F).

En cuanto a los números en binario, se antepone 0b a una secuencia de dígitos en binario (0 y 1).
"""

>>> diez = 10
>>> diez_binario = 0b1010
>>> diez_octal = 0o12
>>> diez_hex = 0xa
>>> print(diez)
10
>>> print(diez_binario)
10
>>> print(diez_octal)
10
>>> print(diez_hex)
10

