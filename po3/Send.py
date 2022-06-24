from PyQt5.QtCore import pyqtSlot, QObject, QModelIndex

class Send(QObject):
    def __init__(self, program):
        QObject.__init__(self)
        self.program = program
        self.context = self.program.engine.rootObjects()[0]
    def myPrint(self):
        print(dir(self.context.getElement("mapModel")))
    def SetGridSize(self):
        world = self.program.world
        self.context.getElement("grid").setProperty("rows", world.GetY())
        self.context.getElement("grid").setProperty("columns", world.GetX())
    def SetGrid(self):
        world = self.program.world
        rect = []
        for i in range(world.GetY()):
            for j in range(world.GetX()):
                rect.append({
                    "width" : 30,
                    "height" : 30,
                    "color" : world.GetColor(j,i)
                })
        self.context.clearList()
        self.context.addToList(rect)
    def AddLog(self):
        world = self.program.world
        log = world.GetLog()
        for string in log:
            self.context.addToLog({
                "text" : string
            })
        world.ClearLog()
