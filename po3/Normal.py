from World import World
from Direction import Direction
from Move import Move
import random

class Normal(World):
    def __init__(self,x,y):
        super().__init__(x,y)
    def RandomMove(self,x,y,empty):
        possibleDirections = 4
        directions = [True,True,True,True]
        if y<=0 or (empty and self.map[x][y-1]!=None):
            possibleDirections-=1
            directions[Direction.Up] = False
        if x>=self.x - 1 or (empty and self.map[x+1][y]!=None):
            possibleDirections-=1
            directions[Direction.Right] = False
        if y>=self.y-1 or (empty and self.map[x][y+1]!=None):
            possibleDirections-=1
            directions[Direction.Down] = False
        if x<=0 or (empty and self.map[x-1][y]!=None):
            possibleDirections-=1
            directions[Direction.Left] = False
        if possibleDirections==0:
            return Move(Direction.Steady)
        position = random.randint(0,possibleDirections-1)
        i=0
        while i <= position:
            if i>=4:
                return Move(Direction.Steady)
            if not directions[i]:
                position+=1
            i+=1
        return Move(position)
    