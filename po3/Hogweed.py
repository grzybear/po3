from Plant import Plant

class Hogweed(Plant):
    def __init__(self,x,y,world):
        super().__init__(10,world,x,y)
    def GetSymbol(self):
        return '#'
    
    def NewOrganism(self,x,y):
        return Hogweed(x,y,self.world)

    def GetColor(self):
        return "#9dad7b"
    def Name(self):
        return "Hogweed"
    def Collision(self,attacker):
        attacker.Die(self)
        self.Die(attacker)
    def Kill(self,x,y):
        target = self.world.GetOrganism(x,y)
        if target != None and not issubclass(type(target),Plant):
            target.Die(self)
    def Action(self):
        self.Kill(self.x+1, self.y)
        self.Kill(self.x, self.y+1)
        self.Kill(self.x-1, self.y)
        self.Kill(self.x, self.y-1)
        super().Action()