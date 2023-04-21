for e in iterable:
    # Tu código aquí
else:
    # Este código siempre se ejecuta si no
    # se ejecutó la sentencia break en el bloque for

"""
Es decir, el código del bloque else se ejecutará siempre y 
cuando no se haya ejecutado la sentencia break dentro del bloque del for.
Veamos un ejemplo:
"""
numeros = [1, 2, 4, 3, 5, 8, 6]

for n in numeros:
    if n == 3:
        break
else:
    print('No se encontró el número 3')

# Como en el ejemplo anterior la secuencia numeros contiene al número 3,
# la instrucción print nunca se ejecutará.