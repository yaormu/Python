"""
U2 - 2 | Estructuras condicionales
En esta práctica trabajaremos en el uso de la estructura de control de flujo condicional,
usando expresiones booleanas junto las sentencias if, else y elif para poder expresar 
los casos de nuestro interés e indicar el conjunto de acciones que se deben ejecutar.

Aunque la estructura formada con esas sentencias es sencilla de manejar, se debe tener 
especial cuidado de que las expresiones booleanas estén bien formadas y describan 
correctamente el caso o escenario que se quiere representar, es decir, que el código 
deseado se ejecute únicamente en las condiciones deseadas.

Por ejemplo, si una aplicación solo muestra contenido a personas mayores de edad, 
el siguiente código representa un error para lograr este objetivo, dado que estaría 
excluyendo a las personas con una edad de exactamente 18 años.

if edad > 18:
    mostrar_contenido()
else:
    informar_bloqueo()

💡 Problema: Años bisiestos
Los años bisiestos son aquellos años en donde se agrega un día más al año en el mes de 
febrero con el propósito de realizar un ajuste razonable con respecto al año solar. 
Esto se debe a que un año solar no equivale a exactamente 365 días, sino a 365.2425 días 
aproximadamente. Para definir si un año bisiesto se aplica una serie de reglas.

- Los años divisibles entre 4 son bisiestos.
- Los años que son divisibles entre 4, pero no entre 100, son bisiestos.
- Los años divisibles entre 100, pero que no son divisibles entre 400 no son bisiestos.
- Los años divisibles entre 100 y entre 400 son bisiestos

En este ejercicio deberá realizar un programa que reciba un año y determine si es un año 
bisiesto o no.

⌨️ Entrada
¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función 
input.

El programa recibirá un único valor de entrada.
- año: número entero positivo (tipo int) que representa el año ingresado.

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de
prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan 
la función print.

El programa debe imprimir en la salida una única línea.

- es_bisiesto: cadena de texto con valor "Es un año bisiesto" o "No es un año bisiesto" 
según corresponda el caso.

🧩 Ejemplos
¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. 
Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1
1537
Salida Ejemplo 1
No es un año bisiesto

Entrada Ejemplo 2
1900
Salida Ejemplo 2
No es un año bisiesto

Entrada Ejemplo 3
2000
Salida Ejemplo 3
Es un año bisiesto
"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 8-12 líneas de código)
# Entrada del programa (~ 1 línea).
año = int(input())

# Evaluación de condiciones y salida del programa por escenario (~ 7-11 líneas).
if año % 4 != 0: 
	print("No es un año bisiesto")
elif año % 4 == 0 and año % 100 != 0:
	print("Es un año bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
	print("No es un año bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es un año bisiesto")
