from itertools import combinations
from gamelogic import Kakuro
class Solve():

    def build_table():
        table = {}
        digits = range(1, 10)

        for length in range(2, 10):
            for combo in combinations(digits, length):
                s = sum(combo)
                key = (length, s)
                table.setdefault(key, []).append(combo)

        return table

    
    global kombinationen 
    kombinationen = build_table()
    def solver(k):
        
        num_opt_best = {1,2,3,4,5,6,7,8,9}
        num_opt = set()
        num_opt2 = set()
        x_best = 0
        y_best = 0
        for x in range(k.x):
            for y in range(k.y):
                if(k.contentx[x][y]==0 and k.contenty[x][y]==0):
                    for optionen in kombinationen[k.getrowlength("right",x,y), k.getrowvalue("right",x,y)]:
                        for num in optionen:
                            num_opt.add(num)
                    for optionen in kombinationen[k.getrowlength("down",x,y), k.getrowvalue("down",x,y)]:
                        for num in optionen:
                            num_opt2.add(num)
                            num_opt = num_opt.intersection(num_opt2)
                    if len(num_opt_best)>len(num_opt):
                        num_opt_best = num_opt
                        x_best = x
                        y_best = y

        return num_opt_best, x_best, y_best            