"""
U2 - 1 | Expresiones y operadores booleanos

En esta actividad trabajaremos en la formulación de expresiones booleanas en Python. 

El objetivo es poder aplicar los operadores booleanos para crear fórmulas que ayuden a 
representar casos de nuestro interés.

Con la ayuda de estas expresiones podemos definir los estados o situaciones en las que se 
encuentra un programa en ejecución. 
Aunque el concepto detrás de los valores booleanos es simple, es común cometer errores en
la construcción de expresiones lógicas que involucren múltiples condiciones.

💡 Problema: Un punto y un rectángulo
En esta ocasión vamos a trabajar con coordenadas cartesianas. 
La ubicación de un rectángulo en este sistema se puede definir mediante dos valores x y y 
que representan la posición de la esquina inferior izquierda de la figura. 
Además, se utilizan los valores w y h, representando el ancho y el alto de la figura, respectivamente.

Nota: existen distintas maneras de definir un área rectangular por medio de coordenadas cartesianas. 
No se debe confundir este enfoque con el que define los 4 valores como las coordenadas de dos esquinas 
opuestas del rectángulo. 
En este caso, esta esquina opuesta corresponde a los valores x + w y y + h, respectivamente.

En la siguiente imagen se ilustra cómo serían los rectángulos para las entradas (x=0, y=0, w=5, h=5), 
(x=7, y=2, w=4, h=2) y (x=7, y=−4, w=1, h=3). 
Dado que el punto de referencia es la esquina inferior izquierda, los valores de w y h definen 
el tamaño de los segmentos aledaños al punto, siempre en la dirección positiva de los ejes x y y.

En este ejercicio deberá realizar un programa que defina si un punto dado, con posición horizontal 
px y posición vertical py, se encuentra dentro de un rectángulo (x, y, w, h). 
Los puntos ubicados en el borde, como el punto (0,0) con la primera figura, también se considera 
que están contenidos dentro del rectángulo.

⌨️ Entrada
¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa debe recibir seis entradas:
- x: número decimal (tipo float) con la posición horizontal de la esquina inferior izquierda del rectángulo.
- y: número decimal (tipo float) con la posición vertical de la esquina inferior izquierda del rectángulo.
- w: número decimal (tipo float) con el ancho del rectángulo.
- h: número decimal (tipo float) con la altura del rectángulo.
- px: número decimal (tipo float) con la posición horizontal del punto.
- py: número decimal (tipo float) con la posición vertical del punto.

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. 
Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

- está_dentro: valor booleano que indica si el punto (px, py) está dentro del rectángulo 
descrito (True) o no (False).

🧩 Ejemplos
Entrada Ejemplo 1
0
0
2
2
0
0
Salida Ejemplo 1
True

Entrada Ejemplo 2
-5
-5
10
10
2
3
Salida Ejemplo 2
True

Entrada Ejemplo 3
1
1
2
2
0
1
Salida Ejemplo 3
False
"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 7-10 líneas de código)
# Entrada del programa (~ 6 líneas).
# Posición y dimensiones del rectángulo.
x = float(input())
y = float(input())
w = float(input())
h = float(input())

# Posición del punto.
px = float(input())
py = float(input())

# Operación booleana y salida del programa (~ 1-4 líneas).
esta_dentro=(px >= x) and (px <= (x + w)) and (py >= y) and (py <=(y + h)) 
print(esta_dentro)