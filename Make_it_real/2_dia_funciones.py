#FUNCIONES
#mismas condiciones de una variable en minuscula
def nombre_de_la_funcion():
    pass #Palabra reservada que permite declara una funcion, pero no pasa nada con el

#1- Declarar o definir la funcion
#2- Llamar a la funcion

def saludar():
    print("Bienvenido a mi tienda")
    print("La camiseta que tenemos en promocion")
    print("Disfruta comprando")

#Llamar la funcion
saludar()

#3- Parametros
def saludito(frase_especial):
    print("Bienvenido la tienda")
    print("La frase para hoy " + frase_especial)
    print("Wow")

saludito("Donde comen uno, comen dos")

def saludo_dos(nombre_tienda, oferta_tienda):
    print("Bienvenido la tienda: " + nombre_tienda)
    print("La oferta para hoy: " + oferta_tienda)
    print("Wow")

saludo_dos("Justo&Bueno", "Carnes frias")

#keyword arguments = palabras clave
#colocar los parametros sin orden
def saludo_tres(nombre_tienda, oferta_tienda):
    print("Bienvenido la tienda: " + nombre_tienda)
    print("La oferta para hoy: " + oferta_tienda)
    print("Wow")

saludo_tres(oferta_tienda="Carnes frias", nombre_tienda="Justo&Bueno")


#default arguments = argumentos por defecto
def saludo_4(nombre_tienda, oferta_tienda="Patacones"):
    print("Bienvenido la tienda: " + nombre_tienda)
    print("La oferta para hoy: " + oferta_tienda)
    print("Wow")

saludo_4(nombre_tienda="Carulla")

#default arguments = argumentos por defecto
def saludo_5(nombre_tienda, oferta_tienda="Bananos"):
    print("Bienvenido la tienda: " + nombre_tienda)
    print("La oferta para hoy: " + oferta_tienda)
    print("Wow")

saludo_4("Olimpica")

#return
#para guardar el resultado de una funcion en una variable
def divir_por_4(numero):
    return numero / 4

resultado = divir_por_4(16)

print(resultado)

#Retornar mas valores
def valor_al_cuadrado(valor_x, valor_y):
    x_2 = valor_x * valor_x
    y_2 = valor_y * valor_y
    return x_2, y_2

x_al_cuadrado, y_al_cuadrado = valor_al_cuadrado(1, 3)

print(x_al_cuadrado)
print(y_al_cuadrado)

#otra forma de llamar
print(x_al_cuadrado, y_al_cuadrado)

#scope() alcance de la variable
# variable local estaria dentro de la funcion
# variable global estaria por fuera

"""
BUENAS PRACTIAS
La buena practica es que los print esten por fuera de la funcion

Se debe de utilizar es el return dentro de la funcion, ya que el resultado obtenido lo podemos guardar en una variable, y aprovechar ese tipo resultado con la variable que retorno desde la funcion

Los return no necesitan parentisis
"""

#Ejemplo mala practica
def propina(total, porcentaje):
  print(total * porcentaje)/100

propina(100, 2) 

#Ejemplo de buena practica
def propina2(total,porcentaje):
  total_tip = (total * porcentaje) / 100
  return total_tip

print(propina2(100, 2))