import numpy as np
from solve import isSolved

# AI is cross

grid = [
    [1, 1, 9],
    [1, -1, 9],
    [-1, 9, 9]
]

scores = {
    'cross' : 1,
    'naught' : -1,
    "tie" : 0
}

# Using Minimax algorithm
def AiTurn(grid):
    bestScore = -np.Infinity
    for y in range(0,3):
        for x in range(0,3):
            # if empty
            if grid[y][x] == 9:
                grid[y][x] = 1
                score = Minimax(grid, 0 , False)
                grid[y][x] = 9
                if score > bestScore:
                    bestScore = score
                    move = (x, y)
    return move

def Minimax(grid, depth, maximizingPlayer):
    solved = isSolved(grid)
    if solved != None:
        return scores[solved[0]]
    if maximizingPlayer:
        bestScore = -np.Infinity
        for y in range(0,3):
            for x in range(0,3):
                # if empty
                if grid[y][x] == 9:
                    grid[y][x] = 1
                    score = Minimax(grid, depth + 1 , False)
                    grid[y][x] = 9
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = np.Infinity
        for y in range(0,3):
            for x in range(0,3):
                # if empty
                if grid[y][x] == 9:
                    grid[y][x] = -1
                    score = Minimax(grid, depth + 1 , True)
                    grid[y][x] = 9
                    bestScore = min(score, bestScore)
        return bestScore


AiTurn(grid)
