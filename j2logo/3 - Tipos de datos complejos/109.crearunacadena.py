"""
Crear una cadena de texto en Python es muy sencillo. Simplemente encierra una secuencia de caracteres entre comillas simples '' o dobles "".
"""

>>> s = 'Hola Pythonista'
>>> s
'Hola Pythonista'
>>> type(s)
<class 'str'>

>>> s2 = "Me gusta Python"
>>> s2
'Me gusta Python'
>>> type(s2)
<class 'str'>

"""
Si quieres o necesitas que un string ocupe más de una línea, entonces debes encerrar el texto entre tres comillas simples '''...''' o dobles """...""".
"""

>>> s = '''
... Este string
...    ocupa más
...     de
...  una línea'''

>>> s
'\nEste string\n   ocupa más\n    de\n una línea'

>>> print(s)

Este string
   ocupa más
    de
 una línea

"""
Como puedes observar, el uso de las tres comillas (simples o dobles) guarda el carácter de fin de línea. Esto se puede evitar añadiendo el carácter \ al final de cada línea.
"""

>>> s = '''Este string \
...    ocupa más \
...     de \
...  una línea'''

>>> s
'Este string    ocupa más     de  una línea'

>>> print(s)
Este string    ocupa más     de  una línea

"""
?? OJO: No confundas un string multilínea con un docstring. Un docstring es un string multilínea que se utiliza para documentar un módulo, función, clase o método, entre otros.
"""

"""
Además, dos cadenas se pueden concatenar con el operador +, o incluso repetir, usando el operador *. El resultado en ambos casos es un nuevo string.
"""

>>> hola = 'hola'
>>> s = hola + ' Pythonista'
>>> s
'hola Pythonista'

>>> s2 = hola * 3 + ' Pythonista'
>>> s2
'holaholahola Pythonista'

"""
Y para terminar esta sección, simplemente resaltar que dos strings literales se pueden concatenar si aparecen juntos uno tras otro.
"""

>>> s = 'Hola' ' Pythonista'
>>> s
'Hola Pythonista'

>>> s = ('Hola'
... ' Pythonista'
... ' ¿Te gusta Python?')
>>> s
'Hola Pythonista ¿Te gusta Python?'