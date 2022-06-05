##Laboratorio 6
##Miranda Coloma 4° Medio B
#Creación de clase personaje para un videojuego
class Player:
    #construir la clase con los atributos requeridos
    def __init__(self, name, attack_pwr, resistance, velocity, life=100):
        self.name=name
        self.attack_pwr=attack_pwr
        self.resistance=resistance
        self.velocity=velocity
        self.life=life
    #hacer el método de ataque con el parámetro establecido
    def attack(self, oponent):
        daño=self.attack_pwr/oponent.resistance
        oponent.life-=daño
        print(oponent.name, "ha perdido", daño, "puntos de vida!\nAhora su vida es", oponent.life)
        return ""
    #hacer el método para ver cuál de los dos personajes es más rápido
    def is_faster(self, oponent):
        if self.velocity>oponent.velocity:
            print(self.name, "es más rápido!")
        elif oponent.velocity>self.velocity:
            print(oponent.name, "es más rápido!")
        else:
            print("Ambos tienen la misma velocidad!")
        return ""
#declarar objetos de la clase para probar el código
Grinch=Player("Grinch",30,70,20)
Gato=Player("Gato",40,50,40)
#probar métodos
print(Grinch.attack(Gato))
print(Gato.is_faster(Grinch))