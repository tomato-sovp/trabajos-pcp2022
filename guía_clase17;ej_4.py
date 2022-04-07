##Juego dado
import random
num_dado=random.randint(1,6)
num_jugador=int(input("Adivine el número obtenido en un lanzamiento de un dado de 6 caras: "))
print("El número obtenido en el lanzamiento fue: ",num_dado)
if num_jugador==num_dado:
    print("¡Felicidades! Adivinó correctamente")
else:
    print("Lamentablemente su adivinanza fue incorrecta")
