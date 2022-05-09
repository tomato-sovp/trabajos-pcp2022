##Problema 2; rotación e inversión imagen
##Miranda Coloma 4° Medio B
#declarar la imagen
imagen=[
    [[58,23,125],[150,255,0],[0,0,0],[14,0,99]],
    [[0,0,200],[34,25,0],[0,65,0],[8,0,45]],
    [[58,0,1],[70,25,0],[0,80,165],[255,255,255]]
    ]
#función para invertir la imagen
def invertir_img(imagen):
    #iterar en el primer nivel de la lista
    for j in range(len(imagen)):
        #iterar en el segundo nivel de la lista
        for i in range(len(imagen[0])):
            #iterar en el tercer nivel de la lista
            for k in range(len(imagen[0][0])):
                #invertir la imagen
                imagen[j][i][k]=255-imagen[j][i][k]
    return (imagen)
#función para rotar la imagen (de 4x3, no sirve para otros tamaños) en 90° grados
def rotar_img(imagen):
    #lista vacía donde estará finalmente la imagen rotada
    img_rotada=[]
    #para convertir las columnas en filas
    contador_a=2
    nivel1=[]
    nivel2=[]
    nivel3=[]
    nivel4=[]
    while contador_a>=0:
        nivel1.append(imagen[contador_a][0])
        nivel2.append(imagen[contador_a][1])
        nivel3.append(imagen[contador_a][2])
        nivel4.append(imagen[contador_a][3])
        contador_a-=1
    #para agregar todas las filas a la matriz
    img_rotada.append(nivel1);img_rotada.append(nivel2)
    img_rotada.append(nivel3);img_rotada.append(nivel4)
    return(img_rotada)
#probando el funcionamiento adecuado de las funciones
print(rotar_img(imagen))
print(invertir_img(imagen))
                
        
