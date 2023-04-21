miLista=["Maria", "Nata", "Lucy", "Jose", 5, True, 80]

print(miLista[:])

# Acceder a una posicion expecifica
print(miLista[2])

# Acceder a una posicion expecifica al reves
print(miLista[-3])

# Acceder a los 3 primeros elementos
print(miLista[0:3]) #Se podria delcarar [:3] sin el 0

# Agregar elementos al final de la lista
miLista.append("Rubencho")

print(miLista[:])

# Agregar elementos en una posicion especifica
miLista.insert(2,"Sharlotte")

# Agregar varios elementos 
miLista.extend("Jaime", "Bryan", "David", "Elmer")

# Conocer el indice de un elemento 
print(miLista.index("Martin"))

#Comprobar si se encuentra un elemento
print("Pepe" in miLista)    #Imprime True si esta o False si no se encuentra

#Eliminar elemento
milista.remove("Lucy")

milista.remove(5)

print(milista[:])

#Eliminar ultimo elemento de la lista
milista.pop()

# Unir listas
miLista2=["Pato", "Farid", "Alex"]

miLista3=miLista+miLista2

print(miLista3[:])

#Repetir listas
miLista4=["Rigo", "Gustavo", "Jorge"]*3
print(miLista4[:])