"""
tuple unpacking (desempaquetado de una tupla). Realmente el unpacking se puede 
aplicar sobre cualquier objeto de tipo secuencia, aunque se usa mayoritariamente 
con las tuplas, y consiste en lo siguiente:
"""

>>> bebidas = 'agua', 'café', 'batido'
>>> a, b, c = bebidas
>>> a
'agua'
>>> b
'café'
>>> c
'batido'

# Como puedes apreciar, es un tipo de asignación múltiple. Requiere que haya tantas variables a la izquierda
# del operador de asignación = como elementos haya en la secuencia.
