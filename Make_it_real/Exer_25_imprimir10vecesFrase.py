'''
Escribe un programa que le pida al usuario ingresar una frase. El programa debe imprimir la frase en la consola 10 veces.

Nota: utiliza un ciclo para imprimir la frase las 10 veces.
'''

frase = input('Ingresa una frase')

a = 1
while a < 10:
    print(frase)
    a = a + 1

#Otra forma
frase = input('Ingresa una frase')

for i in range(11):
    print(frase)