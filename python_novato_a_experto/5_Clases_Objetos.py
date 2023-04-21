class Cerveza:
    def __init__(self, nombre): #metodo
        self.nombre = nombre
    
    def fermentar(self):
        print("Cerveza añeja")
    
    def creada(self, fecha = 1900): #puede asignar valor al parametro
        print("Cerveza fabricada " + str(fecha) + " año")

mi_cerveza = Cerveza("Poker")

print(mi_cerveza.nombre)

mi_cerveza.fermentar()

mi_cerveza.creada()