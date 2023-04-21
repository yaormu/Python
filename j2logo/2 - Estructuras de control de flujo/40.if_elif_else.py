if cond1:
    bloque cond1 (sentencias si se evalúa la cond1 a True)
elif cond2:
    bloque cond2 (sentencias si cond1 es False pero cond2 es True)
...
else:
    bloque else (sentencias si todas las condiciones se evalúan a False)

"""
Es decir, en esta ocasión, se comprueba la condición cond1. Si se evalúa a True, se ejecuta el bloque bloque cond1 y después el flujo continúa después del bloque if.

Sin embargo, si cond1 se evalúa a False, se comprueba la condición cond2. Si esta se evalúa a True, se ejecuta el bloque de sentencias bloque cond2. En caso contrario, pasaría a comprobar la condición del siguiente elif y así sucesivamente hasta que llegue al else, que se ejecuta si ninguna de las condiciones anteriores se evaluaron a True.

Veamos un ejemplo. Imagina que queremos comprobar si un número es menor que 0, igual a 0 o mayor que 0 y en cada situación debemos ejecutar un código diferente. Podemos hacer uso de la estructura if … elif … else anterior:
"""
x = 28
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:
    print(f'{x} es mayor que 0')
else:
    print('x es 0')










