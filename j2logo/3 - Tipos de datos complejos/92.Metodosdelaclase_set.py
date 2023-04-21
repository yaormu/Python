# listando los métodos principales de la clase set en Python:

Método					Descripción
add(e)					Añade un elemento al conjunto.
clear()				Elimina todos los elementos del conjunto.
copy()					Devuelve una copia superficial del conjunto.
difference(iterable)			Devuelve la diferencia del conjunto con el iterable como un conjunto nuevo.
difference_update(iterable)		Actualiza el conjunto tras realizar la diferencia con el iterable.
discard(e)				Elimina, si existe, el elemento del conjunto.
intersection(iterable)			Devuelve la intersección del conjunto con el iterable como un conjunto nuevo.
intersection_update(iterable)		Actualiza el conjunto tras realizar la intersección con el iterable.
isdisjoint(iterable)			Devuelve True si dos conjuntos son disjuntos.
issubset(iterable)			Devuelve True si el conjunto es subconjunto del iterable.
issuperset(iterable)			Devuelve True si el conjunto es superconjunto del iterable.
pop()					Obtiene y elimina un elemento de forma aleatoria del conjunto.
remove(e)				Elimina el elemento del conjunto. Si no existe lanza un error.
symmetric_difference(iterable) 	Devuelve la diferencia simétrica del conjunto con el iterable como un conjunto nuevo.
symmetric_difference_update(iterable)	Actualiza el conjunto tras realizar la diferencia simétrica con el iterable.
union(iterable)			Devuelve la unión del conjunto con el iterable como un conjunto nuevo.
update(iterable)			Actualiza el conjunto tras realizar la unión con el iterable.

❗️ NOTA: Los operadores |, &, … toman siempre como operandos objetos de tipo set. Sin embargo, sus respectivas versiones como métodos union(), intersection(), … toman como argumentos un iterable (lista, tupla, conjunto, etc.).
