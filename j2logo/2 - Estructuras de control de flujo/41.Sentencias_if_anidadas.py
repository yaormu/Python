"""
En cualquiera de los bloques de sentencias anteriores se puede volver a incluir una sentencia if, o if … else … o if … elif … else …

Por ejemplo, podemos simular el caso de la última sección de la siguiente manera:
"""

x = 28
if x < 0:
    print(f'{x} es menor que 0')
else:
    if x > 0:
        print(f'{x} es mayor que 0')
    else:
        print('x es 0')