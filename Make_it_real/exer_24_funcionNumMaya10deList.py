'''
Completa el siguiente programa para imprimir los números que sean mayores a 10.

nums = [1, 23, 5, 8, 40, 12, 2, 67, 24, 9, 39]
# // escribe tu código acá
El resultado debería ser el siguiente:

23
40
12
67
24
39
'''

def mayor_10(lista):

    for numeros in lista:

        if numeros > 10:

            print(numeros)



nums = [1, 23, 5, 8, 40, 12, 2, 67, 24, 9, 39]



print(mayor_10(nums))