"""
el uso principal de la sentencia while es ejecutar repetidamente un bloque de código mientras se cumpla una condición.

La estructura de esta sentencia while es la siguiente:

while condición:
    bloque de código
Es decir, mientras condición se evalúe a True, se ejecutarán las instrucciones y sentencias de bloque de código.

Aquí, condición puede ser un literal, el valor de una variable, el resultado de una expresión o el valor devuelto por una función.

?? IMPORTANTE: El cuerpo del bloque while está indicado con un sangrado mayor. Dicho bloque termina cuando se encuentre la primera línea con un sangrado menor.
"""

numero = 0
print('Tabla del 3')
while numero <= 10:
    print(f'{numero * 3}')
    numero += 1
print('Fin')


"""
En el script anterior se inicializa una variable numero con el valor 0.

Seguidamente se muestra un mensaje y en la línea 3 aparece una sentencia while. En esta sentencia se comprueba si el valor de la variable numero es menor o igual a 10.

Como se evalúa a True, se muestra por pantalla el resultado de multiplicar numero por 3 y después se incrementa el valor de numero en 1.

A continuación, se debería ejecutar el código de la línea 6. Sin embargo, como hemos definido un bucle while, el flujo de ejecución del programa no continúa por la línea 6, sino que vuelve a la línea 3 y de nuevo se evalúa si la expresión numero <= 10 sigue siendo True. En esta ocasión el valor de numero es 1, por lo que la expresión da como resultado True y vuelven a ejecutarse las líneas de la sentencia while.

Esto será así hasta que numero sea igual a 11. En esa ocasión la expresión de comparación se evaluará a False y el flujo continuará, ahora sí, por la línea 6.

El resultado del script anterior es el siguiente (la tabla de multiplicar del número 3):
"""

Tabla del 3
0
3
6
9
12
15
18
21
24
27
30
Fin