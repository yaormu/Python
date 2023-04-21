# Asigna a la variable <a> el valor 1
a = 1

# Asigna a la variable <a> el resultado de la expresión 3 * 4
a = 3 * 4

# Asigna a la variable <a> la cadena de caracteres 'Pythonista'
a = 'Pythonista'

"""
Si intentamos usar una variable que no ha sido definida/inicializada previamente, el intérprete nos mostrará un error:

>>> print(a)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'a' is not defined
"""

"""
Para terminar esta sección de variables en Python, vamos a introducir el concepto tipo de dato. Al asignar un valor a una variable, dicho valor pertenece a un conjunto de valores conocido como tipo de dato. Un tipo de dato define una serie de características sobre esos datos y las variables que los contienen como, por ejemplo, las operaciones que se pueden realizar con ellos. En Python, los tipos de datos básicos son los numéricos (enteros, reales y complejos), los boolenaos (True, False) y las cadenas de caracteres.

A diferencia de otros lenguajes, en Python no es necesario indicar el tipo de dato cuando se define una variable. Además, en cualquier momento, una variable que es de un tipo puede convertirse en una variable de otro tipo cualquiera:
"""

a = 1  # La variable a es de tipo entero (int)
b = 'Hola'  # La variable b es de tipo cadena de caracteres
