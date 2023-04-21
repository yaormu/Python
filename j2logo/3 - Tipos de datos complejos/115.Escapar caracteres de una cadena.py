"""
Como un string está limitado por los caracteres '' o "", ¿qué ocurre si necesito usar el carácter ' o " dentro de una cadena?

Lo más fácil si tienes que usar el carácter ' en tu cadena, es encerarla entre comillas dobles. Por el contrario, si necesitas usar " dentro del string, enciérralo entre comillas simples.
"""

>>> s = 'Dijo: "Hola Pythonista"'
>>> print(s)
Dijo: "Hola Pythonista"

>>> s = "Dijo: 'Hola Pythonista'"
>>> print(s)
Dijo: 'Hola Pythonista'

"""
También puedes usar la combinación \' para mostrar una comilla simple o \" para mostrar una comilla doble, independientemente de si la cadena está encerrada entre comillas simples o dobles.
"""

>>> s = 'Dijo: \'Hola Pythonista\''
>>> print(s)
Dijo: 'Hola Pythonista'

>>> s = "Dijo: \"Hola Pythonista\""
>>> print(s)
Dijo: "Hola Pythonista"

"""
Además del carácter ' y ", hay otros caracteres especiales que para ser usados dentro de una cadena necesitan ser «escapados» con el carácter \. Son, entre otros, los siguientes: tabulador (\t), barra invertida (\\), retroceso (\b), nueva línea (\n) o retorno de carro (\r).
"""

# Ejemplo para declarar una ruta en Windows
>>> s = 'C:\\Users\\Documents\\'
>>> print(s)
C:\Users\Documents\

# Nueva línea más tabulador
>>> s = 'Hola\n\tPythonista'
>>> print(s)
Hola
  Pythonista