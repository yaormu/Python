# Variables
my_string_var = "My string variable"
print(my_string_var)

my_int_var = 5
print(my_int_var)

my_bool_var = False
print(my_bool_var)

# Concatenar variables en print
print(my_string_var, my_int_var, my_bool_var)

# Parsear int a string
converter_var_int_to_string = str(my_int_var)
print(converter_var_int_to_string)
print(type(converter_var_int_to_string)) # str

print("Este es el valor de:", my_bool_var)

# Algunas funciones del sistema
print(len(my_string_var))

# Variables en una sola línea
name, surname, alias, age = "Ruben", "Dario", "Bencho", 35
print("Me llamo", name, surname, "me apodan", alias, "tengo una edad de", age, "años")

# Inputs - pedir e ingresar datos
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)

# cambiamos el tipo
name = 35
age = 'jose'

print(name)
print(age)

# Forzando el tipo
address: str = "Mi dirección"
address = 32 # pero igual podemos cambiar el tipo
print(address)












