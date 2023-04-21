"""
Esta clase solo se puede instanciar con dos valores/objetos: True para representar verdadero y False para representar falso.
"""

Por defecto, cualquier objeto es considerado como verdadero con dos excepciones:

Que implemente el método __bool__() y este devuelva False.
Que impleménte el método __len__() y este devuelva 0.
Además, los siguientes objetos/instancias también son consideradas falsas:

None
False
El valor cero de cualquier tipo numérico: 0, 0.0, 0j, …
Secuencias y colecciones vacías (veremos estos tipos en otros tutoriales): '', (), [], {}, set(), range(0)