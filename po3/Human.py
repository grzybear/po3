from Animal import Animal
from Direction import Direction
from Move import Move
import random

class Human(Animal):
    def __init__(self, x, y,world):
        super().__init__(5,4,world,x,y)
        self.cooldown = 0
    
    def GetSymbol(self):
        return 'H'
    
    def NewOrganism(self,x,y):
        return Human(x,y,self.world)

    def GetColor(self):
        if self.cooldown >= 5: return "red"
        return "yellow"
    def Name(self):
        return "Human"
    def Collision(self, attacker):
        if self.cooldown < 5:
            super().Collision(attacker)
        else:
            if self.HasTargetLowerPower(attacker):
                attacker.Die(self)
            else:
                attacker.Back()
    def Action(self):
        dir = self.world.GetHumanDirection()
        print(dir)
        if dir == Direction.Ability and self.cooldown<=0:
            self.cooldown = 10
            self.world.AddToLog(self.Name() + " used ability")
        else:
            self.SetOld()
            move = Move(dir)
            self.x += move.GetX()
            self.y += move.GetY()
            if self.x < 0 or self.y < 0 or self.x >= self.world.GetX() or self.y >= self.world.GetY():
                self.Back()
            self.cooldown -= 1
    