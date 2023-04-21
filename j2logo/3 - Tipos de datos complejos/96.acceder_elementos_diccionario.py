"""
Acceder a un elemento de un diccionario es una de las principales operaciones por las que existe este tipo de dato. 
El acceso a un valor se realiza mediante indexación de la clave. 
Para ello, simplemente encierra entre corchetes la clave del elemento d[clave]. 
En caso de que la clave no exista, se lanzará la excepción KeyError.
"""

>>> d = {'uno': 1, 'dos': 2, 'tres': 3}
>>> d['dos']
2

>>> d[4]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 4

"""
La clase dict también ofrece el método get(clave[, valor por defecto]). Este método devuelve el valor correspondiente a la clave clave. En caso de que la clave no exista no lanza ningún error, sino que devuelve el segundo argumento valor por defecto. Si no se proporciona este argumento, se devuelve el valor None.
"""

>>> d = {'uno': 1, 'dos': 2, 'tres': 3}
>>> d.get('uno')
1

# Devuelve 4 como valor por defecto si no encuentra la clave
>>> d.get('cuatro', 4)
4

# Devuelve None como valor por defecto si no encuentra la clave
>>> a = d.get('cuatro')
>>> a
>>> type(a)
<class 'NoneType'>