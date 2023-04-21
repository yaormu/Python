x = 17
if x < 20:
    print('x es menor que 20')


# Veamos otro ejemplo:


valores = [1, 3, 4, 8]
if 5 in valores:
    print('está en valores')
print('fin')

"""
En este caso tenemos una lista de valores. El if comprueba si el número 5 se encuentra entre estos valores. Como la expresión devuelve como resultado False, porque 5 no está entre los valores, el código anterior simplemente mostrará por pantalla la cadena fin.

Si repetimos el ejemplo anterior, modificando la condición a esta otra 3 in valores, el resultado del programa sería:
"""

está en valores
fin



"""
?? RECUERDA: En principio, en Python todos los objetos/instancias se evalúan a True a excepción de None, False, 0 de todos los tipos numéricos y secuencias/colecciones vacías, que se evalúan a False.
"""