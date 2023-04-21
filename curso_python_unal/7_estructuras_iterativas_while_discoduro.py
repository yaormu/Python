"""
U2 - 3 | Estructuras iterativas (while)
En esta práctica trabajaremos en el uso de las estructuras iterativas indefinidas 
y en particular, en la aplicación de las sentencias while, break y continue.

Una de las mayores dificultades que se puede tener con las estructuras iterativas es que 
se puede perder la noción del código que se ejecuta en nuestro programa. 
Cuando una estructura iterativa se ejecuta, es posible que no se haya considerado un caso, 
que el valor de una variable no se actualice o que se manejen rangos de valores inesperados. 
El resultado de esos errores es obtener resultados fuera de lo deseado o esperado.

💡 Problema: Disco duro
Se ha decidido realizar una copia de seguridad de todos los archivos de una empresa 
pequeña. Para esto, se necesita adquirir un nuevo disco duro que pueda almacenar toda 
esa información. Se quiere gastar lo mínimo posible, por lo que se plantea comprar el 
dispositivo que tenga la capacidad mínima necesaria para realizar el respaldo.

Inicialmente, identifica que toda la información que se desea almacenar tiene un tamaño 
total w (en Giga Bytes o GB), y que en el proveedor de tecnología con el que se va a 
adquirir el disco duro solo vende unidades con capacidades determinadas en potencias de 
2, disponibles desde 1 GB.

En este ejercicio deberá realizar un programa que reciba el tamaño en GB de los archivos 
que se desean almacenar e imprima en pantalla la capacidad necesaria en GB del dispositivo
de almacenamiento.

⌨️ Entrada
¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan 
la función input.

El programa recibirá un único valor de entrada:
- tamaño: número decimal (tipo float) entre 0 y 10000, que representa el tamaño total 
en GB de los archivos que se desea almacenar.

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de 
prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan 
la función print.

El programa debe imprimir en la salida una única línea.

- capacidad: el programa debe imprimir una cadena de texto con el número entero positivo 
que representa la capacidad del disco duro necesario para almacenar los archivos. 
Este número debe ser la potencia de 2 más cercana mayor o igual que el tamaño de los 
archivos y se deberá escribir con el siguiente formato:

La capacidad requerida es de <valor> GB.

🧩 Ejemplos
¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. 
Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1
0.98
Salida Ejemplo 1
La capacidad requerida es de 1 GB.

Entrada Ejemplo 2
23.50
Salida Ejemplo 2
La capacidad requerida es de 32 GB.

Entrada Ejemplo 3
256.15
Salida Ejemplo 3
La capacidad requerida es de 512 GB.
"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 5 líneas de código)
w = 0 
capacidad = 2 ** w

# Entrada del programa (~ 1 línea).
tamaño = float(input())                       # Reemplace 'None' por el código necesario. 

# Cálculo de la capacidad (~ 3 líneas).
while capacidad < tamaño: 
    capacidad = 2 ** w 
    w = w + 1 
    
    if capacidad > tamaño: 
        continue

# Salida del programa (~ 1 línea).
print(f'La capacidad requerida es de {capacidad} GB.')