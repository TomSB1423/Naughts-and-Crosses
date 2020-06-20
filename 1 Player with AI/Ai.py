import numpy as np
from solve import isSolved

# AI is cross

scores = {
    'cross' : 1,
    'naught' : -1,
    "tie" : 0
}

# Using Minimax algorithm
def AiTurn(grid):
    # If AI goes first then choose middle square - just speeds things up
    openSpaces = 0
    for y in range(0,3):
        for x in range(0,3):
            if grid[x][y] == 9:
                openSpaces += 1
    if grid[1][1] == 9 and openSpaces == 9:
        return (1, 1)
    # loop through 
    bestScore = -np.Infinity
    for y in range(0,3):
        for x in range(0,3):
            # if empty look for solutions
            if grid[y][x] == 9:
                grid[y][x] = 1
                # recursivly call Minimax to get scores for each square
                score = Minimax(grid, 0 , False)
                grid[y][x] = 9
                if score > bestScore:
                    bestScore = score
                    move = (x, y)
    # Return final AI move
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