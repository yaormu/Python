'''
Escribe un programa que imprima los números pares del 1 al 100.
'''
for num in range(0, 102, 2):
    print(num)

#Otra alternativa

for i in range(101):
    if i % 2 == 0:
        print(i)