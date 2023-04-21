"""
La sentencia while la puedes usar en multitud de ocasiones. A continuación te mostraré un escenario típico de uso de bucle while: Comprobar si existe un elemento en una secuencia.

Imagina que tienes la siguiente lista de valores [5, 1, 9, 2, 7, 4] y quieres saber si el número 2 está contenido en dicha lista. La estructura típica de bucle while para ello es como sigue:
"""

valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')


"""
Como puedes observar, en el ejemplo, se utilizan 3 variables de control:

encontrado: Indica si el número 2 ha sido encontrado en la lista.
indice: Contiene el índice del elemento de la lista valores que va a ser evaluado.
longitud: Indica el número de elementos de la lista valores.
"""

"""
?? NOTA: El anterior es solo un ejemplo para que veas cómo funciona la sentencia while. En realidad, en Python se puede usar el operador in para comprobar de forma más eficiente si un elemento está contenido en una secuencia.
"""