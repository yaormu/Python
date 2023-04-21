"""
U3 - 4 | Conjuntos
En esta práctica trabajaremos en la creación de conjuntos de Python, y en la aplicación
práctica de sus operaciones básicas.

💡 Problema: Semejanza de textos
¿Cómo podemos conocer si dos textos son semejantes?

Una forma de medir la semejanza entre dos textos, se plantea medir esta semejanza con la cantidad 
de palabras y signos de puntuación utilizados y compartidos por ambos textos.

En primer lugar, se podría conocer cuantas palabras distintas fueron usadas en total al escribir 
los dos textos, para tener una idea del tamaño del vocabulario usado por sus escritores. 
Además, para determinar si podría tenerse una semejanza se podría ver los términos repetidos, 
calculando cuantas de estas palabras se encuentran tanto en el primer documento como en el segundo.

En esta actividad deberá escribir un programa que reciba dos líneas con cadenas de texto distintas, 
y que imprima como resultado el número de palabras compartidas y el total de palabras únicas 
encontradas en ambas cadenas.

Por ejemplo, si vemos las siguientes dos frases: "vaso medio lleno" y "vaso medio vacío". 
Podemos notar que comparten "vaso" y "medio", por lo que nuestro valor para palabras compartidas 
es 2. Además, tenemos las palabras "vacío" y "lleno", las cuales son únicas, ya que pertenecen a 
la primera o a la segunda frase, pero no a ambas, por lo que tendríamos un valor de 2 para palabras 
únicas.

⌨️ Entrada
¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa deberá recibir dos entradas, cada una en una línea:

- listado_a: cadena de texto que contiene palabras separadas por espacios en blanco, pertenecientes 
al conjunto a.
- listado_b: cadena de texto que contiene palabras separadas por espacios en blanco, pertenecientes
al conjunto b.

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. 
Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir dos líneas de salida:

- palabras_compartidas: número entero con la cantidad de palabras que tienen en común las dos 
cadenas.
- palabras_unicas número entero con la cantidad de palabras únicas encontradas en ambas cadenas.

🧩 Ejemplos
¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. 
Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1                               Salida Ejemplo 1
Bello es mejor que feo                          3
Explícito es mejor que implícito                4

Entrada Ejemplo 2                               Salida Ejemplo 2
Ahora es mejor que nunca                        4
Aunque nunca es a menudo mejor que ya mismo     6

⚠️ Notas
Puede obtener una lista con las palabras separadas por espacios de una cadena con el método .split(),
de la siguiente forma:

> "uno dos tres cuatro".split()
['uno', 'dos', 'tres', 'cuatro']
"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 4-10 líneas de código)
# Entrada del programa | transformación a conjuntos (~ 2-6 líneas).

listado_a = set(input().split())
listado_b = set(input().split())

diferenciaA = listado_a & listado_b
diferenciaB = listado_a ^ listado_b

print(len(diferenciaA))
print(len(diferenciaB))



# Procesar conjuntos | salida del programa (~ 2-4 líneas)