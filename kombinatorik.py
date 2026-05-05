from itertools import combinations
from gamelogic import Kakuro


def build_table():
    table = {}
    digits = range(1, 10)

    for length in range(2, 10):
        for combo in combinations(digits, length):
            s = sum(combo)
            key = (length, s)
            table.setdefault(key, []).append(combo)

    return table

kombinationen = build_table()

def solver(k):
    for x in k.x:
        for y in k.y:
            if(k.contentx[x][y]==0):
