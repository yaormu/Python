"""
U2 - 4 | Estructuras iterativas (for y range)
En esta práctica trabajaremos con las estructuras de control iterativas basadas en 
iterables, y en particular del uso de la sentencia for en rangos numéricos.

Aunque la sentencia while y la sentencia for tienen grandes similitudes, cada uno tiene 
una función clara. En el caso de while se suele utilizar en las ocasiones donde no se 
tiene certeza de cuantas iteraciones se debe realizar. 
Mientras que la sentencia for se aplica cuando se puede saber cuántos ciclos se deben 
ejecutar; esto se cumple en la mayoría de los casos al tatar con objetos iterables, 
ya que siempre se puede saber su tamaño. 
El uso de una sentencia o de la otra en cada caso está relacionado con la aplicación 
buenas prácticas y la legibilidad de un código.

💡 Problema: Calculando Pi
Uno de los métodos más famosos para calcular el número pi (π), por su facilidad de 
implementación, es la igualdad matemática conocida como Serie de Leibniz. 
Esta se apoya en varias propiedades matemáticas para determinar el valor de π al realizar 
una sumatoria infinita de números definidos en un patrón sencillo. 
Aunque en la práctica no es posible considerar realizar infinitas operaciones, 
aún se puede lograr cierta aproximación, ya que conforme mayor sea el número de valores 
empleados en la sumatoria, más cerca estará el resultado obtenido del valor de pi (π).

La igualdad de la Serie de Leibniz es la siguiente:
1/1−1/3+1/5−1/7+1/9−...=π/4

Como puede notar, la serie está compuesta por las fracciones con numerador 1 y denominador
impar en orden, intercalando entre valores positivos y negativos. 
El resultado es el valor π4, que se puede multiplicar por 4 al final para obtener el valor 
aproximado de π.

En este ejercicio deberá realizar un programa que retorne el valor aproximado de π, 
obtenido de realizar la serie de Leibniz de manera que los denominadores de las fracciones
sean menores a un número entero n. 
En este sentido, el denominador del último elemento corresponde al valor n−1, o a n−2 
cuando n sea impar.

Por ejemplo, para un valor n de 10 o de 11 se realizaría la misma sumatoria con un 
resultado con muy poca precisión del valor real:

π≈4(1/1−1/3+1/5−1/7+1/9)=3.3396825397

Para este ejercicio, deberá indicar el valor con 10 dígitos decimales.

⌨️ Entrada
¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan 
la función input.

El programa recibirá un único valor de entrada:
- n: número entero (tipo int), que representa el límite excluido de los enteros 
usados como denominador en la sumatoria.

🖥️ Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir en la salida una única línea.
- pi: número decimal (tipo float) con el valor obtenido de la aproximación del número π 
con la sumatoria de la serie de Leibniz.

🧩 Ejemplos
¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de 
ejemplo. Utilice las entradas provistas y compare el resultado con las salidas 
correspondientes.

Entrada Ejemplo 1
11
Salida Ejemplo 1
3.3396825397

Entrada Ejemplo 2
100
Salida Ejemplo 2
3.1215946526

Entrada Ejemplo 3
25615
Salida Ejemplo 3
3.1416707359
"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 7-10 líneas de código)

# Entrada del programa (~ 1 línea).
n = int(input())
c = 0

# Serie de Leibniz (~ 5-8 líneas). 
pi = 0
for x in range(1, n, 2):
    pi = pi+(((-1) ** c)*(1/x))
    c += 1
pi = pi * 4

# Salida del programa con 10 decimales (~ 1 línea).
print(f"{pi:.10f}")