##Pregunta 1; empresa de videojuegos
##Miranda Coloma 4° Medio B
##Aclaración: las funciones o atributos tienen en su mayoría nombres en inglés porque generalmente al ser un
# idioma más compacto, resultan con nombres más cortos, pero todo es de mi invención (lo que es inferible 
# también por la simplicidad del código)

#declarar clase personaje
class Personaje:
    def __init__(self, name, attack_pwr, resistance, velocity, life):
        self.name=name
        self.attack_pwr=attack_pwr
        self.resistance=resistance
        self.velocity=velocity
        self.life=life
    #métodos
    def attack(self, oponent):
        oponent.life-=(self.attack_pwr/oponent.resistance)
        print(oponent.name,"ha perdido ", self.attack_pwr/oponent.resistance,"puntos de vida!")
        print("Ahora la vida de", oponent.name,"es",oponent.life)
        return " "
    def is_faster(self,oponent):
        if self.velocity>oponent.velocity:
            print(self.name,"es más rápido!")
        elif oponent.velocity>self.velocity:
            print(oponent.name,"es más rápido!")
        else:
            print("Tienen la misma velocidad!")
        return ""

#declarar personaje
Uno=Personaje("Uno", 200, 30, 40, 100)
Dos=Personaje("Dos",150, 70, 60, 100)
#probando las funciones
print(Dos.attack(Uno))
print(Uno.is_faster(Dos))