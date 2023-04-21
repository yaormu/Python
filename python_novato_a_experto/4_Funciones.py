#definition function
def suma():
    print("Hola soy una suma")

suma()
suma()

#function with variable
def sumatoria(numero1, numero2):
    print("El resultado es: " + str(numero1 + numero2))

sumatoria(5, 10)


#function with return
def suma_numeros(numero1, numero2):
    return numero1 + numero2

resultado = suma_numeros(5, 25)
print(str(resultado))

#function subtraction
def resta(num1, num2):
    return num1 - num2

resultado_resta = resta(5, 10)
print(str(resultado_resta))

#function indicating parameter
def resta2(num1, num2):
    return num1 - num2

resultado_resta2 = resta(num2=5, num1=10)
print(str(resultado_resta2))

#function default values
def resta_defecto(num1=0, num2=0):
    return (num1 - num2)

result_res = resta_defecto()
print(str(result_res))

#function with indeterminate parameter
def variosNumeros(*numeros):
    for numero in numeros:
        print(str(numero))

variosNumeros(1,2,3,4,5)

#indeterminate parameter, sum of numbers
def sumar_varios_numeros(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

resultado_total = sumar_varios_numeros(1,2,3,4,5,6,7,8,9,0)
print(str(resultado_total))