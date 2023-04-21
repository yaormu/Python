"""
Un caso es especial de bucle for se da al recorrer los elementos de un diccionario. Dado que un diccionario está compuesto por pares clave/valor, hay distintas formas de iterar sobre ellas.
"""
# 1 – Recorrer las claves del diccionario.

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in valores:
    print(k)

A
E
I
O

# 2 – Iterar sobre los valores del diccionario

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for v in valores.values():
    print(v)

4
3
1
0

# 3 – Iterar a la vez sobre la clave y el valor de cada uno
# de los elementos del diccionario.

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v)

k=A, v=4
k=E, v=3
k=I, v=1
k=O, v=0