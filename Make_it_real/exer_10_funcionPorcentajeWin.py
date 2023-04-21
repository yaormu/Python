'''
Escribe una función llamada porcentaje_de_victorias que reciba dos números: victorias y derrotas. La función debe retornar el porcentaje de victorias.

# escribe la función porcentaje_de_victorias acá

# código de prueba
print(porcentaje_de_victorias(5, 5)) # 50
print(porcentaje_de_victorias(7, 0)) # 100
print(porcentaje_de_victorias(6000, 4000)) # 60
'''

def porcentaje_de_victorias(victorias, derrotas):
    total_jugado = victorias + derrotas
    return victorias * 100 / total_jugado

print(porcentaje_de_victorias(5, 5)) # 50
print(porcentaje_de_victorias(7, 0)) # 100
print(porcentaje_de_victorias(6000, 4000)) # 60