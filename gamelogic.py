# Checklist:
    # Speicherformat Kakuro
    # Brute Force solver
class Kakuro:
    def __init__(self, x, y, default_value=0):
        self.x = x
        self.y = y
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

    def getrowlength(self ,direction , x, y):
        length = 0
        if(direction == "right"):
            for i in range(len(self.contentx)-x):
                if(self.contentx[i+x][y] == 0):
                    length = length + 1
                else:
                    break
            #längezähler rechts mit forloop

        if(direction == "down"):
            for j in range(len(self.contenty[0])-y):
                if(self.contentx[x][j+y] == 0):
                    length = length + 1
                else:
                    break
            #längezähler down mit forloop

        return length
        
k = Kakuro(10,10)
k.bfill()
print(k.getrowlength("down",5,2))
print(k.contentx)