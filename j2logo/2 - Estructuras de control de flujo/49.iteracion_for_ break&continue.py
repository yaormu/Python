"""
break se utiliza para finalizar y salir el bucle, por ejemplo, si se cumple alguna condición.

Por su parte, continue salta al siguiente paso de la iteración, ignorando todas las sentencias que le siguen y que forman parte del bucle.

Un ejemplo es la mejor manera de entenderlo.
"""

# Uso de break. Encontrar un elemento en una colección

coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        break
    print(e)

# Uso de continue. Imprimir solo los números pares de una colección

coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e % 2 != 0:
        continue
    print(e)

#En este caso, el código anterior mostrará los números 2, 4, 8 y 4.


