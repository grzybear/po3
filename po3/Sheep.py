from Animal import Animal

class Sheep(Animal):
    def __init__(self, x, y,world):
        super().__init__(4,4,world,x,y)
    
    def GetSymbol(self):
        return 'S'
    
    def NewOrganism(self,x,y):
        return Sheep(x,y,self.world)

    def GetColor(self):
        return "#e3e3de"
    def Name(self):
        return "Sheep"