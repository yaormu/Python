#open crea archivo
#w+ sobreescribe
#open("miarchivo.txt","w+")

#Crear, escribir y cerrar
f=open("miarchivo.txt","w+")
f.write("escribir en archivo")
#adicionar texto
f=open("miarchivo.txt","a+")
f.write(" adionamos mas texto")
f.close();

#mostrar el texto del archivo
#r solo lectura
f=open("miarchivo.txt","r")
contenido = f.read()
print(contenido)