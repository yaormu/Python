'''
print('Hola mundo')

#input()
print('Ingrese nombre')
x = input()
print('Hola ' + x)

#no necesidad comillas
print(7)
print(true)
print(['ana', 27])

#imprimir desde la variable
x = 35
mensaje = 'Hola a todos!'
print(mensaje)
print(x)

#ERRORES
#SintaxError    falta alguna coma, algo asi
#NameError      interprete no reconoce una palabra

# int, float
un_integer = 2
un_float = 2.1

print(un_integer + 3)

#division, ZeroDivisionError
print(573 - 12 + 5)
print(25 * 2)
print(10 / 5)
print(10 / 0)   #ZeroDivisionError

precio_cafe = 1.50
numero_cafes = 4

print(precio_cafe * numero_cafes)

#exponentes
print(15 ** 2)
print(2 ** 10)  #a la diez
print(9 ** 3)   #Al cubo

#raiz cuadrada
print(4 ** 0.5)

#modulo %
print(29 % 5)   #4
print(32 % 3)   #2
print(44 % 2)   #0  numero par
'''
#concatenacion (+)
cumple_uno = 'Yo tengo '
edad = 36
cumple_dos = ' años'
mensaje_completo = cumple_uno + str(edad) + cumple_dos
print(mensaje_completo)

#Mas igual
numero_km = 5
numero_km += 4
print(numero_km)

recorrido = 'Estuve corriendo xxx'
recorrido += '#running'
recorrido += ', #5k'
print(recorrido)

#String multilinea
mi_parrafo = """
sfsf asdfsd asdgsg asgdasdg asgdagas
sfsf asdfsd asdgsg asgdasdg asgdagas
sfsf asdfsd asdgsg asgdasdg asgdagas
sfsf asdfsd asdgsg asgdasdg asgdagas
"""
print(mi_parrafo)

mi_nombre_completo = "mi nombre"
print(mi_nombre_completo)

#1 nombramiento de variables en minuscula
print("Ingrese su nombre: ")
frase = input()
print(frase)

#2 
num1 = input("Ingrese numero 1: ")
num2  = input("Ingrese numero 2: ")

resultado = int(num1) + int(num2)
print(type(resultado))
print(resultado)

# str() volver a string
# int() volver a numero

#en una sola linea
# resultado = print(input("Ingrese algo"))

#punt y coma no es necesario
#result = int(num1)

#Contatenacion - Se puede usar interpolacion
actual = 2021
nacimiento = int(input("Ingresa año nacimiento: "))
edad = actual - nacimiento
print(f'Tienes: {edad} años actualmente')