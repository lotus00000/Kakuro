# Checklist:
    # Speicherformat Kakuro
    # Brute Force solver
class Kakuro:
    def __init__(self, x, y, difficulty, default_value=0):
        self.x = x
        self.y = y
        self.difficulty = difficulty
        self.contentx = [[default_value for _ in range(x)] for _ in range(y)]
        self.contenty = [[default_value for _ in range(x)] for _ in range(y)]
    def bfill(Kakuro):
        for i in range(Kakuro.x):
            Kakuro.contentx[i][0] = "B"
        for j in range(Kakuro.y):
            Kakuro.contentx[0][j] = "B"   
    #xplane    
        for i in range(Kakuro.x):
            Kakuro.contenty[i][0] = "B"
        for j in range(Kakuro.y):
            Kakuro.contenty[0][j] = "B"  
    #yplane
    def getrowlength(direction, x, y):
        if(direction=="right"):
            None
            #längezähler rechts mit forschleife
        if(direction=="down"):
            None
            #längezähler down mit forschleife
        

