from PyQt5.QtGui import QGuiApplication
from Program import Program
import os, sys

class App:
    def __init__(self):
        self.qt_app = QGuiApplication(sys.argv)
        self.program = Program()
    def Go(self):
        self.program.Turn()
