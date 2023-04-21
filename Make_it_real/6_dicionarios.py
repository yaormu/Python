#Diccionarios
#llave:valor
#clave:valor
#Estructura de datos
#avena: 3, tostada: 6, zumo: 5, muffin: 2

menu = {"avena": 3, "tostada": 6, "zumo": 5, "muffin": 2}

print(type(menu))

#se llama por la llave y no por el indice como las listas
print(menu['tostada'])

#Formas de inicializar un diccionario vario
location = {}
location = dict()
print(type(location))

#Hay 2 formas de añadir elementos al diccionarios
#1era forma de añadir elemento al diccionario
menu["empanada"] = 4    #añadir elemento a dicionario menu
location["Paris"] = 9   #añadir elemento a diccionario location

print(menu)
print(location)

#2da forma de añadir elemento al diccionario
location.update({"Milan": 10})
print(location)

#Si actualizamos el diccionario con una clave: valor que ya esta incluida
#se actualizara con el dicho valor

#si en diccionario tenemos llave:valor repetidos este tendra en cuenta la última llave:valor

#los diccionarios pueden tener otros diccionarios internamente y tambien pueden poseer listas
#En este ejemplo zumo guardara una lista
#Tambien muffin contendra otra lista diccionario
menu2 = {"avena": 3, "tostada": 6, "zumo": [5, 4], "muffin": {"costo1": 23, "costo2": 40}}
print(menu2)

#iterar en diccionario
universidad = {
                "alumnos": ["ana", "andrea", "juan"],
                "edades": [23, 24, 25],
                "promedio":{
                            "matematicas": 4.8,
                            "estadisticas": 4.5,
                            "fisica": 3.9
                            }
                }

print(universidad)

#Opciones de iterar
#iterar sobre llaves y valores
#iterar sobre llaves
#iterar sobre valores

#iterar sobre llaves y valores
for key, value in universidad.items():
    print("Esta es la llave: ", key)
    print("Este es el valor", value)

#iterar sobre llaves
for key in universidad:
    print("Esta es la llave: ", key)

#iterar sobre valores
for key in universidad:
    print("Este es el valor: ", universidad[key])

#Diferencia entre diccionario y formato JSON, ya que son parecidos pero no son lo mismo
#Diccionario es una estructura datos pares/valor en particular para python
#JSON permite comunicarse entre entre aplicaciones, es un lenguaje anostico, comun mente para realizar API's


