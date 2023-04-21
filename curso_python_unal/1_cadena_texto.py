"""
Problema: Transformando cadenas de texto
Realizar un programa que reciba una cadena de texto, aplique una serie de transformaciones, siguiendo las reglas escritas a continuación; y al final imprima el resultado obtenido.
- Todos los caracteres deben de estar completamente en minúscula.
- Las vocales 'a', 'e' y 'o' deben de ser reemplazadas por el carácter 'i'.
- De igual manera, se deberán reemplazar sus versiones con acento ('Á', 'á', 'É', 'é', 'Ó' y 'ó') por el carácter 'í'.

Entrada 1
Bienvenido al curso de programación con Python
Salida 1
biinvinidi il cursi di prigrimiciín cin pythin

Entrada 2
El único modo de hacer un gran trabajo es amar lo que haces
Salida 2
il únici midi di hicir un grin tribiji is imir li qui hicis

Entrada 3
Si no sueltas el pasado, ¿con qué mano agarras el futuro?
Salida 3
si ni suiltis il pisidi, ¿cin quí mini igirris il futuri?
"""
# Entrada del programa (~ 1 línea).
cadena = input("Ingrese dato: ")  

cadena = cadena.lower()
cadena = cadena.replace('a', 'i')
cadena = cadena.replace('e', 'i')
cadena = cadena.replace('o', 'i')
cadena = cadena.replace('á', 'í')
cadena = cadena.replace('é', 'í')
cadena = cadena.replace('ó', 'í')

# Operaciones en cadenas de texto (~ 9 líneas)
resultado = cadena.replace('a', 'i')

# Salida del programa (~ 1 línea).
print(resultado)