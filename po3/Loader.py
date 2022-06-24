import pickle
from Normal import Normal

class Loader:
    def __init__(self,world):
        self.world = world
    def Save(self):
        with open("save.txt", "wb") as file:
            pickle.dump(self.world,file)
    def Load(self):
        with open("save.txt", "rb") as file:
            self.world=pickle.load(file)
        return self.world