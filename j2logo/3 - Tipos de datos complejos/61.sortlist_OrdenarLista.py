"""
Las listas son secuencias ordenadas. Esto quiere decir que sus elementos 
siempre se devuelven en el mismo orden en que fueron añadidos.

No obstante, es posible ordenar los elementos de una lista con el método sort().
El método sort() ordena los elementos de la lista utilizando únicamente el operador < 
y modifica la lista actual (no se obtiene una nueva lista):
"""

# Lista desordenada de números enteros
>>> numeros = [3, 2, 6, 1, 7, 4]

# Identidad del objeto numeros
>>> id(numeros)
4475439216

# Se llama al método sort() para ordenar los elementos de la lista
>>> numeros.sort()
>>> numeros
[1, 2, 3, 4, 6, 7]

# Se comprueba que la identidad del objeto numeros es la misma
>>> id(numeros)
4475439216
