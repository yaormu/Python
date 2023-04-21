'''
Escribe una función llamada sumar_lista que reciba una lista y retorne la suma de todos los elementos:

# escribe la función sumar_lista

# código de prueba
print(sumar_lista([1, 2, 3])) # 6
print(sumar_lista([5, 1, 8, 7])) # 21
print(sumar_lista([])) # 0

Nota: Este ejercicio se puede hacer con ciclos y con una función incluida en Python. Intenta buscar las dos formas pero utiliza los ciclos para solucionar este ejercicio.
'''

def sumar_lista (lista_numeros):
    suma = 0
    for i in lista_numeros:
        suma += i
    return suma

# código de prueba
print(sumar_lista([1, 2, 3])) # 6
print(sumar_lista([5, 1, 8, 7])) # 21
print(sumar_lista([])) # 0  