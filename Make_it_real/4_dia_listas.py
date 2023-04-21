"""
Una lista es un set ordenado de objetos
Una lista empieza y termina en corchetes [y]
Cada item es separado por coma [67, 63]
Buena practica añadir espacio despues de la coma
"""

#Asignar lista a una variable
alturas = [1.9, 1.7, 1.5, 1.2, 1.3]
print(alturas)

nombres = ["ana", "ruben", "erika", "lucy"]
print(nombres)

#Pueden contener varios datos
mix = [12, "juan", True]
print(mix)

#Las listas son contenedores de valores, para por tener varios valores, no solo uno como la variable

#Las listas tambien puede contener otras listas
list_list = [["ana", 23], ["juan", 25], ["andrea", 26]]
print(list_list)

#Lista vacias
lista_vacia = []

#Crecer una lista (vacias  con valores)
# 1- Agregando solo un dato con ".append()"
print(lista_vacia)

lista_vacia.append(1)
print(lista_vacia)

#Añadir otra lista
lista_vacia.append([1, 2])

#Añadir multiples valores
# 2- "signo/operador"
lista_vacia = lista_vacia + [2, 3, "ana"]
print(lista_vacia)

#Buena practica
lista_con_valores = [2, 3, "ana"]
lista_vacia += lista_con_valores
print(lista_vacia)

#Indice de las lista
alturas = [1.9, 1.7, 1.5, 1.2, 1.3]
nombres = ["ana", "ruben", "erika", "lucy"]

#Seleccion de un elemento basado en su indice
print(alturas[1])   #1.7
print(nombres[2])   #erika

#editar, cambiar un valor, las lista son mutables
alturas[1] = 2
print(alturas)

# seleccion fuera del rango
# print(alturas[6]) #Generara error

#ver si existe elemento
print(3 in alturas) #false

#se puede comprobar
if 3 in alturas:
    print("Si se encuentra")
else:
    print("No se encuentra")

#Añadir valor en una posicion deseada
# se usa insert()
alturas = [1.9, 1.7, 1.5, 1.2, 1.3]
alturas.insert(2, "alturas")
print(alturas)  #[1.9, 1.7, "alturas", 1.2, 1.3]

#Eliminar indice especifico pop()
alturas.pop(2)  #eliminar la posicion
alturas.pop()   #Al no pasar ningun parametro eliminar el último

# Eliminar toda lista "del"
# del alturas
# print(alturas) genera error ya no existe lista

#vaciar lista
alturas.clear()
print(alturas)

#selecionar el último indice en caso de la lista ser muy larga y no conocer el dato
altura = [1.9, 1.7, 1.5, 1.2, 1.3, 1.9, 1.7, 1.5, 1.2, 1.3,]
print(altura[-1])

#Selecion de partes de la lista, un trozo: slicing list
#letras[indice]
#letras[inicio:fin]
#fin = valor - 1
#fin = indice + 1

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

sublista = letras[1:6]
print(sublista) #['b', 'c', 'd', 'e', 'f']

#si va empezar desde la posicion 0 se puede omitir escribirla
print(letras[:3])   #['a', 'b', 'c']

#Selecion desde la posicion 2 hasta el final
print(letras[2:])   #['c', 'd', 'e', 'f', 'g']

print(letras[-3:])  #['e', 'f', 'g']

print(letras[:-3])  #['a', 'b', 'c', 'd']

#Range es un tipo de datos en python (diferente a las listas, pero se combina bien con las listas)

mi_rango = range(2, 10) 
print(list(mi_rango))   #[2, 3, 4, 5, 6, 7, 8, 9]

#Crear lista  de dos en dos
mi_rango = range(2, 10, 2)
print(list(mi_rango))   #[2, 4, 6, 8]

#convertir en lista
mi_rango = range(2, 10, 2)
mi_rango_list = list(mi_rango)

print(mi_rango_list)
print(len(mi_rango_list))

#iterar sobre una lista
ejemplo = ['rojo', 'amarillo', 'azul', 'verde']

print(len(ejemplo))

for color in range(len(ejemplo)):
    print(ejemplo[color])

#EMPAREJA
#zip - objeto en python
alturas = [1.9, 1.7, 1.5, 1.2, 1.3]
nombres = ["ana", "ruben", "erika", "lucy"]

print(list(zip(alturas, nombres)))
