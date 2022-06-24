from PyQt5.QtCore import pyqtSlot, QObject
from Direction import Direction

class Get(QObject):
    def __init__(self, program):
        QObject.__init__(self)
        self.program = program
    @pyqtSlot(str)
    def PrintRectangleAlbocos(self, rect):
        print(rect)
    @pyqtSlot()
    def Next(self):
        self.program.Turn()
    @pyqtSlot(int,str)
    def NewOrganism(self,index,name):
        if index < 0 : return
        world = self.program.world
        x = index % world.GetX()
        y = int(index / world.GetX())
        if world.GetOrganism(x,y)!=None: return
        self.program.generator.Add(name,x,y)
        self.program.send.SetGrid()
    @pyqtSlot(str)
    def HumanDir(self, string):
        direction = Direction.Steady
        match string:
            case "Up":
                direction = Direction.Up
            case "Down":
                direction = Direction.Down
            case "Left":
                direction = Direction.Left
            case "Right":
                direction = Direction.Right
            case "Ability":
                direction = Direction.Ability
        print(direction)
        self.program.world.SetHumanDirection(direction)
        self.program.Turn()
    @pyqtSlot()
    def Save(self):
        self.program.Save()
    
    @pyqtSlot()
    def Load(self):
        self.program.Load()