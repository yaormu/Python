'''
Escribe una función llamada promedio que reciba una lista de números y retorne el promedio:

# escribe la función promedio

# código de prueba
print(promedio([1, 2, 3])) # 2
print(promedio([8, 4, 7, 9])) # 7
print(promedio([])) # 0
'''

def promedio(lista):
    suma = sum(lista)
    if suma > 0:
        return(suma // len(lista))
    else:
        return suma

print(promedio([1, 2, 3])) # 2
print(promedio([8, 4, 7, 9])) # 7
print(promedio([])) # 0