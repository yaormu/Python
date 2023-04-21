# 1- Control de flujo / Condicionales

# 2- Expresiones Booleanas = Clausula que pueda ser evaluada a True o False

# 3- Operadores Relaciones = Comparar dos items y retorna True o False, tambien llamados comparadores
# Primeros operadores
# Igual ==
# No igual / Diferente de !=

#comparacion
print(1 == 1)   #True
print(1 != 1)   #True
print(3 == 1)   #False
print('3' == 3) #False

#Saber de que tipo es:
print(type('3'))  #'str'
print(type(3))    #'int'

# 4- Variables booleanas
var = 10
var2 = "hola"
var3 = True
var4 = '3'
var5 = 3

print(var4 == var5) #False

dado_a_false = True
dato_a_true = True

print(dado_a_false == dato_a_true)  #True

bool_uno = 5 != 7
bool_dos = 1 + 1 !=2
bool_tres = 3 * 3 == 9

print(bool_uno) #True
print(bool_dos) #False
print(bool_tres) #True

# 5- Sentencias IF(Preguntas)
'''
if esta_lloviendo:
    llevar_sombrilla()

if 2 == 2:
    llevar_sombrilla()
'''

if 2 == 2:
    print('Sombrilla')  #Sombrilla

#La forma correcta y adecuada seria guardar en una variable
bool_cuatro = 2 == 2
if bool_cuatro:
    print('Sombrilla')  #Sombrilla

# Otros operadores
# mayor que >
# menor que <
# mayor o igual que >=
# menor o igual que <=

def checkear_edad(edad):
    if edad >= 13:
        return True

print(checkear_edad(13))  #True


# 6- Operadores Booleanas
# and ==> combian dos expresiones booleanas y evalua a True si AMBAS son True y devuelve False de lo contrario

print((1 + 1 == 2) and (2 + 2 == 4))  #True
#True and True = True

print((1 + 1 == 2) and (2 < 1)) #False
#True and False = False

# or ==> Combina dos expresiones booleanas y evalua a True SI CUALQUIERA DE LAS DOS son True

print((1 + 1 == 2) or (2 < 1)) #True
#True or False = True

print((2 + 1 == 2) or (2 < 1)) #False
#False or False = False

# not ==> reversa el resultado
print(not True == True) #False

# 7- Sentencia Else y Elif
def checkear_edad(edad):
    if edad >= 13:
        return True
    elif edad >= 8:
        return "mayor o igual a 8"
    else:
        return False

def gracias(donacion):
    if donacion >= 10000 and donacion <= 50000:
        print("Gracias, su nivel es platinum")
    elif donacion >= 5000:
        print("Gracias, su nivel es gold")
    elif donacion >= 1000:
        print("Gracias, su nivel es silver")
    else:
        print("Gracias, su nivel es bronce")

gracias(75000)  #Gracias, su nivel es gold
#Se debe tener en cuenta como se realizan las condiciones, como en e anterior resultado