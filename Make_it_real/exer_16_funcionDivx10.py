"""
Escribe una función llamada divisible_por_10 que reciba un parámetro num que retorne True si num es divisible por 10 y False de lo contrario.

# escribe la función divisible_por_10 acá

# código de prueba
print(divisible_por_10(100)) # True
print(divisible_por_10(1980)) # True
print(divisible_por_10(38)) # False
"""

def divisible_por_10(num):
    return True if num%10 == 0 else False


# código de prueba
print(divisible_por_10(100)) # True
print(divisible_por_10(1980)) # True
print(divisible_por_10(38)) # False