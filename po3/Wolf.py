from Animal import Animal

class Wolf(Animal):
    def __init__(self, x, y,world):
        super().__init__(9,5,world,x,y)
    
    def GetSymbol(self):
        return 'W'
    
    def NewOrganism(self,x,y):
        return Wolf(x,y,self.world)

    def GetColor(self):
        return "#a19193"
    def Name(self):
        return "Wolf"