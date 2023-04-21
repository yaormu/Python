"""
El caso es que la suma de la representación en punto flotante en binario del número 1,1 y de la representación en punto flotante en binario del número 2,2, dan como resultado 3,3000000000000003
"""

>>> 1.1 + 2.2
3.3000000000000003

"""
Puedes usar el tipo float sin problemas para representar cualquier número real (siempre teniendo en cuenta que es una aproximación lo más precisa posible). Por tanto para longitudes, pesos, frecuencias, …, en los que prácticamente es lo mismo 3,3 que 3,3000000000000003 el tipo float es el más apropiado.
"""

>>> real = 1.1 + 2.2  # real es un float
>>> print(real)
3.3000000000000003  # Representación aproximada de 3.3
>>> print(f'{real:.2f}')
3.30  # real mostrando únicamente 2 cifras decimales

"""
Al igual que los números enteros, un float se crea a partir de un literal, o bien como resultado de una expresión o una función.
"""

>>> un_real = 1.1  # El literal debe incluir el carácter .
>>> otro_real = 1/2  # El resultado de 1/2 es un float
>>> not_cient = 1.23E3  # float con notación científica (1230.0)