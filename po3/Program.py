from PyQt5.QtCore import *
from PyQt5.QtQml import *
from Send import Send
from Get import Get
from WorldGenerator import WorldGenerator
from Loader import Loader
import os, time

class Program(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.generator = WorldGenerator()
        self.world = self.generator.GetWorld()
        self.loader = Loader(self.world)
        self.engine = None
        self.CreateEngine()
        self.send.SetGridSize()
        self.send.SetGrid()
    def CreateEngine(self):
        self.engine = QQmlApplicationEngine()
        self.engine.load("main.qml")
        self.SetContext()
    def SetContext(self):
        self.get = Get(self)
        self.send = Send(self)
        context = self.engine.rootContext()
        #context.setContextProperty("upload", self.upload)
        context.setContextProperty("Get", self.get)
    def Turn(self):
        self.world.CalculateTurn()
        self.send.SetGrid()
        self.send.AddLog()
    def Save(self):
        self.loader.Save()
    def Load(self):
        self.world = self.loader.Load()
        self.generator.SetWorld(self.world)
        self.send.SetGridSize()
        self.Turn()