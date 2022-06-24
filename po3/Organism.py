from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, power, initiative, world, x, y):
        self.power = power
        self.initiative = initiative
        self.world = world
        self.x = x
        self.y = y

    def UpdateCoordinates(self, move):
        self.x += move.x
        self.y += move.y
    def SetCoordinates(self,x,y):
        self.x = x
        self.y = y
    def Back(self):
        nothing = 0
    def IncreasePower(self,power):
        self.power += power
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def GetPower(self):
        return self.power
    def HasTargetHigherPower(self, target):
        return target.power > self.power
    def HasTargetLowerPower(self, target):
        return target.power < self.power
    def HasTargetLowerInitiative(self, target):
        return target.initiative < self.initiative
    def Die(self,killer):
        self.world.AddToLog(killer.Name() + " killed " + self.Name())
        self.world.DeleteOrganism(self)
    
    @abstractmethod
    def Action(self):pass
    @abstractmethod
    def Collision(self, attacker):pass
    @abstractmethod
    def GetSymbol(self):pass
    @abstractmethod
    def NewOrganism(self,x,y):pass
    @abstractmethod
    def Name(self):pass
    @abstractmethod
    def GetColor(self):pass