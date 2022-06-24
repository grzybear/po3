from Plant import Plant

class Nightshade(Plant):
    def __init__(self,x,y,world):
        super().__init__(99,world,x,y)
    def GetSymbol(self):
        return ':'
    
    def NewOrganism(self,x,y):
        return Nightshade(x,y,self.world)

    def GetColor(self):
        return "#a7a1d4"    
    def Name(self):
        return "Nightshade"
    def Collision(self,attacker):
        attacker.Die(self)
        self.Die(attacker)