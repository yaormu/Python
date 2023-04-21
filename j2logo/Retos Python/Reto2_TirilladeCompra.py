'''

El Centro Comercial Unaleño continúa trabajando en la creación de un carrito de compras. 



Para esto se requiere la creación de varias tareas que deben programarse en funciones detalladas a continuación:



Lectura de n artículos



-Se requiere leer una cantidad n de artículos que representan la compra de un cliente.


-Un artículo por ahora lleva nombre y precio.


-Esta función debe retornar la tirilla de compras en texto




# Cálculo de descuento



Dado el valor total de la compra se pretende realizar una nueva campaña titulada 
compra más 
y gasta menos con los siguientes descuentos:


-Por compras mayores a 150000 lleva un 10% de descuento.

-Por compras mayores a 300000 lleva un 15% de descuento.

-Por compras mayores a 700000 lleva un 20% de descuento.



Dadas las dos funcionalidades anteriores ayude al centro comercial a generar una tirilla de compra
donde se muestren los productos comprados, el valor a pagar y el descuento que se le hizo al cliente.


Entrada: 
Diferentes datos en el siguiente orden:

-La cantidad de artículos en el carrito

-El nombre y el precio de cada artículo en una línea diferente



Salida: 
Se debe mostrar lo siguiente:
-La tirilla de compra en el formato especificado



Nota: 
Como el centro comercial está siendo muy generoso con los descuentos, el valor a cobrar en caso de tener centavos
se debe aproximar a techo usando la función ceil de python

(https://www.tutorialspoint.com/python/number_ceil.htm)



Ejemplo 1:

Entrada				Salida

3				Centro Comercial Unaleño

Chocolatinas Cohete		Compra más y Gasta Menos

300				NIT: 899.999.063

Mora				Chocolatinas Cohete $300

1000				Mora $1000

Pan de Maiz			Pan de Maiz $300

300				Total: $1600
			
				En esta compra tu descuento fue $0
				    
				Gracias por tu compra



Ejemplo 2:

Entrada				Salida

2				Centro Comercial Unaleño

Televisor			Compra más y Gasta Menos

1500000			    	NIT: 899.999.063

Teatro en Casa			Televisor $1500000

450000				Teatro en Casa $450000
				    
				Total: $1560000
				    				
				En esta compra tu descuento fue $390000
				    
				Gracias por tu compra

'''

cantidad_Productos = 0

nombre_Producto = str(input("Digite nombre del producto: "))

Costo_Producto = int(input("Digite costo unitario del producto: "))

if valorComprar > 150000
    

def compra(producto, valor)
    if valorCompar>150000
    valorTotal=(v15000*0.10)