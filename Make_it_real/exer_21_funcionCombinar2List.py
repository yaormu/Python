'''
Escribe una función llamada combinar que reciba dos listas y retorne una nueva lista con los elementos combinados en tuplas:

# escribe la función combinar acá

# código de prueba
print(combinar([1, 2], ['a', 'b'])) # [(1, 'a'), (2, 'b')]
print(combinar(["Pedro", "Maria"], [15, 22])) # [("Pedro", 15), ("Maria", 22)]
'''

def combinar(lista1, lista2):

    return list(zip(lista1,lista2))

print(combinar([1, 2], ['a', 'b'])) # [(1, 'a'), (2, 'b')]
print(combinar(["Pedro", "Maria"], [15, 22])) # [("Pedro", 15), ("Maria", 22)]