Qué es una tupla
La clase tuple en Python es un tipo contenedor, compuesto, que en un principio se pensó para almacenar grupos de elementos heterogéneos, aunque también puede contener elementos homogéneos.

Junto a las clases list y range, es uno de los tipos de secuencia en Python, con la particularidad de que son inmutables. Esto último quiere decir que su contenido NO se puede modificar después de haber sido creada.

En general, para crear una tupla en Python simplemente hay que definir una secuencia de elementos separados por comas.

Por ejemplo, para crear una tupla con los números del 1 al 5 se haría del siguiente modo:

>>> numeros = 1, 2, 3, 4, 5
Como te indicaba, la clase tuple también puede almacenar elementos de distinto tipo:

>>> elementos = 3, 'a', 8, 7.2, 'hola'
Incluso pueden contener otros elementos compuestos y objetos, como listas, otras tuplas, etc.:

>>> tup = 1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola'
A continuación te indico las diferentes formas que existen de crear una tupla en Python:

Para crear una tupla vacía, usa paréntesis () o el constructor de la clase tuple() sin parámetros.
Para crear una tupla con un único elemento: elem, o (elem, ). Observa que siempre se añade una coma.
Para crear una tupla de varios elementos, sepáralos con comas: a, b, c o (a, b, c).
Las tuplas también se pueden crear usando el constructor de la clase, tuple(iterable). En este caso, el constructor crea una tupla cuyos elementos son los mismos y están en el mismo orden que los ítems del iterable. El objeto iterable puede ser una secuencia, un contenedor que soporte la iteración o un objeto iterador.

❗️IMPORTANTE: El hecho que determina que una secuencia de elementos sea una tupla es la coma , no los paréntesis. Los paréntesis son opcionales y solo se necesitan para crear una tupla vacía o para evitar ambigüedades.

# Aquí, a, b y c no son una tupla, sino tres argumentos con
# los que se llama a la función "una_funcion"
>>> una_funcion(a, b, c)
# Aquí, a, b y c son tres elementos de una tupla. Esta tupla,
# es el único argumento con el que se invoca a la 
# función "una_funcion"
>>> una_funcion((a, b, c))

