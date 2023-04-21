"""
Al igual que ocurre con las listas (y todos los tipos secuenciales), está permitido usar 
índices negativos para acceder a los elementos de una tupla. En este caso, 
el índice -1 hace referencia al último elemento de la secuencia, 
el -2 al penúltimo y así, sucesivamente:
"""

>>> bebidas = ('agua', 'café', 'batido', 'sorbete')
>>> bebidas[-1]
'sorbete'
>>> bebidas[-3]
'café'
