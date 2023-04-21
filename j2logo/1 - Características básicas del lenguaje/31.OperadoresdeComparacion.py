"""
Los operadores de comparación se utilizan, como su nombre indica, para comparar dos o más valores. El resultado de estos operadores siempre es True o False.
"""

>>> x = 9
>>> y = 1
>>> x < y
False
>>> x > y
True
>>> x == y
False


"""
Los objetos de diferentes tipos, excepto los tipos numéricos, nunca se comparan igual. El operador == siempre está definido, pero para algunos tipos de objetos (por ejemplo, objetos de clase) es equivalente a is.

Las instancias no idénticas de una clase normalmente se comparan como no iguales a menos que la clase defina el método __eq__().

Las instancias de una clase no se pueden ordenar con respecto a otras instancias de la misma clase u otros tipos de objeto, a menos que la clase defina los métodos __lt__(), __gt__().

Los operadores de comparación se pueden concatenar. Ejemplo:
"""

# Las comparaciones siguientes son idénticas

>>> x = 9
>>> 1 < x and x < 20
True

>>> 1 < x < 20
True