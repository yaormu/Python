# variables

texto = "Datos de variable"
nombre = "Yamid Ortiz"
altura = "187cm"
year = 2020

# Primer forma de contatenar
# Se convierte en string la variable year ya que es un entero
print(f"{texto} - {nombre} - {altura} - {str(year)}")

# Otra forma de contatenar
print(texto + " - " + nombre + " - " + altura + " - " + str(year))   