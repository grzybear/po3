from Plant import Plant

class Dandelion(Plant):
    def __init__(self,x,y,world):
        super().__init__(0,world,x,y)
    def GetSymbol(self):
        return '*'
    
    def NewOrganism(self,x,y):
        return Dandelion(x,y,self.world)

    def GetColor(self):
        return "#dff5f5"
    def Name(self):
        return "Dandelion"
    def Action(self):
        for i in range(3):
            super().Action()