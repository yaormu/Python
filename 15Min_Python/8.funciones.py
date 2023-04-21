# El dato se pide por fuera de la funcion, y se
# imprimira 3 el resultado al invocarse

solicitud_estatura = int(input("Ingrese su estatura: "))

def mostraAltura(altura):
    
    if altura >= 180:
        print("Eres una persona alta")
    else:
        print("Eres una persona baja")

mostraAltura(solicitud_estatura)
mostraAltura(solicitud_estatura)
mostraAltura(solicitud_estatura)