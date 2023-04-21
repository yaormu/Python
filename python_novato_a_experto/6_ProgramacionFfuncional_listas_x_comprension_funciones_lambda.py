#El uso range hasta el valor que quermos llegar
lista = range(5)

for numeros in lista:
    print(str(numeros))
    
    
#Lista por comprensión
listaMultiplicadaPor1000 = [i * 1000 for i in range(10)]
print(listaMultiplicadaPor1000)

multiplicadoPorElMismoNumero = [i * i for i in range(10)]
print(multiplicadoPorElMismoNumero)

multiplicacionporelmismoyposicion = [(i,i * i) for i in range(10)]
print(multiplicacionporelmismoyposicion)

#funcion lambda
multiplica = lambda num1,num2: num1*num2

resultado = multiplica(2, 8)
print(resultado)