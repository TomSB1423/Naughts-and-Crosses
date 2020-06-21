import numpy as np
from solve import isSolved

# AI is cross

scores = {
    'cross' : 1,
    'naught' : -1,
    "tie" : 0
}
loops = 0

# Using Minimax algorithm
def AiTurn(grid):
    global loops
    loops = 0
    bestScore = -np.Infinity
    # Alpha Beta pruning values
    a = -np.Infinity
    b = np.Infinity

    # Reduces the wait time py moving to the center if it is the first go
    openSpaces = 0
    for y in range(0,3):
        for x in range(0,3):
            if grid[x][y] == 9:
                openSpaces += 1
    if openSpaces == 9:
        return (1, 1)

    for y in range(0,3):
        for x in range(0,3):
            # if empty look for solutions
            if grid[y][x] == 9:
                grid[y][x] = 1
                # recursivly call Minimax to get scores for each square
                score = Minimax(grid, a, b, False)
                grid[y][x] = 9
                if score > bestScore:
                    bestScore = score
                    move = (x, y)
    # Return final AI move
    print(loops)
    return move

def Minimax(grid, a, b, maximizingPlayer):
    global loops
    loops += 1

    solved = isSolved(grid)
    if solved != None:
        return scores[solved[0]]
    
    maxMin = (1 if maximizingPlayer else -1)
    bestScore = np.Infinity * -maxMin
    for y in range(0,3):
        for x in range(0,3):
            if grid[y][x] == 9:
                grid[y][x] = maxMin
                score = Minimax(grid, a, b, not maximizingPlayer)
                grid[y][x] = 9
                
                if maximizingPlayer:
                    bestScore = max(score, bestScore)
                    a = max(a, score)
                else:
                    bestScore = min(score, bestScore)
                    b = min(b, score)
                if b <= a:
                    return bestScore    
    return bestScore