##Laboratorio 9; leer un archivo csv con pandas y mostrarlo en matplotlib
##Miranda Coloma 4° Medio B
#Primero se importan las librerías a ocupar
import pandas as pd
import matplotlib.pyplot as plt
#Se establecen los parámetros del plot
plt.rcParams["figure.figsize"]=[20.00,4.00]
plt.rcParams["figure.autolayout"]=True
#Se establecen las columnas a utilizar en el plot
columns=['Fecha','CantidadClaveUnicasNuevas']
#Se lee el archivo csv con pandas
df=pd.read_csv('cu_mensual.csv', usecols=columns)
#Meter la información del archivo csv al plot
plt.plot(df.Fecha, df.CantidadClaveUnicasNuevas)
#Mostrar el plot
plt.show()