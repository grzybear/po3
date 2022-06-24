from Animal import Animal
import random

class Turtle(Animal):
    def __init__(self, x, y,world):
        super().__init__(2,1,world,x,y)
    
    def GetSymbol(self):
        return 'T'
    
    def NewOrganism(self,x,y):
        return Turtle(x,y,self.world)

    def GetColor(self):
        return "#b6f0bc"
    def Name(self):
        return "Turtle"
    def Collision(self, attacker):
        if type(attacker) == type(self):
            attacker.Back()
            attacker.NewAnimal()
        elif self.HasTargetLowerPower(attacker):
            attacker.Die(self)
        elif attacker.GetPower() < 5:
            attacker.Back()
            self.world.AddToLog(self.Name() + " protected itself from " + attacker.Name())
        else:
            self.Die(attacker)
    def Action(self):
        if random.randint(0,3) == 0:
            super().Action()