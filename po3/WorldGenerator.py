from Antelope import Antelope
from CyberSheep import CyberSheep
from Dandelion import Dandelion
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Hogweed import Hogweed
from Nightshade import Nightshade
from Normal import Normal
from Sheep import Sheep
from Turtle import Turtle
from Wolf import Wolf
from Human import Human
import random

class WorldGenerator:
    def __init__(self):
        x = random.randint(10,20)
        y = random.randint(10,20)
        self.world = Normal(x,y)
        self.world.AddNewOrganism(Human(0,0,self.world))
        for s in range(20): 
            i = random.randint(0,x-1)
            j = random.randint(0,y-1)
            if self.world.GetOrganism(i,j) == None:
                match random.randint(0,10):
                    case 0:
                        self.world.AddNewOrganism(Sheep(i,j,self.world))
                    case 1:
                        self.world.AddNewOrganism(Wolf(i,j,self.world))
                    case 2:
                        self.world.AddNewOrganism(Fox(i,j,self.world))
                    case 3:
                        self.world.AddNewOrganism(Turtle(i,j,self.world))
                    case 4:
                        self.world.AddNewOrganism(Antelope(i,j,self.world))
                    case 5:
                        self.world.AddNewOrganism(CyberSheep(i,j,self.world))
                    case 6:
                        self.world.AddNewOrganism(Grass(i,j,self.world))
                    case 7:
                        self.world.AddNewOrganism(Dandelion(i,j,self.world))
                    case 8:
                        self.world.AddNewOrganism(Hogweed(i,j,self.world))
                    case 9:
                        self.world.AddNewOrganism(Nightshade(i,j,self.world))
                    case 10:
                        self.world.AddNewOrganism(Guarana(i,j,self.world))
        self.world.UpdateOrganisms()
    def GetWorld(self):
        return self.world
    def Add(self,name,x,y):
        match name:
            case "Sheep":
                self.world.AddNewOrganism(Sheep(x,y,self.world))
            case "Wolf":
                self.world.AddNewOrganism(Wolf(x,y,self.world))
            case "Fox":
                self.world.AddNewOrganism(Fox(x,y,self.world))
            case "Turtle":
                self.world.AddNewOrganism(Turtle(x,y,self.world))
            case "Antelope":
                self.world.AddNewOrganism(Antelope(x,y,self.world))
            case "CyberSheep":
                self.world.AddNewOrganism(CyberSheep(x,y,self.world))
            case "Grass":
                self.world.AddNewOrganism(Grass(x,y,self.world))
            case "Dandelion":
                self.world.AddNewOrganism(Dandelion(x,y,self.world))
            case "Hogweed":
                self.world.AddNewOrganism(Hogweed(x,y,self.world))
            case "Nightshade":
                self.world.AddNewOrganism(Nightshade(x,y,self.world))
            case "Guarana":
                self.world.AddNewOrganism(Guarana(x,y,self.world))
    def SetWorld(self, world):
        self.world = world
