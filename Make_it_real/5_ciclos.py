#Ciclos

razas = ['bulldog', 'beagles', 'labrador', 'pug', 'golden']

#recorremos el array manualmente
print(razas[0])
print(razas[1])
print(razas[2])
print(razas[3])
print(razas[4])

'''
#ciclo for para recorrer
for <vaiable_temporal> in <lista>
    <accion>
'''
for i in razas:
    print(i)

#crear un rango de 0 a 9, pero lo volvemos lista
print(list(range(9)))

#imprimir 3 veces la palabra
#tambien se puede interar en un diccionario y otras
for i in range(3):
    print('Warngin!')

mis_numeros = [4, 8, 14, 15, 20]
mis_numeros.append(1)

for number in mis_numeros:
    print(mis_numeros)

#break
perros = ['bulldog', 'beagles', 'labrador', 'pug', 'golden']

#encontrar un elemento deseado
#y quiebra el proceso
for i in perros:
    if i == 'beagles':
        print('Encontramos el beagle')
        break
    print(i)

#continue
#si el condicional se cumple, continua
lista_numeros = [1, -2, 3, 0, -2, 1, 5, 6]

#imprimir numeros que cumplan la condicion
#numeros positivos
for i in lista_numeros:
    if i < 0:
        continue
    print(i)

#imprimir los indices de la lista
for i in range(len(lista_numeros)):
    print('indices ', i)

#ciclos concatenados / nesteados (nested)
equipos = [['juan', 'ana'], ['andres', 'pedro'], ['daniel', 'andrea', 'juan p']]

#obtener datos de tod la lista
for equipo in equipos:
    for i in equipo:
        print(i)

#imprimir cada sublista
for equipo in equipos:
    print(equipo)
    for i in equipo:
        print(i)

'''
#ciclo while
inicializador = 0
while condicional:
    operacion a ejecutar
    contador
'''

raza_perros = ['pitbull', 'gran danes', 'pumerania', 'pastor', 'siberiano']

inicializador = 0
while  inicializador < len(raza_perros):
    print(raza_perros[inicializador])
    inicializador += 1

n = 10
sum = 10
i = 1

while  i <= n:
    sum += i
    print('contador ', i)
    print('sumatoria ', sum)
    i += 1

#list comprehensions (compresiones de listas)
#un ciclo for dentro de una lista, para tener como resultado otra lista

carros = ['mazda', 'renault', 'kia', 'chevrolet', 'woskvagen']

#en forma de ciclo for
mazdas = []

for carro in carros:
    if carro == 'mazda':
        mazdas.append('mazda')

print(mazdas)

#forma list comprehensions
#lista = [variable_temporal for variable_temporal in lista if condicional]
#la condicion es opcional si necesitamos algo especifico

chevrolets = [vehiculo for vehiculo in carros if vehiculo == 'chevrolet']

print(chevrolets)

#2 ejemeplo forma list comprehensions
#lista = [variable_temporal for variable_temporal in lista if condicional]
palabras = ["@ana", "#no-filter", "@diego", "#fff", "@dfmp"]

#obtener usuarios empieza por @
usernames = [palabra for palabra in palabras if palabra[0] == "@"]

print(usernames)

#3 ejemeplo forma list comprehensions
#lista = [variable_temporal for variable_temporal in lista if condicional]
#obtener otra lista con un mensaje
mensajes = [usuario + " por favor sigueme!" for usuario in usernames]

print(mensajes)

#4 ejemeplo forma list comprehensions
#lista = [variable_temporal for variable_temporal in lista if condicional]
mis_votos = [23, 45, 32, 1, 24, 17]

#vamos a sumar a cada item el valor de 100
votos_actualizados = [voto + 100 for voto in mis_votos]

print(votos_actualizados)

