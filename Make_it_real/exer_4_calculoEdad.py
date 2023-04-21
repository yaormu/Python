'''
Escribe un programa que le pida al usuario su año de nacimiento e imprima su edad actual en la consola con la frase "Tienes X años". Por ejemplo, asumiendo que el año actual es 2021 y el usuario ingresa 2000, el programa debe imprimir en la consola:

Tienes 21 años
'''

what_age = int(input('write year of birth: '))
age = 2021 - what_age 
print('Tienes ' + str(age) + ' años')