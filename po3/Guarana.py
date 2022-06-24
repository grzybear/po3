from Plant import Plant

class Guarana(Plant):
    def __init__(self,x,y,world):
        super().__init__(0,world,x,y)
    def GetSymbol(self):
        return ':'
    
    def NewOrganism(self,x,y):
        return Guarana(x,y,self.world)

    def GetColor(self):
        return "#e8c3c6"
    def Name(self):
        return "Guarana"
    def Collision(self,attacker):
        attacker.IncreasePower(5)
        self.Die(attacker)