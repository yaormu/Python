"""
Como el resto de tipos secuencia, podemos acceder a los caracteres de una cadena a través de un índice numérico. Un índice es un número entero que indica la posición de un carácter en la cadena. Siempre el primer carácter de la secuencia tiene como índice 0.
"""

>>> s = 'Hola Pythonista'

# Primer carácter de la cadena
>>> s[0]
'H'

# Sexto carácter de la cadena
>>> s[5]
'P'

# Tercer carácter de la cadena
>>> s[2]
'l'

"""
Si se intenta acceder a un índice que está fuera del rango del string, el intérprete lanzará la excepción IndexError. De igual modo, si se utiliza un índice que no es un número entero, se lanzará la excepción TypeError
"""

>>> s = 'Hola Pythonista'

>>> s[30]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: string index out of range

>>> s[1.0]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: string indices must be integers

"""
Los índices también puede ser negativos. En este caso, el índice -1 hace referencia al último carácter, -2 al penúltimo, y así, sucesivamente.
"""

>>> s = 'Hola Pythonista'
>>> s[-1]
'a'
>>> s[-2]
't'