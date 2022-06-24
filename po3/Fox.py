from Animal import Animal
import random

class Fox(Animal):
    def __init__(self, x, y,world):
        super().__init__(3,7,world,x,y)
    
    def GetSymbol(self):
        return 'F'
    
    def NewOrganism(self,x,y):
        return Fox(x,y,self.world)

    def GetColor(self):
        return "#ffd88a"
    def Name(self):
        return "Fox"
    def Action(self):
        self.SetOld()
        move = self.world.RandomMove(self.x,self.y,False)
        self.x += move.GetX()
        self.y += move.GetY()
        target = self.world.GetOrganism(self.x,self.y)
        if target != None and self.HasTargetHigherPower(target):
            self.Back()