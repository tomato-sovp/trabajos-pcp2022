##Problema 1 Project Euler
##Miranda Coloma 4° Medio B
contador=0
for i in range(0,1000):
    if i//3==i/3 or i//5==i/5:
        contador+=i
print(contador)