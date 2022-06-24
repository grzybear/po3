from Animal import Animal
import random

class Antelope(Animal):
    def __init__(self, x, y,world):
        super().__init__(4,4,world,x,y)
    
    def GetSymbol(self):
        return 'A'
    
    def NewOrganism(self,x,y):
        return Antelope(x,y,self.world)

    def GetColor(self):
        return "#c7b89f"
    def Name(self):
        return "Antelope"
    def Collision(self, attacker):
        if type(attacker) == type(self):
            attacker.Back()
            attacker.NewAnimal()
        elif self.HasTargetLowerPower(attacker):
            attacker.Die(self)
        elif random.randint(0,1):
            move = self.world.RandomMove(self.x, self.y, True)
            if move.IsNone():
                self.Die(attacker)
            else:
                self.x+=move.GetX()
                self.y+=move.GetY()
                self.world.UpdateOrganisms()
                self.world.AddToLog(self.Name() + " fled from " + attacker.Name())
        else:
            self.Die(attacker)
    def Action(self):
        for i in range(2):
            super().Action()