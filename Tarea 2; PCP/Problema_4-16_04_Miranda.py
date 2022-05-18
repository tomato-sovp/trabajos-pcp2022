##Problema 4.1
##Miranda Coloma 4° Medio B

#Primero se abre el archivo a editar y se crea un nuevo archivo que va a contener los nombres listados
#Aquí la versatilidad del código se encuentra en que solo es necesario cambiar el nombre del primer
#archivo para utilizarlo en cualquier caso de esta índole.
x=open("archivo.txt","r")
y=open("archivo-lista.txt","w+")
#Después se lee el archivo y se crea una lista vacía que contendrá las líneas del archivo
lines=x.readlines()
lista=[]
#Se usa un iterador para agregar las líneas a la lista
for linea in lines:
    lista.append(linea)
#Se cierra el primer archivo ya que no se volverá a ocupar
x.close()
#Se transforma la lista en un string para después poder separar sus elementos ahora sí individualmente
#dentro de la lista
z=",".join(lista)
lista=z.split()
#Se usa un iterador para escribir los elementos dentro del archivo nuevo con un salto de línea
for i in range(len(lista)):
    y.write(lista[i]+"\n")
#Se cierra el archivo
y.close()
