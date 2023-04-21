'''
Escribe una función llamada propina que reciba dos números: total y porcentaje. La función debe retornar el valor de la propina.

# escribe la función propina acá

# código de prueba
print(propina(100, 50)) # 50
print(propina(200, 10)) # 20
print(propina(5000, 90)) # 4500
'''

def propina(total, porcentaje):
    return total * porcentaje / total

print(propina(100, 50)) # 50
print(propina(200, 10)) # 20
print(propina(5000, 90)) # 4500