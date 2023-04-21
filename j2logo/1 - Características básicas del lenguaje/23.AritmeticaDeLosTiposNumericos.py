"""
Con todos los tipos numéricos se pueden aplicar las operaciones de la aritmética: suma, resta, producto, división, …

En Python está permitido realizar una operación aritmética con números de distinto tipo. En este caso, el tipo numérico «más pequeño» se convierte al del tipo «más grande», de manera que el tipo del resultado siempre es el del tipo mayor. Entendemos que el tipo int es menor que el tipo float que a su vez es menor que el tipo complex.

Por tanto, es posible, por ejemplo, sumar un int y un float:
"""

>>> 1 + 2.0
3.0
>>> 2+3j + 5.7
(7.7+3j)

