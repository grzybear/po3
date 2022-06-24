
class Log:
    def __init__(self):
        self.log = []
    def Add(self,string):
        self.log.append(string)
    def GetLog(self):
        return self.log
    def Clear(self):
        self.log = []