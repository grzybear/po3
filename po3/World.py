from abc import ABC, abstractmethod
from Direction import Direction
from Log import Log

class World(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.log = Log()
        self.organisms = []
        self.newOrganisms = []
        self.map = [[None for _ in range(y)]for _ in range(x)]
        self.humanDirection = Direction.Steady

    def CalculateTurn(self):
        for organism in self.organisms:
            if organism != None:
                self.map[organism.GetX()][organism.GetY()] = None
                organism.Action()
                target = self.map[organism.GetX()][organism.GetY()]
                if target != None and target != organism:
                        target.Collision(organism)
                self.UpdateMap()
        self.UpdateOrganisms()
        #self.PrintMap()

    def PrintMap(self):
        for i in range(self.y):
            string = ""
            for j in range(self.x):
                if self.map[j][i] == None:
                    string += "_"
                else:
                    string += self.map[j][i].GetSymbol()
            print(string)
        print(len(self.organisms)+len(self.newOrganisms))

    def GetOrganism(self,x,y):
        if x<0 or y < 0 or x>=self.x or y>=self.y :
             return None
        else:
            return self.map[x][y]

    def AddNewOrganism(self,organism):
        if self.map[organism.GetX()][organism.GetY()] != None:
            return
        else:
            self.newOrganisms.append(organism)
            self.map[organism.GetX()][organism.GetY()] = organism

    def DeleteOrganism(self,organism):
        endFlag = True
        i = 0
        while i < self.x and endFlag:
            for j in range(self.y):
                if self.map[i][j] == organism:
                    endFlag = False
                    self.map[i][j] = None
                    break
            i+=1
        if organism in self.organisms:
            i = self.organisms.index(organism)
            self.organisms[i] = None
        elif organism in self.newOrganisms:
            i = self.newOrganisms.index(organism)
            self.newOrganisms[i] = None

    def UpdateMap(self):
        for i in range(self.x):
            for j in range(self.y):
                self.map[i][j] = None
        for organism in self.organisms:
            if organism != None:
                if self.map[organism.GetX()][organism.GetY()] == None:
                    self.map[organism.GetX()][organism.GetY()] = organism
        for organism in self.newOrganisms:
            if organism != None:
                if self.map[organism.GetX()][organism.GetY()] == None:
                    self.map[organism.GetX()][organism.GetY()] = organism

    def UpdateOrganisms(self):
        for organism in self.organisms:
            if organism == None:
                self.organisms.remove(organism)
        for organism in self.newOrganisms:
            if organism == None:
                self.newOrganisms.remove(organism)
        while len(self.newOrganisms) > 0:
            self.AddOrganismToMainList(self.newOrganisms[0])
            del self.newOrganisms[0]
    def AddOrganismToMainList(self, newOrganism):
        if newOrganism == None:
            return False
        for organism in self.organisms:
            if organism != None and newOrganism.HasTargetLowerInitiative(organism):
                i = self.organisms.index(organism)
                self.organisms.insert(i, newOrganism)
                return True
        organism = self.organisms.append(newOrganism)
        return False
    def InRange(self, x,y):
        return x >=0 and x < self.x and y >=0 and y < self.y
    def Empty(self,x,y):
        return self.map[x][y] == None
    def GetColor(self,x,y):
        if(self.map[x][y] == None):
            return "#192119"
        else: 
            return self.map[x][y].GetColor()
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def GetHumanDirection(self):
        dir = self.humanDirection
        self.humanDirection = Direction.Steady
        return dir
    def AddToLog(self,string):
        self.log.Add(string)
    def ClearLog(self):
        self.log.Clear()
    def GetLog(self):
        return self.log.GetLog()
    def SetHumanDirection(self, direction):
        self.humanDirection = direction
    

    @abstractmethod
    def RandomMove(self,x,y,empty):pass