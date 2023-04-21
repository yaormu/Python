"""
U1 - 5 | Tarea 1 - Tarea de física (II)

En esta actividad se retomará el problema descrito en el ejemplo anterior de tarea de física y se amplían los requisitos de la solución con el objetivo de evaluar la apropiación de los conceptos discutidos en la unidad.


💡 Problema: Tarea de física (II)

Continúas solucionando los problemas física para tu tarea. Te encuentras con que la dificultad de los ejercicios ha aumentado: ahora, además de definir la posición, debes de encontrar la velocidad. Sigues pensando que la mejor forma para este tipo de problemas es realizar un programa que te ayude a obtener los resultados que necesitas.


Según el libro de texto, la posición de un objeto puede ser calculada por la siguiente ecuación:

x = x0 + v0t + ½at² 

Por otro lado, la velocidad de un objeto puede obtenerse a partir de la siguiente ecuación:

v = v0 + at

Donde x0 es la inicial del objeto, v0 la velocidad inicial, a su aceleració y t el tiempo transcurrido.

En los ejercicios propuestos la posición inicial es recibida en metros (m), la velocidad en kilometros por hora (km/h), la aceleración en metros sobre segundos al cuadrado (m/s2) y el tiempo en segundos (s); mientras que la posición (x) y la velocidad (v) son solicitados en metros (m) y kilometros por hora (km/h) respectivamente.

En el diseño de su programa, nota que es necesario hacer algunas transformaciones para poder obtener los valores que se necesitan en las unidades correspondientes. Algunas de las equivalencias necesarias para estas conversiones son:

1 km/h = 1/3.6m/s que es lo mismo que 1m/s = 3.6 km/h

1 h=3600 s que lo mismo que 1s = 1/3600 h

Para que el resultado que calcule el programa sea lo más claro posible, decide que el resultado sea impreso de la siguiente forma:

La posición final es de <x> m y la velocidad es de <v> km/h

Además, para definir una presentación consistente decide realizar un redondeo del valor obtenido con dos dígitos decimales para la posición y tres dígitos decimales para la velocidad.

⌨️ Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

Su programa deberá recibir cuatro valores x0, v0, a y t respectivamente.

- x0: cadena de texto con la posición inicial (en m)
- v0: cadena de texto con la velocidad inicial (en km/h)
- a: cadena de texto con la posición inicial (en m/s2).
- t: adena de texto con la posición inicial (en s).

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir en la salida una única línea.

- resultado: cadena de texto con el resultado de la ecuación en el formato descrito en el enunciado redondeado con dos dígitos decimales el valor de la posición y con tres dígitos decimales el valor de la velocidad. Como se muestra a continuación: La posición final es de <x> m y la velocidad es de <v> km/h. Donde x corresponde a la posición calculada en metros y v a la velocidad.

🧩 Ejemplos
¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1
15
3.2
0
0
Salida Ejemplo 1
La posición final es de 15.00 m y la velocidad es de 3.200 km/h

Entrada Ejemplo 2
21.1
40
0.1
60
Salida Ejemplo 2
La posición final es de 867.77 m y la velocidad es de 61.600 km/h

Entrada Ejemplo 3
47
6
5e-2
147
Salida Ejemplo 3
La posición final es de 832.23 m y la velocidad es de 32.460 km/h

⚠️ Notas
- Recuerde que para poder realizar operaciones con los valores ingresados, es necesario realizar una transformación de tipo de dato.
- Se recomienda utilizar la sintaxis de cadenas con formato o f-strings para realizar operaciones como el redondeo dentro de una cadena de texto. En este caso, el modificador necesario es :.nf, con n dígitos decimales en un valor decimal o de punto flotante.
"""

# Entrada del programa (~ 4 líneas).
# x0: posición inicial del objeto (en m)
x0 = float(input("ingrese x0: "))
# v0: velocidad inicial (en km/h)
v0 = float(input("ingrese v0: "))
# a: su aceleracion (en m/s2).
a = float(input("ingrese a: "))
# t: tiempo transcurrido (en s).
t = float(input("ingrese t: "))

# Operación y asignación del resultado (~ 1 línea).
# posición de un objeto puede ser calculada por la siguiente ecuación: x = x0 + v0t + ½at²
x = x0 + (v0/3.6) * t + 1 / 2 * a * t ** 2
v = v0 + (a * t) * 3.6

# Salida del programa (~ 1 línea).
print(f'La posición final es de {x:5.2f} m y la velocidad es de {v:6.3f} km/h')