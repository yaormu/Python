Método				Descripción
clear()				Elimina todos los elementos del diccionario.
copy()				Devuelve una copia poco profunda del diccionario.
get(clave[, valor])		Devuelve el valor de la clave. Si no existe, devuelve el valor valor si se indica y si no, None.
items()				Devuelve una vista de los pares clave: valor del diccionario.
keys()				Devuelve una vista de las claves del diccionario.
pop(clave[, valor])		Devuelve el valor del elemento cuya clave es clave y elimina el elemento del diccionario. 
				Si la clave no se encuentra, devuelve valor si se proporciona. 
				Si la clave no se encuentra y no se indica valor, lanza la excepción KeyError.
popitem()			Devuelve un par (clave, valor) aleatorio del diccionario. 
				Si el diccionario está vacío, lanza la excepción KeyError.
setdefault(clave[, valor])	Si la clave está en el diccionario, devuelve su valor. Si no lo está, inserta la clave con el valor valor y lo devuelve 		(si no se especifica valor, por defecto es None).
update(iterable)		Actualiza el diccionario con los pares clave: valor del iterable.
values()			Devuelve una vista de los valores del diccionario.