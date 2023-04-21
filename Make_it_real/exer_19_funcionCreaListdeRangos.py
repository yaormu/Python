'''
Escribe una función crear_rango que reciba un número y retorne una lista desde 1 hasta el número recibido. Si el número es menor a 1 retorna un lista vacía.

# escribe la función crear_rango acá

# código de prueba
print(crear_rango(5)) # [1, 2, 3, 4, 5]
print(crear_rango(1)) # [1]
print(crear_rango(0)) # []
print(crear_rango(-10)) # []
'''

def crear_rango(numero):
    
    if numero < 1:

        return []

    else:
        
        return list(range(1, numero + 1))

print(crear_rango(5)) # [1, 2, 3, 4, 5]
print(crear_rango(1)) # [1]
print(crear_rango(0)) # []
print(crear_rango(-10)) # []