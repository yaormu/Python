"""
Escribe una función llamada gran_exponente que reciba dos parámetros: base y exponente. Si base elevado a exponente es más de 5000 debe retornar True. De lo contrario debe retornar False.

# escribe la función gran_exponente acá

# código de prueba
print(gran_exponente(2, 8)) # False
print(gran_exponente(5, 1000)) # False
print(gran_exponente(6, 900)) # True
"""

def gran_exponente(base, exponente):
  return True if base**exponente > 5000 else False

print(gran_exponente(2, 8)) # False
print(gran_exponente(5, 1000)) # True
print(gran_exponente(6, 900)) # True