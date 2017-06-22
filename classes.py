class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tile:
    def __init__(self, occupier = None):
        self.occupier = occupier

    def setPiece(self,piece):
        self.occupier = piece

    def __getitem__(self, key):
        if (isOccupied):
            if(key == 'c'):
                return self.occupier.color
            elif(key == 'x'):
                return self.occupier.position.x
            elif(key == 'y'):
                return self.occupier.position.y

    def removePiece():
        occupier = None

    def isOccupied():
        if (self.occupier == None):
            return False 
        else:
            return True
    
class Piece:
    def __init__(self,x ,y, c):
        position = Vector(x, y)
        self.color = c

    def __getitem__(self, key):
        if(key == 'c'):
            return self.color
        elif(key == 'x'):
            return self.position.x
        elif(key == 'y'):
            return self.position.y

    def __setitem__(self, key, value):
        if(key == 'c'):
            self.color = value
        elif(key == 'x'):
            self.position.x = value 
        elif(key == 'y'):
            self.position.y = value 

    def move(x,y):
        board[getattr(self,'x')][getattr(self,'y')].removePiece()
        setattr(self, 'x', x)
        setattr(self, 'y', y)
        board[x][y].setPiece(self)

    def canMove(x,y):
        if (board[x][y].isOccupied()):
            return False
        else:
            return True

    def eat(x,y):
        rise = x - getattr(self.position, 'x')
        run = y - getattr(self.position, 'y')
        if (canEat(x,y)):
            board[x][y].removePiece()
            move(getattr(self.position, 'x') + run, getattr(self.position, 'y') + rise)


    def canEat(x, y):
        if(board[x][y].isOccupied() and getattr(board[x][y].occupier, 'c') != getattr(self, 'c')):
            rise = x - getattr(self.position, 'x')
            run = y - getattr(self.position, 'y')
            if(not board[getattr(self.position, 'x') + run][getattr(self.position, 'y') + rise].isOccupied):
                return True 
        return False
            
