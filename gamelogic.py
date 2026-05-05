





class Kakuro:
    def __init__(self, x, y, default_value=0):
        self.x = x
        self.y = y
        self.contentx = [[default_value for _ in range(y)] for _ in range(x)]
        self.contenty = [[default_value for _ in range(y)] for _ in range(x)]

    def bfill(Kakuro):
        for i in range(Kakuro.x):
            Kakuro.contentx[i][0] = "B"
            Kakuro.contenty[i][0] = "B"  
        for j in range(Kakuro.y):
            Kakuro.contentx[0][j] = "B"
            Kakuro.contenty[0][j] = "B"     
  
         
  

   
    
    def getrowvalue(k, direction, x, y):
        if k.contentx[x][y]==0 and k.contenty[x][y] == 0:
            if direction == "right":
                while k.contentx[x][y] == 0 and k.contenty[x][y] == 0:
                    x -= 1 
                return k.contentx[x][y]
            if direction == "down":
                while k.contentx[x][y] == 0 and k.contenty[x][y] == 0:
                    y -= 1 
                return k.contentx[x][y]
            
    def layout(self):
        #für ein Viertel des Kakuros ein nicht abgeschlossenes Muster generieren dann zweimal spiegeln um das ganze Feld zu füllen (Symmetrie ist cool)
        xwidth = len(self.contentx)/2
        yhight = len(self.contenty)/2
        for i in range(xwidth):
            None

    def getrowlength(k ,direction , x, y):
        length = 0
        if x > k.x - 1:
            return "Out of bounds"
        if y > k.y - 1:
            return "Out of bounds"
            
        if direction == "right" and k.contentx[x][y] == 0 and k.contenty[x][y] == 0:
            while k.contentx[x-1][y] == 0 and k.contenty[x-1][y] == 0:
                x -= 1
                print("step left")
            for i in range(k.x - x):
                if k.contentx[x+i][y] == 0 and k.contenty[x+i][y] == 0:
                    length += 1
                else:
                    break


        elif direction == "down" and k.contenty[x][y] == 0 and k.contentx[x][y] == 0:
            while k.contenty[x][y-1] == 0 and k.contentx[x-1][y] == 0:
                y -= 1
                print("step up")
            for i in range(k.y - y):
                if k.contenty[x][y+i] == 0 and k.contentx[x][y+i] == 0:
                    length += 1
                else:
                    break

        return length
    def bsp(k):
        k.contentx[0][1] = 13
        k.contentx[0][2] = 10
        k.contentx[1][3] = 10
        k.contentx[2][4] = 26
        k.contentx[0][4] = "B"
        k.contentx[0][5] = 43
        k.contentx[0][6] = 15
        k.contentx[1][7] = 8
        k.contentx[0][8] = 8
        k.contentx[0][9] = 14
        k.contentx[5][1] = 6
        k.contentx[5][2] = 24
        k.contentx[5][3] = 17
        k.contentx[6][6] = 8
        k.contentx[5][7] = 14
        k.contentx[5][8] = 23
        k.contentx[5][9] = 6
        k.contentx[4][1] = "B"
        k.contentx[4][2] = "B"
        k.contentx[8][3] = "B"

        k.contenty[1][0] = 5
        k.contenty[2][0] = 12
        k.contenty[3][1] = 27
        k.contenty[6][0] = 32
        k.contenty[7][0] = 17
        k.contenty[8][0] = 11
        k.contenty[4][3] = 4
        k.contenty[5][3] = 17
        k.contenty[1][4] = 12
        k.contenty[2][4] = 35
        k.contenty[1][7] = 3
        k.contenty[3][6] = 6
        k.contenty[8][7] = 7
        k.contenty[8][4] = 5
        k.contenty[7][4] = 32
        k.contenty[6][6] = 20
        k.contenty[4][6] = "B"
        k.contenty[5][6] = "B"
        k.contenty[4][7] = "B"
        k.contenty[4][8] = "B"
        k.contenty[4][9] = "B"
        

    #https://stackoverflow.com/questions/61448326/generate-a-dictionary-of-all-possible-kakuro-solutions
        
#k = Kakuro(10,10)
#k.bfill()
#print(k.getrowlength("down",5,2))
#print(k.contentx)