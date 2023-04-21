#ELEMENTS COLLECTION LIST
lista_animales = ["perro", "gato", "caballo", "gato"]

#List with various types
lista_revuelta = ["carro", 3.5, True, 9]

#Add new item to list 
lista_animales.append("vaca")

#Delete animal list item
lista_animales.remove("perro")

#If we indicate delete an element and it is repeated, delete the first
lista_animales.remove("gato")

#Add multiple items to the animals list
lista_animales.extend(["mariposa", "hormiga", "hipopotamo"])

#Insert element in position especific, example position 1
lista_animales.insert(0,"zebra")

#Print animal list with FOR
for animal in lista_animales:
    print(animal)

#DICTIONARY: CONTAINS A KEY ELEMENT AND A VALUE
mi_diccionario = {"clave1":1, "clave2": 2}

diccionario_persona = {"nombre": "leonel", "apellido": "gonzalez", "edad": 32, "estatura": 1.80} 

#To print diccionario_persona
print(diccionario_persona)

MiDiccionario = {"nombre":"leonel","apellido":"gonzalez","edad":"32"}

#update colection dictionary
MiDiccionario.update({"nacionalidad":"mexicano"})

#dictionary keys
clave = MiDiccionario.keys()
#dictionary value
valor = MiDiccionario.values()

#dictionary length
cantidad_elementos = MiDiccionario.items()

#Recorrer dicionario
for clave, valor in cantidad_elementos:
    print(clave + ":" +valor)