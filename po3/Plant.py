from Organism import Organism
from World import World
import random

class Plant(Organism):
    def __init__(self, power, world, x, y):
        super().__init__(power, 1, world, x, y)
        self.growthChance = 10
    def Action(self):
        rand = random.randint(0,10)
        if rand == 0:
            cMove = self.world.RandomMove(self.x, self.y, True)
            if not cMove.IsNone():
                cX = self.x + cMove.GetX()
                cY = self.y + cMove.GetY()
                self.world.AddNewOrganism(self.NewOrganism(cX, cY))
    def Collision(self,attacker):
        self.Die(attacker)
    def Die(self,killer):
        self.world.AddToLog(killer.Name() + " ate " + self.Name())
        self.world.DeleteOrganism(self)
    