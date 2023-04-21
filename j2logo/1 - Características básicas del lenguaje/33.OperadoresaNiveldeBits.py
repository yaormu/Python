"""
Los operadores a nivel de bits actúan sobre los operandos como si fueran una cadena de dígitos binarios. Como su nombre indica, actúan sobre los operandos bit a bit. Son los siguientes


Operación	Descripción
x | y		or bit a bit de x e y.
x ^ y		or exclusivo bit a bit de x e y.
x & y		and bit a bit de x e y.
x << n		Desplaza x n bits a la izquierda.
x >> n		Desplaza x n bits a la derecha.
~x		not x. Obtiene los bits de x invertidos.

Supongamos que tenemos el entero 2 (en bits es 00010) y el entero 7 (00111). El resultado de aplicar las operaciones anteriores es:
"""
>>> x = 2
>>> y = 7
>>> x | y
7
>>> x ^ y
5
>>> x & y
2
>>> x << 1
4
>>> x >> 1
1
>>> ~x
-3