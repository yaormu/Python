"""
U3 - 3 | Iterando Diccionarios
En esta práctica trabajaremos con el proceso de creación de diccionarios y de acceso a su contenido 
por medio de estructuras iterativas.

💡 Problema: Votación
En una institución educativa de educación media se está realizando el proceso de elección de un 
representante estudiantil, que cumplirá con este rol en el transcurso del año. En esta edición, 
las directivas de la institución están trabajando por implementar nuevas tecnologías y han decidido
solicitar la creación de un programa que haga el recuento de las votaciones.

Para una prueba de la utilidad de la idea en la próxima votación, se decidió usarla como apoyo en 
el conteo de los votos. Para esto, un jurado de votación introducirá por nombre el candidato de 
cada una de las boletas de su mesa. Finalmente, el programa escribirá un reporte con el nombre del 
ganador.

Escriba un programa que reciba una lista de votos por diferentes candidatos y calcule cuál es el 
candidato ganador. Si hay un empate el programa debe imprimir la palabra EMPATE. En caso contrario,
debe imprimir el nombre del candidato ganador.

⌨️ Entrada
¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá 
ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá n + 1 líneas de entrada:

- n: La primera línea de la entrada contiene un entero n indicando el número de votos totales.
- nombres Después de la primera línea, el programa recibirá un total de n lineas con el nombre 
del candidato registrado en el voto.

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. 
Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir en la salida una única línea.

- resultado cadena de texto con el nombre del candidato ganador o con la palabra EMPATE si dos o 
más candidatos tiene el mismo número de votos.

🧩 Ejemplos
¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1       Salida Ejemplo 1
5                       EMPATE
Juan
María
Pedro
María
Juan

Entrada Ejemplo 2       Salida Ejemplo 2
6                       María
Juan
María
Pedro
María
Juan
María
"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 9-16 líneas de código)
# Entrada del programa (~ 1 línea).
# Numero de entradas
num_entradas = int(input())

# variables de ayuda  (~ 1-3 líneas)
# diccionario de candidatos
candidatos = {}

# Obtener los votos e ir sumando según corresponda (~ 3-5 líneas)
for i in range(1, num_entradas + 1):
    candidato = input()

    if candidatos.get(candidato) == None : candidatos[candidato] = 1

    else : candidatos[candidato] += 1

# Definir resultado (~ 3-6 líneas)
maximo = max(candidatos.values())

max_keys = [key for key, value in candidatos.items() if value == maximo]

if (len(max_keys)) >=2: resultado="EMPATE"

else: resultado = max(candidatos, key = candidatos.get)

# Salida del programa (~ 1 línea).
print(resultado)