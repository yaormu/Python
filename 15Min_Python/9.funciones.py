#veremos que toda la operacion se realice dentro de la funcion

solicitud_estatura = int(input("Ingrese su estatura: "))

def mostraAltura(altura):

    resultado = ""
    
    if altura >= 180:
        resultado = "Eres una persona alta"
    else:
        resultado = "Eres una persona baja"

    return resultado

print(mostraAltura(solicitud_estatura))