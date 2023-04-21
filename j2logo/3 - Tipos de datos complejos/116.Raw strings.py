"""
En relación con la sección anterior, puede haber ocasiones en que se quiera usar el carácter \ pero sin ser utilizado como carácter de escape. Para ello, se puede hacer uso de las raw strings. Una cadena de este tipo comienza anteponiendo el carácter r a las comillas (simples o dobles).
"""

# Aquí, \n es interpretado como nueva línea
>>> s = 'C:\python\noticias'
>>> print(s)
C:\python
oticias

# En una raw string no se interpreta el carácter \
>>> s = r'C:\python\noticias'
>>> print(s)
C:\python\noticias