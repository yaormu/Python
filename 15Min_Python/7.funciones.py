# funciones
# Solicitara 3 veces los datos y se imprimira los resultados

def mostraAltura():
    altura = int(input("Ingrese su estatura: "))

    if altura >= 180:
        print("Eres una persona alta")
    else:
        print("Eres una persona baja")

mostraAltura()
mostraAltura()
mostraAltura()
