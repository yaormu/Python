Representación de un objeto como cadena
Una singularidad de la clase str es que a su constructor se le puede pasar cualquier objeto. Al hacer esto, la función str() devuelve la representación en forma de cadena de caracteres del propio objeto (si se pasa un string devuelve el string en sí).

Normalmente, al llamar a la función str(objeto) lo que se hace internamente es llamar al método __str__() del objeto. Si este método no existe, entonces devuelve el resultado de invocar a repr(objeto).