En realidad, en Python existen dos clases para representar conjuntos: set y frozenset. La principal diferencia es que set es mutable, por lo que después de ser creado, se pueden añadir y/o eliminar elementos del conjunto, como veremos en secciones posteriores. Por su parte, frozenset es inmutable y su contenido no puede ser modificado una vez que ha sido inicializado.

Para crear un conjunto de tipo frozenset, se usa el constructor de la clase frozenset():

>>> f = frozenset([3, 5, 6, 1, 5])
>>> f
frozenset({1, 3, 5, 6})
🎯 NOTA: El único modo en Python de tener un conjunto de conjuntos es utilizando objetos de tipo frozenset como elementos del propio conjunto.
