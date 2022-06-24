from Organism import Organism
from World import World

class Animal(Organism):
    def __init__(self, power, initiative, world, x, y):
        super().__init__(power, initiative, world, x, y)
        self.SetOld()
    
    def SetOld(self):
        self.oldX = self.x
        self.oldY = self.y
    
    def Back(self):
        self.x = self.oldX
        self.y = self.oldY
    
    def Action(self):
        self.SetOld()
        move = self.world.RandomMove(self.x,self.y,False)
        self.x += move.GetX()
        self.y += move.GetY()
    
    def Collision(self,attacker):
        if type(attacker) == type(self):
            attacker.Back()
            attacker.NewAnimal()
        elif self.HasTargetLowerPower(attacker):
            attacker.Die(self)
        else:
            self.Die(attacker)
    def NewAnimal(self):
        cMove = self.world.RandomMove(self.x, self.y, True)
        if not cMove.IsNone():
            cX = self.x + cMove.GetX()
            cY = self.y + cMove.GetY()
            self.world.AddNewOrganism(self.NewOrganism(cX,cY))