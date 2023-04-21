"""
Otro tipo básico de Python, e imprescindible, son las secuencias o cadenas de caracteres. Este tipo es conocido como string aunque su clase verdadera es str.

Formalmente, un string es una secuencia inmutable de caracteres en formato Unicode.

Para crear un string, simplemente tienes que encerrar entre comillas simples '' o dobles "" una secuencia de caracteres.

Se puede usar indistintamente comillas simples o dobles, con una particularidad. Si en la cadena de caracteres se necesita usar una comilla simple, tienes dos opciones: usar comillas dobles para encerrar el string, o bien, usar comillas simples pero anteponer el carácter \ a la comilla simple del interior de la cadena. El caso contrario es similar.
"""

>>> hola = 'Hola "Pythonista"'
>>> hola_2 = 'Hola \'Pythonista\''
>>> hola_3 = "Hola 'Pythonista'"

>>> print(hola)
Hola "Pythonista"

>>> print(hola_2)
Hola 'Pythonista'

>>> print(hola_3)
Hola 'Pythonista'


"""
A diferencia de otros lenguajes, en Python no existe el tipo «carácter». No obstante, se puede simular con un string de un solo carácter:
"""

>>> caracter_a = 'a'
>>> print(caracter_a)
a