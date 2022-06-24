from Plant import Plant

class Grass(Plant):
    def __init__(self,x,y,world):
        super().__init__(0,world,x,y)
    def GetSymbol(self):
        return ','
    
    def NewOrganism(self,x,y):
        return Grass(x,y,self.world)

    def GetColor(self):
        return "#cee8c1"
    def Name(self):
        return "Grass"