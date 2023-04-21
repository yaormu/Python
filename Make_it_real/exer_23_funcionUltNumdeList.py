'''
Escribe una función llamada ultimo que reciba una lista y retorne el último elemento. Si la lista es vacía debe retornar "La lista está vacía":

# escribe la función ultimo acá

# código de prueba
print(ultimo([3, 2, 1])) # 1
print(ultimo([5, 1, 8, 7])) # 7
print(ultimo([])) # "La lista está vacía"
'''

def ultimo(lista):

    if len(lista) == 0:

        return "La lista está vacía"

    else:

        return lista[len(lista) - 1]

print(ultimo([3, 2, 1])) # 1
print(ultimo([5, 1, 8, 7])) # 7
print(ultimo([])) # "La lista está vacía"