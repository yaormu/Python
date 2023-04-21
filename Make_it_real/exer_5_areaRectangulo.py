'''
El área de un rectángulo se calcula con la siguiente fórmula:

base * altura
Escribe un programa que le pida al usuario la base y la altura de un rectángulo, e imprima la frase "El área es " seguido del área calculada. Por ejemplo:

Ingresa la base del rectángulo: 5
Ingresa la altura del rectángulo: 10

El área es 50
'''

base = int(input('Write Base: '))
height = int(input('Write Height: '))

area = base * height

print('The area is '+ str(area))
