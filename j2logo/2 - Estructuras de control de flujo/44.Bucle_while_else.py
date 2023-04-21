"""
Al igual que sucede con el bucle for, podemos alterar el flujo de ejecución del bucle while con las sentencias break y continue:

break se utiliza para finalizar y salir el bucle, por ejemplo, si se cumple alguna condición.
Por su parte, continue salta al siguiente paso de la iteración, ignorando todas las sentencias que le siguen y que forman parte del bucle.
"""

valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
        break
    else:
        indice += 1
if encontrado:
    print(f'El elemento 2 ha sido encontrado en el índice {indice}')
else:
    print('El elemento 2 no se encuentra en la lista de valores')

"""
Lo que he hecho ha sido eliminar de la condición de continuación del bucle la comprobación de la variable encontrado. Además, he añadido la sentencia break si el número 2 se encuentra en la lista.

Por otro lado, al bucle while le podemos añadir la sentencia opcional else. El bloque de código del else se ejecutará siempre y cuando la condición de la sentencia while se evalúe a False y no se haya ejecutado una sentencia break.
"""

valores = [5, 1, 9, 2, 7, 4]

indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        print(f'El elemento 2 ha sido encontrado en el índice {indice}')
        break
    else:
        indice += 1
else:
    print('El elemento 2 no se encuentra en la lista de valores')

# En esta ocasión se ha eliminado completamente el uso de la 
# variable de control encontrado.