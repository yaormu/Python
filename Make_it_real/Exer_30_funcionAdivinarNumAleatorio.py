'''
Escribe un programa que piense un número de 1 a 10 de forma aleatoria y le pida al usuario que lo trate de adivinar. El usuario puede intentar indefinidamente hasta que encuentre el número.

Un ejemplo de la ejecución del programa podría ser el siguiente, asumiendo que el número es 2:

Adivina el número: 5
Fallaste!

Adivina el número: 2
Felicitaciones, lo encontraste!
'''

import random

def adivinar() :
  numero = random.randint(1, 10)
  while True :
    adivina = int(input("Adivina el número : "))
    if numero == adivina : 
      print("Felicitaciones, lo encontraste!")
      break
    print("Fallaste!")

print("Adivina el número entre 1 y 10")
adivinar()

'''
#OTRA FORMA
import random

numero = int(input("Adivina el número: "))

while numero != random.randrange(1, 10):
    print("Fallaste!")
    numero = int(input("Adivina el número: "))
print("Felicitaciones, lo encontraste!")
'''