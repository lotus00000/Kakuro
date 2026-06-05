from itertools import combinations
import copy
import random
import math



def build_table():
        table = {}
        digits = range(1, 10)

        for length in range(2, 10):
            for combo in combinations(digits, length):
                s = sum(combo)
                key = (length, s)
                table.setdefault(key, []).append(set(combo))

        return table

class Kakuro:
    
    def __init__(self, x, y, nodeslimit = 30, min_puzzlesize = 15, seedlength = 4,internalnodelimit = 3, default_value=0):
        self.x = x
        self.y = y
        self.internalnodelimit = internalnodelimit
        self.nodeslimit = nodeslimit
        self.min_puzzlesize = min_puzzlesize
        self.seedlength = seedlength*2
        self.contentx = [[default_value for _ in range(y)] for _ in range(x)]
        self.contenty = [[default_value for _ in range(y)] for _ in range(x)]
        self.answers = [[default_value for _ in range(y)] for _ in range(x)]
        

    def bfill(Kakuro):
        for i in range(Kakuro.x):
            for j in range(Kakuro.y):
                Kakuro.contentx[i][j] = "B"
                Kakuro.contenty[i][j] = "B"  
    def bfill2(Kakuro):
        
        for j in range(Kakuro.y):
            Kakuro.contentx[0][j] = "B"
            Kakuro.contenty[0][j] = "B"    
        for i in range(Kakuro.x):       
            Kakuro.contentx[i][0] = "B"
            Kakuro.contenty[i][0] = "B"
             
    def getrowvalue(k, direction, x, y):
        if k.contentx[x][y]==0 and k.contenty[x][y] == 0:
            if direction == "right":
                while x>0 and k.contentx[x][y] == 0 and k.contenty[x][y] == 0:
                    x -= 1 
                if k.contentx[x][y]=="B":return 0 
                return k.contentx[x][y] 
            if direction == "down":
                while y>0 and k.contentx[x][y] == 0 and k.contenty[x][y] == 0:
                    y -= 1
                if k.contenty[x][y]=="B":return 0 
                return k.contenty[x][y]    
            
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
            while x>0 and k.contentx[x-1][y] == 0 and k.contenty[x-1][y] == 0:
                x -= 1
                #print("step left")
            for i in range(k.x - x):
                if k.contentx[x+i][y] == 0 and k.contenty[x+i][y] == 0:
                    length += 1
                else:
                    break


        elif direction == "down" and k.contenty[x][y] == 0 and k.contentx[x][y] == 0:
            while y>0 and k.contenty[x][y-1] == 0 and k.contentx[x][y-1] == 0:
                y -= 1
                #print("step up")
            for i in range(k.y - y):
                if k.contenty[x][y+i] == 0 and k.contentx[x][y+i] == 0:
                    length += 1
                else:
                    break

        return length
    
    

    
    def refine(k, x, y, table):
        
        x_speicher, y_speicher = x, y
        answers_x, answers_y = set(), set()
        kombinationen_x, kombinationen_y = [], []
        
        while x>0 and k.contentx[x-1][y] == 0 and k.contenty[x-1][y] == 0:
            x -= 1
        for i in range(k.x - x):
            if k.contentx[x+i][y] == 0 and k.contenty[x+i][y] == 0 and k.answers[x+i][y]!= 0:
                answers_x.add(int(k.answers[x+i][y]))
            elif k.contentx[x+i][y] != 0 or k.contenty[x+i][y] != 0: break
        x = x_speicher
        
        while y>0 and k.contentx[x][y-1] == 0 and k.contenty[x][y-1] == 0:
            y -= 1          
        for i in range(k.y - y):
            if k.contenty[x][y+i] == 0 and k.contentx[x][y+i] == 0 and k.answers[x][y+i]!= 0:
                answers_y.add(int(k.answers[x][y+i]))
            elif  k.contenty[x][y+i] != 0 or k.contentx[x][y+i] != 0: break
        y = y_speicher
        #print("Antworten", answers_x,type(answers_x), answers_y, type(answers_y))
        for optionen in table[k.getrowlength("right",x,y), k.getrowvalue("right",x,y)]:
            if answers_x.issubset(optionen):
                #print(f"{answers_x} is subset of {optionen}")
                opt = optionen - answers_x
                #print(opt)               
                kombinationen_x.append(opt)
        
        for optionen in table[k.getrowlength("down",x,y), k.getrowvalue("down",x,y)]:
            if answers_y.issubset(optionen): 
                #print(f"{answers_y} is subset of {optionen}")
                opt = optionen - answers_y
                               
                kombinationen_y.append(opt)
        #print(kombinationen_x, "-------------", kombinationen_y)   
        # 
        # pain in the ass debugging int( ) typecast missing
        #      
        return kombinationen_x,kombinationen_y
    
    def legal(k,x,y):
        answers_speicher = set()
        x_speicher = x
        y_speicher = y
        
        while x>0 and k.contentx[x-1][y] == 0 and k.contenty[x-1][y] == 0:
            x -= 1
        for i in range(k.x - x):
            if k.contentx[x+i][y] == 0 and k.contenty[x+i][y] == 0:
                if k.answers[x+i][y]!= 0:
                    if k.answers[x+i][y] in answers_speicher:
                        return False
                    answers_speicher.add(k.answers[x+i][y])
            else:break

        x = x_speicher
        if k.getrowlength("right", x, y)==len(answers_speicher):
            sum = 0
            for num in answers_speicher:
                #print(num, type(num))
                sum+=int(num)
            if k.getrowvalue("right", x, y)!=sum:return False
        
        answers_speicher.clear()

        while y>0 and k.contentx[x][y-1] == 0 and k.contenty[x][y-1] == 0:
            y -= 1          
        for i in range(k.y - y):
            if k.contenty[x][y+i] == 0 and k.contentx[x][y+i] == 0:
                if k.answers[x][y+i]!= 0:
                    if k.answers[x][y+i] in answers_speicher:
                        return False
                    answers_speicher.add(k.answers[x][y+i])
            else:break

        y = y_speicher
        if k.getrowlength("down", x, y)==len(answers_speicher):
            sum = 0
            for num in answers_speicher:
                sum += int(num)
            if k.getrowvalue("down", x, y)!=sum:return False

        return True
    def solver0(k,x,y):
        kombinationen = build_table()
        num_opt = set()
        num_opt2 = set()
        kombinationen_x, kombinationen_y = k.refine(x,y,kombinationen)
        for optionen in kombinationen_x:
            for num in optionen:
                num_opt.add(num)
        
        for optionen in kombinationen_y:
            for num in optionen:
                num_opt2.add(num)
        num_opt = num_opt.intersection(num_opt2)
        return num_opt
    
    def solverl1(k):
                
            num_opt_best = {1,2,3,4,5,6,7,8,9}
            x_best = 0
            y_best = 0
            for x in range(k.x):
                for y in range(k.y):
                    
                    
                    if(k.answers[x][y]==0 and k.contentx[x][y]==0 and k.contenty[x][y]==0 and 2<k.getrowvalue("right",x,y) and 0<k.getrowlength("right",x,y) and 2<k.getrowvalue("down",x,y) and 0<k.getrowlength("down",x,y)):
                        
                        num_opt = k.solver0(x,y)
                        if len(num_opt_best)>len(num_opt) and len(num_opt) != 0:
                            
                            num_opt_best = num_opt
                            x_best = x
                            y_best = y
                            if len(num_opt_best)==1:break
            
            
            return num_opt_best,x_best,y_best
    def puzzlecomplete(k):
        for i in range(k.x):
            for j in range(k.y):
                if k.answers[i][j]==0 and k.contentx[i][j]==0 and k.contenty[i][j]==0:
                    return False
        return True
    
    def recursiveshell(k,nodesvisited = 0):
        if k.puzzlecomplete():return True, nodesvisited  
        optionen, x, y = k.solverl1()
        if len(optionen)>k.internalnodelimit:
            return False, nodesvisited
        for num in optionen:
            
            if nodesvisited > k.nodeslimit:
                return False, nodesvisited
            nodesvisited += 1
            
            k.answers[x][y] = num

            if k.legal(x, y):

                state, nodesvisited = k.recursiveshell(nodesvisited)
                if state:
                    return True, nodesvisited
                
            k.answers[x][y] = 0

        return False, nodesvisited





    

    def bsp(k):
        k.bfill2()
        k.contentx[0][1] = 13
        #k.answers[1][1]=4
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
        

    def generator(k, seed = random.randint(100000000000,999999999999) ):
        #print(f"seed:{seed}")
        seed = int(str(seed).replace('0', '1'))
        k.bfill()
        digits = []
        seedkoordinaten = []

        while seed > 0:
            digits.append(seed % 10)
            seed //= 10
        digits.reverse()

        i = 0
        for num in digits:
            #print(num)
            if i == 1:
                y = num
                k.contentx[x][y] = 0
                k.contenty[x][y] = 0
                seedkoordinaten.append((x,y))
                
                i = 0
            else:
                x = num
                i = 1
        k.symmetry()
        k.legalize()
        
        for start in seedkoordinaten:
            sx, sy = start
            for goal in seedkoordinaten:
                #sx, sy = x, y
                p = 0 
                while not k.pathexists(start,goal) and  p<100:
                    dx = goal[0] - sx
                    dy = goal[1] - sy
                    if abs(dx)>abs(dy):
                        step_x = 1 if dx > 0 else -1
                        step_y = 0
                    else:
                        step_x = 0
                        step_y = 1 if dy > 0 else -1
                    nx, ny = sx + step_x, sy + step_y
                    if 0 <= nx < len(k.contentx) and 0 <= ny < len(k.contentx[0]):
                        k.contentx[nx][ny] = 0
                        k.contenty[nx][ny] = 0
                    p += 1
                    sx, sy = nx, ny
            k.bfill2()
            k.legalize()
            
    def symmetry(k):
        for y in range(len(k.contentx[0])):
            for x in range (math.ceil(len(k.contentx)/2)):
                if k.contentx[x+1][y] == 0 or "B":
                    k.contentx[len(k.contentx)-x-1][y] = k.contentx[x+1][y]
                    k.contentx[len(k.contenty)-x-1][y] = k.contenty[x+1][y]

    def legalize(k):
        legal = False
        while legal == False:
            legal, x, y, direction = k.layoutlegal()
            if legal == False:
                if direction == "down":
                    if y+1 < len(k.contenty[0]):
                        k.contentx[x][y+1]=0
                        k.contenty[x][y+1]=0
                    else:
                        k.contentx[x][y-1]=0
                        k.contenty[x][y-1]=0
                else:
                    if x+1 < len(k.contenty):
                        k.contentx[x+1][y]=0
                        k.contenty[x+1][y]=0
                    else:
                        k.contentx[x-1][y]=0
                        k.contenty[x-1][y]=0
                       
    def layoutlegal(k):
        for i in range(k.x):
            for j in range(k.y):
                if k.contentx[i][j]==0:
                    if k.getrowlength("down",i,j) == 1:
                        return False, i, j, "down"
                    if k.getrowlength("right",i,j) == 1:
                        return False, i, j, "right"
        return True, None, None, None

    def pathexists(k, start, goal):
        sx, sy = start
        gx, gy = goal
        zeilen = k.y
        reihen = k.x

        if k.contentx[sx][sy]=="B" or k.contentx[gx][gy]=="B":
            return False

        checked = [[False for _ in range(reihen)] for _ in range(zeilen)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if (x, y) == (gx, gy):
                return True
            checked[x][y] = True
            for d1, d2 in directions:
                new_x, new_y = x + d1, y + d2
                if 0 <= new_x < reihen and 0 <= new_y < zeilen and not checked[new_x][new_y]and k.contentx[new_x][new_y]==0:
                    if dfs(new_x,new_y):
                        return True
            return False
        return dfs(sx,sy)
    
    def constraintcreator(k):
        
        for x in range(len(k.contentx)):
            for y in range(len(k.contentx[0])):
                if k.contentx[x][y] == 0 and k.answers[x][y] == 0:
                    k.tryout(x,y)

    def tryout(k,x,y):
        table = build_table()
        len_x = k.getrowlength("right",x,y)
        len_y = k.getrowlength("down",x,y)
        val_x = []
        val_y = []
        for key, value in table.items():
            if key[0] == len_x:
                val_x.append(key[1])
        
            if key[0] == len_y:
                val_y.append(key[1])    
        
        for i in val_x:
            for j in val_y:
                x_1 = x
                y_1 = y
                while x>0 and k.contentx[x][y] == 0 and k.contenty[x][y] == 0:
                    x -= 1
                if k.contentx[x][y]== "B":
                    k.contentx[x][y]=i
                x = x_1
                while y>0 and k.contentx[x][y] == 0 and k.contenty[x][y] == 0:
                    y -= 1
                if k.contenty[x][y]== "B":
                    k.contenty[x][y]=j
                y = y_1
                
    def randomfill(k):
        for x in range(k.x):
            for y in range(k.y):
                
                if k.contentx[x][y]==0 and k.contenty[x][y]==0 and k.answers[x][y]==0:
                    legal = False
                    i = 0
                    while legal == False:
                        i+=1
                        k.answers[x][y]=random.randint(1,9) 
                        legal = k.checklegal2(x,y)
                        
                        if i == 100:
                            k.wipeanswers()
                            k.randomfill()
                        

    def sumup(k):
        for x in range(k.x):
            for y in range(k.y):
                
                answers_speicher = set()
                x_speicher = x
                if k.answers[x][y]!=0:
                    while x>0 and k.contentx[x-1][y] == 0 and k.contenty[x-1][y] == 0:
                        x -= 1
                    for i in range(k.x - x):
                        if k.contentx[x+i][y] == 0 and k.contenty[x+i][y] == 0:
                            answers_speicher.add(k.answers[x+i][y])
                        else:break
                    sum = 0
                    for num in answers_speicher:
                        sum+=int(num)
                        
                    k.contentx[x-1][y] = sum
                    x = x_speicher
                    answers_speicher.clear()
                
                    while y>0 and k.contentx[x][y-1] == 0 and k.contenty[x][y-1] == 0:
                        y -= 1          
                    for i in range(k.y - y):
                        if k.contenty[x][y+i] == 0 and k.contentx[x][y+i] == 0:
                                answers_speicher.add(k.answers[x][y+i])
                        else:break
                    sum = 0
                    for num in answers_speicher:
                        sum += int(num)
                    k.contenty[x][y-1] = sum
                    

    def checksize(k):
        i = 0
        for x in range(k.x):
            for y in range(k.y):
                if k.contentx[x][y]==0 and  k.contentx[x][y]==0 and k.answers[x][y]==0:
                    i += 1
        if i<k.min_puzzlesize:
            return False, i
        return True, i

    def checklegal2(k,x,y):
        answers_speicher = set()
        x_speicher = x
        
        while x>0 and k.contentx[x-1][y] == 0 and k.contenty[x-1][y] == 0:
            x -= 1
        for i in range(k.x - x):
            if k.contentx[x+i][y] == 0 and k.contenty[x+i][y] == 0:
                if k.answers[x+i][y]!= 0:
                    if k.answers[x+i][y] in answers_speicher:
                        return False
                    answers_speicher.add(k.answers[x+i][y])
            else:break

        x = x_speicher  
        answers_speicher.clear()

        while y>0 and k.contentx[x][y-1] == 0 and k.contenty[x][y-1] == 0:
            y -= 1          
        for i in range(k.y - y):
            if k.contenty[x][y+i] == 0 and k.contentx[x][y+i] == 0:
                if k.answers[x][y+i]!= 0:
                    if k.answers[x][y+i] in answers_speicher:
                        return False
                    answers_speicher.add(k.answers[x][y+i])
            else:break
        return True
    def loadingscreen(k):
        k.answers[2][4] = "K"
        k.answers[3][4] = "A"
        k.answers[4][4] = "K"
        k.answers[5][4] = "U"            
        k.answers[6][4] = "R"
        k.answers[7][4] = "O"
    def wipeanswers(k):
        for x in range(len(k.answers)):
            for y in range(len(k.answers[0])):
                k.answers[x][y]=0   
    #https://stackoverflow.com/questions/61448326/generate-a-dictionary-of-all-possible-kakuro-solutions
        
#k = Kakuro(10,10)
#k.bfill()
#print(k.getrowlength("down",5,2))
#print(k.contentx)