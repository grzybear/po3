from Direction import Direction

class Move:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __init__(self, d):
        self.x = 0
        self.y = 0
        match d:
            case Direction.Right:
                self.x = 1       
            case Direction.Down:
                self.y = 1
            case Direction.Left:
                self.x = -1
            case Direction.Up:
                self.y = -1
            case Direction.UpRight:
                self.x = 1
                self.y = -1
            case Direction.DownRight: 
                self.x = 1
                self.y = 1
            case Direction.DownLeft:
                self.x = -1
                self.y = 1
            case Direction.UpLeft:
                self.x = -1
                self.y = -1
    def GetX(self):
        return self.x
    def GetY(self):
        return self.y
    def IsNone(self):
        return self.x == 0 and self.y == 0