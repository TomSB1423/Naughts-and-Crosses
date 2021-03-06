import numpy as np

def isSolved(matrix):
    for i in range(np.ma.size(matrix, 1)):
        # Checks columns
        if abs(np.sum(matrix, axis=(0))[i]) == 3:
            if matrix[0][i] == 1:
                crossWin = True
            else:
                crossWin = False
            starPos = (i, 0)
            endPos = (i, 2)
            return crossWin, starPos, endPos

        # Checks rows
        elif abs(np.sum(matrix, axis=(1))[i]) == 3:
            if matrix[i][0] == 1:
                crossWin = True
            else:
                crossWin = False
            starPos = (0, i)
            endPos = (2, i)
            return crossWin, starPos, endPos

    # Checks diagonals
    if abs(sum(matrix[i][i] for i in range(np.ma.size(matrix, 1)))) == 3:
        if matrix[0][0] == 1:
            crossWin = True
        else:
            crossWin = False
        starPos = (0, 0)
        endPos = (2, 2)
        return crossWin, starPos, endPos
    elif abs(sum(np.fliplr(matrix)[i][i] for i in range(np.ma.size(matrix, 1)))) == 3:
        if matrix[2][0] == 1:
            crossWin = True
        else:
            crossWin = False
        starPos = (0, 2)
        endPos = (2, 0)
        return crossWin, starPos, endPos

    # Check if Tie
    openSpaces = 0
    for y in range(0,3):
        for x in range(0,3):
            if matrix[x][y] == 9:
                openSpaces += 1
    if openSpaces == 0:
        return ['tie']
    return None
