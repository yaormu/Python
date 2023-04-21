"""
U1 - 4 | Ejemplo: Tarea de física (I)
En este ejemplo se demuestra la aplicación de los conceptos vistos durante la primera unidad del curso. Para esta ocasión crearemos un programa que pueda resolver un típico problema de física.


💡 Problema: Tarea de física (I)

Mientras realiza los deberes de un curso de física en el que se encuentra inscrito, identifica que es común tener que definir la posición en el caso de movimiento rectilíneo uniformemente acelerado. En cierto punto, concluye que es preferible crear un programa de computador que genere rápidamente la respuesta a realizar muchas veces la misma operación manualmente con la calculadora.


Según el libro de texto, la posición de un objeto puede ser calculada por la siguiente ecuación:


x = x0 + v0t + ½at² 


Para que el resultado que calcule el programa sea lo más claro posible, decide que el resultado sea impreso de la siguiente forma:

La posición final es <valor> metros.


Además, para definir una presentación consistente decide realizar un redondeo del valor obtenido con dos dígitos decimales.

⌨️ Entrada
¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

Su programa deberá recibir cuatro valores x0, v0, a y t respectivamente.

- x0: cadena de texto con la posición inicial (en m)
- v0: cadena de texto con la velocidad inicial (en m/s)
- a: cadena de texto con la posición inicial (en m/s2).
- t: adena de texto con la posición inicial (en s).

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir en la salida una única línea.

- resultado: cadena de texto con el resultado de la ecuación en el formato descrito en el enunciado redondeado con dos dígitos decimales. Como se muestra a continuación: La posición final es <valor> metros. Donde valor corresponde a la posición calculada en metros.

🧩 Ejemplos
¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1
15
3.2
0
0
Salida Ejemplo 1
La posición final es 15.00 metros.

Entrada Ejemplo 2
21.1
40
0.1
60
Salida Ejemplo 2
La posición final es 2601.10 metros.

Entrada Ejemplo 3
47
6
5e-2
147
Salida Ejemplo 3
La posición final es 1469.22 metros.

⚠️ Notas
- Recuerde que para poder realizar operaciones con los valores ingresados, es necesario realizar una tranformación de tipo de dato.
- Se recomienda utilizar la sintaxis de cadenas con formato o f-strings para realizar operaciones como el redondeo dentro de una cadena de texto. En este caso, el modificador necesario es :.2f, con dos dígitos decimales en un valor decimal o de punto flotante.
"""
# Entrada del programa (~ 4 líneas).
# x0: cadena de texto con la posición inicial (en m)
x0 = float(input("ingrese x0: "))
# v0: cadena de texto con la velocidad inicial (en m/s)
v0 = float(input("ingrese v0: "))
# a: cadena de texto con la posición inicial (en m/s2).
a = float(input("ingrese a: "))
# t: adena de texto con la posición inicial (en s).
t = float(input("ingrese t: "))

# Operación y asignación del resultado (~ 1 línea).
#x = x0 + v0t + ½at² 

x = x0 + v0 * t + 1/2 * a * t ** 2

# Salida del programa (~ 1 línea).
print(f'La posición final es {x:6.2f} metros.')
