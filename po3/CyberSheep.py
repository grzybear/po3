from Animal import Animal
import random

class CyberSheep(Animal):
    def __init__(self, x, y,world):
        super().__init__(11,4,world,x,y)
    
    def GetSymbol(self):
        return 'C'
    
    def NewOrganism(self,x,y):
        return CyberSheep(x,y,self.world)

    def GetColor(self):
        return "#000000"
    def Name(self):
        return "CyberSheep"
        
    def Action(self):
        x = -1
        y = -1
        min = self.world.GetX() + self.world.GetY()
        for i in range(self.world.GetX()):
            for j in range(self.world.GetY()):
                organism = self.world.GetOrganism(i,j)
                if organism != None and organism.Name() == "Hogweed":
                    d = self.GetDistance(i,j)
                    if d < min:
                        min = d
                        x = i
                        y = j
        if x != -1:
            if x > self.x:
                self.x += 1
            elif x < self.x:
                self.x -= 1
            elif y > self.y:
                self.y += 1
            elif y < self.y:
                self.y -= 1
        else:
            super().Action()
                
                    
    def Die(self,killer):
        if killer.Name() != "Hogweed":
            super().Die(killer)
        else:
            self.world.AddToLog(killer.Name() + " tried to kill " + self.Name())
    def GetDistance(self,x,y):
        return abs(self.x - x) + abs(self.y - y)