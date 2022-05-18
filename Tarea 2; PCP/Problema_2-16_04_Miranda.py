##Mutación Melmac
##Miranda Coloma 4° Medio B
#Definir la clase con atributos nombre y adn
class Persona:
    def __init__(self,name,adn):
        self.name=name
        self.adn=adn
    #definir método para identificar si el adn está mutado (True o False)
    def is_mut(self,adn):
        print("ADN: ",self.adn)
        nukes=list(adn)
        mut=0
        pregunta=0
        for j in range(len(nukes)):
            if nukes[j-1]==nukes[j] or len(nukes)<20:
                mut+=1
            else:
                mut+=0
        if mut>0:
            pregunta=True
        else:
            pregunta=False
        return pregunta


Esteban=Persona("Esteban","ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(Esteban.is_mut(Esteban.adn))