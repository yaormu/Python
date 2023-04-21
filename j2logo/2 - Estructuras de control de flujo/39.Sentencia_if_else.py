"""
Hay ocasiones en que la sentencia if básica no es suficiente y es necesario ejecutar un conjunto de instrucciones o sentencias cuando la condición se evalúa a False.
"""

if condición:
    bloque de código (cuando condición se evalúa a True)
else:
    bloque de código 2 (cuando condición se evalúa a False)

"""
Imagina que estás implementado un programa en el que necesitas realizar la división de dos números. Si divides un número entre 0, el programa lanzará un error y terminará. Para evitar esto, podemos añadir una sentencia if ... else... como en el ejemplo siguiente:
"""

resultado = None
x = 10
y = 2
if y > 0:
    resultado = x / y
else:
    resultado = f'No se puede dividir {x} entre {y}'
print(resultado)

"""
El resultado del script anterior es 5.0. Si ahora actualizamos el valor de y a 0, el resultado sería este otro:
"""
No se puede dividir 10 entre 0